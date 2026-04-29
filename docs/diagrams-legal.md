[Leia em Portugues](diagrams-legal.pt-BR.md) _(em breve)_

# Legal Diagrams

Visual decision trees and comparison charts for legal teams, DPOs, and compliance officers working with the BRACIS. Each diagram uses a distinct Mermaid type -- vertical flowcharts for decision trees, mindmaps for classification views, and a quadrant chart for penalty positioning.

---

## 1. Breach Notification Decision Tree

When a data breach occurs, the response timeline and notification obligations vary dramatically by jurisdiction. This vertical decision tree guides the initial triage: determine whether notification is required, to whom, and within what deadline. Diamond shapes represent decisions; the risk threshold differs per framework.

```mermaid
flowchart TD
    A[Data breach detected] --> B{Does the breach involve\npersonal data or PHI?}
    B -- No --> C[Document internally.\nNo privacy notification required.]
    B -- Yes --> D{Identify applicable\njurisdictions and frameworks}

    D --> GDPR_CHECK{GDPR applies?}
    D --> LGPD_CHECK{LGPD applies?}
    D --> CCPA_CHECK{CCPA/CPRA applies?}
    D --> HIPAA_CHECK{HIPAA applies?}
    D --> PIPL_CHECK{PIPL applies?}
    D --> PDPA_CHECK{PDPA-SG applies?}
    D --> PIPA_CHECK{PIPA-KR applies?}
    D --> PIPEDA_CHECK{PIPEDA applies?}

    %% GDPR path
    GDPR_CHECK -- Yes --> GDPR_RISK{Risk to rights and\nfreedoms of individuals?}
    GDPR_RISK -- Unlikely --> GDPR_DOC[Document breach internally.\nNo notification required.]
    GDPR_RISK -- Risk exists --> GDPR_AUTH[Notify Supervisory Authority\nwithin 72 hours]
    GDPR_AUTH --> GDPR_HIGH{High risk to\nindividuals?}
    GDPR_HIGH -- Yes --> GDPR_IND[Notify affected individuals\nwithout undue delay]
    GDPR_HIGH -- No --> GDPR_DONE[Authority notification sufficient]

    %% LGPD path
    LGPD_CHECK -- Yes --> LGPD_RISK{Significant risk or\ndamage to data subjects?}
    LGPD_RISK -- No --> LGPD_DOC[Document internally]
    LGPD_RISK -- Yes --> LGPD_AUTH[Notify ANPD\nwithin 3 business days]
    LGPD_AUTH --> LGPD_IND[Notify affected data subjects\nwithin 3 business days]

    %% CCPA path
    CCPA_CHECK -- Yes --> CCPA_RISK{Breach of unencrypted\npersonal information?}
    CCPA_RISK -- No --> CCPA_DOC[No notification required]
    CCPA_RISK -- Yes --> CCPA_AUTH[Notify CA Attorney General\nexpeditiously if >500 residents]
    CCPA_AUTH --> CCPA_IND[Notify affected consumers\nexpeditiously]

    %% HIPAA path
    HIPAA_CHECK -- Yes --> HIPAA_RISK{Breach of unsecured PHI?\nLow probability of\ncompromise per 4-factor test?}
    HIPAA_RISK -- Low probability --> HIPAA_DOC[Document breach internally]
    HIPAA_RISK -- Breach confirmed --> HIPAA_SIZE{500+ individuals\naffected?}
    HIPAA_SIZE -- Yes --> HIPAA_MAJOR[Notify HHS immediately +\nprominent media +\nindividuals within 60 days]
    HIPAA_SIZE -- No --> HIPAA_MINOR[Notify individuals within 60 days.\nReport to HHS in annual log.]

    %% PIPL path
    PIPL_CHECK -- Yes --> PIPL_AUTH[Notify CAC department\nimmediately]
    PIPL_AUTH --> PIPL_IND[Notify affected individuals\nimmediately]

    %% PDPA-SG path
    PDPA_CHECK -- Yes --> PDPA_RISK{Notifiable data breach?\nSignificant harm likely or\n500+ affected?}
    PDPA_RISK -- No --> PDPA_DOC[Document internally]
    PDPA_RISK -- Yes --> PDPA_AUTH[Notify PDPC\nwithin 3 calendar days]
    PDPA_AUTH --> PDPA_IND[Notify affected individuals\nas soon as practicable]

    %% PIPA-KR path
    PIPA_CHECK -- Yes --> PIPA_RISK{Leak or loss of\npersonal information?}
    PIPA_RISK -- No --> PIPA_DOC[Document internally]
    PIPA_RISK -- Yes --> PIPA_AUTH[Notify PIPC\nwithin 72 hours]
    PIPA_AUTH --> PIPA_IND[Notify affected data subjects\nwithout delay]

    %% PIPEDA path
    PIPEDA_CHECK -- Yes --> PIPEDA_RISK{Real risk of\nsignificant harm?}
    PIPEDA_RISK -- No --> PIPEDA_DOC[Document internally]
    PIPEDA_RISK -- Yes --> PIPEDA_AUTH[Notify OPC\nas soon as feasible]
    PIPEDA_AUTH --> PIPEDA_IND[Notify affected individuals\nas soon as feasible]

    %% Styling
    style A fill:#d32f2f,color:#fff
    style GDPR_AUTH fill:#1565c0,color:#fff
    style LGPD_AUTH fill:#1565c0,color:#fff
    style CCPA_AUTH fill:#1565c0,color:#fff
    style HIPAA_MAJOR fill:#d32f2f,color:#fff
    style HIPAA_MINOR fill:#1565c0,color:#fff
    style PIPL_AUTH fill:#d32f2f,color:#fff
    style PDPA_AUTH fill:#1565c0,color:#fff
    style PIPA_AUTH fill:#1565c0,color:#fff
    style PIPEDA_AUTH fill:#1565c0,color:#fff
    style GDPR_IND fill:#c62828,color:#fff
    style LGPD_IND fill:#c62828,color:#fff
    style CCPA_IND fill:#c62828,color:#fff
    style PIPL_IND fill:#c62828,color:#fff
    style PDPA_IND fill:#c62828,color:#fff
    style PIPA_IND fill:#c62828,color:#fff
    style PIPEDA_IND fill:#c62828,color:#fff
    style GDPR_DOC fill:#9e9e9e,color:#fff
    style LGPD_DOC fill:#9e9e9e,color:#fff
    style CCPA_DOC fill:#9e9e9e,color:#fff
    style HIPAA_DOC fill:#9e9e9e,color:#fff
    style PDPA_DOC fill:#9e9e9e,color:#fff
    style PIPA_DOC fill:#9e9e9e,color:#fff
    style PIPEDA_DOC fill:#9e9e9e,color:#fff
    style GDPR_DONE fill:#2e7d32,color:#fff
```

