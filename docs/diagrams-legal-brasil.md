[Read in English](diagrams-legal.md)

# Panorama Regulatório Brasileiro

Diagramas visuais do ecossistema regulatório brasileiro para advogados, DPOs, encarregados de dados e times jurídicos. Abrange privacidade, setor financeiro, governo, saúde, infraestrutura crítica e telecomunicações.

---

## 1. Ecossistema Regulatório Brasileiro -- Visão Geral

O Brasil possui um dos ecossistemas regulatórios mais fragmentados do mundo, com 60 frameworks setoriais emitidos por mais de uma dezena de órgãos reguladores. Este mindmap organiza todos os 60 frameworks por regulador ou domínio, facilitando a identificação de quais normas se aplicam a cada tipo de organização.

```mermaid
mindmap
  root("Regulação Brasileira — 60 frameworks")
    LGPD e Privacidade
      LGPD — 46 controles
      ANPD Regulamentos — 25 controles
      Marco Civil — 28 controles
      Decreto 8.771 — 19 controles
    Banco Central — BCB
      Bacen 4893 — ciber IFs
      BCB 85 — ciber IPs
      BCB 3.978 — PLD IFs
      BCB 44 — PLD IPs
      BCB Conj. 2 — incidentes
      BCB IN 291 — notificação
      BCB 304 — VASPs
      Open Finance
      Pix Security
      Pix MED 2.0
    Conselho Monetário Nacional — CMN
      CMN 4.557 — riscos
      CMN 4.968 — auditoria
      CMN 4.606 — compliance
    Comissão de Valores Mobiliários — CVM
      CVM 35 — ciber capitais
      CVM 50 — PLD capitais
      CVM 88 — crowdfunding
      CVM 175 — fundos
      CVM 135 — mercados organizados
      CVM 193 — ESG
    Seguros — CNSP e SUSEP
      CNSP 381 — ciber seguros
      CNSP 393 — sanções
      CNSP 408 — meios remotos
      CNSP 416 — controles internos
      SUSEP 638 — ciber técnico
      SUSEP 612 — PLD seguros
      Open Insurance
    Governo e Segurança da Informação — GSI/PR
      PNSI
      PNCiber
      IN GSI 1
      IN GSI 3
      IN GSI 5
      ReGIC
      PNSIC
    Saúde — ANVISA, CFM, ANS
      ANVISA 134
      ANVISA SaMD
      ANVISA BPF
      CFM Telemedicina
      CFM IA
      TISS
      PEP
      Receituário
    Infraestrutura Crítica
      ANEEL 964
      ONS ARCiber
      R-Ciber
      ANATEL IoT
      RBAC 107
      RBAC 108
    Leis Complementares
      LAI
      Gov Digital
      ICP-Brasil
      Crimes Ciber
      Info Classificada
      Dados Gov
      Marco Legal Cripto
      PLD/FT Base
      Doutrina Ciber
```

---

## 2. LGPD -- Direitos dos Titulares

A LGPD confere aos titulares de dados pessoais um conjunto abrangente de direitos, concentrados no art. 18, com complemento no art. 20 para decisões automatizadas. Esses direitos podem ser exercidos a qualquer momento mediante requisição ao controlador ou ao encarregado de dados.

```mermaid
mindmap
  root("Direitos dos Titulares — LGPD art. 18")
    Confirmação de tratamento
      art. 18, I
    Acesso aos dados
      art. 18, II
    Correção de dados incompletos ou desatualizados
      art. 18, III
    Anonimização, bloqueio ou eliminação
      art. 18, IV
      Dados desnecessários, excessivos ou em desconformidade
    Portabilidade
      art. 18, V
      Mediante requisição expressa e regulamentação da ANPD
    Eliminação com consentimento
      art. 18, VI
      Dados tratados com base no consentimento
    Informação sobre compartilhamento
      art. 18, VII
      Entidades públicas e privadas com quem houve uso compartilhado
    Informação sobre não consentimento
      art. 18, VIII
      Possibilidade e consequências de não fornecer consentimento
    Revogação do consentimento
      art. 18, IX
      Procedimento gratuito e facilitado
    Revisão de decisões automatizadas
      art. 20
      Decisões tomadas unicamente com base em tratamento automatizado
    Oposição ao tratamento
      art. 18, parágrafo 2
      Tratamento com base em hipótese diversa do consentimento em caso de descumprimento
```

---

