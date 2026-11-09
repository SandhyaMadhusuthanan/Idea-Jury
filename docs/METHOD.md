# Method and sources

This project's prompts, rubric and code were written from scratch. The ideas
behind them come from published work. Citing it here is how you can check the
thinking rather than trust it.

| idea used | source |
|---|---|
| Ask about past behaviour, not future promises; do not pitch early; end with a costly ask | Rob Fitzpatrick, *The Mom Test* (2013) |
| One-page model of customer, problem, channels, revenue and costs; rank the riskiest assumptions | Ash Maurya, *Running Lean* (Lean Canvas) |
| Smallest experiment that can disprove a hypothesis (concierge, smoke test, pre-sale) | Eric Ries, *The Lean Startup* (2011) |
| Premortem: imagine it failed, then explain why (the Prosecutor's method) | Gary Klein, "Performing a Project Premortem", Harvard Business Review (2007) |
| Decide stop conditions in advance (kill criteria) so you cannot move the goalposts later | Annie Duke, *Quit* (2022) |
| Contribution margin and break-even: price minus variable cost, fixed cost divided by that | standard managerial accounting |

## Design choices, and why

- **Independent jurors.** They do not see each other's rulings, to avoid anchoring.
- **Fixed rules, not mood.** Thresholds live in `rubric.yaml` and are applied by `score.py`, so every verdict can be audited and re-run.
- **Evidence caps.** Without real buyer evidence, demand scores are capped, because opinions are not evidence.
- **Claim tags.** `[S]`, `[A]` and `[U]` force the report to show how much of it is guesswork.
- **Kill criteria before the test.** Written in advance and checked by `/retest`.
- **Known weakness.** All jurors are one underlying model. Their agreement is correlated, so it is weaker evidence than eight independent humans would give. The remedy is real buyers, not more jurors.
- **Regulatory facts are looked up, not remembered.** Jurors are told to cite official sources and mark anything unverified as `[U]`.

## Adding your own lens

A lens is a Markdown file with one section per juror, appended to that juror's
prompt. See `skills/jury/references/lens-india-local.md` for the shape.
