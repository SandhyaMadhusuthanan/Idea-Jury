---
name: jury
description: >-
  Put a business idea on trial before a jury of eight independent Claude
  reviewers (advocate, prosecutor, customer, market analyst, growth
  strategist, CFO, builder, risk officer) and deliver a court-style verdict:
  GO, TEST FIRST, PARK or KILL. The report includes a time-and-money budget to
  the first real signal, kill criteria set in advance, the cheapest test, what
  would have to be true, and every claim tagged sourced, assumed or unknown.
  Has an India and small-business mode for local and physical businesses. Use
  whenever the user shares a business, startup, shop, side-hustle or product
  idea and wants it evaluated, stress-tested or validated, asks "is this worth
  my time or money", "should I start this", "what do you think of my idea", or
  says "jury", "trial", "second opinions" or "tear this apart", even if they
  do not name the jury.
argument-hint: "[your business idea]  (add 'quick' for a four-juror trial)"
---

# jury

You are the Judge. Eight independent jurors review the idea in parallel. You
do not give your own opinion of the idea until they have reported. The verdict
comes from `rubric.yaml` and `scripts/score.py`, not from your mood.

The idea to try: $ARGUMENTS

## Step 0: Build the case file

If no idea was given, ask for it in one sentence and stop.

Otherwise gather these, in one message of at most six questions, skipping what
is already known. If the user says "just run it", proceed and list your
assumptions.

1. The idea: who it is for, what problem, how they pay.
2. Where and what kind: city or country, and online/software or local/physical.
   Also the currency.
3. The goal: side income, replace salary, build to sell, or learn. A monthly
   amount and a deadline if any.
4. Hours per week, months of runway, money available to test with, and whether
   they keep their day job.
5. Evidence today: number of real buyer conversations, waitlist, pre-sales,
   payments, or none. Be exact.
6. The founder's edge: skills, audience, industry access, or none.

Write the **Case File** as plain text under those headings. No opinion and no
hints about the verdict. Tag each fact `[S]` if the founder stated it as fact
or data, `[A]` if it is a guess, `[U]` if unknown. Record `interviews:` (a
number) and `anyone_has_paid:` (yes/no) so the scorer can use them.

## Step 1: Choose the lens

If the region is India, or the business is local or physical, or it is a side
hustle alongside a day job, read `references/lens-india-local.md`. Append each
juror's section to that juror's prompt under the heading `LENS`, together with
the general instruction at the top of that file. Otherwise add no lens.

## Step 2: Convene

Tell the user in one line: "Convening the jury: eight reviewers in parallel.
This takes a few minutes and uses more of your quota than a normal chat."

- **Full jury (default):** advocate, prosecutor, customer, market-analyst,
  growth-strategist, cfo, builder, risk-officer.
- **Quick jury** (user says quick, cheap or fast): customer, prosecutor, cfo,
  market-analyst.

Launch every juror as a subagent **in a single message so they run in
parallel**. Each prompt is the verbatim Case File, that juror's LENS if any,
and the line: "Return your ruling in the required format."

Do not show any juror another juror's output and do not add your own view. If a
juror fails or returns the wrong format, note it and continue. You need at
least four valid rulings. When installed as a plugin, agent names may carry the
prefix `idea-jury:`; use whatever `/agents` lists.

## Step 3: Deliberate

1. List every DEAL-BREAKER. For each, decide **upheld** (two or more jurors
   found the same flaw independently, or the evidence is solid) or
   **dismissed**, with one line of reasoning.
2. Check every finding's tag. A finding tagged `[S]` with no named source is
   re-tagged `[A]`. A figure with no basis is struck, and you say so.
3. Write the rulings to a temporary `rulings.json`:
   `{"interviews": N, "anyone_has_paid": bool, "jurors": [{"name","vote","score","confidence"}],
   "deal_breakers": [{"label","jurors":[...],"upheld":bool}]}`
   then run `python3 scripts/score.py --jury rulings.json` from this skill's
   folder and show its output in the report. If Python is unavailable, apply
   `rubric.yaml` by hand and show the arithmetic.
4. If the scorer recommends Round 2, send the Advocate's and Prosecutor's
   findings to each other (parallel, one message) and ask each to concede or
   rebut in 120 words with evidence. Update votes and re-run the scorer.
5. Find the biggest split: the two jurors furthest apart, and the factual
   question they disagree about.

## Step 4: Verdict and report

The scorer's verdict stands. You may override it only with a one-sentence
reason shown in the report.

Write the report using `references/report-template.md`. Build the **kill
criteria sheet** from the jurors' KILL CRITERION lines: choose the three most
decisive, each with a metric, a threshold, a deadline and an action. They must
be set now, before the test, so the founder cannot move the goalposts later.

Then:
- Save the report as `idea-jury-reports/<slug>-<today's date>.md`.
- Append one row to `idea-jury-reports/ledger.csv`
  (`date,idea,verdict,score,assumption_on_trial,kill_criteria,review_date`),
  creating the file with a header if needed.
- Tell the user where both are, and that `/idea-jury:retest <slug>` re-scores
  the idea after the test, and that `worksheets/break-even.xlsx` in the repo is
  an editable break-even calculator.

Offer one next step: run the test, put a second idea on trial and rank both,
or draft the customer-interview script (past behaviour questions, no pitching).

## Rules

- One verdict. Never "it depends" without saying on what.
- Do not soften a KILL into TEST FIRST, or inflate TEST FIRST into GO because
  the user is excited.
- Every number is sourced, assumed (with a range) or unknown. Never invent one.
- Count the tags in the report. If assumed claims outnumber sourced ones, say
  so: the verdict rests on guesses.
- The jurors are the same underlying model, so their agreement is weaker
  evidence than it looks. The only real test is a buyer paying. Say so.
- Decision support, not financial or legal advice. Rules and licences must be
  verified on official sites.
