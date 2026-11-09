# idea-jury

**Is this business idea worth your time and money?** Eight independent Claude reviewers put it on trial, and a transparent rulebook, not a mood, decides the verdict.

```
/idea-jury:jury a home-style tiffin service for office workers in Coimbatore
```

## Who it is for

First-time founders, small shop owners and people with a day job who want to try a side business. It has a built-in **India and small-business mode** (rupees, WhatsApp-and-word-of-mouth growth, local competition, licences to verify) for food, retail, tuition, services, small manufacturing and agriculture, where "search GitHub and Product Hunt" is useless. It also works for software and online ideas.

## What you get

Not a score to argue with. A plan you can act on:

- **Verdict:** GO, TEST FIRST, PARK or KILL, with the exact rule that decided it
- **Budget to the first real signal:** hours, money and weeks before you get honest evidence, and what you lose if you stop
- **Kill criteria, written before you start:** for example "fewer than 5 of 30 people pre-pay in 3 weeks, then stop"
- **Cheapest test:** the smallest experiment that could disprove the idea
- **What would have to be true:** the assumptions the idea depends on, weakest first
- **Break-even and time-worth:** units per day, and what your hours earn if it works
- **Every claim tagged:** `[S]` sourced, `[A]` assumed, `[U]` unknown, with a count at the end. If guesses outnumber sources, the report says the verdict rests on guesses.

See a full hand-worked example: [`examples/tiffin-coimbatore.md`](examples/tiffin-coimbatore.md). Its numbers are illustrative placeholders, not market data.

## The jury

| juror | job |
|---|---|
| Advocate | the strongest honest case for the idea |
| Prosecutor | the strongest honest case against it (a premortem) |
| Customer | role-plays the real buyer: would I pay? |
| Market Analyst | competitors, alternatives, bottom-up market size |
| Growth Strategist | can you reach the first 10 and first 100 buyers? |
| CFO | unit economics, break-even, is it worth your time in money terms |
| Builder | smallest shippable version, can you execute |
| Risk Officer | licences, regulation, platform and reputational risk |

Jurors cannot see each other's rulings. If the jury splits, the Advocate and Prosecutor get a rebuttal round.

## How it differs

Several idea validators already exist (see below). This one differs in substance:

1. **Local and small-business first**, with an India lens, not only SaaS.
2. **The output is a budget and a set of stop lines**, not just a score.
3. **An editable rulebook:** every weight and threshold is in [`skills/jury/rubric.yaml`](skills/jury/rubric.yaml). A small script, [`score.py`](skills/jury/scripts/score.py), applies it and prints the arithmetic. Change a number and the verdict changes.
4. **Facts separated from guesses** with `[S]/[A]/[U]` tags on every claim.
5. **Works without AI:** a printable [worksheet](worksheets/idea-worksheet.md), an editable [break-even spreadsheet](worksheets/break-even.xlsx) and the scorer need no API key.
6. **Tracks an idea over time:** `/idea-jury:retest` checks your pre-set stop lines against the new results, re-scores, and logs the history in `ledger.csv`.

## Install

### Option A: as a plugin (recommended)

```
/plugin marketplace add SandhyaMadhusuthanan/Idea-Jury
/plugin install idea-jury@idea-jury
```

Commands are namespaced: `/idea-jury:jury`, `/idea-jury:retest`.

### Option B: manual copy

```
git clone https://github.com/SandhyaMadhusuthanan/Idea-Jury.git
mkdir -p ~/.claude/skills ~/.claude/agents
cp -r Idea-Jury/skills/* ~/.claude/skills/
cp Idea-Jury/agents/*.md ~/.claude/agents/
```

Commands have no prefix here: `/jury` and `/retest`. Everything else in this README works the same. Just drop the `idea-jury:` part. Type `/agents` to confirm the eight jurors loaded.

Use one option or the other, not both, or you'll get duplicate jurors.
## Commands