## 3. LGPD -- Bases Legais para Tratamento

O tratamento de dados pessoais no Brasil só é lícito quando enquadrado em uma das dez bases legais taxativamente previstas no art. 7 da LGPD. O consentimento não é hierarquicamente superior às demais bases — cada hipótese é independente e autossuficiente.

```mermaid
mindmap
  root("Bases Legais — LGPD art. 7")
    Consentimento
      art. 7, I
      Livre, informado, inequívoco
      Para dados sensíveis: consentimento específico e destacado — art. 11, I
    Obrigação legal ou regulatória
      art. 7, II
      Cumprimento de obrigação legal pelo controlador
    Administração pública
      art. 7, III
      Tratamento necessário para execução de políticas públicas
    Estudos e pesquisa
      art. 7, IV
      Por órgão de pesquisa, preferencialmente com anonimização
    Execução de contrato
      art. 7, V
      A pedido do titular, para execução ou procedimentos preliminares
    Exercício regular de direitos
      art. 7, VI
      Em processo judicial, administrativo ou arbitral
    Proteção da vida
      art. 7, VII
      Proteção da vida ou da incolumidade física do titular ou de terceiro
    Tutela da saúde
      art. 7, VIII
      Exclusivamente em procedimento de saúde, por profissional ou serviço de saúde
    Legítimo interesse
      art. 7, IX
      Finalidades legítimas com base em situações concretas
      Exige teste de balanceamento — art. 10
    Proteção do crédito
      art. 7, X
      Inclusive quanto à legislação pertinente
```

---

## 4. Setor Financeiro -- Hierarquia Regulatória

O sistema financeiro brasileiro é regulado por uma estrutura hierárquica de conselhos e autarquias. O CMN define políticas macro, que são implementadas pelo BCB e pela CVM. No mercado de seguros, o CNSP desempenha papel análogo, com a SUSEP como supervisora. Cada regulador emite normas setoriais específicas de cibersegurança, PLD/FT e controles internos.

```mermaid
flowchart TD
    CMN["CMN\nConselho Monetário Nacional"] --> BCB["BCB\nBanco Central do Brasil"]
    CMN --> CVM["CVM\nComissão de Valores Mobiliários"]
    CNSP["CNSP\nConselho Nacional de Seguros Privados"] --> SUSEP["SUSEP\nSuperintendência de Seguros Privados"]

    CMN --> CMN_N["CMN 4.557 — gestão de riscos\nCMN 4.968 — auditoria interna\nCMN 4.606 — compliance"]

    BCB --> BCB_CIBER["Bacen 4893 — ciber IFs\nBCB 85 — ciber IPs"]
    BCB --> BCB_PLD["BCB 3.978 — PLD IFs\nBCB 44 — PLD IPs"]
    BCB --> BCB_INC["BCB Conj. 2 — incidentes\nBCB IN 291 — notificação"]
    BCB --> BCB_ECO["Open Finance\nPix Security\nPix MED 2.0\nBCB 304 — VASPs"]

    CVM --> CVM_CIBER["CVM 35 — ciber capitais"]
    CVM --> CVM_PLD["CVM 50 — PLD capitais"]
    CVM --> CVM_MKT["CVM 88 — crowdfunding\nCVM 175 — fundos\nCVM 135 — mercados organizados\nCVM 193 — ESG"]

    CNSP --> CNSP_N["CNSP 381 — ciber seguros\nCNSP 393 — sanções\nCNSP 408 — meios remotos\nCNSP 416 — controles internos"]

    SUSEP --> SUSEP_N["SUSEP 638 — ciber técnico\nSUSEP 612 — PLD seguros\nOpen Insurance"]

    style CMN fill:#1565c0,color:#fff
    style BCB fill:#1976d2,color:#fff
    style CVM fill:#1976d2,color:#fff
    style CNSP fill:#1565c0,color:#fff
    style SUSEP fill:#1976d2,color:#fff
    style CMN_N fill:#e3f2fd,color:#000
    style BCB_CIBER fill:#e8f5e9,color:#000
    style BCB_PLD fill:#fff3e0,color:#000
    style BCB_INC fill:#fce4ec,color:#000
    style BCB_ECO fill:#f3e5f5,color:#000
    style CVM_CIBER fill:#e8f5e9,color:#000
    style CVM_PLD fill:#fff3e0,color:#000
    style CVM_MKT fill:#f3e5f5,color:#000
    style CNSP_N fill:#e3f2fd,color:#000
    style SUSEP_N fill:#e3f2fd,color:#000
```

