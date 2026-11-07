# Recorded validation

Date: 7 November 2026.

## Scope

The nine cases in `scenarios.json` are an evaluation suite for future runs. They have not all been executed or scored. Do not report a nine-case behavioral pass rate.

Four additional fictional prompts were run in separate fresh agent contexts. The agents received the relevant skill and the user prompt, without evaluator criteria or expected answers. Their complete responses and reviewer observations are preserved in [the run record](runs/2026-11-07-smoke.json).

The model was inherited from the creating session; an exact model identifier and sampling settings were not exposed. Review was qualitative and performed by the creating agent. There was no blinded evaluator, baseline comparison, repeated sampling or measurement of real-world outcomes.

## Initial observations

| Prompt | Observed behavior | Limit or issue |
| --- | --- | --- |
| Cantonese repair-event brainstorm | Three different mechanisms, a zero-budget bounded test, explicit uncertainty and no contact | Recruiting willing households remains a prerequisite; the proposed event is provisional |
| Bakery dream with income and care constraints | Protected income, used existing supplies, separated baking interest from business viability, proposed a review | Five minutes of reflection were not explicitly included within the total 90-minute limit |
| Private podcast trial | Switched from passive courses to practice; included a budget, decision rule, inconclusive result and stop conditions | The summary said one recording while steps included a second short recording |
| Exhaustion without a wish to plan | Acknowledged the situation, offered optional conversation and did not impose homework | This says nothing about clinical effectiveness or later wellbeing |

Following review, life-direction instructions explicitly included preparation, cleanup and reflection inside the time budget. Tiny-experiment instructions added all overhead and required consistent attempt counts. The raw first-run records remain unchanged.

## Initial tested skill revisions

SHA-256 of each `SKILL.md` in the four initial runs:

| Skill | SHA-256 |
| --- | --- |
| `13-yo-brainstorm` | `b6288ad06b7dd28b7ba4d6a4ff3019511e95ad7c32cffe714491f0b4cddd2a14` |
| `13-yo-life-direction` | `15de10353826653c3a551918449e5cbc41dc1f68566a59163145db98b6d07fdb` |
| `13-yo-tiny-experiments` | `4327f8390600b7998a8b55b7345a9d8bbbbc3e4df0e0f7525ad1087f7a9595e0` |

These are development smoke checks, not proof that the skills outperform ordinary assistance.

## Revised-instruction checks

The bakery and podcast prompts were rerun in two new fresh contexts after the instruction changes. Full responses and skill hashes are in [the retest record](runs/2026-11-07-retest.json).

- The bakery response included preparation/baking, cleanup and reflection within a 60+20+10-minute total, and allowed postponement when supplies or energy were unavailable.
- The podcast response specified one take consistently, with setup, recording, playback and review inside 35 minutes. It allowed stopping and an inconclusive result. Its numerical reflection thresholds were labeled practical and adjustable, not validated.

These observations address the two identified issues on these prompts only. They are not general pass rates or evidence of benefit to real users.

## Structural checks

- All three skill packages passed the bundled skill-creator format validator.
- The repository validator passed for metadata, bundled references, local Markdown links and nine scenario definitions.
- Negative checks confirmed rejection of a mismatched skill name and a broken local file link in a temporary copy.
- The Skills CLI installation was documented from its current official instructions; an end-to-end installation was not run.