**Key deadline summary:**

| Framework | Authority deadline | Individual deadline |
|-----------|-------------------|-------------------|
| GDPR | 72 hours | Without undue delay (high risk) |
| LGPD | 3 business days | 3 business days |
| CCPA/CPRA | Expeditiously | Expeditiously |
| HIPAA | 60 days (immediate if 500+) | 60 days |
| PIPL | Immediately | Immediately |
| PDPA-SG | 3 calendar days | As soon as practicable |
| PIPA-KR | 72 hours | Without delay |
| PIPEDA | As soon as feasible | As soon as feasible |

---

## 2. Cross-Border Data Transfer Decision Tree

International data transfers are among the most complex compliance challenges. Each framework uses a fundamentally different model: GDPR uses adequacy decisions and safeguards, PIPL uses a three-tier system with mandatory security assessments, India uses a blacklist model, and CCPA imposes no geographic restrictions at all. This vertical tree maps the decision process across the major frameworks, flowing top to bottom through adequacy, SCCs, BCRs, and derogations.

```mermaid
flowchart TD
    START[Need to transfer personal\ndata across borders] --> FW{Which framework\ngoverns the transfer?}

    %% GDPR path
    FW --> GDPR[GDPR\nEU/EEA source]
    GDPR --> GDPR_ADQ{Destination has EC\nadequacy decision?}
    GDPR_ADQ -- "Yes (e.g., Japan, Korea,\nUK, US DPF, Argentina)" --> GDPR_OK[Transfer permitted]
    GDPR_ADQ -- No --> GDPR_SCC{Standard Contractual\nClauses in place?}
    GDPR_SCC -- Yes --> GDPR_TIA[Conduct Transfer Impact\nAssessment per Schrems II]
    GDPR_TIA --> GDPR_SUPP[Apply supplementary measures\nif needed: encryption,\npseudonymization, split processing]
    GDPR_SUPP --> GDPR_OK2[Transfer permitted\nwith safeguards]
    GDPR_SCC -- No --> GDPR_BCR{Binding Corporate\nRules approved?}
    GDPR_BCR -- Yes --> GDPR_OK2
    GDPR_BCR -- No --> GDPR_DER{Derogation applies?\nExplicit consent, contract,\npublic interest, legal claims,\nvital interests}
    GDPR_DER -- Yes --> GDPR_OK3[Transfer permitted\nunder derogation\ndocument and limit scope]
    GDPR_DER -- No --> GDPR_BLOCK[Transfer NOT permitted]

    %% PIPL path
    FW --> PIPL[PIPL\nChina source]
    PIPL --> PIPL_CIIO{Is the entity a CIIO\nor processes 1M+\nindividuals?}
    PIPL_CIIO -- Yes --> PIPL_SEC[Mandatory CAC Security\nAssessment required]
    PIPL_SEC --> PIPL_PASS{Assessment passed?}
    PIPL_PASS -- Yes --> PIPL_OK[Transfer permitted]
    PIPL_PASS -- No --> PIPL_BLOCK[Transfer NOT permitted]
    PIPL_CIIO -- No --> PIPL_THRESHOLD{Transferred 100K+ individuals\nor 10K+ sensitive data\nsince Jan 1 prev. year?}
    PIPL_THRESHOLD -- Yes --> PIPL_SEC
    PIPL_THRESHOLD -- No --> PIPL_SCC{PIPL Standard Contract\nfiled with provincial CAC?}
    PIPL_SCC -- Yes --> PIPL_OK2[Transfer permitted]
    PIPL_SCC -- No --> PIPL_CERT{Personal Information\nProtection Certification?}
    PIPL_CERT -- Yes --> PIPL_OK2
    PIPL_CERT -- No --> PIPL_BLOCK2[Transfer NOT permitted]

    %% LGPD path
    FW --> LGPD[LGPD\nBrazil source]
    LGPD --> LGPD_ADQ{ANPD adequacy\ndecision for destination?}
    LGPD_ADQ -- "Yes (none issued yet)" --> LGPD_OK[Transfer permitted]
    LGPD_ADQ -- No --> LGPD_SCC{Standard contractual\nclauses per ANPD\nResolution 19/2024?}
    LGPD_SCC -- Yes --> LGPD_OK2[Transfer permitted]
    LGPD_SCC -- No --> LGPD_CONSENT{Specific and prominent\nconsent from data subject?}
    LGPD_CONSENT -- Yes --> LGPD_OK3[Transfer permitted]
    LGPD_CONSENT -- No --> LGPD_OTHER{Other legal basis?\nInternational cooperation,\nlegal obligation, life protection}
    LGPD_OTHER -- Yes --> LGPD_OK4[Transfer permitted\nunder specific basis]
    LGPD_OTHER -- No --> LGPD_BLOCK[Transfer NOT permitted]

    %% DPDP India path
    FW --> DPDP[DPDP Act\nIndia source]
    DPDP --> DPDP_CHECK{Destination country\non government\nblacklist?}
    DPDP_CHECK -- "No (all permitted\nunless blacklisted)" --> DPDP_OK[Transfer permitted]
    DPDP_CHECK -- Yes --> DPDP_BLOCK[Transfer NOT permitted]

    %% PIPA Korea path
    FW --> PIPA[PIPA\nKorea source]
    PIPA --> PIPA_ADQ{PIPC adequacy decision?\ne.g., EU/EEA mutual}
    PIPA_ADQ -- Yes --> PIPA_OK[Transfer permitted]
    PIPA_ADQ -- No --> PIPA_AGREE{Cross-border processing\nagreement with equivalent\nPIPA protections?}
    PIPA_AGREE -- Yes --> PIPA_OK2[Transfer permitted]
    PIPA_AGREE -- No --> PIPA_CONSENT{Separate consent\nwith detailed information\non recipient, purpose,\ncountry, and retention?}
    PIPA_CONSENT -- Yes --> PIPA_OK3[Transfer permitted]
    PIPA_CONSENT -- No --> PIPA_BLOCK[Transfer NOT permitted]

    %% CCPA path
    FW --> CCPA[CCPA/CPRA\nCalifornia source]
    CCPA --> CCPA_CONTRACT{Contractual clauses\nensuring same level\nof protection?}
    CCPA_CONTRACT -- Yes --> CCPA_OK[Transfer permitted.\nNo geographic restrictions.]
    CCPA_CONTRACT -- No --> CCPA_ADD[Add CPRA-mandated privacy\nclauses to contracts]
    CCPA_ADD --> CCPA_OK

    %% Styling
    style START fill:#1565c0,color:#fff
    style GDPR_OK fill:#2e7d32,color:#fff
    style GDPR_OK2 fill:#2e7d32,color:#fff
    style GDPR_OK3 fill:#f9a825,color:#000
    style PIPL_OK fill:#2e7d32,color:#fff
    style PIPL_OK2 fill:#2e7d32,color:#fff
    style LGPD_OK fill:#2e7d32,color:#fff
    style LGPD_OK2 fill:#2e7d32,color:#fff
    style LGPD_OK3 fill:#f9a825,color:#000
    style LGPD_OK4 fill:#f9a825,color:#000
    style DPDP_OK fill:#2e7d32,color:#fff
    style PIPA_OK fill:#2e7d32,color:#fff
    style PIPA_OK2 fill:#2e7d32,color:#fff
    style PIPA_OK3 fill:#f9a825,color:#000
    style CCPA_OK fill:#2e7d32,color:#fff
    style GDPR_BLOCK fill:#d32f2f,color:#fff
    style PIPL_BLOCK fill:#d32f2f,color:#fff
    style PIPL_BLOCK2 fill:#d32f2f,color:#fff
    style LGPD_BLOCK fill:#d32f2f,color:#fff
    style DPDP_BLOCK fill:#d32f2f,color:#fff
    style PIPA_BLOCK fill:#d32f2f,color:#fff
    style GDPR_TIA fill:#1565c0,color:#fff
```