**Legenda de cores:** azul = órgão regulador, verde = cibersegurança, laranja = PLD/FT, rosa = incidentes, roxo = ecossistemas abertos e mercados.

---

## 5. Três Linhas de Defesa -- Regulação Financeira Brasileira

O modelo de três linhas de defesa é a espinha dorsal da governança financeira no Brasil. A primeira linha (operações) implementa controles no dia a dia. A segunda linha (riscos e compliance) supervisiona e monitora. A terceira linha (auditoria) avalia independentemente a eficácia das duas primeiras.

```mermaid
flowchart TD
    subgraph L1["1ª Linha: Operações"]
        L1_A["CMN 4.606 — Compliance"]
        L1_B["Bacen 4893 / BCB 85 — Controles cibersegurança"]
        L1_C["SUSEP 638 — Controles técnicos"]
        L1_D["CVM 35 — Controles ciber capitais"]
    end

    subgraph L2["2ª Linha: Riscos e Compliance"]
        L2_A["CMN 4.557 — Gestão de riscos"]
        L2_B["CNSP 416 — Controles internos seguros"]
        L2_C["BCB 3.978 / CVM 50 — PLD/FT"]
        L2_D["SUSEP 612 / BCB 44 — PLD/FT setorial"]
    end

    subgraph L3["3ª Linha: Auditoria"]
        L3_A["CMN 4.968 — Auditoria interna"]
        L3_B["BCB Conj. 2 — Notificação de incidentes"]
        L3_C["BCB IN 291 — Procedimentos de reporte"]
        L3_D["CNSP 393 — Sanções administrativas"]
    end

    L1 --> L2 --> L3

    style L1 fill:#e8f5e9,stroke:#2e7d32,color:#000
    style L2 fill:#fff8e1,stroke:#f57f17,color:#000
    style L3 fill:#ffebee,stroke:#c62828,color:#000
```

---

## 6. Governo Federal -- Cadeia de Comando de Segurança da Informação

A segurança da informação no governo federal brasileiro é estruturada em uma cadeia hierárquica que parte da Presidência da República, passa pelo GSI/PR e se desdobra em políticas nacionais, instruções normativas e procedimentos operacionais. As INs do GSI possuem interseções diretas com NIST 800-53 e ISO 27001.

```mermaid
flowchart TD
    PR["Presidência da República"] --> GSI["GSI/PR\nGabinete de Segurança Institucional"]

    GSI --> PNSI["PNSI\nPolítica Nacional de\nSegurança da Informação"]
    GSI --> PNCiber["PNCiber\nPolítica Nacional de\nCibersegurança"]

    PNSI --> IN1["IN GSI/PR 1\nGovernança de SI na APF"]
    PNSI --> ReGIC["ReGIC\nGestão de Incidentes\nCibernéticos Federais"]

    IN1 --> IN3["IN GSI/PR 3\nProcessos Operacionais de SI"]
    IN1 --> IN5["IN GSI/PR 5\nCloud na APF"]

    PNSIC["PNSIC\nPolítica Nacional de Segurança\nde Infraestruturas Críticas"] -.-> PNSI
    PNSIC -.-> PNCiber

    DG["Dados Gov\nCompartilhamento de\nDados na APF"] -.-> PNSI
    IC["Info Classificada\nClassificação de\nInformações Sigilosas"] -.-> IN1

    IN1 -. "intersecta" .-> NIST["NIST 800-53\nGovernança, riscos, incidentes"]
    IN3 -. "intersecta" .-> ISO["ISO 27001 Anexo A\nControles operacionais"]

    style PR fill:#1565c0,color:#fff
    style GSI fill:#1976d2,color:#fff
    style PNSI fill:#2e7d32,color:#fff
    style PNCiber fill:#2e7d32,color:#fff
    style IN1 fill:#4caf50,color:#fff
    style IN3 fill:#66bb6a,color:#fff
    style IN5 fill:#66bb6a,color:#fff
    style ReGIC fill:#ef5350,color:#fff
    style PNSIC fill:#ff9800,color:#fff
    style DG fill:#78909c,color:#fff
    style IC fill:#78909c,color:#fff
    style NIST fill:#9e9e9e,color:#fff
    style ISO fill:#9e9e9e,color:#fff
```

