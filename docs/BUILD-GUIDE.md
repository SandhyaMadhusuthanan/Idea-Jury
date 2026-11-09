# How to build and publish this on GitHub

A step-by-step guide from an empty folder to something other people can install in Claude Code with two commands.

## What you are building

A **Claude Code plugin**. A plugin is a folder that bundles skills and subagents. Anyone can install it from a GitHub repo.

```
idea-jury/
├── .claude-plugin/
│   ├── plugin.json         identifies the plugin
│   └── marketplace.json    lets people install it from GitHub
├── agents/                 the eight jurors (one .md file each)
├── skills/
│   ├── jury/               the judge: runs the trial
│   │   ├── SKILL.md
│   │   ├── rubric.yaml     every weight and threshold, editable
│   │   ├── scripts/score.py   applies the rubric, prints the arithmetic
│   │   └── references/     verdict rules, report template, India lens
│   └── retest/             re-scores after your test
├── worksheets/             printable worksheet + break-even.xlsx (no AI needed)
├── examples/               a worked example
├── docs/                   this guide + METHOD.md
├── README.md
└── LICENSE
```

Everything the skill reads at run time (rubric, script, rules, lens) sits inside `skills/jury/`, so it still works when someone installs only the skills folder. Worksheets and examples are for humans and live at the root.

Rule to remember: only `plugin.json` and `marketplace.json` go inside `.claude-plugin/`. Everything else sits at the repo root.

## Step 1. Prerequisites

- A GitHub account
- Git installed (`git --version`)
- Claude Code installed and logged in
- Optional: the GitHub CLI (`gh`), which makes creating the repo one command

## Step 2. Create the repo on GitHub

Browser: github.com, click **New repository**, name it `idea-jury`, set it to **Public**, leave "Add a README" unticked, click **Create repository**.

Or with the CLI:

```
gh repo create idea-jury --public --clone
cd idea-jury
```

Browser route, then clone it:

```
git clone https://github.com/YOUR-GITHUB-USERNAME/idea-jury.git
cd idea-jury
```

## Step 3. Add the files

Copy in everything from the `idea-jury.zip` I gave you (unzip it and copy its contents into your cloned folder), or create the structure by hand:

```
mkdir -p .claude-plugin agents skills/jury/references skills/jury/scripts skills/retest worksheets examples docs
```

Then replace the placeholders:

- `YOUR-GITHUB-USERNAME` in `README.md` and `.claude-plugin/marketplace.json`
- `YOUR NAME` in `LICENSE`

## Step 4. Understand the three kinds of file

0. **The rulebook** (`skills/jury/rubric.yaml` and `scripts/score.py`): all weights and thresholds in one editable file, applied by a small script, so the verdict is auditable rather than a mood.
1. **A juror** (`agents/cfo.md`): a short header (name, description, tools) then instructions. The jurors can only use web search and fetch, so they cannot touch your files.
2. **The judge** (`skills/jury/SKILL.md`): the instructions Claude follows when you type `/jury`. It builds the case file, launches all eight jurors in one message so they run in parallel, tallies, and writes the report.
3. **The rules** (`skills/jury/references/`): the verdict logic and the report layout. Kept in separate files so you can edit them without touching the workflow.

## Step 5. Test it locally before you publish

Open a scratch folder (not the repo) and start Claude Code with the plugin loaded:

```
claude --plugin-dir /path/to/idea-jury
```

Then check, in order:

1. Type `/agents`. You should see the eight jurors listed.
2. Type `/` and look for `jury`. It appears as `idea-jury:jury`.
3. Run a quick trial first: `/idea-jury:jury quick an app that tells freelancers when clients are late paying`
4. Confirm a file appears in `idea-jury-reports/`.
5. Run the full jury once.

6. Run `/idea-jury:retest <slug> <made-up results>` on the report you just made.

Also test the scorer on its own, with no Claude involved:

```
pip install pyyaml
python3 skills/jury/scripts/score.py --solo my-ratings.json
```

(The README shows the file format.) Change a weight in `rubric.yaml`, run it again, and confirm the result changes. That is how you know the rulebook, not the AI, is deciding.

After you edit any file, run `/reload-plugins` or restart Claude Code.

## Step 6. Commit and push

```
git add .
git commit -m "idea-jury: eight-juror business idea trial"
git push origin main
```

## Step 7. Test the install the way a stranger would

Start a new Claude Code session in any folder and run:

```
/plugin marketplace add YOUR-GITHUB-USERNAME/idea-jury
/plugin install idea-jury@idea-jury
```

Restart if asked, type `/agents`, and run a trial. If this works, anyone can do the same.

## Step 8. Make the repo worth installing

- Add a real sample report to the README. Run the jury on an idea, then paste the verdict section in.
- Add repository topics: `claude-code`, `claude-skills`, `claude-plugin`, `subagents`, `startup`.
- Add a one-line description to the repo's About box.
- Tag your first release:

```
git tag v1.0.0
git push --tags
```

## Step 9. Improve it over time

- Bump `"version"` in `plugin.json` whenever you change behaviour (1.0.1 for fixes, 1.1.0 for new features). Users only receive updates when the version changes.
- Run 5 to 10 real ideas through it. Note where the jurors agree too easily or give generic advice, then sharpen that juror's file.
- Good next features: more lenses (another state or country, agriculture, tuition centres), a juror for your niche, a `compare` mode that ranks two ideas, a one-page PDF export of the report.
- Add real worked examples to `examples/`. Run an actual jury on a real local idea and publish the report with the founder's permission: it is the most convincing thing in the repo.

## Troubleshooting

| problem | fix |
|---|---|
| `/jury` not found | with the plugin it is `/idea-jury:jury`; with manual install, check `~/.claude/skills/jury/SKILL.md` exists |
| `/agents` shows no jurors | agent files must be in `agents/` at the repo root, not inside `.claude-plugin/` |
| Jurors run one at a time | the judge must launch them in a single message; check `SKILL.md` Step 1 is unchanged |
| It stops after the questions | that is intended: answer them, or say "just run it" |
| Scorer says PyYAML missing | `pip install pyyaml`; or Claude applies `rubric.yaml` by hand |
| Everyone votes the same | tighten each juror's stance in `agents/`, and keep the rule that unsupported claims are struck |
| Uses too much quota | use `quick` mode, or remove jurors from the list in `SKILL.md` |
| Install says marketplace not found | the repo must be public and contain `.claude-plugin/marketplace.json` |

Plugin features change between Claude Code versions. If a command behaves differently, check https://code.claude.com/docs for the current plugin documentation.
