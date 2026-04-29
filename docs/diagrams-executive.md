[Leia em Portugues](diagrams-executive.pt-BR.md)

# Executive Diagrams

Strategic compliance landscape visualizations for C-level executives, board members, and GRC leadership.

This document presents 136 regulatory frameworks and 2,800+ controls as strategic assets. Each diagram answers a question that matters at the board level: where we have coverage, where the gaps are, and what to prioritize next.

---

## 1. Global Regulatory Coverage

Our framework library spans every major regulatory region. The chart below shows the distribution across geographies, making it clear where your compliance investment delivers the most coverage.

```mermaid
pie title 136 Frameworks by Region
    "Brazil (60)" : 60
    "Global/International (40)" : 40
    "Asia-Pacific (12)" : 12
    "United States (11)" : 11
    "Europe/EU (10)" : 10
    "Middle East & Africa (2)" : 2
    "Canada (1)" : 1
```

**Key takeaway:** Brazil and global standards together account for 74% of the library. Any company operating in Brazil with international clients gets immediate, deep coverage.

---

## 2. Compliance Stack Selector

Not every company needs all 136 frameworks. This decision tree helps executives identify the minimum viable compliance stack based on where the company operates and what sector it serves.

```mermaid
flowchart TD
    START["Where does your company operate?"] --> BR["Brazil"]
    START --> EU["European Union"]
    START --> US["United States"]
    START --> GLOBAL["Global SaaS"]
    START --> APAC["Asia-Pacific"]

    BR --> BR_SECTOR{"What sector?"}
    BR_SECTOR --> BR_FIN["Financial"]
    BR_SECTOR --> BR_INS["Insurance"]
    BR_SECTOR --> BR_HEALTH["Healthcare"]
    BR_SECTOR --> BR_GOV["Government"]
    BR_SECTOR --> BR_GEN["General"]

    BR_FIN --> BR_FIN_STACK["LGPD + BCB 4893\nCMN 4557 + CMN 4606\nPCI DSS + SOC 2"]
    BR_INS --> BR_INS_STACK["LGPD + CNSP 381\nCNSP 393 + SUSEP 638\nSOC 2"]
    BR_HEALTH --> BR_HEALTH_STACK["LGPD + ANVISA 134\nCFM + TISS\nISO 27001"]
    BR_GOV --> BR_GOV_STACK["LGPD + PNSI\nGSI IN1 + GSI IN3\nICP-Brasil + ReGIC"]
    BR_GEN --> BR_GEN_STACK["LGPD + Marco Civil\nISO 27001 + SOC 2"]

    EU --> EU_SECTOR{"What sector?"}
    EU_SECTOR --> EU_FIN["Financial"]
    EU_SECTOR --> EU_GEN["General"]
    EU_SECTOR --> EU_AI["AI Products"]
    EU_FIN --> EU_FIN_STACK["GDPR + DORA\nNIS2 + PCI DSS"]
    EU_GEN --> EU_GEN_STACK["GDPR + NIS2"]
    EU_AI --> EU_AI_STACK["GDPR + NIS2\nEU AI Act + ISO 42001"]

    US --> US_SECTOR{"What sector?"}
    US_SECTOR --> US_FED["Federal / DoD"]
    US_SECTOR --> US_HEALTH["Healthcare"]
    US_SECTOR --> US_FIN["Financial"]
    US_SECTOR --> US_EDU["Education"]
    US_SECTOR --> US_GEN["General"]
    US_FED --> US_FED_STACK["FedRAMP + FISMA\nNIST 800-53 + CMMC"]
    US_HEALTH --> US_HEALTH_STACK["HIPAA + HITRUST\nSOC 2"]
    US_FIN --> US_FIN_STACK["SOX + GLBA\nPCI DSS + SOC 1/2"]
    US_EDU --> US_EDU_STACK["FERPA + COPPA\nSOC 2"]
    US_GEN --> US_GEN_STACK["SOC 2 + CCPA"]

    GLOBAL --> GLOBAL_STACK["SOC 2 + ISO 27001\nGDPR + CCPA\nCSA CCM"]

    APAC --> APAC_REGION{"Which country?"}
    APAC_REGION --> SG["Singapore"]
    APAC_REGION --> AU["Australia"]
    APAC_REGION --> JP["Japan"]
    APAC_REGION --> KR["South Korea"]
    SG --> SG_STACK["PDPA-SG + MAS TRM\nISO 27001"]
    AU --> AU_STACK["Essential Eight\nAPRA CPS 234\nISO 27001"]
    JP --> JP_STACK["APPI + ISMAP\nISO 27001"]
    KR --> KR_STACK["PIPA + K-ISMS-P\nISO 27001"]

    style BR_FIN_STACK fill:#e8f5e9,stroke:#2e7d32
    style BR_INS_STACK fill:#e8f5e9,stroke:#2e7d32
    style BR_HEALTH_STACK fill:#e8f5e9,stroke:#2e7d32
    style BR_GOV_STACK fill:#e8f5e9,stroke:#2e7d32
    style BR_GEN_STACK fill:#e8f5e9,stroke:#2e7d32
    style EU_FIN_STACK fill:#e8f5e9,stroke:#2e7d32
    style EU_GEN_STACK fill:#e8f5e9,stroke:#2e7d32
    style EU_AI_STACK fill:#e8f5e9,stroke:#2e7d32
    style US_FED_STACK fill:#e8f5e9,stroke:#2e7d32
    style US_HEALTH_STACK fill:#e8f5e9,stroke:#2e7d32
    style US_FIN_STACK fill:#e8f5e9,stroke:#2e7d32
    style US_EDU_STACK fill:#e8f5e9,stroke:#2e7d32
    style US_GEN_STACK fill:#e8f5e9,stroke:#2e7d32
    style GLOBAL_STACK fill:#e8f5e9,stroke:#2e7d32
    style SG_STACK fill:#e8f5e9,stroke:#2e7d32
    style AU_STACK fill:#e8f5e9,stroke:#2e7d32
    style JP_STACK fill:#e8f5e9,stroke:#2e7d32
    style KR_STACK fill:#e8f5e9,stroke:#2e7d32
```

