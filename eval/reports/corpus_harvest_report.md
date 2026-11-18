# Real-World Corpus Harvesting & Multi-Domain Audit Report

- **Total Ingested Sentences**: `3112`
- **Clean Human Benchmark**: `3078` (Verified authentic native sentences)
- **Canary Trapped**: `24` (Flaws successfully intercepted by linter)
- **New Anomaly Candidates**: `10` (Flagged for human linguistic review)

## Audit Breakdown by Source & Domain

| ID | Source | Domain | Category | Flaws Trapped | Sample / Flaw Message |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `CORP-ACD-001` | University Research Journal | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-002-RAW` | Peer-Reviewed Journal Abstract (Raw LLM) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'পেপারটি তর্ক করে' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-ACD-002-GOLD` | Peer-Reviewed Journal Abstract (Human Gold) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-003` | Bangla Academy Bhashatotto Journal | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-004-RAW` | Social Science Review (Dhaka University) (Raw LLM) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-004-GOLD` | Social Science Review (Dhaka University) (Human Gold) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-005` | Doctoral Dissertation Defense Guidelines | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-006` | UGC Academic Thesis Style Manual | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-007` | Bangla Academy Research Journal Standard | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-008` | Peer-reviewed Scientific Paper Abstract | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ACD-009` | University Dissertation Protocol | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-001` | Cabinet Division Bangladesh | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-002-RAW` | Deputy Commissioner Office Circular (Raw LLM) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-002-GOLD` | Deputy Commissioner Office Circular (Human Gold) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-003` | Ministry of Public Administration (MoPA) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-004` | Formal D.O. Letter Precedent | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-005` | Office of the Prime Minister / Chief Adviser | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-006` | Ministry of Public Administration Rules Desk | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-007` | Cabinet Division Coordination Wing | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-008` | Finance Division Delegation of Financial Powers | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-009` | Official Gazette Notification Standards | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-010` | Anti-Corruption Commission Protocol | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-001` | Department of Agricultural Extension (DAE) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-002-RAW` | Bangladesh Meteorological Department (BMD) (Raw LLM) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-002-GOLD` | Bangladesh Meteorological Department (BMD) (Human Gold) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-003` | Flood Forecasting and Warning Centre (FFWC) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-004-RAW` | Bangladesh Rice Research Institute (BRRI) (Raw LLM) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-004-GOLD` | Bangladesh Rice Research Institute (BRRI) (Human Gold) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-005` | Ministry of Disaster Management and Relief | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-006` | Bangladesh Rice Research Institute (BRRI) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-007` | Department of Agricultural Extension (DAE) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-008` | Bangladesh Meteorological Department (BMD) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-009` | Disaster Management Bureau (SOD Framework) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-010` | BRRI Saline Tolerant Cultivars Manual | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-011` | BARC Soil Science Protocol | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-001` | Bangladesh Bank (BRPD Circular) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-002` | Press Information Department (PID Handout) | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-003` | National Board of Revenue (NBR SRO) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-004` | Civil Petition Precedent | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-GOV-005` | Ministry of Land Sub-Registry | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-001-RAW` | The Business Standard (TBS) (Raw LLM) | Macroeconomic & Finance | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'দ্বারা চালিত' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-NEWS-001-GOLD` | The Business Standard (TBS) (Human Gold) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-002-RAW` | BDNews24 (Raw LLM) | Judicial & High Court | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'জিজ্ঞেস করে একটি রুল' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-NEWS-002-GOLD` | BDNews24 (Human Gold) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-003-RAW` | Prothom Alo (Sports Desk) (Raw LLM) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-003-GOLD` | Prothom Alo (Sports Desk) (Human Gold) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-004-RAW` | The Daily Star Bangla (Raw LLM) | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-004-GOLD` | The Daily Star Bangla (Human Gold) | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-NEWS-005-RAW` | Dhaka Tribune / Bangla Tribune (Raw LLM) | Disaster Early Warning | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'বড় বিপদের সংকেত' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-NEWS-005-GOLD` | Dhaka Tribune / Bangla Tribune (Human Gold) | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-CIV-001` | Bangladesh National Citizen Portal | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-CIV-002` | Land Revenue Management System | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-CIV-003` | Local Government Division Portal | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-CIV-004` | Department of Immigration & Passports | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-001` | Kashiram Das (Mahabharata) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-002` | Krittibas Ojha (Ramayana) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-003` | Michael Madhusudan Dutt (Meghnadbadh Kavya) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-004` | Rabindranath Tagore (Sanchayita) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-005` | Kazi Nazrul Islam (Bidrohi) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ECM-001` | e-Commerce Operational Guidelines | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ECM-002` | Retail Consumer Portal | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ECM-003` | Consumer Rights Protection Protocol | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ECM-004` | Courier Logistics Dispatch | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ECM-005` | E-Commerce Association of Bangladesh (e-CAB) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ECM-006` | National Logistics Policy Framework | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ECM-007` | Central Sorting Hub Standard Operating Procedure | Consumer E-Commerce & Retail Logistics | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('করিয়া') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `CORP-ECM-008` | Consumer Rights Protection Directorate | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-001` | Modern Literary Fiction Anthology | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-002-RAW` | Literary Translation Benchmark (Raw LLM) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `2` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'ঝোপের চারপাশে পেটানো' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-FIC-002-GOLD` | Literary Translation Benchmark (Human Gold) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-003` | Riverine Bengal Novel Excerpt | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-004-RAW` | Urban Fiction Dialogue (Raw LLM) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `2` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'দিনের শেষে' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-FIC-004-GOLD` | Urban Fiction Dialogue (Human Gold) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-005` | Short Story Psychological Monologue | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-SUP-001` | Omnichannel Support Helpdesk | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-SUP-002` | Telecom Customer Care Protocol | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-SUP-003` | Digital Service Helpline | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-SUP-004` | Interactive Support Bot | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-CS-005` | Omnichannel CRM Support Guidelines | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-CS-006` | Telecommunications Customer Care Manual | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-CS-007` | FinTech Helpdesk Standard Workflow | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-CS-008` | Retail Helpdesk Live Chat Service | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-001` | NCTB Creative Questioning Framework | Education & NCTB Pedagogy | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('পড়িয়া') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `CORP-PED-002-RAW` | NCTB Secondary Assessment Manual (Raw LLM) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-002-GOLD` | NCTB Secondary Assessment Manual (Human Gold) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-003` | Higher Secondary Board Examination Model | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-004-RAW` | NCTB Bengali First Paper Board Question (Raw LLM) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-004-GOLD` | NCTB Bengali First Paper Board Question (Human Gold) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-005` | National Curriculum Framework 2026 | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-006` | Bangla Academy Grammar Standard (NCTB Grade IX-X) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-007` | Board Examination Question Protocol | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-008` | National Curriculum Teachers Guide | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-009` | Directorate of Secondary and Higher Education (DSHE) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-010` | Bangla Academy Orthographic Manual for Schools | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-001` | Directorate General of Health Services (DGHS) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-002-RAW` | Clinical Practice Guidelines (Medicine) (Raw LLM) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-002-GOLD` | Clinical Practice Guidelines (Medicine) (Human Gold) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-003` | Institute of Epidemiology, Disease Control and Research (IEDCR) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-004-RAW` | Bangladesh Paediatric Association (Raw LLM) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-004-GOLD` | Bangladesh Paediatric Association (Human Gold) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-005` | National Mental Health Institute | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-006` | Directorate General of Health Services (DGHS) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-007` | ICDDR,B Diarrheal Diseases Research Protocol | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-008` | EPI Immunization Guidelines Bangladesh | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-009` | BMRC National Clinical Ethical Standards | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-010` | National Institute of Cardiovascular Diseases (NICVD) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-001` | Bangladesh Computer Council (BCC) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-002-RAW` | Software Engineering Team Manual (Raw LLM) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-002-GOLD` | Software Engineering Team Manual (Human Gold) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-003` | Digital Bangladesh / Smart Bangladesh Blueprint | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-004-RAW` | API Architecture Specification (Raw LLM) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-004-GOLD` | API Architecture Specification (Human Gold) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ICT-005` | Cyber Security Agency (BGD e-GOV CIRT) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-001` | Directorate of Land Records and Surveys (DLRS) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-002-RAW` | District Sub-Registry Office Precedent (Raw LLM) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-002-GOLD` | District Sub-Registry Office Precedent (Human Gold) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-003` | Ministry of Land Portal | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-004-RAW` | Civil Court Land Dispute Precedent (Raw LLM) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-004-GOLD` | Civil Court Land Dispute Precedent (Human Gold) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-005` | Assistant Commissioner (Land) AC Land Court | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-006` | Directorate of Registration & SR Office Manual | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-007` | State Acquisition and Tenancy Act 1950 | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-008` | Assistant Commissioner (Land) Mutation Manual | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-009` | Land Survey & Record Manual (RS/BS) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-010` | High Court Division Property Precedent | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-011` | Ministry of Land Circular on Khas Land | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LND-012` | Transfer of Property Act 1882 | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-001` | Supreme Court of Bangladesh (High Court Division) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-002-RAW` | High Court Division Judgment Precedent (Raw LLM) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-002-GOLD` | High Court Division Judgment Precedent (Human Gold) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-003` | Bangladesh Code (Statutory Law) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-004-RAW` | High Court Division Writ Bench (Raw LLM) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-004-GOLD` | High Court Division Writ Bench (Human Gold) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-005` | Supreme Court Bar Association Records | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-006` | Supreme Court of Bangladesh (High Court Division) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-007` | Bangladesh Legal Decisions (BLD) Appellate Division | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-008` | Supreme Court Rules 1973 (Part IV) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-009` | Code of Civil Procedure (CPC) Section 115 | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-010` | Dhaka Law Reports (DLR) Constitutional Bench | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-011` | High Court Bench Order (Certiorari) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-012` | Constitution of Bangladesh (Part III Fundamental Rights) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-013` | Supreme Court of Bangladesh (Appellate Division Precedents) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-014` | High Court Division (Mandamus Bench) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-015` | Administrative Tribunals Act 1980 | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LGL-016` | Supreme Court Bar Law Journal | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-001` | Bangladesh Bank Monetary Policy Department | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-002-RAW` | Financial Express Bangladesh (Raw LLM) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-002-GOLD` | Financial Express Bangladesh (Human Gold) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-003` | BIBM (Bangladesh Institute of Bank Management) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-004-RAW` | Dhaka Chamber of Commerce & Industry (DCCI) (Raw LLM) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-004-GOLD` | Dhaka Chamber of Commerce & Industry (DCCI) (Human Gold) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-005` | National Accounts Statistics (BBS) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-006` | Bangladesh Bank Banking Regulation and Policy Department (BRPD) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-007` | Bangladesh Financial Intelligence Unit (BFIU) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-008` | Ministry of Finance Budget Economic Framework | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-009` | Dhaka Stock Exchange (DSE) Market Review | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-010` | Foreign Exchange Policy Department (FEPD) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-001` | National Daily Newspaper Lead | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-002` | Economic News Dispatch | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-003` | Official Press Statement | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-004` | Investigative Journalism Report | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MFS-001` | Bangladesh Bank MFS Consumer Advisory | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MFS-002` | Expatriate Remittance Guidelines | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MFS-003` | Microcredit Regulatory Authority Bulletin | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MFS-004` | Financial Crime Prevention Desk | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-001` | NCTB Curriculum Manual | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-002` | Bangla Wikipedia (উইকিপিডিয়া) | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-003` | Classical Poetic Corpus | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-004` | Department of Agricultural Extension (DAE) | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-005` | Healthcare Clinical Protocol | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-TRN-001` | Bangla Academy Translation Studies | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-TRN-002` | Comparative Literature Canon | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-TRN-003` | Grammar Register Standardization | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-TRN-004` | Proverb Canon & Pragmatics | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-TRN-005` | Applied Lexicography Guide | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-TRN-006` | Bengali Semantic Studies | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_091744-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_091744-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-103` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-104` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091744-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-103` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-104` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_091907-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-103` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-104` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092031-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-001` | Bangla Wikipedia Linguistics & Academic Research | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-002` | Bangla Wikipedia Linguistics & Academic Research | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-003` | Bangla Wikipedia Linguistics & Academic Research | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-004` | Bangla Wikipedia Linguistics & Academic Research | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-005` | The Daily Star Bangla (Governance & Administration) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-006` | The Daily Star Bangla (Governance & Administration) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-007` | Bangla Wikipedia Public Administration | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-008` | Bangla Wikipedia Public Administration | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-009` | Deutsche Welle (DW Bangla - Climate & Disaster) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-010` | Deutsche Welle (DW Bangla - Climate & Disaster) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-011` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-012` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Gossypium, arboreum |
| `SCRAPED-2026_11_18_092118-013` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-014` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-015` | Bangla Wikipedia Macroeconomics & Central Banking | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-016` | Bangla Wikipedia Macroeconomics & Central Banking | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-017` | The Daily Star Bangla (Governance & Administration) | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-018` | Bangla Wikipedia Public Administration | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-019` | Bangla Wikipedia Public Administration | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-020` | Bangla Wikipedia Public Administration | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-021` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-022` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-023` | Bangla Wikipedia Macroeconomics & Central Banking | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-024` | Bangla Wikipedia Macroeconomics & Central Banking | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-025` | Bangla Wikipedia Public Administration | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-026` | Bangla Wikipedia Public Administration | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-027` | Bangla Wikipedia Public Administration | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-028` | Bangla Wikipedia Public Administration | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-029` | Bangla Wikipedia Land Law & Property Registry | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-030` | Bangla Wikipedia Land Law & Property Registry | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-031` | Bangla Wikipedia Land Law & Property Registry | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-032` | Bangla Wikipedia Land Law & Property Registry | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-033` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-034` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-035` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-036` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-039` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-040` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-041` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-042` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-043` | Bangla Wikipedia Journalism & Media Studies | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-044` | Bangla Wikipedia Journalism & Media Studies | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-045` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-046` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-047` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-048` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-049` | Bangla Wikipedia Agriculture & Agronomy | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-050` | Bangla Wikipedia Agriculture & Agronomy | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-051` | Bangla Wikipedia Agriculture & Agronomy | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-052` | Bangla Wikipedia Agriculture & Agronomy | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-053` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-054` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-055` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-056` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-057` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-058` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-059` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-060` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-061` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-062` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-069` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-070` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-075` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-076` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-079` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-080` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-081` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-082` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-083` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-084` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Help, OAuth |
| `SCRAPED-2026_11_18_092118-085` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-086` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-087` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-088` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_092118-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-091` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-092` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-093` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-094` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-095` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-096` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-097` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-098` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-099` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-100` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-107` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-108` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-109` | Bangla Wikipedia Linguistics & Academic Research | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-110` | Bangla Wikipedia Linguistics & Academic Research | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-111` | Bangla Wikipedia Linguistics & Academic Research | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-112` | Bangla Wikipedia Linguistics & Academic Research | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-113` | Bangla Wikipedia Poetry & Classical Verse | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-114` | Bangla Wikipedia Poetry & Classical Verse | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-115` | Bangla Wikipedia Poetry & Classical Verse | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-116` | Bangla Wikipedia Poetry & Classical Verse | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-117` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-118` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-119` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-120` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-123` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-124` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-125` | Bangla Wikipedia Translation Studies & Lexicography | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-126` | Bangla Wikipedia Translation Studies & Lexicography | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-127` | Bangla Wikipedia Translation Studies & Lexicography | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092118-128` | Bangla Wikipedia Translation Studies & Lexicography | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-001` | Bangla Wikipedia Linguistics & Academic Research | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-002` | Bangla Wikipedia Linguistics & Academic Research | Academic Research & Methodology | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: alphabet |
| `SCRAPED-2026_11_18_092219-003` | Bangla Wikipedia Linguistics & Academic Research | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-004` | Bangla Wikipedia Linguistics & Academic Research | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-005` | Bangla Wikipedia Public Administration | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-006` | Bangla Wikipedia Public Administration | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-007` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-008` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-009` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-010` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-011` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-012` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-013` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-014` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-015` | Bangla Wikipedia Macroeconomics & Central Banking | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-016` | Bangla Wikipedia Macroeconomics & Central Banking | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-017` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-018` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-019` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-020` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-021` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-022` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-023` | Bangla Wikipedia Macroeconomics & Central Banking | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-024` | Bangla Wikipedia Macroeconomics & Central Banking | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-025` | Bangla Wikipedia Bangladesh Government Agencies | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-026` | Bangla Wikipedia Bangladesh Government Agencies | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-027` | Bangla Wikipedia Bangladesh Government Agencies | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-028` | Bangla Wikipedia Bangladesh Government Agencies | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-029` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-030` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-031` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `CANARY_TRAPPED` | `1` | বাহুল্য প্রত্যয়জনিত অপপ্রয়োগ: 'প্রায়শ' শব্দের সাথে অতিরিক্ত 'ই' প্রত্যয় বর্জনীয়। |
| `SCRAPED-2026_11_18_092219-032` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-033` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-034` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-035` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-036` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-039` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-040` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-041` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-042` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-043` | Bangla Wikipedia Journalism & Media Studies | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-044` | Bangla Wikipedia Journalism & Media Studies | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-045` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-046` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-047` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-048` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: abdul, alim |
| `SCRAPED-2026_11_18_092219-049` | Bangla Wikipedia Agriculture & Agronomy | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-050` | Bangla Wikipedia Agriculture & Agronomy | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-051` | Bangla Wikipedia Agriculture & Agronomy | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-052` | Bangla Wikipedia Agriculture & Agronomy | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-053` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-054` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-055` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-056` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-057` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-058` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-059` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-060` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-061` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-062` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-069` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-070` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-075` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-076` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-079` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-080` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-081` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-082` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-083` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-084` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-085` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-086` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-087` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-088` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-091` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-092` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-093` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-094` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-095` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-096` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-097` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-098` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-099` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-100` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-107` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-108` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-109` | Bangla Wikipedia Linguistics & Academic Research | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-110` | Bangla Wikipedia Linguistics & Academic Research | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-111` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-112` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-113` | Bangla Wikipedia Poetry & Classical Verse | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-114` | Bangla Wikipedia Poetry & Classical Verse | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-115` | Bangla Wikipedia Poetry & Classical Verse | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-116` | Bangla Wikipedia Poetry & Classical Verse | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-117` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-118` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-119` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-120` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-123` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-124` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-125` | Bangla Wikipedia Translation Studies & Lexicography | Translation & Calque Naturalization | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_092219-126` | Bangla Wikipedia Translation Studies & Lexicography | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-127` | Bangla Wikipedia Translation Studies & Lexicography | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092219-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-001` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-002` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-003` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-004` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-005` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-006` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-007` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-008` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-009` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-010` | Bangla Wikipedia Agriculture & Agronomy | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-011` | Bangla Wikipedia Disaster Risk Management | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-012` | Bangla Wikipedia Disaster Risk Management | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-013` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-014` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তারা' (সাধারণ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ 'থাকেন' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_18_092321-015` | Bangla Wikipedia Macroeconomics & Central Banking | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-016` | Bangla Wikipedia Macroeconomics & Central Banking | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-017` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-018` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-019` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-020` | Bangla Wikipedia Bangladesh Government Agencies | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-021` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-022` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-023` | Bangla Wikipedia Macroeconomics & Central Banking | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-024` | Bangla Wikipedia Macroeconomics & Central Banking | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-025` | Bangla Wikipedia Bangladesh Government Agencies | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-026` | Bangla Wikipedia Bangladesh Government Agencies | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-027` | Bangla Wikipedia Bangladesh Government Agencies | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-028` | Local Verified Corpus (administrative_governance_memos.jsonl) | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-029` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-030` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-031` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-032` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-033` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-034` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-035` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-036` | Bangla Wikipedia Macroeconomics & Central Banking | Macroeconomic & Finance | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_092321-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-039` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-040` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-041` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-042` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-043` | Bangla Wikipedia Journalism & Media Studies | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-044` | Bangla Wikipedia Journalism & Media Studies | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-045` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-046` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-047` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-048` | Bangla Wikipedia Information Technology & Computing | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-049` | Bangla Wikipedia Disaster Risk Management | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-050` | Bangla Wikipedia Disaster Risk Management | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-051` | Bangla Wikipedia Disaster Risk Management | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-052` | Bangla Wikipedia Disaster Risk Management | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-053` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-054` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-055` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-056` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-057` | Bangla Wikipedia Classical Literature & Metrics | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-058` | Bangla Wikipedia Classical Literature & Metrics | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-059` | Bangla Wikipedia Classical Literature & Metrics | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-060` | Bangla Wikipedia Classical Literature & Metrics | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-061` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-062` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-069` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-070` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-075` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-076` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-079` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-080` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-081` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-082` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-083` | Bangla Wikipedia Information Technology & Computing | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-084` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-085` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-086` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-087` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-088` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-091` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-092` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-093` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-094` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-095` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-096` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-097` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-098` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-099` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-100` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-107` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-108` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-109` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-110` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-111` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-112` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-113` | Bangla Wikipedia Classical Literature & Metrics | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-114` | Bangla Wikipedia Classical Literature & Metrics | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-115` | Bangla Wikipedia Classical Literature & Metrics | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-116` | Bangla Wikipedia Classical Literature & Metrics | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-123` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-124` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092321-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-001` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-002` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-003` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-004` | Bangla Wikipedia Bengali Grammar & Philology | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-005` | Local Verified Corpus (administrative_governance_memos.jsonl) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-013` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-014` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-015` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-016` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-021` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-022` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-023` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-024` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-029` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-030` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-031` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-032` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-033` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-034` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-035` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-036` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-039` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-040` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-041` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-042` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-043` | Bangla Wikipedia Journalism & Media Studies | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-044` | Bangla Wikipedia Journalism & Media Studies | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-045` | Bangla Wikipedia Computer Science & Software | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-046` | Bangla Wikipedia Computer Science & Software | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-047` | Bangla Wikipedia Computer Science & Software | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-048` | Bangla Wikipedia Computer Science & Software | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-053` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-054` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-055` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-056` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-057` | Bangla Wikipedia Classical Literature & Metrics | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-058` | Bangla Wikipedia Classical Literature & Metrics | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-059` | Bangla Wikipedia Bengali Metres & Prosody | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-061` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-062` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-069` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-070` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-075` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-076` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-079` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-080` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-081` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-082` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-083` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-084` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-085` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-086` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-087` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-088` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-091` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-092` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-093` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-094` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-095` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-096` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-097` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-098` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-099` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-100` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-107` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-108` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-109` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-110` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-111` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-112` | Bangla Wikipedia Bengali Grammar & Philology | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-123` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-124` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092432-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-001` | Bangla Wikipedia Research Methodology & Linguistics | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-002` | Bangla Wikipedia Research Methodology & Linguistics | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-003` | Bangla Wikipedia Research Methodology & Linguistics | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-004` | Bangla Wikipedia Research Methodology & Linguistics | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-013` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-014` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-015` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-016` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-021` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-022` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-023` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-024` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-029` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-030` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-031` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-032` | Bangla Wikipedia Legal Framework & Conveyancing | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-033` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-034` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-035` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-036` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-039` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-040` | Bangla Wikipedia Bangladesh Case Law & Jurisprudence | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-041` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-042` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-043` | Bangla Wikipedia Journalism & Media Studies | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-044` | Bangla Wikipedia Mass Media & Press | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-045` | Bangla Wikipedia Computer Science & Software | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-046` | Bangla Wikipedia Computer Science & Software | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-047` | Bangla Wikipedia Computer Science & Software | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-048` | Bangla Wikipedia Computer Science & Software | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-053` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-054` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-055` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-056` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-061` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-062` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-069` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-070` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-075` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-076` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-079` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-080` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-081` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-082` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-083` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-084` | Bangla Wikipedia Computer Science & Software | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-085` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-086` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-087` | Bangla Wikipedia Legal Framework & Conveyancing | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `CANARY_TRAPPED` | `1` | বাহুল্য প্রত্যয়জনিত অপপ্রয়োগ: 'প্রায়শ' শব্দের সাথে অতিরিক্ত 'ই' প্রত্যয় বর্জনীয়। |
| `SCRAPED-2026_11_18_092607-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-091` | Bangla Wikipedia Bangladesh Constitution & Governance | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-092` | Bangla Wikipedia Bangladesh Constitution & Governance | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-093` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-094` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-095` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-096` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-097` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-098` | The Business Standard (TBS Bangla Media Dispatch) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-099` | Bangla Wikipedia Mass Media & Press | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-100` | Bangla Wikipedia Mass Media & Press | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: PWSBH |
| `SCRAPED-2026_11_18_092607-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-107` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-108` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-109` | Bangla Wikipedia Research Methodology & Linguistics | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-110` | Bangla Wikipedia Research Methodology & Linguistics | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-111` | Local Verified Corpus (academic_research_theses.jsonl) | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-112` | Local Verified Corpus (academic_research_theses.jsonl) | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-123` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-124` | Bangla Wikipedia Clinical Medicine & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092607-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-001` | Local Verified Corpus (academic_research_theses.jsonl) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-013` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-014` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-015` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-016` | The Business Standard (TBS Bangla Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-021` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-022` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-023` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-024` | The Business Standard (TBS Bangla Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-029` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-031` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-033` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-034` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-035` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-036` | The Business Standard (TBS Bangla Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-039` | Bangla Wikipedia Bangladesh Constitution & Governance | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-040` | Bangla Wikipedia Bangladesh Constitution & Governance | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-041` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-042` | The Business Standard (TBS Bangla Media Dispatch) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-043` | Bangla Wikipedia Mass Media & Press | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-044` | Bangla Wikipedia Mass Media & Press | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-045` | Bangla Wikipedia Computer Science & Software | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-047` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-053` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-054` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-055` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-056` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-061` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-062` | The Business Standard (TBS Bangla Commerce) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-069` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-070` | The Business Standard (TBS Bangla Support & Telecom) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-075` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-076` | Bangla Wikipedia Education & Pedagogy | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-091` | Bangla Wikipedia Bangladesh Constitution & Governance | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-092` | Bangla Wikipedia Bangladesh Constitution & Governance | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-093` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-094` | The Business Standard (TBS Bangla Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-099` | Bangla Wikipedia Mass Media & Press | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-100` | Bangla Wikipedia Mass Media & Press | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-107` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-108` | Bangla Wikipedia Education & Pedagogy | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-123` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092739-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-039` | Bangla Wikipedia Bangladesh Constitution & Governance | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-040` | Bangla Wikipedia Bangladesh Constitution & Governance | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-043` | Bangla Wikipedia Mass Media & Press | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-044` | Bangla Wikipedia Mass Media & Press | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-053` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-054` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-055` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: com |
| `SCRAPED-2026_11_18_092900-056` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-061` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-062` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-069` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-070` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-076` | Bangla Wikipedia Education in Bangladesh | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-091` | Bangla Wikipedia Bangladesh Constitution & Governance | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-092` | Bangla Wikipedia Bangladesh Constitution & Governance | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-099` | Bangla Wikipedia Mass Media & Press | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-100` | Bangla Wikipedia Mass Media & Press | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_092900-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-123` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_092900-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-039` | Bangla Wikipedia Bangladesh Constitution & Governance | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-040` | Bangla Wikipedia Bangladesh Constitution & Governance | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `CANARY_TRAPPED` | `1` | পুরুষ ও ক্রিয়াপদের সঙ্গতিহীনতা: 'আমি' (উত্তম পুরুষ) এর সাথে বেমানান ক্রিয়াপদ 'হবে' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_18_093019-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-043` | Bangla Wikipedia Mass Media & Press | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-044` | Bangla Wikipedia Mass Media & Press | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-053` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: information |
| `SCRAPED-2026_11_18_093019-054` | Bangla Wikipedia Digital Systems & Public Portals | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-061` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-062` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-069` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-070` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-092` | Bangla Wikipedia Bangladesh Constitution & Governance | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-100` | Bangla Wikipedia Mass Media & Press | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-123` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093019-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-061` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-062` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Packt |
| `SCRAPED-2026_11_18_093141-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-069` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-070` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_093141-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-123` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093141-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-061` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: nopCommerce |
| `SCRAPED-2026_11_18_093303-062` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-069` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-070` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-071` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-072` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-123` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093303-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-061` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-062` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-123` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093424-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `CANARY_TRAPPED` | `1` | বাহুল্য প্রত্যয়জনিত অপপ্রয়োগ: 'প্রায়শ' শব্দের সাথে অতিরিক্ত 'ই' প্রত্যয় বর্জনীয়। |
| `SCRAPED-2026_11_18_093544-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-061` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-062` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-063` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-064` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-123` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093544-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Google |
| `SCRAPED-2026_11_18_093710-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-061` | Bangla Wikipedia Postal & Courier Logistics | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-062` | Bangla Wikipedia Postal & Courier Logistics | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-063` | Bangla Wikipedia Postal & Courier Logistics | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-064` | Bangla Wikipedia Postal & Courier Logistics | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_093710-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-123` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093710-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-061` | Bangla Wikipedia Postal & Courier Logistics | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-062` | Bangla Wikipedia Postal & Courier Logistics | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-063` | Bangla Wikipedia Postal & Courier Logistics | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-064` | Bangla Wikipedia Retail & Consumer Markets | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-123` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_093838-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-061` | Bangla Wikipedia Retail & Consumer Markets | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-062` | Bangla Wikipedia Retail & Consumer Markets | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-079` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-080` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-124` | Bangla Wikipedia Public Health & Epidemiology | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094005-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094132-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তারা' (সাধারণ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ 'বলেন' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_18_094257-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094257-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094425-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তারা' (সাধারণ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ 'হলেন' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_18_094551-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তারা' (সাধারণ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ 'করেছিলেন' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_18_094551-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-103` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-104` | Bangla Wikipedia Banking & Grassroots Finance | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094551-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-077` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-078` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-079` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-080` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-081` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-082` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-083` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-084` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-085` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-086` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-087` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-088` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-089` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-090` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-091` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-092` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-093` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-094` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-095` | Bangla Wikipedia Currency & Financial Inclusion | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-096` | Bangla Wikipedia Currency & Financial Inclusion | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-097` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-098` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-099` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-100` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-101` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-102` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-103` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-104` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-105` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-106` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-107` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-108` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-109` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-110` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-111` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-112` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-113` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-114` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-115` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-116` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-117` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-118` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-119` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_094713-120` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
