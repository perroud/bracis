# BRACIS — Brazilian Regulatory and Compliance Information Standard

**O primeiro repositório aberto de frameworks de compliance com cobertura completa da regulação brasileira em formato machine-readable.**

BRACIS disponibiliza 136 frameworks de compliance como YAML estruturado — de LGPD e BCB 4.893 a ISO 27001 e NIST CSF — com 123 mapeamentos cruzados, 8 matrizes legais e schema validado projetado para pipelines DevSecOps.

Construído por engenheiros, para engenheiros. Times de GRC são bem-vindos.

---

## Por que o BRACIS existe

Toda plataforma relevante de compliance cobre GDPR, NIST, PCI-DSS e ISO 27001.

Nenhuma cobre a regulação brasileira.

LGPD, BCB 4.893, ANVISA RDC 657, CFM 2.454/2026, ONS ARCiber, CVM, CNSP, Marco Civil — frameworks obrigatórios para qualquer empresa operando no Brasil — não existem em nenhum lugar em formato machine-readable. Sem YAML. Sem controles estruturados. Sem mapeamentos cruzados com frameworks globais. Sem integração com pipelines DevSecOps.

O BRACIS preenche essa lacuna.

---

## O que está incluído

**136 frameworks de compliance** cobrindo regulação brasileira, padrões globais e requisitos regionais nos setores financeiro, saúde, energia, telecomunicações, governo e tecnologia.

**Cobertura da regulação brasileira** — o diferencial principal:
- LGPD e regulamentos da ANPD
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

**123 mapeamentos cruzados** incluindo:
- `lgpd_to_bacen-4893` — `gdpr_to_lgpd` — `cfm-ia_to_nist-ai-rmf`
- `eu-mdr_to_anvisa-samd` — `hipaa_to_iso-27001` — `nist-800-53_to_iso-27001`
- Grafo completo de relacionamentos disponível em `mappings/_framework-relationships.yaml`

**8 matrizes legais** para análise comparativa entre jurisdições:
- Requisitos de notificação de incidentes por jurisdição
- Direitos do titular por framework
- Regras de transferência internacional de dados
- Requisitos de DPO
- Obrigações de retenção de dados
- Requisitos de consentimento
- Categorias de dados sensíveis
- Penalidades e enforcement

**Taxonomias setoriais** cobrindo serviços financeiros, saúde, governo, defesa e tecnologia — com aplicabilidade de frameworks mapeada por setor.

**Schema validado** com definições JSON Schema para frameworks, controles e mapeamentos. Todo conteúdo passa por `yamllint` e validação de schema em cada commit.

---

## Estrutura

```
bracis/
├── frameworks/          # 136 frameworks de compliance em YAML
│   └── {id}/
│       ├── framework.yaml      # Metadados e controles do framework
│       ├── controls/           # Arquivos de controle individuais
│       └── i18n/               # Traduções
├── mappings/            # 123 mapeamentos cruzados
├── legal/               # 8 matrizes legais
├── industries/          # Taxonomias setoriais
├── regions/             # Taxonomias regionais
├── techstacks/          # DevSecOps, GitOps, Platform Engineering
└── schema/              # JSON Schema para validação
```

---

## Como usar

**Navegar pelos frameworks**

Cada framework está em `frameworks/{id}/framework.yaml` com metadados completos, escopo, autoridade regulatória e controles estruturados.

**Usar os mapeamentos cruzados**

Se você já tem conformidade com ISO 27001 e precisa avaliar sua lacuna em relação ao BCB 4.893, comece com `mappings/bcb-85_to_bacen-4893.yaml`. Cada mapeamento inclui níveis de confiança semântica por relacionamento de controle.

**Validar suas contribuições**

```bash
pip install -r requirements.txt
python scripts/validate.py
```

**Integrar com seu pipeline**

O BRACIS fornece a camada de conhecimento regulatório. Tooling de integração com pipeline está fora do escopo deste repositório.

---

## Como o BRACIS se compara

| | BRACIS | CISO Assistant | OSCAL | OpenControl |
|---|---|---|---|---|
| Regulação brasileira | 63+ frameworks | Nenhum | Nenhum | Nenhum |
| Mapeamentos cruzados | 123 | Limitado | Parcial | Nenhum |
| YAML machine-readable | Sim | Formato proprietário | XML/JSON/YAML | YAML |
| Integração DevSecOps | Roadmap | Não | Não | Não |
| Manutenção ativa | Sim | Sim | Sim | Não |
| Licença | MIT | AGPL-3.0 | Domínio público | Apache 2.0 |

---

## Contribuindo

O BRACIS é construído pela comunidade. Contribuições são bem-vindas para:

- Novos frameworks regulatórios brasileiros
- Mapeamentos cruzados
- Traduções (`i18n/`)
- Melhorias de schema
- Correções em controles existentes

Consulte [CONTRIBUTING.md](../CONTRIBUTING.md) para as diretrizes.

> **Issues e contribuições são gerenciadas no GitLab:** [gitlab.com/perroud/bracis](https://gitlab.com/perroud/bracis)
> Este repositório GitHub é um mirror read-only.

---

## Licença

O conteúdo dos frameworks BRACIS está licenciado sob a [Licença MIT](../LICENSE).

Definições de schema, scripts de validação e documentação também são MIT.

Arquivos de integração com pipeline não fazem parte deste repositório.

---

## Agradecimentos

O BRACIS foi iniciado por [Eduardo Perroud](https://linkedin.com/in/eperroud).

---

*For the English documentation, see [README.md](../README.md).*
