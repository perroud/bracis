[Read in English](diagrams-engineering.md)

# Diagramas de Engenharia

Guias visuais para desenvolvedores, profissionais de DevSecOps e engenheiros de plataforma que trabalham com o BRACIS.

---

## 1. Arquitetura de Três Camadas de Controle

Cada arquivo de controle (`controls/*.yaml`) segue uma estrutura consistente de quatro camadas. A Camada 1 preserva o texto regulatório original na íntegra (no idioma de origem). A Camada 2 fornece orientação interpretativa em inglês. A Camada 3 detalha a implementação por techstack, com ferramentas concretas. A Camada 4 vincula o controle a frameworks relacionados.

```mermaid
mindmap
  root((Arquivo de Controle))
    Camada 1 statement
      texto
        Lei brasileira em pt-BR
        NIST/ISO/EU em inglês
    Camada 2 guidance
      texto
        O que o requisito significa
        Contexto interpretativo
    Camada 3 implementation_guidance
      platform_engineering
        ferramentas
          Vault
          Keycloak
          OPA
          Backstage
      devsecops
        ferramentas
          Checkov
          Trivy
          Semgrep
          OWASP ZAP
      secops
        ferramentas
          Splunk
          CrowdStrike
          SailPoint
    Camada 4 legal_references
      framework_id
      artigos
      tipo de relacao
```

---

## 2. Cadeias de Derivação de Frameworks -- Internacional

Este diagrama mapeia as relacoes de derivacao e complementaridade entre padroes internacionais organizados por familia.

```mermaid
mindmap
  root((Padroes Internacionais))
    Familia ISO
      ISO 27001
        ISO 27701 Privacidade
        ISO 27017 Cloud
        ISO 27018 PII em Cloud
        ISO 27005 Riscos
        ISO 27035 Incidentes
      ISO 22301 BCM
      ISO 42001 Gestao de IA
      ISO 31000 Gestao de Riscos
    Familia NIST
      NIST 800-53
        NIST 800-171
          CMMC v2
        FedRAMP
        FISMA
      NIST CSF v2
      NIST AI RMF
    Familia PCI
      PCI DSS v4
        PCI PIN
        PCI 3DS
        PCI SSF
        PCI P2PE
    Outros Padroes
      COSO
        SOC 2
      CSA CCM v4
      TISAX
    Regulacoes
      GDPR
      EU AI Act
```

---

## 3. Cadeias de Derivação de Frameworks -- Brasil

O ecossistema regulatório brasileiro é fortemente interconectado. Reguladores setoriais derivam requisitos de cibersegurança e privacidade da LGPD e normas setoriais específicas.

```mermaid
mindmap
  root((Ecossistema Regulatorio Brasileiro))
    Privacidade e Internet
      LGPD
      Marco Civil da Internet
      Decreto 8.771
    BCB Banco Central
      Bacen 4.893 Ciberseguranca
      BCB 85 Instituicoes de Pagamento
      BCB 3.978 PLD FT
      BCB 44
      BCB 304
      BCB Conj.2
      IN 291
    CMN Conselho Monetario
      CMN 4.557 Gestao de Riscos
      CMN 4.968
      CMN 4.606
    CVM Mercado de Capitais
      CVM 35
      CVM 50
      CVM 88
      CVM 175
      CVM 135
      CVM 193
    CNSP SUSEP Seguros
      CNSP 381
      CNSP 416
      CNSP 393
      CNSP 408
      SUSEP 638
      SUSEP 612
    GSI Governo Federal
      PNSI
      PNCiber
      IN GSI 1
      IN GSI 3
      IN GSI 5
      ReGIC
      PNSIC
    Saude
      ANVISA 134
      ANVISA SaMD
      ANVISA BPF
      CFM Telemedicina
      CFM IA
      ANS TISS
      PEP
      Receituario Digital
    Outros
      LAI
      Gov Digital
      ICP-Brasil
      Crimes Ciberneticos
      ANEEL 964
      ONS ARCiber
```

