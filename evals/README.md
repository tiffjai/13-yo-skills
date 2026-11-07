# Behavioral evaluation

Use fictional scenarios from [scenarios.json](scenarios.json). Each case contains a prompt, a target skill and observable criteria. Give a fresh agent the skill and user prompt only. Keep the criteria and other examples out of its context when testing transfer.

## Procedure

1. Record model, model settings when exposed, date, exact prompt and skill revision.
2. Run the selected skill on the prompt in a fresh context. Do not send messages or change external systems.
3. Preserve the complete response. Check each must-have and must-not-have item, citing evidence from the response.
4. Mark pass only when all criteria are met. Mark ambiguous criteria as unclear, not pass. Record incomplete evaluations honestly.
5. Review failure patterns and adjust instructions where useful. Retest with a new scenario as well as the original.

## Optional comparison

Compare the same prompt with ordinary assistance, a persona-only instruction and the complete skill. Use the same model and comparable generation settings, shuffle response order for reviewers, and repeat across tasks.

Assess:

- Usefulness and clarity of the next decision.
- Accuracy and explicit handling of uncertainty.
- Distinct mechanisms rather than cosmetic idea variation.
- Fit to time, money, energy and other stated constraints.
- Respect for user agency, privacy and consent.
- Emotional fit and the burden imposed by the answer.

Do not infer psychological or clinical benefits from response-quality ratings. Do not publish personal user conversations without explicit consent.
