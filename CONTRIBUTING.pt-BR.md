# Contribuindo para o BRACIS

Obrigado pelo interesse em contribuir. O BRACIS é construído pela comunidade e cada contribuição — de uma correção de texto a um novo framework regulatório — torna o projeto mais útil para engenheiros e times de GRC no Brasil e no mundo.

---

## O que você pode contribuir

**Novos frameworks**
Frameworks regulatórios brasileiros são o foco principal, mas frameworks globais e regionais são bem-vindos se ainda não estiverem no repositório e seguirem o schema.

**Mapeamentos cruzados**
Se você identificar uma relação significativa entre dois frameworks já presentes no BRACIS, um novo arquivo de mapeamento é uma contribuição de alto valor.

**Correções**
Mudanças no texto regulatório. Descrições de controles imprecisas ou desatualizadas. Erros de metadados. Todas as correções são bem-vindas.

**Traduções**
Cada framework suporta diretórios `i18n/`. Se um framework existe apenas em inglês e você pode fornecer uma tradução em português, ou vice-versa, essa é uma contribuição valiosa.

**Melhorias de schema**
Se você encontrar uma limitação estrutural no schema de framework, controle ou mapeamento, abra uma issue para discutir antes de submeter um PR.

---

## Antes de começar

Verifique os frameworks existentes em `frameworks/` e os mapeamentos em `mappings/` para evitar duplicar trabalho já em andamento.

Para adições significativas — um novo framework regulatório ou um lote de mapeamentos — abra uma issue primeiro descrevendo o que pretende adicionar. Isso evita esforço desperdiçado caso a contribuição se sobreponha a algo já em desenvolvimento.

---

## Estrutura de arquivos de framework

Cada framework segue esta estrutura:

```
frameworks/{id}/
├── framework.yaml        # Obrigatório
├── controls/             # Obrigatório — um arquivo por controle
│   └── {control-id}.yaml
└── i18n/                 # Opcional — traduções
    └── pt-BR/
        └── framework.yaml
```

IDs de framework usam kebab-case minúsculo baseado na autoridade emissora e identificador. Exemplos: `lgpd`, `bacen-4893`, `anvisa-samd`, `iso-27001-2022`.

---

## Critérios de qualidade

Toda contribuição deve passar na validação antes de ser aceita:

```bash
pip install -r requirements.txt
python scripts/validate.py
```

Além da validação automatizada, a revisão avaliará:

**Precisão** — Os controles devem refletir o texto e a intenção real da fonte regulatória. Paráfrase é aceitável. Distorção não é. Se você tiver dúvida sobre a interpretação de um controle, indique isso na descrição do PR.

**Completude** — Uma contribuição de framework deve cobrir o escopo que declara. Um framework parcial é aceitável se o escopo estiver explicitamente documentado em `framework.yaml`.

**Rastreabilidade** — Cada controle deve referenciar sua fonte: o artigo, cláusula ou seção da regulação original. Sem rastreabilidade, o controle não tem valor em auditoria.

**Consistência** — Siga as convenções de nomenclatura, formatos de campo e padrões estruturais já estabelecidos no repositório. Em caso de dúvida, consulte `frameworks/lgpd/` ou `frameworks/iso-27001-2022/` como implementações de referência.

**Confiança nos mapeamentos** — Mapeamentos cruzados devem incluir um nível de confiança semântica por relação. Não mapeie controles que sejam apenas vagamente relacionados sem indicar o nível de confiança com precisão.

---

## Submetendo um pull request

Faça fork do repositório e crie um branch com nome descritivo:
- `add/framework-{id}` para novos frameworks
- `add/mapping-{source}-to-{target}` para novos mapeamentos
- `fix/{id}-{description}` para correções
- `i18n/{id}-{language}` para traduções

Escreva uma descrição clara no PR explicando o que você adicionou ou alterou e por quê. Para novos frameworks, inclua uma referência à fonte regulatória.

Todos os PRs exigem pelo menos uma revisão antes do merge. As revisões focam nos critérios de qualidade acima, não em preferências de estilo.

---

## O que não será aceito

Frameworks ou controles sem fontes regulatórias rastreáveis.

Conteúdo que represente erroneamente o texto regulatório de formas que possam induzir uma auditoria ao erro.

Arquivos de integração com pipeline de qualquer tipo. O BRACIS é a camada de conhecimento regulatório. Tooling de integração está fora do escopo.

---

## Dúvidas

Abra uma issue. Perguntas sobre interpretação regulatória, design de schema ou escopo de contribuição são todos tópicos válidos para discussão pública.

---

*For the English version, see [CONTRIBUTING.md](CONTRIBUTING.md).*
