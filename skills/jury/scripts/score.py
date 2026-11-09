#!/usr/bin/env python3
"""Deterministic scorer for idea-jury. No AI, no network, no API key.

Reads rubric.yaml and applies it to ratings, showing the arithmetic.

  python3 score.py --solo  ratings.json   # you rate 8 dimensions 0-5
  python3 score.py --jury  rulings.json   # eight (or four) juror rulings

Add --rubric path/to/rubric.yaml to use a different rubric.
Requires PyYAML:  pip install pyyaml
"""
import argparse, json, os, sys

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_RUBRIC = os.path.join(HERE, "..", "rubric.yaml")


def load(path):
    with open(path, encoding="utf-8") as fh:
        return yaml.safe_load(fh)


def buyer_evidence_ok(case, rub):
    be = rub["buyer_evidence"]
    return (case.get("interviews", 0) >= be["min_interviews"]
            or (be["or_anyone_has_paid"] and case.get("anyone_has_paid", False))
            or case.get("buyer_evidence", False))


def solo(data, rub):
    dims = rub["dimensions"]
    rmax = rub["rating_max"]
    ratings = data["ratings"]
    missing = [d for d in dims if d not in ratings]
    if missing:
        sys.exit("Missing ratings for: " + ", ".join(missing))
    evidence = buyer_evidence_ok(data, rub)
    lines, total, wsum = [], 0, 0
    for d, spec in dims.items():
        r = ratings[d]
        if not 0 <= r <= rmax:
            sys.exit(f"{d}: rating must be 0-{rmax}")
        capped = r
        if not evidence and d in rub["evidence_caps"]:
            capped = min(r, rub["evidence_caps"][d])
        note = f"  (capped from {r}: no buyer evidence)" if capped != r else ""
        lines.append(f"  {d:<20} {capped} x {spec['weight']} = {capped * spec['weight']}{note}")
        total += capped * spec["weight"]
        wsum += spec["weight"]
    score = round(total / (rmax * wsum) * 100)
    flags = data.get("flags", [])
    kill_flags = [f for f in flags if f in rub["flags_force_kill"]]
    cap_flags = [f for f in flags if f in rub["flags_cap_at_test_first"]]
    sv = rub["solo_verdict"]
    if kill_flags:
        verdict, rule = "KILL", f"fatal flag: {', '.join(kill_flags)}"
    elif score < sv["kill_below"]:
        verdict, rule = "KILL", f"score {score} is below {sv['kill_below']}"
    elif score >= sv["go_min"] and evidence and not cap_flags:
        verdict, rule = "GO", f"score {score} >= {sv['go_min']} with buyer evidence"
    else:
        why = []
        if score < sv["go_min"]:
            why.append(f"score {score} < {sv['go_min']}")
        if not evidence:
            why.append("no buyer evidence yet")
        if cap_flags:
            why.append("flag: " + ", ".join(cap_flags))
        verdict, rule = "TEST FIRST", "; ".join(why)
    return {"mode": "solo", "verdict": verdict, "rule": rule, "score": score,
            "buyer_evidence": evidence, "detail": lines,
            "points": f"{total}/{rmax * wsum}"}


