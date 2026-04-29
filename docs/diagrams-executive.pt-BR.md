[Read in English](diagrams-executive.md)

# Diagramas Executivos

Visualizacoes estrategicas do panorama de compliance para executivos, conselhos e lideranca de GRC.

Este documento apresenta 136 frameworks regulatórios e mais de 2.800 controles como ativos estratégicos. Cada diagrama responde a uma pergunta relevante para a liderança: onde temos cobertura, onde estão as lacunas e o que priorizar.

---

## 1. Cobertura Regulatória Global

Nossa biblioteca de frameworks abrange todas as principais regiões regulatórias. O grafico abaixo mostra a distribuicao por geografia.

```mermaid
pie title 136 Frameworks por Regiao
    "Brasil (60)" : 60
    "Global/Internacional (40)" : 40
    "Asia-Pacifico (12)" : 12
    "Estados Unidos (11)" : 11
    "Europa/UE (10)" : 10
    "Oriente Medio e Africa (2)" : 2
    "Canada (1)" : 1
```

**Conclusão:** Brasil e padroes globais juntos representam 74% da biblioteca. Qualquer empresa operando no Brasil com clientes internacionais obtem cobertura imediata e profunda.

---

## 2. Seletor de Stack de Compliance

Nem toda empresa precisa de todos os 136 frameworks. Esta árvore de decisão ajuda executivos a identificar o stack mínimo de compliance com base em onde a empresa opera e qual setor atende.

```mermaid
flowchart TD
    START["Onde sua empresa opera?"] --> BR["Brasil"]
    START --> EU["Uniao Europeia"]
    START --> US["Estados Unidos"]
    START --> GLOBAL["SaaS Global"]
    START --> APAC["Asia-Pacifico"]

    BR --> BR_SECTOR{"Qual setor?"}
    BR_SECTOR --> BR_FIN["Financeiro"]
    BR_SECTOR --> BR_INS["Seguros"]
    BR_SECTOR --> BR_HEALTH["Saude"]
    BR_SECTOR --> BR_GOV["Governo"]
    BR_SECTOR --> BR_GEN["Geral"]

    BR_FIN --> BR_FIN_STACK["LGPD + BCB 4893 CMN 4557 + CMN 4606 PCI DSS + SOC 2"]
    BR_INS --> BR_INS_STACK["LGPD + CNSP 381 CNSP 393 + SUSEP 638 SOC 2"]
    BR_HEALTH --> BR_HEALTH_STACK["LGPD + ANVISA 134 CFM + TISS ISO 27001"]
    BR_GOV --> BR_GOV_STACK["LGPD + PNSI GSI IN1 + GSI IN3 ICP-Brasil + ReGIC"]
    BR_GEN --> BR_GEN_STACK["LGPD + Marco Civil ISO 27001 + SOC 2"]

    EU --> EU_SECTOR{"Qual setor?"}
    EU_SECTOR --> EU_FIN["Financeiro"]
    EU_SECTOR --> EU_GEN["Geral"]
    EU_SECTOR --> EU_AI["Produtos de IA"]
    EU_FIN --> EU_FIN_STACK["GDPR + DORA NIS2 + PCI DSS"]
    EU_GEN --> EU_GEN_STACK["GDPR + NIS2"]
    EU_AI --> EU_AI_STACK["GDPR + NIS2 EU AI Act + ISO 42001"]

    US --> US_SECTOR{"Qual setor?"}
    US_SECTOR --> US_FED["Federal / DoD"]
    US_SECTOR --> US_HEALTH["Saude"]
    US_SECTOR --> US_FIN["Financeiro"]
    US_SECTOR --> US_EDU["Educacao"]
    US_SECTOR --> US_GEN["Geral"]
    US_FED --> US_FED_STACK["FedRAMP + FISMA NIST 800-53 + CMMC"]
    US_HEALTH --> US_HEALTH_STACK["HIPAA + HITRUST SOC 2"]
    US_FIN --> US_FIN_STACK["SOX + GLBA PCI DSS + SOC 1/2"]
    US_EDU --> US_EDU_STACK["FERPA + COPPA SOC 2"]
    US_GEN --> US_GEN_STACK["SOC 2 + CCPA"]

    GLOBAL --> GLOBAL_STACK["SOC 2 + ISO 27001 GDPR + CCPA CSA CCM"]

    APAC --> APAC_REGION{"Qual pais?"}
    APAC_REGION --> SG["Singapura"]
    APAC_REGION --> AU["Australia"]
    APAC_REGION --> JP["Japao"]
    APAC_REGION --> KR["Coreia do Sul"]
    SG --> SG_STACK["PDPA-SG + MAS TRM ISO 27001"]
    AU --> AU_STACK["Essential Eight APRA CPS 234 ISO 27001"]
    JP --> JP_STACK["APPI + ISMAP ISO 27001"]
    KR --> KR_STACK["PIPA + K-ISMS-P ISO 27001"]

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

**Conclusão:** Comece com o menor stack que cobre suas obrigacoes regulatorias. Voce sempre pode expandir depois. As caixas verdes sao os pontos de partida recomendados.

---

## 3. Modelo das Três Linhas de Defesa

O compliance não é responsabilidade de uma única equipe. Este diagrama mostra como o BRACIS se mapeia a cada linha de defesa.

```mermaid
flowchart TD
    subgraph LINE1["1a Linha -- Operacoes"]
        PE["Platform Engineering implementation_guidance"]
        DSO["DevSecOps implementation_guidance"]
        TOOLS1["OWASP ASVS / SLSA CIS Controls / DISA STIG PCI SSF / NIST 800-218"]
    end

    subgraph LINE2["2a Linha -- Riscos e Compliance"]
        GRC["Analise de Lacunas GRC Mapeamentos cruzados"]
        LEGAL["Matrizes Legais 8 matrizes multijurisdicionais"]
        POLICY["Frameworks de Politica ISO 27001 / NIST CSF COBIT / SOC 2"]
    end

    subgraph LINE3["3a Linha -- Auditoria"]
        CERT["Certificacoes ISO 27001 / ISO 27701 SOC 1 / SOC 2"]
        REG["Auditorias Regulatorias FedRAMP / CMMC DORA / HIPAA"]
        REPORT["Relatorios ao Conselho 123 mapeamentos cruzados"]
    end

    LINE1 --> LINE2 --> LINE3

    style LINE1 fill:#e3f2fd,stroke:#1565c0,color:#000
    style LINE2 fill:#fff3e0,stroke:#e65100,color:#000
    style LINE3 fill:#fce4ec,stroke:#b71c1c,color:#000