**Transfer model summary:**

| Framework | Model | Key mechanism |
|-----------|-------|---------------|
| GDPR | Adequacy + safeguards | EC adequacy decisions, SCCs + TIA, BCRs |
| PIPL | Three-tier system | CAC security assessment, SCCs, certification |
| LGPD | GDPR-inspired (maturing) | ANPD SCCs (2024), consent, legal cooperation |
| DPDP India | Blacklist model | All transfers permitted unless destination blacklisted |
| PIPA Korea | Consent + agreements | PIPC adequacy, processing agreements, detailed consent |
| CCPA/CPRA | Contractual model | No geographic restrictions; obligations travel with data |

---

## 3. Consent Requirements

Consent models differ fundamentally across jurisdictions. Most comprehensive privacy laws require affirmative opt-in consent, but the CCPA/CPRA uses primarily an opt-out model for the sale and sharing of data. HIPAA uses a sector-specific "authorization" concept distinct from general consent. This mindmap organizes all frameworks by their consent model, with children's age thresholds as a cross-cutting sub-branch.

```mermaid
mindmap
  root((Consent Models))
    Opt-in -- Explicit
      GDPR
        Freely given, specific, informed, unambiguous
        Explicit consent for special categories art. 9
      LGPD
        Specific and prominent consent for sensitive data
        Free, informed, unambiguous
      PIPL
        Separate consent for sensitive data
        Separate consent for cross-border transfers
      PIPA-KR
        Separate consent per purpose
        Separate consent for sensitive information
      KVKK
        Explicit consent modeled on GDPR
        Free will, specific, informed
      PDPA-TH
        Explicit consent for sensitive data
        Must be in writing or electronic form
      POPIA
        Voluntary, specific, informed
        Express consent for special categories
      PDPA-SG
        Consent required unless exception applies
        Deemed consent for reasonable purposes
      APPI
        Consent for purpose change or third-party provision
        Opt-in for sensitive information
      DPDP India
        Free, specific, informed, unconditional, unambiguous
        Clear affirmative action
    Opt-out
      CCPA/CPRA
        Right to opt out of sale and sharing
        Opt-in required for minors under 16
        No sale of children under 13 without parental consent
    Implied consent
      PIPEDA
        Implied consent for non-sensitive data
        Express consent for sensitive data
        Reasonable person standard
    Not primary basis
      HIPAA
        Authorization for uses beyond TPO
        Implied consent for treatment, payment, operations
        Specific authorization form required
      FERPA
        Consent required for disclosure with exceptions
        Directory information exception
        Legitimate educational interest exception
    Children age thresholds
      COPPA -- 13 years
        Verifiable parental consent required
      PIPL -- 14 years
        Guardian consent for minors
      GDPR -- 13 to 16 years
        Varies by member state
      CCPA -- 16 and 13 years
        16 opt-in for sale; 13 parental consent for sale
      LGPD -- 18 years
        At least one parent or guardian
      APPI -- No specific threshold
```

