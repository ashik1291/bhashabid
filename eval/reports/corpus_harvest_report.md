# Real-World Corpus Harvesting & Multi-Domain Audit Report

- **Total Ingested Sentences**: `1392`
- **Clean Human Benchmark**: `1283` (Verified authentic native sentences)
- **Canary Trapped**: `68` (Flaws successfully intercepted by linter)
- **New Anomaly Candidates**: `41` (Flagged for human linguistic review)

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
| `CORP-ADM-001` | Cabinet Division Bangladesh | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-002-RAW` | Deputy Commissioner Office Circular (Raw LLM) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-002-GOLD` | Deputy Commissioner Office Circular (Human Gold) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-003` | Ministry of Public Administration (MoPA) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-004` | Formal D.O. Letter Precedent | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-ADM-005` | Office of the Prime Minister / Chief Adviser | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-001` | Department of Agricultural Extension (DAE) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-002-RAW` | Bangladesh Meteorological Department (BMD) (Raw LLM) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-002-GOLD` | Bangladesh Meteorological Department (BMD) (Human Gold) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-003` | Flood Forecasting and Warning Centre (FFWC) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-004-RAW` | Bangladesh Rice Research Institute (BRRI) (Raw LLM) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-004-GOLD` | Bangladesh Rice Research Institute (BRRI) (Human Gold) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-AGR-005` | Ministry of Disaster Management and Relief | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
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
| `CORP-PED-001` | NCTB Creative Questioning Framework | Education & NCTB Pedagogy | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('পড়িয়া') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `CORP-PED-002-RAW` | NCTB Secondary Assessment Manual (Raw LLM) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-002-GOLD` | NCTB Secondary Assessment Manual (Human Gold) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-003` | Higher Secondary Board Examination Model | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-004-RAW` | NCTB Bengali First Paper Board Question (Raw LLM) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-004-GOLD` | NCTB Bengali First Paper Board Question (Human Gold) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-PED-005` | National Curriculum Framework 2026 | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-001` | Directorate General of Health Services (DGHS) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-002-RAW` | Clinical Practice Guidelines (Medicine) (Raw LLM) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-002-GOLD` | Clinical Practice Guidelines (Medicine) (Human Gold) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-003` | Institute of Epidemiology, Disease Control and Research (IEDCR) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-004-RAW` | Bangladesh Paediatric Association (Raw LLM) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-004-GOLD` | Bangladesh Paediatric Association (Human Gold) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MED-005` | National Mental Health Institute | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
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
| `CORP-LEG-001` | Supreme Court of Bangladesh (High Court Division) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-002-RAW` | High Court Division Judgment Precedent (Raw LLM) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-002-GOLD` | High Court Division Judgment Precedent (Human Gold) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-003` | Bangladesh Code (Statutory Law) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-004-RAW` | High Court Division Writ Bench (Raw LLM) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-004-GOLD` | High Court Division Writ Bench (Human Gold) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-LEG-005` | Supreme Court Bar Association Records | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-001` | Bangladesh Bank Monetary Policy Department | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-002-RAW` | Financial Express Bangladesh (Raw LLM) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-002-GOLD` | Financial Express Bangladesh (Human Gold) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-003` | BIBM (Bangladesh Institute of Bank Management) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-004-RAW` | Dhaka Chamber of Commerce & Industry (DCCI) (Raw LLM) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-004-GOLD` | Dhaka Chamber of Commerce & Industry (DCCI) (Human Gold) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-MAC-005` | National Accounts Statistics (BBS) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
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
| `MISTAKE-LEARN-20261115_143634_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143634_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143634_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143634_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143635_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143635_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143635_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143635_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143636_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143636_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143636_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143636_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-013` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-014` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-015` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-016` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143639_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143639_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143639_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143639_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143645_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143645_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143645_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143645_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143650_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143650_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143650_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143650_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143651_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143651_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143651_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143651_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143652_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143652_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143652_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143652_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143653_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143653_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143653_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143653_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143654_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143654_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143654_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143654_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143659-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143659_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143659_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143659_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143659_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143707_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143707_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143707_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143707_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143707_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143707_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143707_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143707_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143709_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143709_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143709_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143709_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-013` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-014` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-015` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-016` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143711_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143711_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143711_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143711_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143713_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143713_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143713_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143713_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143715_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143715_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143715_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143715_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143716_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143716_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143716_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143716_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143718_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143718_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143718_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143718_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143719_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143719_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143719_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143719_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143720_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143720_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143720_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143720_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143722-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143722_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143722_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143722_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143722_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143731_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143731_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143731_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143731_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143731_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143731_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143731_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143731_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143732_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143732_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143732_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143732_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-013` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-014` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-015` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-016` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143734_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143734_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143734_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143734_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143736_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143736_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143736_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143736_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143739_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143739_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143739_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143739_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143740_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143740_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143740_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143740_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143742_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143742_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143742_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143742_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143743_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143743_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143743_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143743_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143745_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143745_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143745_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143745_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143747-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143747_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143747_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143747_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143747_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143755_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143755_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143755_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143755_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143755_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143755_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143755_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143755_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143756_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143756_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143756_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143756_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-013` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-014` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-015` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-016` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143758_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143758_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143758_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143758_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143800_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143800_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143800_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143800_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143803_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143803_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143803_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143803_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143804_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143804_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143804_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143804_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143807_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143807_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143807_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143807_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143807_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143807_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143807_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143807_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143809_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143809_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143809_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143809_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143812-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143812_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143812_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143812_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143812_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143820_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143820_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143820_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143820_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143820_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143820_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143820_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143820_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143821_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143821_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143821_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143821_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-013` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-014` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-015` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-016` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143823_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143823_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143823_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143823_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143825_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143825_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143825_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143825_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143828_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143828_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143828_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143828_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143830_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143830_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143830_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143830_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143832_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143832_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143832_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143832_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143833_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143833_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143833_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143833_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143834_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143834_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143834_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143834_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143836-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143836_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143836_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143836_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143836_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143844_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143844_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143844_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143844_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143845_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143845_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143845_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143845_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143846_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143846_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143846_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143846_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-013` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-014` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-015` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-016` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143848_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143848_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143848_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143848_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143850_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143850_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143850_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143850_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143853_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143853_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143853_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143853_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143854_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143854_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143854_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143854_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143856_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143856_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143856_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143856_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143857_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143857_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143857_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143857_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143858_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143858_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143858_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143858_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143901-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143901_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143901_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143901_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143901_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143909_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143909_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143909_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143909_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143909_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143909_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143909_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143909_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143910_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143910_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143910_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143910_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-013` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-014` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-015` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-016` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143912_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143912_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143912_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143912_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143914_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143914_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143914_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143914_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143916_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143916_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143916_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143916_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143918_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143918_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143918_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143918_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143920_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143920_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143920_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143920_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143921_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143921_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143921_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143921_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143922_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143922_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143922_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143922_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143925-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143925_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143925_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143925_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143925_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143934_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143934_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143934_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143934_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143934_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143934_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143934_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143934_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143936_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143936_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143936_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143936_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-013` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-014` | Bangla Wikipedia Government Portals & Public Services | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143939_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143939_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143939_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143939_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-019` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-020` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143942_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143942_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143942_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143942_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-027` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-028` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143946_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143946_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143946_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143946_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143948_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143948_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_143948_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143948_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143951_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143951_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143951_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143951_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143952_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143952_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143952_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143952_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143955_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143955_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143955_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143955_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-051` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-052` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-055` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-056` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_143958-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143958_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143958_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143958_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_143958_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144007_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144007_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144007_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144007_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144007_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144007_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144007_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144007_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144009_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144009_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144009_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144009_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144012_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144012_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144012_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144012_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144013_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144013_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144013_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144013_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144016_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144016_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144016_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144016_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144020_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144020_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144020_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144020_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144022_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144022_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144022_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144022_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144025_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144025_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144025_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144025_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144026_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144026_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144026_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144026_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144028_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144028_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144028_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144028_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144031-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144031_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144031_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144031_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144031_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144040_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144040_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144040_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144040_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144040_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144040_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144040_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144040_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144042_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144042_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144042_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144042_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144045_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144045_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144045_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144045_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144046_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144046_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144046_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144046_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144049_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144049_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144049_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144049_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144052_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144052_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144052_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144052_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144054_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144054_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144054_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144054_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144057_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144057_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144057_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144057_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144059_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144059_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144059_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144059_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144100_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144100_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144100_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144100_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144104-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144104_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144104_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144104_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144104_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144113_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144113_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144113_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144113_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144113_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144113_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144113_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144113_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144116_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144116_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144116_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144116_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144117_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144117_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144117_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144117_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144118_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144118_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144118_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144118_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: ASP, NET, SQL |
| `SCRAPED-2026_11_15_144139-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144122_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144122_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144122_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144122_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144126_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144126_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144126_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144126_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144128_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144128_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144128_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144128_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144131_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144131_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144131_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144131_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144133_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144133_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144133_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144133_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144135_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144135_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144135_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144135_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: paparazzo |
| `SCRAPED-2026_11_15_144139-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144139-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144139_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144139_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144139_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144139_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144148_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144148_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144148_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144148_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144148_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144148_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144148_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144148_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144150_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144150_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144150_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144150_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144152_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144152_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144152_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144152_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144153_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144153_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144153_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144153_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Authorize, net |
| `SCRAPED-2026_11_15_144211-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: nopCommerce |
| `MISTAKE-LEARN-20261115_144156_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144156_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144156_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144156_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144159_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144159_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144159_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144159_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144202_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144202_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144202_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144202_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144205_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144205_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144205_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144205_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144206_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144206_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144206_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144206_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144208_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144208_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144208_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144208_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144211-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144211_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144211_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144211_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144211_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144221_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144221_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144221_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144221_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144221_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144221_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144221_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144221_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144224_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144224_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144224_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144224_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144226_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144226_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144226_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144226_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144227_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144227_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144227_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144227_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Packt |
| `SCRAPED-2026_11_15_144247-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: nopCommerce |
| `SCRAPED-2026_11_15_144247-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Codeplex |
| `SCRAPED-2026_11_15_144247-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144231_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144231_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144231_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144231_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144235_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144235_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144235_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144235_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144237_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144237_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144237_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144237_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144240_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144240_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144240_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144240_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144242_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144242_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144242_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144242_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144244_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144244_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144244_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144244_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তারা' (সাধারণ) এর সাথে সম্ভ্রমাত্মক ক্রিয়াপদ 'করেন' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_15_144247-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144247-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144247_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144247_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144247_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144247_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144256_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144256_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144256_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144256_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144256_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144256_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144256_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144256_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144258_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144258_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144258_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144258_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144300_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144300_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144300_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144300_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144301_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144301_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144301_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144301_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144304_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144304_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144304_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144304_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144307_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144307_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144307_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144307_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144309_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144309_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144309_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144309_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144312_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144312_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144312_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144312_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144313_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144313_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144313_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144313_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144315_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144315_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144315_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144315_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144318-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144318_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144318_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144318_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144318_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144327_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144327_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144327_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144327_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144327_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144327_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144327_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144327_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144330_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144330_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144330_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144330_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144332_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144332_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144332_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144332_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144333_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144333_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144333_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144333_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144337_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144337_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144337_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144337_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144341_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144341_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144341_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144341_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144343_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144343_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144343_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144343_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144346_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144346_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144346_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144346_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144348_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144348_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144348_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144348_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144351_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144351_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144351_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144351_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144355-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144355_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144355_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144355_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144355_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144405_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144405_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144405_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144405_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144405_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144405_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144405_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144405_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144406_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144406_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144406_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144406_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144409_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144409_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144409_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144409_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144410_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144410_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144410_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144410_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144414_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144414_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144414_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144414_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144418_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144418_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144418_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144418_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144419_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144419_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144419_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144419_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144422_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144422_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144422_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144422_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144424_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144424_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144424_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144424_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144427_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144427_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144427_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144427_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144430-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144430_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144430_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144430_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144430_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144439_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144439_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144439_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144439_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144439_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144439_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144439_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144439_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144442_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144442_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144442_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144442_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144444_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144444_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144444_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144444_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144446_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144446_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144446_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144446_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144449_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144449_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144449_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144449_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144452_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144452_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144452_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144452_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144454_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144454_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144454_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144454_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144457_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144457_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144457_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144457_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144459_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144459_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144459_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144459_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144501_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144501_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144501_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144501_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144506-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: Peterme, com |
| `MISTAKE-LEARN-20261115_144506_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144506_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144506_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144506_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144515_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144515_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144515_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144515_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144515_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144515_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144515_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144515_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144517_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144517_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144517_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144517_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144518_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144518_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144518_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144518_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144519_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144519_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144519_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144519_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144522_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144522_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144522_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144522_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144524_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144524_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144524_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144524_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144526_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144526_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144526_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144526_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144528_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144528_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144528_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144528_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144529_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144529_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144529_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144529_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144532_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144532_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144532_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144532_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144536-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144536_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144536_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144536_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144536_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144545_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144545_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144545_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144545_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144545_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144545_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144545_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144545_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144547_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144547_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144547_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144547_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144550_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144550_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144550_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: NID |
| `MISTAKE-LEARN-20261115_144550_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144551_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144551_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144551_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144551_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-023` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-024` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144553_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144553_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144553_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144553_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144557_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144557_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144557_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144557_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144559_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144559_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144559_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144559_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144601_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144601_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144601_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144601_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144603_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144603_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144603_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144603_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144605_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144605_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144605_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144605_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144609-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: mojo |
| `MISTAKE-LEARN-20261115_144609_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144609_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144609_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144609_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144617_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_144617_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144617_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144617_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144617_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144617_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144617_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144617_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144619_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144619_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144619_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144619_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144621_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: MUT |
| `MISTAKE-LEARN-20261115_144621_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144621_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144621_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Citizen Digital Services & Smart Governance | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144622_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144622_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144622_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144622_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-021` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-022` | Bangla Wikipedia E-Commerce & Retail | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-023` | Bangla Wikipedia Postal & Courier Logistics | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-024` | Bangla Wikipedia Postal & Courier Logistics | Consumer E-Commerce & Retail Logistics | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144626_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144626_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144626_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144626_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-029` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-030` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-031` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-032` | Bangla Wikipedia Telecommunications & Customer Experience | Customer Support & Conversational Chat | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144630_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144630_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144630_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144630_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144632_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144632_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144632_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144632_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144634_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144634_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144634_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144634_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144635_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144635_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144635_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144635_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144637_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144637_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144637_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144637_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-053` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-054` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-055` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-056` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-057` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-058` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-059` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_144640-060` | Bangla Wikipedia Journalism & Media Studies | Mass Media & Digital Journalism | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144640_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144640_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144640_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_144640_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | MFS, Microfinance & Grassroots FinTech | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
