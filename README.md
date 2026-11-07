# What Would a 13-Year-Old Genius Do?

**Stay curious. Keep your expertise. Try something small.**

Three reusable AI skills for people brainstorming ideas, figuring out life, or finding a next step they can actually try. Bring a young inventor's questions to adult problems, then check the answer against evidence and real constraints.

[廣東話指南](README.zh-HK.md) · [Research and limits](RESEARCH.md) · [Evaluation scenarios](evals/scenarios.json)

The name is a creative metaphor. Keep the AI's full reasoning and knowledge; borrow the curiosity, willingness to question habits and enjoyment of trying things. No special claim is made about age thirteen or genius.

## Choose a skill

| Skill | Use it for | What you get |
| --- | --- | --- |
| [`13-yo-brainstorm`](skills/13-yo-brainstorm/SKILL.md) | A product, project, business or everyday problem | Different approaches, a recommendation and a small test |
| [`13-yo-life-direction`](skills/13-yo-life-direction/SKILL.md) | Feeling lost, a career fork, competing ambitions or personal progression | A map of what matters, realistic directions and one manageable next step |
| [`13-yo-tiny-experiments`](skills/13-yo-tiny-experiments/SKILL.md) | An idea you want to test before committing | A question, an action, a budget, useful signals and a review decision |

Each skill works on its own. They can also form a sequence: explore possibilities, choose a direction, run a test, then revise. You can stop after any step.

## Install

With the [Skills CLI](https://skills.sh/docs/cli), run:

```bash
npx skills add tiffjai/13-yo-skills
```

Select the skills and supported agent you want in the installer. The CLI is a third-party installer and may download dependencies; the skill contents themselves require no code, API keys or paid service.

For manual installation, clone the repository and copy the complete folder of each desired skill from `skills/` into your agent's documented skills directory. Keep its `SKILL.md`, `agents/` and `references/` together. The format follows the [Agent Skills specification](https://agentskills.io/specification); discovery and invocation vary by host.

In a regular chat app without a skill loader, paste the chosen `SKILL.md` as instructions and describe your situation. Include relevant reference content if you want examples or the research background. This is manual prompting, not an installed skill.

## Try it

Use your agent's skill picker or invocation syntax. In clients that support `$skill-name`:

```text
Use $13-yo-brainstorm to help me reduce repetitive reporting work.
I have one hour, no software budget and cannot upload work data.
```

```text
Use $13-yo-life-direction. I want a change, but I need stable income.
Help me compare a few directions and choose one manageable next step.
```

```text
Use $13-yo-tiny-experiments. I might enjoy design work.
What could I try in two hours before paying for a course?
```

```text
用 $13-yo-life-direction，用廣東話幫我諗下一步。
我想穩定，但又想學新嘢；唔好一次過畀太多功課我。
```

Share only context you are comfortable sharing. Your priorities, available energy and real constraints matter more than an impressive plan.

## How the skills behave

- Ask useful basic questions and separate facts from assumptions.
- Explore genuinely different options, then assess their trade-offs.
- Respect money, time, access, care responsibilities and other people's boundaries.
- Treat rest, stability, connection and enjoyment as possible forms of progress.
- Recommend a small, reversible next step with a clear way to learn from it.
- Match your language, including written Cantonese when requested.
- Preserve your agency: no contact, spending, publishing or consequential changes without the necessary authorization.

These are reflection and problem-solving workflows, not therapy, diagnosis or predictions of your future. Research inspires parts of the design; the complete workflows have not been scientifically validated. See [RESEARCH.md](RESEARCH.md) for exactly what the cited papers support.

## Check or improve the collection

For maintainers, structural checks require Python 3.10+ and PyYAML:

```bash
python -m pip install -r requirements-dev.txt
python scripts/validate.py
```

The validator checks package metadata, references, examples and evaluation-case structure. It does not score model behavior. To evaluate behavior, use the prompts and rubric in [evals/README.md](evals/README.md). See [recorded checks](evals/RESULTS.md) for the current validation scope.

Contributions are welcome: improve a workflow, add an accessible example, or report a case where the advice became generic, overconfident or burdensome. Use fictional or consented examples and never submit private workplace or personal records. Do not present one good response as proof of universal effectiveness.

## License

[MIT](LICENSE). Created by [tiffjai](https://github.com/tiffjai).