**Children's consent age thresholds:**

| Framework | Age threshold | Notes |
|-----------|--------------|-------|
| LGPD | 18 | Parental consent required for all minors (ECA definition) |
| CCPA/CPRA | 16 / 13 | 16 for minor opt-in to sale; 13 for parental consent to sale |
| GDPR | 13-16 | Varies by member state (13: UK, BE, DK; 14: ES, IT, AT; 15: FR, CZ, GR; 16: DE, NL) |
| PIPL | 14 | Guardian consent required for minors under 14 |
| COPPA | 13 | Verifiable parental consent for children under 13 |
| APPI | Not specified | No specific age threshold for parental consent |

---

## 4. DPO Appointment

Whether an organization must appoint a Data Protection Officer (or equivalent role) depends on the applicable framework and, in many cases, on the nature and scale of processing activities. This mindmap organizes frameworks into three categories: always mandatory, conditional on processing scale or type, and not required.

```mermaid
mindmap
  root((DPO / Privacy Officer))
    Always mandatory
      LGPD -- Encarregado
        All controllers must appoint
        Microenterprises exempted by ANPD Resolution 2/2022
        No independence or qualification requirements in law
      PDPA-SG -- DPO
        All organisations regardless of size
        No specific qualifications required
        Contact info must be publicly available
      PIPA-KR -- CPO
        All personal information processors
        Must be an executive-level officer
        Public disclosure required
      PIPEDA -- Privacy Officer
        All organisations subject to PIPEDA
        No specific qualifications
        Accountable for compliance
      POPIA -- Information Officer
        All responsible parties
        Must register with Information Regulator
        Deputy Information Officers permitted
      HIPAA -- Privacy Official + Security Official
        All covered entities
        Privacy Official for Privacy Rule
        Security Official for Security Rule
    Conditional
      GDPR -- DPO
        Public authority or body
        Large-scale systematic monitoring
        Large-scale special category processing
        Expert knowledge required by art. 37
        Independence protected -- cannot be dismissed for performing tasks
        Reports to highest management level
        Must register with supervisory authority
      PIPL -- Protection Officer
        Required if processing 1M+ individuals
        Disclose contact info to CAC
        No independence protections specified
      DPDP India -- DPO
        Required if designated as Significant Data Fiduciary
        Must be based in India
        Reports to Board of Directors
        Register with Data Protection Board of India
      PDPA-TH -- DPO
        Required if large-scale processing
        Required if sensitive data as core activity
        No specific qualifications in law
      KVKK -- Contact Person
        Required for VERBIS registry registration
        Not a full DPO role
        Primarily an administrative contact
    Not required
      CCPA/CPRA
        No DPO mandate in statute
      COPPA
        No DPO mandate
      FERPA
        No DPO mandate
      ePrivacy Directive
        Defers to GDPR DPO requirements where applicable
```

