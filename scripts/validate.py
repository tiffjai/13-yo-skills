#!/usr/bin/env python3
"""Validate this collection's structure; do not claim to test AI behavior."""

import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("Install development dependencies: python -m pip install -r requirements-dev.txt")


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {"13-yo-brainstorm", "13-yo-life-direction", "13-yo-tiny-experiments"}


def validate() -> list[str]:
    errors: list[str] = []
    found: set[str] = set()
    for skill in sorted((ROOT / "skills").iterdir()):
        if not skill.is_dir():
            continue
        found.add(skill.name)
        path = skill / "SKILL.md"
        if not path.is_file():
            errors.append(f"{skill.name}: missing SKILL.md")
            continue
        content = path.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not match:
            errors.append(f"{path.relative_to(ROOT)}: invalid frontmatter delimiters")
            continue
        try:
            meta = yaml.safe_load(match.group(1))
        except yaml.YAMLError as exc:
            errors.append(f"{skill.name}: invalid YAML: {exc}")
            continue
        if not isinstance(meta, dict) or set(meta) != {"name", "description"}:
            errors.append(f"{skill.name}: require exactly name and description metadata")
            continue
        if meta["name"] != skill.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill.name):
            errors.append(f"{skill.name}: invalid or mismatched name")
        if len(skill.name) > 64:
            errors.append(f"{skill.name}: name exceeds 64 characters")
        description = meta["description"]
        if not isinstance(description, str) or not 1 <= len(description.strip()) <= 1024:
            errors.append(f"{skill.name}: invalid description length/type")
        if len(content.splitlines()) >= 500:
            errors.append(f"{skill.name}: keep SKILL.md below 500 lines")
        for relative in ("agents/openai.yaml", "references/examples.md", "references/research.md"):
            if not (skill / relative).is_file():
                errors.append(f"{skill.name}: missing {relative}")
        ui_path = skill / "agents/openai.yaml"
        if ui_path.is_file():
            try:
                data = yaml.safe_load(ui_path.read_text(encoding="utf-8"))
                interface = data["interface"]
                label = interface["short_description"]
                if not isinstance(label, str) or not 25 <= len(label) <= 64:
                    errors.append(f"{skill.name}: invalid short description")
                if f"${skill.name}" not in interface["default_prompt"]:
                    errors.append(f"{skill.name}: default prompt must invoke the skill")
                if not interface.get("display_name"):
                    errors.append(f"{skill.name}: missing display name")
            except (yaml.YAMLError, KeyError, TypeError) as exc:
                errors.append(f"{skill.name}: invalid UI metadata: {exc}")
    if found != EXPECTED:
        errors.append(f"Expected {sorted(EXPECTED)}, found {sorted(found)}")

    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts:
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"\bTODO\b|\[INSERT|\[PLACEHOLDER", text):
            errors.append(f"{path.relative_to(ROOT)}: unfinished placeholder")
        for target in re.findall(r"(?<!!)\[[^\]]+\]\(([^\s)]+)\)", text):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:|#", target):
                continue
            relative = target.split("#", 1)[0]
            resolved = (path.parent / relative).resolve()
            if not resolved.is_relative_to(ROOT) or not resolved.exists():
                errors.append(f"{path.relative_to(ROOT)}: missing/outside local link {target}")

    try:
        cases = json.loads((ROOT / "evals/scenarios.json").read_text(encoding="utf-8"))
        seen = set()
        covered = set()
        if not isinstance(cases, list) or not cases:
            raise ValueError("cases must be a nonempty list")
        for case in cases:
            case_id = case["id"]
            if not isinstance(case_id, str) or not case_id or case_id in seen:
                errors.append("Duplicate, missing or invalid evaluation case id")
            seen.add(case_id)
            if case["skill"] not in EXPECTED:
                errors.append(f"{case_id}: unknown skill")
            covered.add(case["skill"])
            if not isinstance(case["prompt"], str) or not case["prompt"].strip():
                errors.append(f"{case_id}: empty prompt")
            for field in ("must_have", "must_not_have"):
                values = case[field]
                if not isinstance(values, list) or not values or not all(isinstance(v, str) and v.strip() for v in values):
                    errors.append(f"{case_id}: {field} must be a nonempty string list")
        if covered != EXPECTED:
            errors.append("Evaluation scenarios must cover every skill")
    except (OSError, ValueError, TypeError, KeyError) as exc:
        errors.append(f"Invalid evaluation scenarios: {exc}")
    return errors


if __name__ == "__main__":
    problems = validate()
    if problems:
        for problem in problems:
            print(f"FAIL: {problem}")
        sys.exit(1)
    print("PASS: 3 skill packages, UI metadata, local links and 9 evaluation scenarios.")
    print("Structural validation only; behavioral results are recorded separately.")