**Key takeaway:** Start with the smallest stack that covers your regulatory obligations. You can always expand later. The green boxes are your recommended starting points.

---

## 3. Three Lines of Defense Model

Compliance is not a single team's job. The three lines of defense model distributes responsibility across the organization. This diagram shows how BRACIS maps to each line.

```mermaid
flowchart TD
    subgraph LINE1["1st Line -- Operations"]
        PE["Platform Engineering\nimplementation_guidance"]
        DSO["DevSecOps\nimplementation_guidance"]
        TOOLS1["OWASP ASVS / SLSA\nCIS Controls / DISA STIG\nPCI SSF / NIST 800-218"]
    end

    subgraph LINE2["2nd Line -- Risk & Compliance"]
        GRC["GRC Gap Analysis\nCross-framework mappings"]
        LEGAL["Legal Matrices\n8 cross-jurisdiction matrices"]
        POLICY["Policy Frameworks\nISO 27001 / NIST CSF\nCOBIT / SOC 2"]
    end

    subgraph LINE3["3rd Line -- Audit"]
        CERT["Certifications\nISO 27001 / ISO 27701\nSOC 1 / SOC 2"]
        REG["Regulatory Audits\nFedRAMP / CMMC\nDORA / HIPAA"]
        REPORT["Board Reporting\n123 cross-framework mappings"]
    end

    LINE1 --> LINE2 --> LINE3

    style LINE1 fill:#e3f2fd,stroke:#1565c0,color:#000
    style LINE2 fill:#fff3e0,stroke:#e65100,color:#000
    style LINE3 fill:#fce4ec,stroke:#b71c1c,color:#000
```

**Key takeaway:** The 1st line uses implementation guidance daily. The 2nd line uses cross-framework mappings and legal matrices for continuous monitoring. The 3rd line uses certifications and mappings for audit evidence.

