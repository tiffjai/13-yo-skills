# Research, inspiration and limits

Sources checked on 7 November 2026. Distinguish a paper's measured findings from the collection author's design choices. None of these papers evaluates this collection, establishes age thirteen as optimal, or proves that a "genius" persona produces better advice.

## Psychology

| Source | What was studied | What it suggests for the design | Important limit |
| --- | --- | --- | --- |
| Zabelina & Robinson (2010), *Child's Play: Facilitating the Originality of Creative Output by a Priming Manipulation*. [DOI](https://doi.org/10.1037/a0015644), [paper](https://www.psychologytoday.com/sites/default/files/attachments/34246/zabelina-robinson-2010a.pdf) | 76 undergraduates randomly assigned to imagine a day off as themselves or as seven-year-olds; the child-imagery group subsequently gave more original creativity-test responses | Try playful reframing before evaluating ideas | Small human priming study; no test of this workflow, current LLMs, thirteen-year-olds or life outcomes |
| Chen et al. (2025), *A Strategic Mindset Enhances Children's Generation of Effective Strategies and Delay of Gratification Across Tasks*. [DOI](https://doi.org/10.1037/dev0001916), [paper](https://www.gregorywalton.com/uploads/4/9/4/4/49448111/chen_et_al_2025.pdf) | Two randomized experiments with 237 children aged five to six; strategy-eliciting questions supported strategy generation and longer waiting in delay tasks | When stuck, ask what alternative method could help | Tests self-regulation in preschool children, not adult life planning, creative AI or career success |
| Kalaivanan et al. (2026), *The association between cognitive flexibility and creativity across childhood and adolescence: a scoping review*. Published 5 June. [Paper](https://doi.org/10.1186/s40359-026-04886-8) | 14 studies; nine positive associations and five null or inconsistent findings; no consistent age pattern | Explore genuinely different perspectives and representations | Mixed definitions and measures; associations do not establish a causal intervention |
| Saretzki et al. (2026), *Are children really more creative than adults? A mixed-methods examination of creative performance and experience*. Published 21 October. [Paper](https://doi.org/10.1371/journal.pone.0346553) | 92 preschool children and 70 adults; adults had higher externally rated creative performance, while children generally reported stronger confidence and more positive engagement | Keep adult expertise while inviting enjoyment and experimentation | Age-group comparison, not a trial of combining these qualities; preschoolers are not adolescents |

## AI research

| Source | Relevant idea | Limit |
| --- | --- | --- |
| Zheng et al., *Take a Step Back: Evoking Reasoning via Abstraction in Large Language Models* (ICLR 2024; preprint 2023). [Paper](https://arxiv.org/abs/2310.06117) | Ask about higher-level principles before addressing a detailed problem | Benchmark results concern the models and tasks studied; gains are not established for this collection or current models |
| Milička et al. (2024), *Large language models are able to downplay their cognitive abilities to fit the persona they simulate*. [Paper](https://doi.org/10.1371/journal.pone.0298522) | In child-persona false-belief tasks, GPT-3.5 and GPT-4 could reproduce lower-capability behavior | Simulated ages were one to six; this does not show that a thirteen-year-old persona reduces performance. Preserve full model capability explicitly |

## Related open-source approaches

- [Anthropic Product Brainstorming](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/product-brainstorming/SKILL.md): problem exploration, divergent ideation, first-principles decomposition and testing assumptions.
- [ysskrishna AI Agent Skills](https://github.com/ysskrishna/ai-agent-skills): reusable thinking methods including first-principles and creative thinking.
- [Superpowers Brainstorming](https://github.com/obra/superpowers/blob/main/skills/brainstorming/SKILL.md): clarify intent, compare approaches and turn an idea into a design.

These are comparison points and inspiration, not dependencies, endorsements or evidence of effectiveness. The instruction text in this repository is an original synthesis; no third-party skill text is bundled.

## Authored design choices

The following are practical conventions introduced here, not results reported by the papers:

- Separate playful exploration from evidence and feasibility checks.
- Generate three to five options according to the brief.
- Ask at most two important clarification questions at a time.
- Center the user's own values, resources and capacity in life decisions.
- Use a small reversible test and explicitly permit inconclusive results.
- Default spending to zero and change a method after two uninformative attempts.

The last convention is a prompt to review the method, not a validated stopping threshold. A short experiment may produce helpful local observations; it does not establish causality, mental-health benefit or durable personal fit.

## How to evaluate the actual skills

Use the same model and task for three conditions: ordinary assistance, a persona-only instruction, and the structured skill. Blind the response order when practical. Compare usefulness, factual care, diversity of mechanisms, constraint fit, agency and burden. Repeat across cases; retain failures and counterexamples.

See [evaluation instructions](evals/README.md). Structural checks and a few fresh-context examples can detect obvious problems, but neither constitutes a controlled effectiveness study.