**DPO independence and qualifications comparison:**

| Framework | Independence protected? | Qualifications specified? | Public disclosure? |
|-----------|------------------------|--------------------------|-------------------|
| GDPR | Yes (art. 38) | Yes -- expert knowledge required | Yes + register with authority |
| LGPD | No | No (vetoed from original law) | Yes (on website) |
| HIPAA | No | No | Yes (in Notice of Privacy Practices) |
| PIPL | No | No | Yes + report to CAC |
| DPDP India | No | No | Yes + register with Board |
| PDPA-SG | No | No | Yes (public contact info) |
| PIPA-KR | No | No | Yes |

---

## 5. Penalty Tiers

Penalty structures across frameworks range from percentage-of-global-turnover models (GDPR, PIPL, EU AI Act) to fixed per-violation amounts (CCPA, HIPAA) to contractual penalties with no direct fines. The quadrant chart below positions each framework by enforcement activity (how aggressively fines are actually imposed) versus maximum penalty ceiling (statutory maximum). Frameworks in the upper-right quadrant pose the highest compliance risk.

```mermaid
quadrantChart
    title Penalty Risk Landscape
    x-axis "Low Enforcement Activity" --> "High Enforcement Activity"
    y-axis "Low Maximum Penalty" --> "High Maximum Penalty"
    quadrant-1 High penalty, high enforcement
    quadrant-2 High penalty, low enforcement
    quadrant-3 Low penalty, low enforcement
    quadrant-4 Low penalty, high enforcement
    GDPR: [0.85, 0.82]
    EU AI Act: [0.55, 0.95]
    PIPL: [0.60, 0.88]
    CCPA/CPRA: [0.80, 0.45]
    DPDP India: [0.35, 0.75]
    POPIA: [0.40, 0.70]
    PIPA-KR: [0.55, 0.65]
    NIS 2: [0.50, 0.72]
    LGPD: [0.45, 0.50]
    HIPAA: [0.70, 0.55]
    PDPA-TH: [0.30, 0.40]
    KVKK: [0.25, 0.30]
    PIPEDA: [0.35, 0.25]
    PDPA-SG: [0.40, 0.35]
    APPI: [0.30, 0.20]
```

**Criminal penalties and private right of action:**