def jury(data, rub):
    j = rub["jury"]
    rows = data["jurors"]
    n = len(rows)
    if n < 4:
        sys.exit("Need at least 4 valid rulings.")
    votes = {r["name"]: r["vote"].upper() for r in rows}
    b = sum(v == "BACK" for v in votes.values())
    t = sum(v == "TEST" for v in votes.values())
    p = sum(v == "PASS" for v in votes.values())
    wsum = sum(r["confidence"] for r in rows)
    mean = sum(r["score"] * r["confidence"] for r in rows) / wsum
    scores = [r["score"] for r in rows]
    srange = max(scores) - min(scores)
    evidence = buyer_evidence_ok(data, rub)

    upheld = [d for d in data.get("deal_breakers", []) if d.get("upheld")]
    strong = [d for d in upheld if len(set(d["jurors"])) >= j["deal_breaker_kill_min_jurors"]]
    capped = bool(upheld)

    quick = n <= j["quick_jury_max_size"]
    r2 = j["round2_quick"] if quick else j["round2_full"]
    round2 = (b >= r2["min_back"] and p >= r2["min_pass"]) or srange >= r2["score_range"]

    def v(name): return votes.get(name)
    go_req_ok = all(v(x) == "BACK" for x in j["go_required_backers"] if x in votes)
    supporters_ok = all(v(x) in ("BACK", "TEST") for x in j["park_supporters"] if x in votes)
    blockers = [x for x in j["park_blockers"] if v(x) == "PASS"]

    if strong:
        verdict = "KILL"
        rule = "rule 1: deal-breaker upheld by " + "; ".join(
            f"{d['label']} ({', '.join(d['jurors'])})" for d in strong)
    elif p / n >= j["kill_pass_share"]:
        verdict, rule = "KILL", f"rule 2: {p} of {n} jurors voted PASS ({p/n:.0%} >= {j['kill_pass_share']:.0%})"
    elif mean < j["kill_mean_below"]:
        verdict, rule = "KILL", f"rule 2: weighted mean {mean:.1f} < {j['kill_mean_below']}"
    elif (b / n >= j["go_back_share"] and mean >= j["go_mean_min"] and go_req_ok
          and (evidence or not j["go_requires_buyer_evidence"]) and not capped):
        verdict, rule = "GO", f"rule 3: {b} of {n} BACK, mean {mean:.1f}, required backers agree, buyer evidence present"
    elif supporters_ok and blockers:
        verdict, rule = "PARK", f"rule 4: market voters support it, but {', '.join(blockers)} voted PASS on fit/timing"
    else:
        reasons = []
        if capped: reasons.append("an upheld deal-breaker caps it")
        if not evidence: reasons.append("no buyer evidence yet")
        if b / n < j["go_back_share"]: reasons.append(f"only {b} of {n} BACK")
        verdict = "TEST FIRST"
        rule = "rule 5: " + ("; ".join(reasons) or "does not meet GO, KILL or PARK conditions")

    lines = [f"  {r['name']:<18} {r['vote'].upper():<5} score {r['score']:>4}  conf {r['confidence']}" for r in rows]
    return {"mode": "jury", "verdict": verdict, "rule": rule,
            "tally": {"BACK": b, "TEST": t, "PASS": p, "n": n},
            "weighted_mean": round(mean, 2), "score_range": srange,
            "buyer_evidence": evidence, "round2_recommended": round2,
            "upheld_deal_breakers": [d["label"] for d in upheld], "detail": lines}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--solo"); g.add_argument("--jury")
    ap.add_argument("--rubric", default=DEFAULT_RUBRIC)
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    a = ap.parse_args()
    rub = load(a.rubric)
    res = solo(json.load(open(a.solo)), rub) if a.solo else jury(json.load(open(a.jury)), rub)
    if a.json:
        print(json.dumps(res, indent=2)); return
    print(f"MODE     {res['mode']}  (rubric v{rub['version']}: {os.path.abspath(a.rubric)})")
    print("\n".join(res["detail"]))
    if res["mode"] == "solo":
        print(f"POINTS   {res['points']}  ->  SCORE {res['score']}/100")
    else:
        t = res["tally"]
        print(f"TALLY    BACK {t['BACK']} / TEST {t['TEST']} / PASS {t['PASS']}   weighted mean {res['weighted_mean']}   range {res['score_range']}")
        print(f"ROUND 2  {'recommended' if res['round2_recommended'] else 'not needed'}")
    print(f"BUYER EVIDENCE  {'yes' if res['buyer_evidence'] else 'no'}")
    print(f"VERDICT  {res['verdict']}   ({res['rule']})")


if __name__ == "__main__":
    main()
