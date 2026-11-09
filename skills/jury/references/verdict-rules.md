# Verdict rules

The numbers live in `../rubric.yaml`. The logic is applied by
`../scripts/score.py`. This file explains the logic in words so you can read
and audit it. If this file and `rubric.yaml` ever disagree, `rubric.yaml` wins.

Inputs: each juror's vote (BACK, TEST, PASS), score (0-10), confidence (1-5)
and any deal-breaker.

Checked in this order:

1. **Deal-breakers.** A fatal flaw found independently by two or more jurors and
   not refuted by evidence is *upheld*, and the verdict is **KILL**. One upheld
   deal-breaker from a single juror caps the verdict at **TEST FIRST**.
2. **KILL.** Too many PASS votes, or a low confidence-weighted mean score.
3. **GO.** A large share of jurors BACK, a high mean score, the Customer and the
   CFO both BACK, no upheld deal-breaker, **and direct buyer evidence in the
   case file** (someone has paid, or enough real buyer conversations
   happened). Without buyer evidence the best verdict is **TEST FIRST**. A jury
   of AI reviewers cannot replace buyers.
4. **PARK.** The Customer and Market Analyst support it, but the Builder, CFO or
   Risk Officer votes PASS for a reason about this founder or this moment
   (hours, runway, skills, capital, licence, timing). The idea is real; the fit
   is wrong. State what would change the answer.
5. **Otherwise TEST FIRST.**

**Round 2.** When the jury splits, or scores are far apart, the Advocate and
Prosecutor each get the other's findings and reply in 120 words with a
concession or an evidenced rebuttal. Votes are updated and the scorer re-run.

**Weighted mean** = sum(score x confidence) / sum(confidence).

Every verdict must show: which rule decided it, the tally, the strongest
dissent, the assumption on trial, and the cheapest test.