---

## 4. Regulatory Dependency Map

Regulations do not exist in isolation. Understanding how the major regulatory families relate to each other prevents duplicate work and reveals shared controls.

```mermaid
mindmap
    root((Compliance Frameworks))
        ISO Family
            ISO 27001
                ISO 27701
                ISO 27017
                ISO 27018
                ISO 27005
                ISO 27035
                ISO 22301
                ISO 42001
        NIST Family
            NIST 800-53
                NIST CSF v2
                NIST 800-171
                    CMMC v2
                FedRAMP
                FISMA
                NIST AI RMF
                NIST Privacy
        PCI Family
            PCI DSS v4
                PCI PIN
                PCI 3DS
                PCI SSF
                PCI P2PE
        Privacy Laws
            GDPR
                LGPD
                CCPA/CPRA
                PIPL
                DPDP India
                PDPA-SG
                APPI Japan
                PIPA Korea
                KVKK Turkey
                PIPEDA
                POPIA
```

**Key takeaway:** ISO 27001 and GDPR are the two gravitational centers. Implementing ISO 27001 covers significant portions of NIST, PCI, and sector-specific frameworks. GDPR compliance creates a baseline for nearly every other privacy law.

---

## 5. Penalty Risk Landscape

Not all regulations carry equal enforcement risk. This quadrant positions key frameworks by enforcement activity and maximum penalty size, helping executives prioritize where non-compliance is most costly.

```mermaid
quadrantChart
    title Penalty Risk Assessment
    x-axis Low Enforcement --> High Enforcement
    y-axis Low Penalty --> High Penalty
    quadrant-1 Critical Risk
    quadrant-2 High Penalty Low Enforcement
    quadrant-3 Monitor
    quadrant-4 High Enforcement Low Penalty
    GDPR: [0.90, 0.85]
    CCPA: [0.75, 0.55]
    PIPL: [0.40, 0.90]
    EU AI Act: [0.30, 0.95]
    KVKK: [0.30, 0.30]
    PIPEDA: [0.35, 0.25]
    HIPAA: [0.80, 0.45]
    LGPD: [0.60, 0.60]
    DORA: [0.70, 0.80]
    SOX: [0.85, 0.70]
    POPIA: [0.25, 0.35]
    DPDP: [0.20, 0.50]
```

**Key takeaway:** GDPR, SOX, and DORA sit in the critical risk quadrant. The EU AI Act and PIPL carry massive penalty ceilings but lower enforcement maturity today.

---

## 6. Compliance Maturity Roadmap

Compliance is a journey, not a destination. This roadmap shows a phased approach from foundational standards to full automated compliance.

```mermaid
timeline
    title Compliance Maturity Roadmap
    section Phase 1 -- Foundation
        ISO 27001 : SOC 2 : Local privacy law -- GDPR, LGPD, or CCPA : NIST CSF v2
    section Phase 2 -- Industry
        PCI DSS v4 : HIPAA or DORA : CMMC or FedRAMP : Sector regulators -- Bacen 4893, CNSP 381
    section Phase 3 -- Advanced
        Supply chain -- SLSA, NIST 800-218 : AI governance -- ISO 42001, NIST AI RMF : Privacy engineering -- ISO 27701 : Resilience -- NIS2, DORA, ISO 22301
    section Phase 4 -- Excellence
        Full cross-framework mapping -- 123 files : Legal matrices -- 8 jurisdictions : Continuous compliance monitoring : Audit-ready evidence
```

**Key takeaway:** Phase 1 alone covers 60-70% of most compliance requirements. Each subsequent phase adds depth and sector specificity. Phase 4 turns compliance from a cost center into a competitive advantage through systematic coverage.

---

## 7. Data Lifecycle and Compliance Touchpoints

Every stage of the data lifecycle triggers regulatory obligations. This diagram maps those touchpoints to the specific legal matrices and frameworks in BRACIS.

