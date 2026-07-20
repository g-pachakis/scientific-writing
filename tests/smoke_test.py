#!/usr/bin/env python3
"""Standard-library smoke checks for the scientific-writing package."""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PACKAGE_NAME = "scientific-writing"
VERSION = "1.0.0"
SKILLS = {
    "write",
    "research-planning",
    "literature-and-citations",
    "data-and-evidence",
    "study-design-and-reporting",
    "drafting-and-notation",
    "figures-and-tables",
    "conclusions-and-abstract",
    "review-and-integrity",
    "document-output",
}
FORBIDDEN_TERMS = (
    re.compile(r"\b(?:LCA|MDPI|NTUA|SimaPro)\b", re.IGNORECASE),
    re.compile(r"scholarly-excellence", re.IGNORECASE),
    re.compile(r"\bWebSearch\b"),
    re.compile(r"\bRead\b[^\n]*\bpages\b"),
)
LINK = re.compile(r"(?<!!)\[[^]]*]\(([^)]+)\)")
NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
SKILL_MARKERS = {
    "write": ("Scope:", "Companion skills:", "Never fabricate"),
    "research-planning": ("evidence map", "Do not invent"),
    "literature-and-citations": ("Working library", "Cited set", "Never invent"),
    "data-and-evidence": ("Evidence ledger", "Verification state", "sensitive unpublished data"),
    "study-design-and-reporting": ("Route by study type", "reporting guideline", "Never invent"),
    "drafting-and-notation": ("Evidence-first drafting", "Notation registry", "Never invent"),
    "figures-and-tables": ("Caption contract", "Verify rendered output", "Never rely on color alone"),
    "conclusions-and-abstract": ("Abstract last", "stable results", "Do not"),
    "review-and-integrity": ("Select rigor", "Sensitive unpublished data", "Before a pass claim"),
    "document-output": ("Markdown", "Capability boundary", "Never"),
}


class Checks:
    def __init__(self):
        self.failures = []

    def require(self, condition, message):
        if not condition:
            self.failures.append(message)

    def json(self, relative_path):
        path = ROOT / relative_path
        if not path.is_file():
            self.failures.append(f"missing {relative_path}")
            return None
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, json.JSONDecodeError) as error:
            self.failures.append(f"invalid {relative_path}: {error}")
            return None
        if not isinstance(value, dict):
            self.failures.append(f"invalid {relative_path}: top level must be an object")
            return None
        return value


def package_checks(checks):
    package = checks.json("package.json")
    plugin = checks.json(".claude-plugin/plugin.json")
    marketplace = checks.json(".claude-plugin/marketplace.json")

    if package is not None:
        checks.require(package.get("name") == PACKAGE_NAME, "package.json name must be scientific-writing")
        checks.require(package.get("version") == VERSION, "package.json version must be 1.0.0")
        pi = package.get("pi")
        checks.require(isinstance(pi, dict), "package.json pi field must be an object")
        if isinstance(pi, dict):
            checks.require(pi.get("skills") == ["./skills"], "package.json must declare Pi skills path ./skills")
            checks.require(pi.get("prompts") == ["./prompts"], "package.json must declare Pi prompts path ./prompts")
    if plugin is not None:
        checks.require(plugin.get("name") == PACKAGE_NAME, "plugin name must be scientific-writing")
        checks.require(plugin.get("version") == VERSION, "plugin version must be 1.0.0")
    if marketplace is not None:
        checks.require(marketplace.get("name") == PACKAGE_NAME, "marketplace name must be scientific-writing")
        plugins = marketplace.get("plugins")
        checks.require(
            isinstance(plugins, list) and len(plugins) == 1 and isinstance(plugins[0], dict),
            "marketplace must declare exactly one plugin object",
        )
        if isinstance(plugins, list) and len(plugins) == 1 and isinstance(plugins[0], dict):
            entry = plugins[0]
            checks.require(entry.get("name") == PACKAGE_NAME, "marketplace plugin name must be scientific-writing")
            checks.require(entry.get("version") == VERSION, "marketplace plugin version must be 1.0.0")
            checks.require(entry.get("source") == "./", "marketplace plugin source must be ./")

    manifests = [value for value in (package, plugin) if value is not None]
    if marketplace is not None and isinstance(marketplace.get("plugins"), list) and marketplace["plugins"]:
        if isinstance(marketplace["plugins"][0], dict):
            manifests.append(marketplace["plugins"][0])
    if manifests:
        checks.require(
            all(item.get("name") == PACKAGE_NAME and item.get("version") == VERSION for item in manifests),
            "package, plugin, and marketplace name/version must agree",
        )

    for path in ROOT.rglob("*"):
        forbidden_name = path.name in {"__pycache__", ".DS_Store", "Thumbs.db"} or path.name.startswith("~$")
        if forbidden_name or (path.is_file() and path.suffix in {".pyc", ".pyo", ".pyd"}):
            checks.failures.append(f"forbidden generated file: {path.relative_to(ROOT)}")


def frontmatter(text):
    match = re.match(r"\A---\n(.*?)\n---(?:\n|\Z)", text, re.DOTALL)
    if not match:
        return None
    values = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            values[key.strip()] = value.strip().strip("'\"")
    return values