```

**Conclusão:** A 1a linha usa a implementation_guidance diariamente. A 2a linha usa mapeamentos cruzados e matrizes legais para monitoramento continuo. A 3a linha usa certificacoes e mapeamentos como evidencia de auditoria.

---

## 4. Mapa de Dependência Regulatória

Regulações não existem de forma isolada. Entender como as principais famílias regulatórias se relacionam evita trabalho duplicado e revela controles compartilhados.

```mermaid
mindmap
    root((Frameworks de Compliance))
        Familia ISO
            ISO 27001
                ISO 27701
                ISO 27017
                ISO 27018
                ISO 27005
                ISO 27035
                ISO 22301
                ISO 42001
        Familia NIST
            NIST 800-53
                NIST CSF v2
                NIST 800-171
                    CMMC v2
                FedRAMP
                FISMA
                NIST AI RMF
                NIST Privacy
        Familia PCI
            PCI DSS v4
                PCI PIN
                PCI 3DS
                PCI SSF
                PCI P2PE
        Leis de Privacidade
            GDPR
                LGPD
                CCPA/CPRA
                PIPL
                DPDP India
                PDPA-SG
                APPI Japao
                PIPA Coreia
                KVKK Turquia
                PIPEDA
                POPIA
```

**Conclusão:** ISO 27001 e GDPR sao os dois centros gravitacionais. Implementar ISO 27001 cobre parcelas significativas do NIST, PCI e frameworks setoriais. Conformidade com GDPR cria uma baseline para quase toda outra lei de privacidade.

---

## 5. Panorama de Risco de Penalidades

Nem todas as regulações carregam o mesmo risco de enforcement. Este quadrante posiciona os principais frameworks por atividade de fiscalização e tamanho máximo de penalidade.

```mermaid
quadrantChart
    title Avaliacao de Risco de Penalidades
    x-axis "Baixo Enforcement" --> "Alto Enforcement"
    y-axis "Baixa Penalidade" --> "Alta Penalidade"
    quadrant-1 Risco Critico
    quadrant-2 Alta Penalidade Baixo Enforcement
    quadrant-3 Monitorar
    quadrant-4 Alto Enforcement Baixa Penalidade
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

**Conclusão:** GDPR, SOX e DORA estao no quadrante de risco critico. O EU AI Act e o PIPL carregam tetos de penalidade massivos mas enforcement ainda em maturacao.

---

## 6. Roteiro de Maturidade em Compliance

