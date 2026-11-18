# Real-World Corpus Harvesting & Multi-Domain Audit Report

- **Total Ingested Sentences**: `1100`
- **Clean Human Benchmark**: `1083` (Verified authentic native sentences)
- **Canary Trapped**: `14` (Flaws successfully intercepted by linter)
- **New Anomaly Candidates**: `3` (Flagged for human linguistic review)

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
| `SCRAPED-2026_11_18_071402-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-005` | Local Verified Corpus (administrative_governance_memos.jsonl) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-006` | Local Verified Corpus (administrative_governance_memos.jsonl) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-007` | Local Verified Corpus (administrative_governance_memos.jsonl) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-008` | Local Verified Corpus (administrative_governance_memos.jsonl) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-017` | Local Verified Corpus (administrative_governance_memos.jsonl) | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-103` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-104` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-129` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-130` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-131` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071402-132` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তারা' (সাধারণ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ 'করতেন' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_18_071633-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-103` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-104` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Google |
| `SCRAPED-2026_11_18_071633-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Google, YouTube |
| `SCRAPED-2026_11_18_071633-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-129` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-130` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-131` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071633-132` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-103` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-104` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-129` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-130` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-131` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_071915-132` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-103` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-104` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-129` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-130` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-131` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072142-132` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তারা' (সাধারণ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ 'হলেন' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_18_072425-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_072425-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-103` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-104` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Login |
| `SCRAPED-2026_11_18_072425-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `CANARY_TRAPPED` | `1` | বাংলা একাডেমি পদ পৃথকীকরণ রীতি: 'এছাড়া' এর পরিবর্তে পৃথক পদ হিসেবে 'এ ছাড়া' লেখা বাঞ্ছনীয়। |
| `SCRAPED-2026_11_18_072425-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-129` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-130` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-131` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072425-132` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-033` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-034` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-035` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-036` | Prothom Alo (National & Economy) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-037` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-038` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-039` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-040` | BBC News Bangla (Judicial & Legal) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-041` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-042` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-043` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-044` | BBC News Bangla (Media & Journalism) | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-065` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-066` | Prothom Alo (Literature & Society) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-067` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-068` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-073` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-074` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-075` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-076` | Prothom Alo (Education & Pedagogy) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-077` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-078` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-079` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-080` | BBC News Bangla (Healthcare & Science) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-089` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-090` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-091` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-092` | BBC News Bangla (Judicial & Legal) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-093` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-094` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-095` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-096` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-097` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-098` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-099` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-100` | BBC News Bangla (Media & Journalism) | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-101` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-102` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-103` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-104` | Prothom Alo (FinTech & Mobile Banking) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-105` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-106` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-107` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-108` | Prothom Alo (Education & Pedagogy) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-121` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-122` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-123` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-124` | BBC News Bangla (Healthcare & Science) | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-129` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-130` | Prothom Alo (Literature & Society) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-131` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072710-132` | Bangla Wikipedia Bengali Literature & Fiction | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-001` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-002` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-003` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-004` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-005` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-006` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-007` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-008` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-009` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-010` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-011` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-012` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-013` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-014` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-015` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-016` | Prothom Alo (National & Economy) | Banking & Macroeconomics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-017` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-018` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-019` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-020` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Administrative Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-021` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-022` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-023` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-024` | Prothom Alo (National & Economy) | Tax & Customs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-025` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-026` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-027` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-028` | Local Verified Corpus (administrative_governance_memos.jsonl) [Rotated] | Official Administrative | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-029` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-030` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-031` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-032` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Conveyancing & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-033` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-034` | Local Verified Corpus (macroeconomics_banking.jsonl) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-035` | Local Verified Corpus (macroeconomics_banking.jsonl) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-036` | Local Verified Corpus (macroeconomics_banking.jsonl) | Macroeconomic & Finance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-037` | Local Verified Corpus (legal_constitutional_writs.jsonl) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-038` | Local Verified Corpus (legal_constitutional_writs.jsonl) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-039` | Local Verified Corpus (legal_constitutional_writs.jsonl) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-040` | Local Verified Corpus (legal_constitutional_writs.jsonl) | Judicial & High Court | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-041` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-042` | Local Verified Corpus (mass_media_digital_journalism.jsonl) [Rotated] | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-043` | Local Verified Corpus (mass_media_digital_journalism.jsonl) [Rotated] | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-044` | Local Verified Corpus (mass_media_digital_journalism.jsonl) [Rotated] | Sports Vernacular | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-045` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-046` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-047` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-048` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | Corporate & Tech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-049` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-050` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-051` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-052` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Disaster Early Warning | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-053` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-054` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-055` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-056` | Local Verified Corpus (citizen_digital_services_governance.jsonl) [Rotated] | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-057` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-058` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-059` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-060` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-061` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-062` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-063` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-064` | Local Verified Corpus (consumer_ecommerce_logistics.jsonl) [Rotated] | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-065` | Local Verified Corpus (creative_fiction_dialogue.jsonl) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-066` | Local Verified Corpus (creative_fiction_dialogue.jsonl) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-067` | Local Verified Corpus (creative_fiction_dialogue.jsonl) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-068` | Local Verified Corpus (creative_fiction_dialogue.jsonl) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-069` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-070` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-071` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-072` | Local Verified Corpus (customer_support_conversational_chat.jsonl) [Rotated] | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-073` | Local Verified Corpus (education_nctb_pedagogy.jsonl) | Education & NCTB Pedagogy | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('পড়িয়া') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `SCRAPED-2026_11_18_072954-074` | Local Verified Corpus (education_nctb_pedagogy.jsonl) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-075` | Local Verified Corpus (education_nctb_pedagogy.jsonl) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-076` | Local Verified Corpus (education_nctb_pedagogy.jsonl) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-077` | Local Verified Corpus (healthcare_clinical_epidemiology.jsonl) [Rotated] | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-078` | Local Verified Corpus (healthcare_clinical_epidemiology.jsonl) [Rotated] | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-079` | Local Verified Corpus (healthcare_clinical_epidemiology.jsonl) [Rotated] | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-080` | Local Verified Corpus (healthcare_clinical_epidemiology.jsonl) [Rotated] | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-081` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-082` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-083` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-084` | Local Verified Corpus (ict_software_cloud_engineering.jsonl) [Rotated] | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-085` | Local Verified Corpus (bangladesh_bank_pid_circulars.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-086` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-087` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-088` | Local Verified Corpus (land_registry_khatiyan_deeds.jsonl) [Rotated] | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-089` | Local Verified Corpus (legal_constitutional_writs.jsonl) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-090` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-091` | Local Verified Corpus (legal_constitutional_writs.jsonl) [Rotated] | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-092` | Local Verified Corpus (legal_constitutional_writs.jsonl) [Rotated] | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-093` | Local Verified Corpus (macroeconomics_banking.jsonl) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-094` | Local Verified Corpus (macroeconomics_banking.jsonl) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-095` | Local Verified Corpus (macroeconomics_banking.jsonl) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-096` | Local Verified Corpus (macroeconomics_banking.jsonl) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-097` | Local Verified Corpus (bdnews24_tbs_parallel.jsonl) [Rotated] | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-098` | Local Verified Corpus (mass_media_digital_journalism.jsonl) [Rotated] | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-099` | Local Verified Corpus (mass_media_digital_journalism.jsonl) [Rotated] | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-100` | Local Verified Corpus (mass_media_digital_journalism.jsonl) [Rotated] | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-101` | Local Verified Corpus (mfs_microfinance_grassroots_fintech.jsonl) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-102` | Local Verified Corpus (mfs_microfinance_grassroots_fintech.jsonl) [Rotated] | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-103` | Local Verified Corpus (mfs_microfinance_grassroots_fintech.jsonl) [Rotated] | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-104` | Local Verified Corpus (mfs_microfinance_grassroots_fintech.jsonl) [Rotated] | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-105` | Local Verified Corpus (education_nctb_pedagogy.jsonl) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-106` | Local Verified Corpus (education_nctb_pedagogy.jsonl) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-107` | Local Verified Corpus (education_nctb_pedagogy.jsonl) | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-108` | Local Verified Corpus (education_nctb_pedagogy.jsonl) [Rotated] | Education & Pedagogy | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('পড়িয়া') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `SCRAPED-2026_11_18_072954-109` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-110` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-111` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-112` | Local Verified Corpus (academic_research_theses.jsonl) [Rotated] | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-113` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-114` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-115` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-116` | Local Verified Corpus (classical_poetry_payar_prosody.jsonl) [Rotated] | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-117` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-118` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-119` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-120` | Local Verified Corpus (agronomy_meteorology_disaster.jsonl) [Rotated] | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-121` | Local Verified Corpus (healthcare_clinical_epidemiology.jsonl) [Rotated] | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-122` | Local Verified Corpus (healthcare_clinical_epidemiology.jsonl) [Rotated] | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-123` | Local Verified Corpus (healthcare_clinical_epidemiology.jsonl) [Rotated] | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-124` | Local Verified Corpus (healthcare_clinical_epidemiology.jsonl) [Rotated] | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-125` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-126` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-127` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-128` | Local Verified Corpus (translation_calque_naturalization.jsonl) [Rotated] | Translation & Calque Naturalization | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-129` | Local Verified Corpus (creative_fiction_dialogue.jsonl) | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-130` | Local Verified Corpus (creative_fiction_dialogue.jsonl) [Rotated] | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-131` | Local Verified Corpus (creative_fiction_dialogue.jsonl) [Rotated] | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_18_072954-132` | Local Verified Corpus (creative_fiction_dialogue.jsonl) [Rotated] | Creative Fiction & Spoken Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