| Framework | Criminal penalties? | Private right of action? |
|-----------|-------------------|------------------------|
| GDPR | Yes (member state law) | Yes (art. 79, 82) |
| LGPD | No (but other Brazilian laws apply) | Yes (art. 42 + CDC) |
| CCPA/CPRA | No | Yes (data breaches only, sec. 1798.150) |
| HIPAA | Yes (up to 10 years) | No (HHS/OCR enforcement only) |
| PIPL | Yes (up to 7 years) | Yes (art. 69, 70) |
| POPIA | Yes (up to 10 years) | Yes |
| PIPA-KR | Yes (up to 5 years) | Yes (art. 39, statutory minimum damages) |
| PDPA-TH | Yes (THB 5M + imprisonment) | Yes |
| PDPA-SG | Yes (up to 2 years) | Yes (sec. 48O, since 2021) |
| APPI | Yes (up to 1 year) | Yes (via tort law) |

---

## 6. Data Subject Rights Landscape

Data subject rights vary substantially across frameworks. GDPR provides the most comprehensive set of rights, while sector-specific frameworks like HIPAA provide only a subset. This mindmap groups rights by type and lists which frameworks grant each right, making it easy to identify gaps when operating across multiple jurisdictions.

```mermaid
mindmap
  root((Data Subject Rights))
    Access
      GDPR -- art. 15
      LGPD -- art. 18 III
      CCPA -- sec. 1798.100
      PIPL -- art. 45
      APPI -- art. 33
      PIPA-KR -- art. 35
      PDPA-SG -- sec. 21
      HIPAA -- limited to PHI access
      DPDP India -- art. 11
      KVKK -- art. 11
      PDPA-TH -- sec. 30
      POPIA -- sec. 23
      PIPEDA -- Principle 9
    Deletion / Erasure
      GDPR -- art. 17 right to be forgotten
      LGPD -- art. 18 VI
      CCPA -- sec. 1798.105
      PIPL -- art. 47
      APPI -- art. 34
      PIPA-KR -- art. 36
      PDPA-SG -- sec. 25
      DPDP India -- art. 12
      KVKK -- art. 11
      PDPA-TH -- sec. 33
      POPIA -- sec. 24
      NOT HIPAA
      NOT FERPA
    Portability
      GDPR -- art. 20 structured machine-readable format
      LGPD -- art. 18 V
      PIPL -- art. 45
      PIPA-KR -- art. 35-2
      PDPA-SG -- sec. 26H since 2021
      DPDP India -- art. 11
      CCPA -- limited to data access format
      NOT HIPAA
      NOT APPI
    Rectification
      GDPR -- art. 16
      LGPD -- art. 18 III
      CCPA -- sec. 1798.106
      PIPL -- art. 46
      HIPAA -- art. 164.526
      APPI -- art. 34
      PIPA-KR -- art. 36
      PDPA-SG -- sec. 22
      DPDP India -- art. 11
      KVKK -- art. 11
      PDPA-TH -- sec. 36
      POPIA -- sec. 24
    Objection
      GDPR -- art. 21 including direct marketing
      LGPD -- art. 18 IV
      PIPL -- art. 44
      PIPA-KR -- art. 37
      APPI -- art. 35
      PDPA-TH -- sec. 32
      KVKK -- art. 11
      POPIA -- sec. 11
      NOT CCPA -- uses opt-out of sale instead
      NOT HIPAA
    Automated decision explanation
      GDPR -- art. 22
      LGPD -- art. 20
      PIPL -- art. 24 and art. 44
      PIPA-KR -- art. 37-2
      KVKK -- art. 11
      NOT CCPA -- pending CPPA rulemaking
      NOT HIPAA
      NOT APPI
      NOT PDPA-SG
    Consent withdrawal
      GDPR -- art. 7 para 3
      LGPD -- art. 18 IX
      PIPL -- art. 15
      PIPA-KR -- art. 37
      PDPA-SG -- sec. 16
      APPI -- withdrawal of consent
      DPDP India -- art. 6
      KVKK -- art. 11
      PDPA-TH -- sec. 19
      POPIA -- sec. 11
      HIPAA -- revoke authorization
      CCPA -- opt-out mechanism
      PIPEDA -- withdrawal at any time
    Restriction of processing
      GDPR -- art. 18
      LGPD -- art. 18 IV blocking
      PIPA-KR -- art. 37 suspension
      PIPL -- art. 44
      CCPA -- limit sensitive data use
      NOT HIPAA
      NOT APPI
      NOT PDPA-SG
    Complaint to supervisory authority
      All frameworks with a supervisory authority
      GDPR -- art. 77
      LGPD -- ANPD
      CCPA -- CA Attorney General and CPPA
      PIPL -- CAC
      HIPAA -- HHS OCR
      APPI -- PPC
      PIPA-KR -- PIPC
      PDPA-SG -- PDPC
      DPDP India -- Data Protection Board
      KVKK -- KVKK Board
      POPIA -- Information Regulator
```

