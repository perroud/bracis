[Leia em Portugues](diagrams-engineering.pt-BR.md)

# Engineering Diagrams

Visual guides for developers, DevSecOps, and platform engineers working with BRACIS.

---

## 1. Three-Layer Control Architecture

Every control file (`controls/*.yaml`) follows a consistent four-layer structure. Layer 1 preserves the original regulatory text verbatim (in its source language). Layer 2 provides interpretive guidance in English. Layer 3 breaks implementation down by techstack, each with concrete tooling. Layer 4 links the control to related frameworks.

```mermaid
mindmap
  root((Control File<br/>controls/*.yaml))
    Layer 1: statement
      prose
        Brazilian law in pt-BR
        NIST/ISO/EU in English
    Layer 2: guidance
      prose
        What the requirement means
        Interpretive context
    Layer 3: implementation_guidance
      platform_engineering
        prose
        tools
          Vault
          Keycloak
          OPA
          Backstage
      devsecops
        prose
        tools
          Checkov
          Trivy
          Semgrep
          OWASP ZAP
      secops
        prose
        tools
          Splunk
          CrowdStrike
          SailPoint
    Layer 4: legal_references
      framework_id
      articles
      relationship type
        supports
        implements
        equivalent-to
        mapped
```

---

## 2. Framework Derivation Chains -- International

This diagram maps the derivation and complementarity relationships between international standards organized by family. The ISO family radiates from 27001, the NIST family from 800-53, and the PCI family from DSS v4.

```mermaid
mindmap
  root((International<br/>Standards))
    ISO Family
      ISO 27001
        ISO 27701 Privacy
        ISO 27017 Cloud
        ISO 27018 PII in Cloud
        ISO 27005 Risk
        ISO 27035 Incident
      ISO 22301 BCM
        ISO 27031 ICT Readiness
      ISO 42001 AI Management
      ISO 31000 Risk Management
    NIST Family
      NIST 800-53
        NIST 800-171
          CMMC v2
        FedRAMP
        FISMA
        NIST 800-37 RMF
        NIST 800-61 Incident
      NIST CSF v2
        NIST Privacy Framework
      NIST AI RMF
    PCI Family
      PCI DSS v4
        PCI PIN
        PCI 3DS
        PCI SSF
        PCI P2PE
    Other Standards
      COSO
        SOC 2
      CSA CCM v4
      TISAX
    Regulations
      GDPR
      EU AI Act
```

**Legend:** Each branch represents a derivation or strong relationship chain. ISO 42001 and NIST AI RMF are equivalent. ISO 27018 complements GDPR. CSA CCM v4 complements ISO 27017.

---

## 3. Framework Derivation Chains -- Brazil

The Brazilian regulatory ecosystem is heavily interconnected. Sector-specific regulators (BCB, CVM, SUSEP, ANATEL, ANVISA) derive cybersecurity and privacy requirements from the LGPD and sector-specific norms, often referencing each other.

```mermaid
mindmap
  root((Brazil<br/>Regulatory<br/>Ecosystem))
    Privacy and Internet
      LGPD
      Marco Civil da Internet
      Decreto 8.771
    BCB - Banco Central
      Bacen 4.893 Cybersecurity
      BCB 85 Payment Institutions
        Pix Security
        Pix MED 2.0
      BCB 3.978 AML/CFT
      BCB 44
      BCB 304
      BCB Conj.2
      IN 291
    CMN - Conselho Monetario
      CMN 4.557 Risk Mgmt
      CMN 4.968
      CMN 4.606
    CVM - Capital Markets
      CVM 35
      CVM 50
      CVM 88
      CVM 175
      CVM 135
      CVM 193
    CNSP/SUSEP - Insurance
      CNSP 381
      CNSP 416
      CNSP 393
      CNSP 408
      SUSEP 638
      SUSEP 612
    GSI - Government Cyber
      PNSI
      PNCiber
      IN GSI 1
      IN GSI 3
      IN GSI 5
      ReGIC
      PNSIC
    Health Sector
      ANVISA 134
      ANVISA SaMD
      ANVISA BPF
      CFM Telemedicina
      CFM IA
      ANS TISS
      PEP
      Receituario Digital
    Other
      LAI
      Gov Digital
      ICP-Brasil
      Crimes Ciberneticos
      ANEEL 964
      ONS ARCiber
```