```mermaid
flowchart TD
    COLLECT["Data Collection"] --> PROCESS["Data Processing"]
    PROCESS --> STORE["Data Storage"]
    STORE --> SHARE["Data Sharing /\nCross-border Transfer"]
    STORE --> DSR["Data Subject\nRequest"]
    STORE --> BREACH["Data Breach"]

    COLLECT -.- C_REQ["consent-requirements-matrix.yaml\nGDPR Art 6-7, LGPD Art 7-8"]
    PROCESS -.- P_REQ["sensitive-data-categories-matrix.yaml\nISO 27001, NIST 800-53"]
    STORE -.- S_REQ["data-retention-matrix.yaml\nEncryption: ISO 27018, PCI DSS"]
    SHARE -.- SH_REQ["cross-border-transfer-matrix.yaml\nGDPR Ch V, LGPD Art 33-36"]
    DSR -.- DSR_REQ["data-subject-rights-matrix.yaml\nAccess, Deletion, Portability"]
    BREACH -.- B_REQ["breach-notification-matrix.yaml\npenalties-matrix.yaml\ndpo-requirements-matrix.yaml"]

    style COLLECT fill:#e3f2fd,stroke:#1565c0
    style PROCESS fill:#e3f2fd,stroke:#1565c0
    style STORE fill:#e3f2fd,stroke:#1565c0
    style SHARE fill:#fff3e0,stroke:#e65100
    style DSR fill:#fff3e0,stroke:#e65100
    style BREACH fill:#ffcdd2,stroke:#b71c1c

    style C_REQ fill:#f5f5f5,stroke:#9e9e9e
    style P_REQ fill:#f5f5f5,stroke:#9e9e9e
    style S_REQ fill:#f5f5f5,stroke:#9e9e9e
    style SH_REQ fill:#f5f5f5,stroke:#9e9e9e
    style DSR_REQ fill:#f5f5f5,stroke:#9e9e9e
    style B_REQ fill:#f5f5f5,stroke:#9e9e9e
```

**Key takeaway:** Our 8 legal matrices cover every stage of the data lifecycle across 17 jurisdictions. A data breach triggers 3 matrices simultaneously — preparation here has the highest risk-reduction ROI.

---

## 8. Brazil Regulatory Ecosystem

Brazil has one of the most complex regulatory landscapes for technology companies, with 60 frameworks across 10+ regulators. This map shows the major regulatory bodies organized by sector, with LGPD as the connective thread across all of them.

```mermaid
mindmap
    root((Brazil Compliance\nEcosystem))
        LGPD + ANPD
            Core privacy law
            National Data Protection Authority
        BCB / CMN -- Financial
            BCB 4893
            BCB 3978
            BCB 304
            CMN 4557
            CMN 4606
            CMN 4968
            6 more frameworks
        CVM -- Capital Markets
            CVM 35
            CVM 50
            CVM 88
            CVM 135
            CVM 175
            CVM 193
        CNSP / SUSEP -- Insurance
            CNSP 381
            CNSP 393
            CNSP 408
            CNSP 416
            SUSEP 612
            SUSEP 638
        GSI / PR -- Government Security
            PNSI
            PNCiber
            GSI IN1
            GSI IN3
            GSI IN5
            ReGIC
            R-Ciber
            ICP-Brasil
        ANATEL -- Telecom
            ANATEL IoT
            R-Ciber Telecom
        ANEEL / ONS -- Energy
            ANEEL 964
            ONS ARCiber
        ANVISA / CFM / ANS -- Healthcare
            ANVISA 134
            ANVISA BPF
            ANVISA SaMD
            CFM IA
            CFM Telemedicina
            TISS
        ANAC -- Aviation
            ANAC SGSO
            ANAC Ciber
```

**Key takeaway:** LGPD is the thread that connects every sector in Brazil. Financial services is the most heavily regulated sector with 22 frameworks across 4 regulators. Any company operating in Brazil's financial sector must plan for significant compliance investment.