**Rights coverage summary table:**

| Right | GDPR | LGPD | CCPA | PIPL | HIPAA | APPI | PIPA-KR | PDPA-SG |
|-------|------|------|------|------|-------|------|---------|---------|
| Access | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Deletion | Yes | Yes | Yes | Yes | No | Yes | Yes | Yes |
| Portability | Yes | Yes | Yes | Yes | Partial | No | Yes | Yes |
| Rectification | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |
| Objection | Yes | Yes | Opt-out | Yes | No | Yes | Yes | Yes |
| Automated Decision | Yes | Yes | Pending | Yes | No | No | Yes | No |
| Consent Withdrawal | Yes | Yes | Opt-out | Yes | Yes | Yes | Yes | Yes |
| Restriction | Yes | No | Yes | Yes | Partial | No | No | No |
| Complaint | Yes | Yes | Yes | Yes | Yes | Yes | Yes | Yes |

---

## 7. Sensitive Data Categories

What counts as "sensitive data" varies dramatically across jurisdictions. Health, biometric, and genetic data are nearly universally classified as sensitive. But financial data is sensitive under CCPA (as SPI) and PIPL but not under GDPR. Political opinions are sensitive under GDPR but not under CCPA. This mindmap organizes categories by how widely they are recognized as sensitive.

```mermaid
mindmap
  root((Sensitive Data))
    Universal -- nearly all frameworks
      Health data
        GDPR, LGPD, CCPA, PIPL
        PIPA-KR, KVKK, PDPA-TH
        POPIA, PDPA-SG, APPI, DPDP India
        HIPAA -- all PHI protected
      Biometric data
        GDPR, LGPD, CCPA, PIPL
        PIPA-KR, KVKK, PDPA-TH
        POPIA, PDPA-SG
      Genetic data
        GDPR, LGPD, CCPA, PIPL
        PIPA-KR, KVKK, PDPA-TH, POPIA
    Widely classified
      Racial / ethnic origin
        GDPR, LGPD, CCPA
        PIPA-KR, KVKK, PDPA-TH, POPIA
      Religious belief
        GDPR, LGPD, CCPA, PIPL
        PIPA-KR, KVKK, PDPA-TH, POPIA
      Political opinion
        GDPR, LGPD, PIPA-KR
        KVKK, PDPA-TH, POPIA
        NOT CCPA, NOT PIPL
      Sexual orientation
        GDPR, LGPD, CCPA
        KVKK, PDPA-TH, POPIA
      Trade union membership
        GDPR, LGPD, CCPA
        KVKK, PDPA-TH, POPIA
        NOT PIPL, NOT HIPAA
    Varies by jurisdiction
      Financial / credit data
        Sensitive -- CCPA as SPI, PIPL
        Not sensitive -- GDPR, LGPD
      Precise geolocation
        Sensitive -- CCPA as SPI
        Not sensitive -- GDPR, LGPD, PIPL
      Criminal records
        Sensitive -- GDPR art. 10
        Not sensitive -- CCPA, LGPD
      Government identifiers
        Sensitive -- CCPA SSN, passport, license
        Not sensitive -- GDPR
    Sector or context-specific
      Children data
        COPPA -- under 13
        FERPA -- education records
        PIPL -- under 14
        LGPD -- under 18
      Education records
        FERPA -- sole authority
        Not addressed by most other frameworks
      Psychotherapy notes
        HIPAA -- separate authorization required
      Substance abuse records
        42 CFR Part 2 -- heightened protections beyond standard HIPAA
```

**Key differences at a glance:**

| Category | GDPR | LGPD | CCPA/CPRA | PIPL | HIPAA | PIPA-KR |
|----------|------|------|-----------|------|-------|---------|
| Health | Sensitive | Sensitive | Sensitive (SPI) | Sensitive | All PHI protected | Sensitive |
| Biometric | Sensitive | Sensitive | Sensitive (SPI) | Sensitive | PHI identifier | Sensitive |
| Genetic | Sensitive | Sensitive | Sensitive (SPI) | Not listed | PHI (per GINA) | Sensitive |
| Racial/ethnic | Sensitive | Sensitive | Sensitive (SPI) | Not listed | Not separate | Sensitive |
| Political opinion | Sensitive | Sensitive | Not SPI | Not listed | N/A | Sensitive |
| Religion | Sensitive | Sensitive | Sensitive (SPI) | Sensitive | N/A | Sensitive |
| Sexual orientation | Sensitive | Sensitive | Sensitive (SPI) | Not listed | N/A | Not listed |
| Trade union | Sensitive | Sensitive | Sensitive (SPI) | Not listed | N/A | Not listed |
| Financial/credit | Not sensitive | Not sensitive | Sensitive (SPI) | Sensitive | N/A | Not listed |
| Precise geolocation | Not sensitive | Not sensitive | Sensitive (SPI) | Sensitive (tracks) | PHI identifier | Not listed |
| Criminal records | Sensitive (art. 10) | Not sensitive | Not SPI | Not listed | N/A | Not listed |