**Legenda:** linhas contínuas = derivação direta; linhas tracejadas = complementa ou intersecta.

---

## 7. Saúde -- Ecossistema Regulatório

A regulação de saúde digital no Brasil é fragmentada entre três órgãos principais: ANVISA (dispositivos médicos e farma), CFM (exercício profissional médico) e ANS (saúde suplementar). A LGPD permeia todo o ecossistema como camada transversal de proteção de dados de saúde, e frameworks internacionais como IEC 62443, EU AI Act e NIST AI RMF possuem interseções relevantes.

```mermaid
mindmap
  root("Regulação de Saúde Digital")
    ANVISA
      IN 134 — sistemas computadorizados GMP — 36 controles
      SaMD — dispositivos médicos software — 25 controles
      BPF — boas práticas de fabricação — 20 controles
      Receituário — receita digital — 20 controles
    CFM
      Telemedicina — 30 controles
      IA na Medicina — 35 controles
      PEP — Prontuário Eletrônico do Paciente — 20 controles
    ANS
      TISS — troca de informações em saúde suplementar — 30 controles
    Interseções transversais
      LGPD — dados de saúde como dado sensível — art. 11
      IEC 62443 — segurança de dispositivos industriais e médicos
      EU AI Act e NIST AI RMF — classificação de risco para IA em saúde
      ICP-Brasil — assinatura digital para receituário e PEP
```

---

## 8. Infraestrutura Crítica -- Mapa Setorial

A Política Nacional de Segurança de Infraestruturas Críticas (PNSIC) é o guarda-chuva que abrange energia, telecomunicações, aviação e outros setores essenciais. Cada setor possui seu regulador específico e normas próprias de cibersegurança, mas todos convergem na LGPD, PNSI e PNCiber como camadas transversais.

```mermaid
flowchart TD
    PNSIC["PNSIC\nPolítica Nacional de Segurança\nde Infraestruturas Críticas"] --> ENERGIA["Energia"]
    PNSIC --> TELECOM["Telecomunicações"]
    PNSIC --> AVIACAO["Aviação"]
    PNSIC --> TRANSVERSAL["Camada Transversal"]

    ENERGIA --> ANEEL["ANEEL 964\nCibersegurança do\nsetor elétrico — 18 controles"]
    ANEEL --> ONS["ONS ARCiber\nControles mínimos para\nagentes do SIN — 24 controles"]
    ANEEL -. "intersecta" .-> NERC["NERC CIP"]
    ANEEL -. "intersecta" .-> IEC["IEC 62443"]

    TELECOM --> RCIBER["R-Ciber\nCibersegurança telecom\n25 controles"]
    TELECOM --> IoT["ANATEL IoT\nCertificação de equipamentos\n20 controles"]
    RCIBER -. "intersecta" .-> IN3["IN GSI/PR 3"]

    AVIACAO --> RBAC107["RBAC 107\nAeródromos — AVSEC ciber\n8 controles"]
    AVIACAO --> RBAC108["RBAC 108\nOperadores aéreos — AVSEC ciber\n8 controles"]

    TRANSVERSAL --> LGPD_T["LGPD"]
    TRANSVERSAL --> PNSI_T["PNSI"]
    TRANSVERSAL --> PNCiber_T["PNCiber"]

    style PNSIC fill:#e65100,color:#fff
    style ENERGIA fill:#ff9800,color:#fff
    style TELECOM fill:#ff9800,color:#fff
    style AVIACAO fill:#ff9800,color:#fff
    style TRANSVERSAL fill:#1565c0,color:#fff
    style ANEEL fill:#fff3e0,color:#000
    style ONS fill:#fff3e0,color:#000
    style RCIBER fill:#fff3e0,color:#000
    style IoT fill:#fff3e0,color:#000
    style RBAC107 fill:#fff3e0,color:#000
    style RBAC108 fill:#fff3e0,color:#000
    style NERC fill:#9e9e9e,color:#fff
    style IEC fill:#9e9e9e,color:#fff
    style IN3 fill:#9e9e9e,color:#fff
    style LGPD_T fill:#e3f2fd,color:#000
    style PNSI_T fill:#e3f2fd,color:#000
    style PNCiber_T fill:#e3f2fd,color:#000
```

---

## 9. PLD/FT -- Cadeia de Prevenção à Lavagem de Dinheiro

