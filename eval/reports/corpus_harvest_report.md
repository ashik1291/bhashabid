# Real-World Corpus Harvesting & Multi-Domain Audit Report

- **Total Ingested Sentences**: `176`
- **Clean Human Benchmark**: `168` (Verified authentic native sentences)
- **Canary Trapped**: `8` (Flaws successfully intercepted by linter)
- **New Anomaly Candidates**: `0` (Flagged for human linguistic review)

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
| `CORP-FIC-004-RAW` | Urban Fiction Dialogue (Raw LLM) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'খারাপ কর্মী তার সরঞ্জামকে দোষ দেয়' প্রমিত বাংলায় কৃত্রিম শোনায়। |
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
