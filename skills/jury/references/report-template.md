# The People vs. {{idea in 6 words}}

**Verdict: {{GO | TEST FIRST | PARK | KILL}}**
Decided by: {{scorer rule, for example "rule 5: no buyer evidence yet; only 3 of 8 BACK"}}
Jury: {{n}} jurors   Weighted mean: {{m}}/10   Date: {{date}}   Region/lens: {{e.g. Coimbatore, India / local}}

## Tally
| juror | vote | score | conf | deal-breaker |
|---|---|---|---|---|
| Advocate | | | | |
| Prosecutor | | | | |
| Customer | | | | |
| Market Analyst | | | | |
| Growth Strategist | | | | |
| CFO | | | | |
| Builder | | | | |
| Risk Officer | | | | |

Scorer output (from `scripts/score.py`):
```
{{paste the scorer output}}
```

## Majority opinion
{{3-5 sentences, each claim tagged [S], [A] or [U].}}

## Dissent
{{The strongest minority view, 2-3 sentences, with the juror's name.}}

## What would have to be true
The idea only works if all of these hold. Each is tagged, and the weakest is first.
| # | assumption | tag | how to find out cheaply |
|---|---|---|---|
| 1 | | A / U | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |

## Budget to the first real signal
| | low | high | tag |
|---|---|---|---|
| Your hours | | | |
| Money to spend (₹ or your currency) | | | |
| Calendar weeks | | | |
| Money at risk if you stop at the kill line | | | |

Effective hourly rate if the goal is reached: {{range}} {{tag}}. Compared with your best alternative use of those hours: {{one line}}.
Break-even: {{units per day / customers per month}} {{tag}}. Recalculate with your own numbers in `worksheets/break-even.xlsx`.

## Kill criteria (set now, before you start)
| # | metric | stop if | by when | then |
|---|---|---|---|---|
| 1 | | | | stop / pivot |
| 2 | | | | |
| 3 | | | | |

Review date: {{date}}. Run `/idea-jury:retest {{slug}}` with the results. If a stop line is hit, the plan is to stop, not to reinterpret the numbers.

## Cheapest test
{{The smallest experiment that could disprove the idea, who it is run on, cost, duration, and the pass line in numbers.}}

## Strongest case for / against
- For (Advocate): {{one line}}
- Against (Prosecutor): {{one line}}

## Deal-breakers
{{Each: upheld or dismissed, and why in one line. Or "none raised".}}

## Claim ledger
Sourced: {{n}}   Assumed: {{n}}   Unknown: {{n}}   {{If assumed > sourced: "This verdict rests mainly on guesses."}}

## Limits
Jurors are the same underlying model, so agreement is weaker evidence than it looks. Rules, licences, taxes and fees must be verified on official sites. Not financial or legal advice. The real test is someone paying you.