A prevenção à lavagem de dinheiro e ao financiamento do terrorismo no Brasil parte da Lei 9.613/1998, que define as obrigações gerais, e se desdobra em normas setoriais para cada segmento regulado. O fluxo operacional obrigatório segue a cadeia KYC, monitoramento, comunicação ao COAF e aplicação de sanções.

```mermaid
flowchart TD
    LEI["Lei 9.613/1998\nPLD/FT Base"]

    LEI --> SF["Sistema Financeiro"]
    LEI --> MC["Mercado de Capitais"]
    LEI --> SEG["Seguros"]
    LEI --> VASP["VASPs e Criptoativos"]

    SF --> BCB3978["BCB 3.978\nPLD para IFs — 38 controles"]
    SF --> BCB44["BCB 44\nPLD para IPs — 33 controles"]

    MC --> CVM50["CVM 50\nPLD capitais — 46 controles"]

    SEG --> SUSEP612["SUSEP 612\nPLD seguros — 40 controles"]

    VASP --> CRIPTO["Lei 14.478\nMarco Legal Cripto"]
    CRIPTO --> BCB304["BCB 304\nRegulamentação VASPs — 26 controles"]

    BCB3978 --> FLUXO["Fluxo Operacional Obrigatório"]
    BCB44 --> FLUXO
    CVM50 --> FLUXO
    SUSEP612 --> FLUXO
    BCB304 --> FLUXO

    FLUXO --> KYC["1. KYC\nConheça Seu Cliente\nIdentificação e qualificação"]
    KYC --> MON["2. Monitoramento\nOperações atípicas\nAlerta automático"]
    MON --> COAF["3. Comunicação ao COAF\nOperações suspeitas\nPrazo: 24 horas"]
    COAF --> SANC["4. Sanções\nBloqueio de ativos\nReporte às autoridades"]

    style LEI fill:#1565c0,color:#fff
    style CRIPTO fill:#7b1fa2,color:#fff
    style KYC fill:#2e7d32,color:#fff
    style MON fill:#f57f17,color:#fff
    style COAF fill:#d32f2f,color:#fff
    style SANC fill:#b71c1c,color:#fff
    style FLUXO fill:#455a64,color:#fff
```

---

## 10. Notificação de Incidentes -- Fluxo Obrigatório

Quando um incidente de segurança ocorre, múltiplas obrigações de notificação podem se sobrepor simultaneamente. Um vazamento de dados pessoais em uma instituição financeira, por exemplo, exige notificação paralela à ANPD, ao BCB e potencialmente ao CTIR Gov. Este fluxograma mapeia a árvore de decisão para cada cenário.

```mermaid
flowchart TD
    INC["Incidente de segurança detectado"] --> DP{Envolve dados\npessoais?}
    INC --> FIN{Envolve sistema\nfinanceiro?}
    INC --> IC{Envolve infraestrutura\ncrítica?}
    INC --> SAUDE{Envolve saúde ou\ndispositivo médico?}

    DP -- Sim --> ANPD["Notificar ANPD + titulares\nPrazo: 3 dias úteis\nRes. CD/ANPD 15/2024\nLGPD art. 48"]
    DP -- Não --> DP_DOC["Documentar internamente"]

    FIN -- Sim --> BCB_NOT["Notificar BCB\nBCB Conj. 2 + BCB IN 291\nPrazo: imediato"]
    FIN -- Não --> FIN_DOC["Avaliar outros reguladores"]

    IC -- Sim --> CTIR["Notificar CTIR Gov\nReGIC\nPrazo: imediato"]
    IC -- Não --> IC_DOC["Documentar internamente"]

    SAUDE -- Sim --> SNVS["Notificar SNVS/ANVISA\nVigilância de dispositivos\nmédicos — tecnovigilância"]
    SAUDE -- Não --> SAUDE_DOC["Documentar internamente"]

    ANPD --> PARALELO["Obrigações frequentemente\nse sobrepõem — notificar\ntodos os reguladores\naplicáveis em paralelo"]
    BCB_NOT --> PARALELO
    CTIR --> PARALELO
    SNVS --> PARALELO

    style INC fill:#d32f2f,color:#fff
    style ANPD fill:#1565c0,color:#fff
    style BCB_NOT fill:#1565c0,color:#fff
    style CTIR fill:#1565c0,color:#fff
    style SNVS fill:#1565c0,color:#fff
    style PARALELO fill:#ff6f00,color:#fff
    style DP_DOC fill:#9e9e9e,color:#fff
    style FIN_DOC fill:#9e9e9e,color:#fff
    style IC_DOC fill:#9e9e9e,color:#fff
    style SAUDE_DOC fill:#9e9e9e,color:#fff
```

