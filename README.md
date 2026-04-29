# BRACIS — Brazilian Regulatory and Compliance Information Standard

**The first open, machine-readable compliance framework library with full coverage of Brazilian regulation.**

BRACIS provides 136 compliance frameworks as structured YAML — from LGPD and BCB 4.893 to ISO 27001 and NIST CSF — with 123 cross-framework mappings, 8 legal matrices, and a validated schema designed for DevSecOps pipelines.

Built by engineers, for engineers. GRC teams welcome.

---

## Why BRACIS

Every major compliance tooling platform covers GDPR, NIST, PCI-DSS, and ISO 27001.

None of them cover Brazilian regulation.

LGPD, BCB 4.893, ANVISA RDC 657, CFM 2.454/2026, ONS ARCiber, CVM, CNSP, Marco Civil — mandatory frameworks for any company operating in Brazil — exist nowhere in machine-readable format. No YAML. No structured controls. No cross-mappings to global frameworks. No integration with DevSecOps pipelines.

BRACIS fills that gap.

---

## What's included

**136 compliance frameworks** spanning Brazilian regulation, global standards, and regional requirements across financial services, healthcare, energy, telecommunications, government, and technology sectors.

**Brazilian regulation coverage** — the primary differentiator:
- LGPD and ANPD regulations
- BCB 4.893, BCB 85, BCB 304, BCB 3978, BCB 44, Conj. 2, IN 291
- CMN 4557, 4606, 4968 — CVM 35, 50, 88, 135, 175, 193
- CNSP 381, 393, 408, 416 — Open Finance — Open Insurance
- ANVISA RDC 657/2022 (SaMD) — ANVISA IN 134/2022 (BPF)
- CFM 2.314/2022 (Telemedicina) — CFM 2.454/2026 (IA na Medicina)
- ANS TISS — PEP
- ONS ARCiber — ANEEL 964 — ANATEL IoT
- Marco Civil — Decreto 8771 — Lei de Acesso à Informação
- ICP-Brasil — Governo Digital — GSI IN1/IN3/IN5
- Doutrina Cibernética — Marco Criptográfico — Crimes Cibernéticos

**123 cross-framework mappings** including:
- `lgpd_to_bacen-4893` — `gdpr_to_lgpd` — `cfm-ia_to_nist-ai-rmf`
- `eu-mdr_to_anvisa-samd` — `hipaa_to_iso-27001` — `nist-800-53_to_iso-27001`
- Full relationship graph available in `mappings/_framework-relationships.yaml`

**8 legal matrices** for cross-jurisdictional analysis:
- Breach notification requirements by jurisdiction
- Data subject rights by framework
- Cross-border transfer rules
- DPO requirements
- Data retention obligations
- Consent requirements
- Sensitive data categories
- Penalties and enforcement

**Industry taxonomies** covering financial services, healthcare, government, defense, and technology — with framework applicability mapped per sector.

**Validated schema** with JSON Schema definitions for frameworks, controls, and mappings. All content passes `yamllint` and schema validation on every commit.

---

## Structure

```
bracis/
├── frameworks/          # 136 compliance frameworks as YAML
│   └── {id}/
│       ├── framework.yaml      # Framework metadata and controls
│       ├── controls/           # Individual control files
│       └── i18n/               # Translations
├── mappings/            # 123 cross-framework mappings
├── legal/               # 8 legal matrices
├── industries/          # Industry taxonomies
├── regions/             # Regional taxonomies
├── techstacks/          # DevSecOps, GitOps, Platform Engineering
└── schema/              # JSON Schema for validation
```

---

## How to use

**Browse frameworks**

Every framework lives in `frameworks/{id}/framework.yaml` with full metadata, scope, regulatory authority, and structured controls.

**Use cross-mappings**

If you are already compliant with ISO 27001 and need to assess your gap against BCB 4.893, start with `mappings/bcb-85_to_bacen-4893.yaml`. Each mapping includes semantic confidence levels per control relationship.

**Validate your contributions**

```bash
pip install -r requirements.txt
python scripts/validate.py
```

**Integrate with your pipeline**

BRACIS provides the regulatory knowledge layer. Pipeline integration tooling is outside the scope of this repository.

---

## How BRACIS compares

| | BRACIS | CISO Assistant | OSCAL | OpenControl |
|---|---|---|---|---|
| Brazilian regulation | 63+ frameworks | None | None | None |
| Cross-framework mappings | 123 | Limited | Partial | None |
| Machine-readable YAML | Yes | Proprietary format | XML/JSON/YAML | YAML |
| DevSecOps integration | Roadmap | No | No | No |
| Active maintenance | Yes | Yes | Yes | No |
| License | MIT | AGPL-3.0 | Public domain | Apache 2.0 |

---

## Contributing

BRACIS is community-driven. Contributions welcome for:

- New Brazilian regulatory frameworks
- Cross-framework mappings
- Translations (`i18n/`)
- Schema improvements
- Corrections to existing controls

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

> **Issues and contributions are managed on GitLab:** [gitlab.com/perroud/bracis](https://gitlab.com/perroud/bracis)
> This GitHub repository is a read-only mirror.

---

## License

BRACIS framework content is licensed under the [MIT License](LICENSE).

Schema definitions, validation scripts, and documentation are also MIT.

Pipeline integration files are not part of this repository.

---

## Acknowledgments

BRACIS was initiated by [Eduardo Perroud](https://linkedin.com/in/eperroud).

---

*Para a documentação em português, veja [docs/README.pt-BR.md](docs/README.pt-BR.md).*