Compliance e uma jornada, nao um destino. Este roteiro mostra uma abordagem em fases, de padroes fundacionais ate cobertura sistematica.

```mermaid
timeline
    title Roteiro de Maturidade em Compliance
    section Fase 1 -- Fundacao
        ISO 27001 : SOC 2 : Lei de privacidade local -- GDPR, LGPD ou CCPA : NIST CSF v2
    section Fase 2 -- Setor
        PCI DSS v4 : HIPAA ou DORA : CMMC ou FedRAMP : Reguladores setoriais -- Bacen 4893, CNSP 381
    section Fase 3 -- Avancado
        Cadeia de suprimentos -- SLSA, NIST 800-218 : Governanca de IA -- ISO 42001, NIST AI RMF : Engenharia de privacidade -- ISO 27701 : Resiliencia -- NIS2, DORA, ISO 22301
    section Fase 4 -- Excelencia
        Mapeamento cruzado completo -- 123 arquivos : Matrizes legais -- 8 jurisdicoes : Monitoramento continuo de compliance : Evidencia pronta para auditoria
```

**Conclusão:** A Fase 1 sozinha cobre 60-70% da maioria dos requisitos de compliance. Cada fase subsequente adiciona profundidade e especificidade setorial.

---

## 7. Ciclo de Vida de Dados e Pontos de Contato Regulatório

Cada etapa do ciclo de vida de dados aciona obrigações regulatórias. Este diagrama mapeia esses pontos de contato para as matrizes legais específicas do BRACIS.

```mermaid
flowchart TD
    COLLECT["Coleta de Dados"] --> PROCESS["Processamento de Dados"]
    PROCESS --> STORE["Armazenamento de Dados"]
    STORE --> SHARE["Compartilhamento / Transferencia Internacional"]
    STORE --> DSR["Requisicao do Titular"]
    STORE --> BREACH["Violacao de Dados"]

    COLLECT -.- C_REQ["consent-requirements-matrix.yaml GDPR Art 6-7, LGPD Art 7-8"]
    PROCESS -.- P_REQ["sensitive-data-categories-matrix.yaml ISO 27001, NIST 800-53"]
    STORE -.- S_REQ["data-retention-matrix.yaml Criptografia: ISO 27018, PCI DSS"]
    SHARE -.- SH_REQ["cross-border-transfer-matrix.yaml GDPR Cap V, LGPD Art 33-36"]
    DSR -.- DSR_REQ["data-subject-rights-matrix.yaml Acesso, Exclusao, Portabilidade"]
    BREACH -.- B_REQ["breach-notification-matrix.yaml penalties-matrix.yaml dpo-requirements-matrix.yaml"]

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

**Conclusão:** Nossas 8 matrizes legais cobrem cada etapa do ciclo de vida de dados em 17 jurisdicoes. Uma violacao de dados aciona 3 matrizes simultaneamente -- a preparacao aqui tem o maior ROI de reducao de risco.

---

## 8. Ecossistema Regulatório Brasileiro

O Brasil possui um dos panoramas regulatórios mais complexos para empresas de tecnologia, com 60 frameworks distribuídos entre mais de 10 reguladores. Este mapa mostra os principais órgãos reguladores organizados por setor, com a LGPD como fio condutor transversal.

```mermaid
mindmap
    root((Ecossistema de Compliance Brasileiro))
        LGPD + ANPD
            Lei geral de protecao de dados
            Autoridade Nacional de Protecao de Dados
        BCB / CMN -- Financeiro
            BCB 4893
            BCB 3978
            BCB 304
            CMN 4557
            CMN 4606
            CMN 4968
            6 frameworks adicionais
        CVM -- Mercado de Capitais
            CVM 35
            CVM 50
            CVM 88
            CVM 135
            CVM 175
            CVM 193
        CNSP / SUSEP -- Seguros
            CNSP 381
            CNSP 393
            CNSP 408
            CNSP 416
            SUSEP 612
            SUSEP 638
        GSI / PR -- Seguranca do Governo
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
        ANEEL / ONS -- Energia
            ANEEL 964
            ONS ARCiber
        ANVISA / CFM / ANS -- Saude
            ANVISA 134
            ANVISA BPF
            ANVISA SaMD
            CFM IA
            CFM Telemedicina
            TISS
        ANAC -- Aviacao
            ANAC SGSO
            ANAC Ciber
```

**Conclusão:** A LGPD e o fio que conecta todos os setores no Brasil. O setor financeiro e o mais regulado, com 22 frameworks distribuidos entre 4 reguladores. Qualquer empresa operando no setor financeiro brasileiro deve planejar investimento significativo em compliance.