| command | use |
|---|---|
| `/idea-jury:jury <idea>` | full trial, eight jurors |
| `/idea-jury:jury quick <idea>` | four jurors (customer, prosecutor, CFO, market analyst) |
| `/idea-jury:retest <slug> <what happened>` | re-score after your test, honouring your stop lines |

Reports are saved to `idea-jury-reports/` in your current folder, with a running `ledger.csv`.

## Use it without AI

1. Print [`worksheets/idea-worksheet.md`](worksheets/idea-worksheet.md) and fill it in. It includes the interview questions and a place for kill criteria.
2. Open [`worksheets/break-even.xlsx`](worksheets/break-even.xlsx), edit the yellow cells.
3. Score yourself: save your ratings as `my-ratings.json` and run the scorer.

```json
{
  "ratings": {"pain": 3, "willingness_to_pay": 2, "reachability": 3, "founder_fit": 4,
              "time_to_first_sale": 3, "market_ceiling": 3, "competition": 3, "economics": 3},
  "interviews": 2,
  "anyone_has_paid": false,
  "flags": []
}
```
```
python3 skills/jury/scripts/score.py --solo my-ratings.json
```

Without buyer evidence (5 real conversations, or any payment), pain is capped at 3 and willingness to pay at 2.

## Customise

- **Weights and thresholds:** `skills/jury/rubric.yaml`
- **A juror's stance:** the file in `agents/`
- **Another region or industry:** copy `skills/jury/references/lens-india-local.md`, write one section per juror, and point `SKILL.md` Step 1 at it. Contributions of new lenses are welcome.

## Cost

A full trial runs eight web-searching subagents, takes a few minutes and uses noticeably more of your Claude usage than a normal chat. Use `quick` for early ideas.

## Limits

The jurors are the same underlying model, so their agreement is weaker evidence than it looks. This is structured opinion, not a forecast, and not financial or legal advice. Licences, taxes and fees must be verified on official sites. The only real validation is someone paying you.

## Method and credits

Prompts and rubric were written from scratch, drawing on public frameworks cited in [`docs/METHOD.md`](docs/METHOD.md): *The Mom Test*, Lean Canvas, the Lean Startup's cheap experiments, the project premortem, kill criteria, and basic unit economics.

**Related projects.** Others are working on nearby problems, and they are worth a look:
- [codeandbeans/idea-validator](https://github.com/codeandbeans/idea-validator): a research-heavy Claude skill that produces a product brief
- [j7an/ideaprobe](https://github.com/j7an/ideaprobe): a plugin with a five-dimension framework and parallel research agents
- [veyralabsgroup/venture-suite](https://github.com/veyralabsgroup/venture-suite): validation with a Bull/Bear/Judge verdict
- [Ciunkos/skills](https://github.com/Ciunkos/skills): includes a business-idea-validator skill

## Sample output

An excerpt from `/idea-jury:jury a home-style tiffin service for office workers in Coimbatore`. The numbers are illustrative placeholders, not market data.

```
VERDICT: TEST FIRST
Decided by: willingness_to_pay capped at 2 (no buyer has paid yet) → total below GO threshold

BUDGET TO FIRST REAL SIGNAL
  Time:   ~10 hrs/week for 3 weeks
  Money:  ₹3,000 (sample meals + printed menu)
  If you stop now, you lose: ₹0 and a few weekends

KILL CRITERIA (written before you start)
  Fewer than 5 of 30 office workers pre-pay for a week's plan within 3 weeks → STOP

CHEAPEST TEST
  Cook 10 sample lunches, offer them to 30 people at one office park, ask for ₹500 advance.

WHAT WOULD HAVE TO BE TRUE
  1. [A] Office workers near you want home-style food at ₹80–100 per meal
  2. [A] You can deliver 20 meals/day without a rented kitchen
  3. [U] Whether society or licence rules allow home-based food sales

BREAK-EVEN   ~14 meals/day at ₹90 (illustrative)
TAG COUNT    [S] 3   [A] 11   [U] 4  → verdict rests mostly on assumptions
```

## License

MIT.