**Resumo de prazos de notificação:**

| Regulador | Framework | Prazo | Destinatário |
|-----------|-----------|-------|--------------|
| ANPD | LGPD + Res. 15/2024 | 3 dias úteis | ANPD + titulares afetados |
| BCB | BCB Conj. 2 + IN 291 | Imediato | BCB (DESIN) |
| CTIR Gov | ReGIC | Imediato | CTIR Gov |
| ANVISA | Tecnovigilância | Conforme gravidade | SNVS |

---

## 11. Penalidades por Regulador

As penalidades no ecossistema regulatório brasileiro variam significativamente em severidade máxima e frequência de aplicação. A ANPD ainda está em fase de maturação de enforcement, enquanto BCB e CVM possuem histórico consolidado de aplicação de multas e sanções administrativas.

```mermaid
quadrantChart
    title Panorama de Risco Sancionatório Brasileiro
    x-axis "Baixa Frequência de Aplicação" --> "Alta Frequência de Aplicação"
    y-axis "Baixa Severidade Máxima" --> "Alta Severidade Máxima"
    quadrant-1 Alta severidade e alto enforcement
    quadrant-2 Alta severidade e baixo enforcement
    quadrant-3 Baixa severidade e baixo enforcement
    quadrant-4 Baixa severidade e alto enforcement
    BCB: [0.85, 0.85]
    CVM: [0.80, 0.80]
    SUSEP: [0.55, 0.60]
    ANPD: [0.40, 0.55]
    ANEEL: [0.60, 0.65]
    ANATEL: [0.65, 0.60]
```

**Detalhamento de penalidades por regulador:**

| Regulador | Penalidade máxima | Sanções adicionais |
|-----------|-------------------|--------------------|
| ANPD (LGPD) | Até R$ 50M por infração ou 2% do faturamento | Publicização, bloqueio/eliminação de dados, suspensão do tratamento |
| BCB | Multa sem teto definido | Suspensão de atividades, intervenção, liquidação extrajudicial |
| CVM | Até R$ 50M | Inabilitação, cassação de registro, suspensão de exercício |
| SUSEP | Multa conforme regulamentação | Suspensão de atividades, cassação de autorização |
| ANEEL | Multa conforme regulamentação | Revogação de autorização, caducidade de concessão |
| ANATEL | Multa conforme regulamentação | Caducidade da outorga, cassação de licença |

---

## 12. Linha do Tempo -- Evolução Regulatória Brasileira

A regulação de cibersegurança e privacidade no Brasil evoluiu rapidamente na última década. O Marco Civil da Internet (2014) estabeleceu os princípios fundacionais, a LGPD (2018) inaugurou a era de proteção de dados, e desde 2020 uma onda de normas setoriais tem densificado o ecossistema em finanças, governo, energia, telecomunicações e saúde.

```mermaid
timeline
    title Evolução Regulatória Brasileira
    2014 : Marco Civil da Internet — Lei 12.965
    2016 : Decreto 8.771 — regulamentação do Marco Civil
    2018 : LGPD promulgada — Lei 13.709
    2019 : Bacen 4893 — cibersegurança para IFs
    2020 : LGPD entra em vigor
         : BCB 85 — cibersegurança para IPs
         : PNSI — Política Nacional de Segurança da Informação
         : PNCiber — Política Nacional de Cibersegurança
    2021 : ANPD operacional
         : SUSEP 638 — cibersegurança para seguros
         : CVM 35 — cibersegurança para mercado de capitais
    2022 : LGPD sanções ativas
         : IN GSI/PR 1, 3 e 5 — governança SI na APF
         : Open Finance — ecossistema bancário aberto
         : Pix Security — segurança do Pix
    2023 : Marco Legal Cripto — Lei 14.478
         : BCB 304 — regulamentação de VASPs
         : CMN 4.557, 4.968, 4.606 — três linhas de defesa
    2024 : Resolução ANPD 15 — notificação de incidentes em 3 dias úteis
         : ANEEL 964 — cibersegurança setor elétrico
         : R-Ciber — cibersegurança telecomunicações
         : Pix MED 2.0 — antifraude aprimorado
```