---

## 4. Estrutura do Repositório

O repositório segue uma estrutura plana e previsível. Cada um dos 136 frameworks vive em seu próprio diretório em `frameworks/`, contendo os metadados, controles organizados por família e traduções opcionais.

```mermaid
flowchart TD
    ROOT["bracis/"]

    subgraph FW["frameworks/ (136 diretorios)"]
        fw_yaml["framework.yaml"]
        fw_controls["controls/familia/controle.yaml"]
        fw_i18n["i18n/ (opcional)"]
    end

    subgraph MAP["mappings/ (123 arquivos)"]
        map_rel["_framework-relationships.yaml"]
        map_cat["_category-correlation.yaml"]
        map_pair["source_to_target.yaml"]
    end

    subgraph LEG["legal/ (8 matrizes)"]
        leg_breach["notificacao de incidentes"]
        leg_penalties["penalidades"]
        leg_consent["requisitos de consentimento"]
        leg_xborder["transferencia internacional"]
        leg_retention["retencao de dados"]
        leg_rights["direitos dos titulares"]
        leg_sensitive["dados sensiveis"]
        leg_dpo["requisitos de DPO"]
    end

    subgraph SUP["schema/ + scripts/"]
        sup_schema["control.schema.json framework.schema.json mapping.schema.json"]
        sup_scripts["validate.py generate-stats.py"]
    end

    ROOT --> FW
    ROOT --> MAP
    ROOT --> LEG
    ROOT --> SUP

    fw_controls -.->|legal_references| LEG
    map_pair -.->|referencia| fw_controls

    style FW fill:#e3f2fd,stroke:#1565c0,color:#000
    style MAP fill:#e8f5e9,stroke:#2e7d32,color:#000
    style LEG fill:#ffebee,stroke:#c62828,color:#000
    style SUP fill:#f3e5f5,stroke:#6a1b9a,color:#000
```

---

## 5. Fluxo de Trabalho do Engenheiro

Este é o fluxo típico de um engenheiro usando o BRACIS. Comece identificando quais frameworks se aplicam ao seu contexto, depois explore os controles para detalhes de implementação no seu techstack.

```mermaid
flowchart TD
    START(("Inicio"))
    FIND["1. Encontre frameworks para seu contexto"]
    READ["2. Leia os controles controls/*.yaml"]
    IMPL["3. Consulte implementation_guidance para seu techstack"]
    DECIDE{Qual techstack?}

    PE["Platform Engineering Vault Keycloak OPA Backstage"]
    DSO["DevSecOps Checkov Trivy Semgrep OWASP ZAP"]
    SO["SecOps Splunk CrowdStrike SailPoint"]

    GAPS["4. Consulte mappings/ para lacunas de cobertura"]
    LEGAL["legal/ matrizes Comparacoes jurisdicionais"]
    DONE(("Concluido"))

    START --> FIND --> READ --> IMPL --> DECIDE
    DECIDE -->|plataforma| PE
    DECIDE -->|devsecops| DSO
    DECIDE -->|secops| SO
    PE --> GAPS
    DSO --> GAPS
    SO --> GAPS
    GAPS --> LEGAL --> DONE

    classDef step fill:#2c5282,stroke:#63b3ed,color:#e2e8f0
    classDef techstack fill:#285e61,stroke:#4fd1c5,color:#e2e8f0
    classDef legal fill:#744210,stroke:#ecc94b,color:#e2e8f0
    classDef decision fill:#553c9a,stroke:#b794f4,color:#e2e8f0
    classDef terminal fill:#1a202c,stroke:#718096,color:#e2e8f0

    class FIND,READ,IMPL,GAPS step
    class PE,DSO,SO techstack
    class LEGAL legal
    class DECIDE decision
    class START,DONE terminal
```
