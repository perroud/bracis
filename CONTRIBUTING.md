# Contributing to BRACIS

Thank you for your interest in contributing. BRACIS is community-driven and every contribution — from a typo fix to a new regulatory framework — makes the project more useful for engineers and GRC teams across Brazil and beyond.

---

## What you can contribute

**New frameworks**
Brazilian regulatory frameworks are the primary focus, but global and regional frameworks are welcome if they are not yet in the repository and follow the schema.

**Cross-framework mappings**
If you identify a meaningful relationship between two frameworks already in BRACIS, a new mapping file is a high-value contribution.

**Corrections**
Regulatory text changes. Control descriptions that are inaccurate or outdated. Metadata errors. All corrections are welcome.

**Translations**
Each framework supports `i18n/` directories. If a framework exists only in English and you can provide a Portuguese translation, or vice versa, that is a valuable contribution.

**Schema improvements**
If you find a structural limitation in the framework, control, or mapping schema, open an issue to discuss before submitting a PR.

---

## Before you start

Check the existing frameworks in `frameworks/` and mappings in `mappings/` to avoid duplicating work already in progress.

For significant additions — a new regulatory framework or a batch of mappings — open an issue first describing what you intend to add. This avoids wasted effort if the contribution overlaps with something already being worked on.

---

## Framework file structure

Every framework follows this structure:

```
frameworks/{id}/
├── framework.yaml        # Required
├── controls/             # Required — one file per control
│   └── {control-id}.yaml
└── i18n/                 # Optional — translations
    └── pt-BR/
        └── framework.yaml
```

Framework IDs use lowercase kebab-case based on the issuing authority and identifier. Examples: `lgpd`, `bacen-4893`, `anvisa-samd`, `iso-27001-2022`.

---

## Quality criteria

Every contribution must pass validation before being accepted:

```bash
pip install -r requirements.txt
python scripts/validate.py
```

Beyond automated validation, the review will assess:

**Accuracy** — Controls must reflect the actual text and intent of the regulatory source. Paraphrasing is acceptable. Distortion is not. If you are unsure about a control's interpretation, note it in the PR description.

**Completeness** — A framework contribution should cover the scope it claims. A partial framework is acceptable if the scope is explicitly documented in `framework.yaml`.

**Traceability** — Every control must reference its source: the article, clause, or section of the original regulation. Without traceability, the control has no audit value.

**Consistency** — Follow the naming conventions, field formats, and structural patterns already established in the repository. When in doubt, look at `frameworks/lgpd/` or `frameworks/iso-27001-2022/` as reference implementations.

**Mappings confidence** — Cross-framework mappings must include a semantic confidence level per relationship. Do not map controls that are loosely related without noting the confidence level accurately.

---

## Submitting a pull request

Fork the repository and create a branch named descriptively:
- `add/framework-{id}` for new frameworks
- `add/mapping-{source}-to-{target}` for new mappings
- `fix/{id}-{description}` for corrections
- `i18n/{id}-{language}` for translations

Write a clear PR description explaining what you added or changed and why. For new frameworks, include a reference to the regulatory source.

All PRs require at least one review before merge. Reviews focus on the quality criteria above, not on style preferences.

---

## What will not be merged

Frameworks or controls without traceable regulatory sources.

Content that misrepresents the regulatory text in ways that could mislead an audit.

Pipeline integration files of any kind. BRACIS is the regulatory knowledge layer. Integration tooling is out of scope.

---

## Questions

Open an issue. Questions about regulatory interpretation, schema design, or contribution scope are all valid topics for public discussion.

---

*Para contribuir em português, as mesmas diretrizes se aplicam. A documentação de contribuição em português estará disponível em breve.*

*Para a versao em portugues, veja [CONTRIBUTING.pt-BR.md](CONTRIBUTING.pt-BR.md).*