**Legend:** Each top-level branch groups frameworks by regulator or sector. BCB norms derive from Bacen 4.893. CNSP/SUSEP derive from CMN risk governance. GSI norms flow from PNSI. Health norms relate to both LGPD and sector-specific regulators.

---

## 4. Repository Structure

The repository follows a flat, predictable structure. Each of the 136 frameworks lives in its own directory under `frameworks/`, containing the metadata, controls organized by family, and optional translations. Cross-framework mappings and legal matrices are kept at the top level.

```mermaid
flowchart TD
    ROOT["bracis/"]

    subgraph FW["frameworks/ (136 directories)"]
        fw_yaml["framework.yaml"]
        fw_controls["controls/family/control.yaml"]
        fw_i18n["i18n/ (optional)"]
    end

    subgraph MAP["mappings/ (123 files)"]
        map_rel["_framework-relationships.yaml"]
        map_cat["_category-correlation.yaml"]
        map_pair["source_to_target.yaml"]
    end

    subgraph LEG["legal/ (8 matrices)"]
        leg_breach["breach-notification"]
        leg_penalties["penalties"]
        leg_consent["consent-requirements"]
        leg_xborder["cross-border-transfer"]
        leg_retention["data-retention"]
        leg_rights["data-subject-rights"]
        leg_sensitive["sensitive-data-categories"]
        leg_dpo["dpo-requirements"]
    end

    subgraph SUP["schema/ + scripts/"]
        sup_schema["control.schema.json\nframework.schema.json\nmapping.schema.json"]
        sup_scripts["validate.py\ngenerate-stats.py"]
    end

    ROOT --> FW
    ROOT --> MAP
    ROOT --> LEG
    ROOT --> SUP

    fw_controls -.->|legal_references| LEG
    map_pair -.->|references| fw_controls

    style FW fill:#e3f2fd,stroke:#1565c0,color:#000
    style MAP fill:#e8f5e9,stroke:#2e7d32,color:#000
    style LEG fill:#ffebee,stroke:#c62828,color:#000
    style SUP fill:#f3e5f5,stroke:#6a1b9a,color:#000
```

---

## 5. Developer Workflow

This is the typical workflow for an engineer using BRACIS. Start by identifying which frameworks apply to your context, then drill into the controls for implementation details targeting your specific techstack. Use the mappings to find cross-framework coverage gaps.

```mermaid
flowchart TD
    START(("Start"))
    FIND["1. Find frameworks<br/>for your context<br/>(industry, region, regulation)"]
    READ["2. Read controls<br/>controls/*.yaml<br/>Understand requirements"]
    IMPL["3. Check implementation_guidance<br/>for your techstack"]
    DECIDE{Which techstack?}

    PE["Platform Engineering<br/>Vault, Keycloak,<br/>OPA, Backstage"]
    DSO["DevSecOps<br/>Checkov, Trivy,<br/>Semgrep, OWASP ZAP"]
    SO["SecOps<br/>Splunk, CrowdStrike,<br/>SailPoint"]

    GAPS["4. Check mappings/<br/>for cross-framework<br/>coverage gaps"]
    LEGAL["legal/ matrices<br/>Jurisdictional<br/>comparisons"]

    DONE(("Done"))

    START --> FIND
    FIND --> READ
    READ --> IMPL
    IMPL --> DECIDE

    DECIDE -->|platform| PE
    DECIDE -->|devsecops| DSO
    DECIDE -->|secops| SO

    PE --> GAPS
    DSO --> GAPS
    SO --> GAPS

    GAPS --> LEGAL
    LEGAL --> DONE

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