def skill_checks(checks, skill_name):
    if not NAME.fullmatch(skill_name):
        checks.failures.append(f"invalid requested skill name: {skill_name!r}")
        return
    path = ROOT / "skills" / skill_name / "SKILL.md"
    if not path.is_file():
        checks.failures.append(f"missing skills/{skill_name}/SKILL.md")
        return
    text = path.read_text(encoding="utf-8")
    metadata = frontmatter(text)
    checks.require(metadata is not None, f"skills/{skill_name}/SKILL.md must have YAML frontmatter")
    if metadata is not None:
        declared_name = metadata.get("name", "")
        description = metadata.get("description", "")
        checks.require(declared_name == skill_name, f"skill name {declared_name!r} must match directory {skill_name!r}")
        checks.require(bool(NAME.fullmatch(declared_name)), f"invalid skill name: {declared_name!r}")
        checks.require(len(declared_name) <= 64, f"skill {skill_name} name exceeds 64 characters")
        checks.require(bool(description), f"skill {skill_name} must have a description")
        checks.require(len(description) <= 1024, f"skill {skill_name} description exceeds 1024 characters")

    body = re.sub(r"\A---\n.*?\n---(?:\n|\Z)", "", text, count=1, flags=re.DOTALL).strip()
    checks.require(len(body.split()) >= 40, f"skill {skill_name} body must contain substantive guidance")
    for marker in SKILL_MARKERS.get(skill_name, ()):
        checks.require(marker.casefold() in body.casefold(), f"skill {skill_name} missing contract marker: {marker}")

    word_limit = 300 if skill_name == "write" else 500
    checks.require(len(text.split()) <= word_limit, f"skill {skill_name} exceeds {word_limit}-word target")

    for target in LINK.findall(text):
        target = target.strip().split(maxsplit=1)[0].strip("<>").split("#", 1)[0].split("?", 1)[0]
        if target and not re.match(r"^(?:[a-z]+:|/|#)", target, re.IGNORECASE):
            checks.require((path.parent / target).resolve().exists(), f"broken link in skill {skill_name}: {target}")
    for pattern in FORBIDDEN_TERMS:
        if pattern.search(text):
            checks.failures.append(f"forbidden runtime term in skill {skill_name}: {pattern.pattern}")


def prompt_checks(checks, required):
    prompt = ROOT / "prompts" / "scientific-writing.md"
    if not prompt.is_file():
        if required:
            checks.failures.append("missing prompts/scientific-writing.md")
        return
    text = prompt.read_text(encoding="utf-8")
    metadata = frontmatter(text)
    checks.require(metadata is not None, "Pi prompt must have YAML frontmatter")
    if metadata is not None:
        checks.require(
            metadata.get("description") == "Route a scientific-writing task to the minimum relevant workflow",
            "Pi prompt description must match package contract",
        )
        checks.require(metadata.get("argument-hint") == "[task]", "Pi prompt argument hint must be [task]")
    checks.require("write" in text and "$ARGUMENTS" in text, "Pi prompt must route arguments to write")


def full_checks(checks):
    skills_dir = ROOT / "skills"
    discovered = {path.name for path in skills_dir.glob("*") if path.is_dir()}
    checks.require(discovered == SKILLS, f"skill inventory must be exactly: {', '.join(sorted(SKILLS))}")
    prompt_checks(checks, required=True)

    readme = ROOT / "README.md"
    if not readme.is_file():
        checks.failures.append("missing README.md")
    else:
        text = readme.read_text(encoding="utf-8")
        rows = set(re.findall(r"^\|\s*`([a-z0-9-]+)`\s*\|", text, re.MULTILINE))
        checks.require(rows == SKILLS, "README skill table must list exactly the complete skill inventory")
        required_docs = (
            "pi install git:github.com/g-pachakis/scientific-writing",
            "/scientific-writing",
            "/skill:write",
            "/plugin marketplace add g-pachakis/scientific-writing",
            "/plugin install scientific-writing@scientific-writing",
            "/scientific-writing:write",
        )
        for command in required_docs:
            checks.require(command in text, f"README must document exact command: {command}")

    runtime_paths = [ROOT / "README.md", *(ROOT / "prompts").glob("*.md"), *(ROOT / "skills").rglob("*.md")]
    for path in runtime_paths:
        if path.is_file():
            text = path.read_text(encoding="utf-8")
            for pattern in FORBIDDEN_TERMS:
                if pattern.search(text):
                    checks.failures.append(f"forbidden stale term in {path.relative_to(ROOT)}: {pattern.pattern}")


def main():
    parser = argparse.ArgumentParser()
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--package", action="store_true", help="check package manifests")
    modes.add_argument("--skill", metavar="NAME", help="check one skill")
    modes.add_argument("--full", action="store_true", help="check complete package")
    args = parser.parse_args()

    checks = Checks()
    if args.skill:
        skill_checks(checks, args.skill)
    else:
        package_checks(checks)
        if args.full:
            for skill_name in sorted(SKILLS):
                skill_checks(checks, skill_name)
            full_checks(checks)
        elif not args.package:
            for path in sorted((ROOT / "skills").glob("*")):
                if path.is_dir():
                    skill_checks(checks, path.name)
            prompt_checks(checks, required=False)

    if checks.failures:
        for failure in checks.failures:
            print(f"FAIL: {failure}")
        return 1
    print("PASS: smoke checks")
    return 0


if __name__ == "__main__":
    sys.exit(main())
