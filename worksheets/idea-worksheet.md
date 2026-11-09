# Idea worksheet (no AI, no API key, just a pen)

Print this. Fill it in before you spend serious money or time. It uses the same
method as the jury, so you can later run the scorer on your own ratings.

Idea: ______________________________________________  Date: __________

## 1. Goal and limits (write numbers, not feelings)
- I want ₹ ________ per month, by ____________ (date).
- I can give ________ hours per week. Runway: ________ months.
- Money I can afford to lose on a test: ₹ ____________.
- I keep my day job while testing:  yes / no

## 2. Who pays, for what
- The person who pays is: ________________________________________
- Their problem, in their words: __________________________________
- What they do about it today, and what it costs them: _______________
- Is the payer also the user? yes / no. If no, can I reach the payer? ____

## 3. Talk to 10 buyers (the Mom Test rules)
Ask about the past, not the future. Do not pitch for the first ten minutes.
- "Tell me about the last time this problem happened."
- "What did you do about it? What did it cost you?"
- "What have you already tried or paid for?"
- "What is the hardest part?"
- "Who else is involved in deciding?"
- End with a costly ask: a deposit, an introduction, or a paid pilot.

| # | who | past behaviour / money spent | paid or pre-paid? (₹) |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
(Continue on the back. Under 5 conversations = no buyer evidence.)

## 4. What would have to be true
Write 5 things that must all be true. Mark each: S sourced, A assumed, U unknown.
1. ______________________________________________ [ S / A / U ]
2. ______________________________________________ [ S / A / U ]
3. ______________________________________________ [ S / A / U ]
4. ______________________________________________ [ S / A / U ]
5. ______________________________________________ [ S / A / U ]
If most are A or U, you are guessing. Test the weakest first.

## 5. Break-even (or use worksheets/break-even.xlsx)
- Price per sale: ₹ ______   Cost per sale: ₹ ______   Left over: ₹ ______
- Fixed costs per month: ₹ ______
- Sales needed per month to break even = fixed costs ÷ left over = ______
- Sales needed per month to hit my goal = (goal + fixed) ÷ left over = ______
- My hours per month: ______  → ₹ per hour at goal = goal ÷ hours = ______
- Is that rate better than what my time earns elsewhere? yes / no

## 6. Rate yourself 0-5 (be harsh; opinions are a 1)
| dimension | weight | my rating | evidence |
|---|---|---|---|
| pain | x3 | | |
| willingness to pay | x3 | | |
| reachability | x2 | | |
| founder fit | x2 | | |
| time to first sale | x2 | | |
| market ceiling | x1 | | |
| competition | x1 | | |
| economics | x1 | | |

Then type the ratings into a file and run
`python3 skills/jury/scripts/score.py --solo my-ratings.json`
(see the README for the file format). Without buyer evidence, pain is capped at
3 and willingness to pay at 2.

## 7. Kill criteria. Write these BEFORE you start. Do not edit them later.
| metric | I stop if | by (date) | then I |
|---|---|---|---|
| e.g. people who pre-pay | fewer than 5 of 30 | in 3 weeks | stop |
| | | | |
| | | | |

Signed: ____________   Review date: ____________