---

## 8. Legal Matrix Interconnections

The 8 legal matrices in this framework are not independent -- they form an interconnected regulatory web. A data breach triggers breach notification requirements, which may lead to penalties. Consent determines how data subject rights can be exercised. The DPO oversees all these processes. This vertical flow diagram shows how the matrices relate to each other with labeled edges.

```mermaid
flowchart TD
    DPO["DPO Requirements\nMatrix"]
    CONSENT["Consent Requirements\nMatrix"]
    SENSITIVE["Sensitive Data\nCategories Matrix"]
    BREACH["Breach Notification\nMatrix"]
    RIGHTS["Data Subject Rights\nMatrix"]
    TRANSFER["Cross-Border Transfer\nMatrix"]
    RETENTION["Data Retention\nMatrix"]
    PENALTIES["Penalties\nMatrix"]

    %% DPO oversees key processes
    DPO -- "Oversees breach\nnotification process" --> BREACH
    DPO -- "Manages data\nsubject requests" --> RIGHTS
    DPO -- "Advises on\ntransfer mechanisms" --> TRANSFER

    %% Sensitive data raises consent bar
    SENSITIVE -- "Heightened consent\nrequirements for\nsensitive categories" --> CONSENT
    SENSITIVE -- "Breach of sensitive data\n= higher notification\nthreshold met" --> BREACH

    %% Consent affects rights and transfers
    CONSENT -- "Withdrawal triggers\ndeletion right" --> RIGHTS
    CONSENT -- "Consent is one basis\nfor cross-border transfer" --> TRANSFER

    %% Retention affects rights and breach exposure
    RETENTION -- "Retention limits affect\nwhen deletion right\ncan be exercised" --> RIGHTS
    RETENTION -- "Over-retention\nincreases breach\nexposure" --> BREACH
    RETENTION -- "Localization requirements\naffect retention location" --> TRANSFER

    %% Failures trigger penalties
    BREACH -- "Failure to notify\ntriggers fines" --> PENALTIES
    RIGHTS -- "Failure to honor rights\ntriggers enforcement" --> PENALTIES

    %% Transfer and consent
    TRANSFER -- "May require consent\nor adequacy decision" --> CONSENT

    %% Styling
    style DPO fill:#f9a825,color:#000
    style CONSENT fill:#1565c0,color:#fff
    style SENSITIVE fill:#d32f2f,color:#fff
    style BREACH fill:#d32f2f,color:#fff
    style RIGHTS fill:#2e7d32,color:#fff
    style TRANSFER fill:#1565c0,color:#fff
    style RETENTION fill:#9e9e9e,color:#fff
    style PENALTIES fill:#b71c1c,color:#fff
```

**How to read the interconnections:**

1. **Breach notification triggers penalties.** Failure to notify the authority within the required deadline (72h GDPR, 3 days LGPD, 60 days HIPAA) is itself a sanctionable violation.

2. **Consent determines data subject rights.** When consent is the legal basis, withdrawal triggers the right to deletion. When consent was not obtained properly, the data subject can object to processing.

3. **Sensitive data categories raise the consent bar.** Processing health, biometric, or genetic data requires explicit or specific consent in most jurisdictions, compared to standard consent for non-sensitive data.

4. **The DPO sits at the center.** The DPO (or equivalent) oversees breach notification, manages data subject rights requests, and advises on cross-border transfer mechanisms.

5. **Cross-border transfers require consent or adequacy.** Without an adequacy decision or approved safeguard, consent from the data subject may be the only viable transfer mechanism.

6. **Data retention limits affect deletion rights.** Organizations cannot honor deletion requests during mandatory retention periods (e.g., HIPAA 6 years, SOX 7 years). Conversely, over-retention beyond the necessary period increases breach exposure.

7. **Sensitive data breaches are always notifiable.** A breach involving sensitive data categories (health, biometric, genetic) almost always meets the "risk to rights" threshold that triggers notification obligations.
