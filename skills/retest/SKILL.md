---
name: retest
description: >-
  Re-score a business idea after the user has run their test. Loads a previous
  idea-jury report, checks the pre-set kill criteria against the new results,
  and either says stop or puts the idea back before a (quick or full) jury with
  the new evidence. Updates the idea ledger so the verdict history is visible.
  Use when the user says "retest", "update my idea", "here are my results",
  "I ran the test", "I talked to N customers", "it didn't work", "re-score",
  or refers to an earlier jury report or idea slug.
argument-hint: "[idea-slug]  [what happened: numbers, quotes, payments]"
---

# retest

Evidence changes verdicts. This skill makes sure the founder follows the stop
lines they wrote down before the test, and re-scores only after that.

Input: $ARGUMENTS

## Step 1: Load

Find `idea-jury-reports/<slug>-*.md` (newest if several) and
`idea-jury-reports/ledger.csv`. If the slug is missing or ambiguous, list the
ledger rows and ask which idea, in one line.

Extract from the old report: the verdict, the **kill criteria sheet**, the
**what would have to be true** table, and the budget.

## Step 2: Get the results

If the user's message has no concrete numbers, ask once for: how many real
buyers they spoke to, how many said yes to the price, how many paid or
pre-paid and how much, hours and money actually spent, and anything that
surprised them. Do not accept "it went well" as a result.

## Step 3: Check the kill criteria first

For each kill criterion, compare the threshold with the actual result and mark
it **HIT**, **MISSED** or **NOT YET TESTABLE**. Show this as a table.

- If any stop line was **hit**, say so plainly and recommend the action the
  founder wrote down (stop or pivot). Do not reinterpret the numbers or invent
  reasons to continue. The founder may still decide otherwise, but the report
  must record that they overrode their own criterion.
- Compare actual hours and money with the budget range.

## Step 4: Re-score

If no stop line was hit, update the **Case File** with the new facts: tag
results `[S]` (the founder's own data), update `interviews:` and
`anyone_has_paid:`, and cross out assumptions that are now known. Do **not**
include the previous verdict, so the jurors stay independent. Then run the
`jury` skill's process on the updated case file (use the quick jury unless the
user asks for the full one), including the scorer.

## Step 5: Report the delta

Show: old verdict, new verdict, what changed it (which assumption moved from
`[A]` or `[U]` to `[S]`), what is still unknown, and the next smallest test
with new kill criteria and a new review date.

Append a row to `idea-jury-reports/ledger.csv` for the retest and save the
new report as `idea-jury-reports/<slug>-<date>-retest.md`.

## Rules

- Stop lines are decided in advance and honoured. That is the point.
- A GO still requires buyer evidence, which the founder's test may now supply.
- If the evidence is thin (under 5 conversations, no payments), say the retest
  cannot move the verdict much and what would.
