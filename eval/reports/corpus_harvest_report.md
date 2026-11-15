# Real-World Corpus Harvesting & Multi-Domain Audit Report

- **Total Ingested Sentences**: `402`
- **Clean Human Benchmark**: `374` (Verified authentic native sentences)
- **Canary Trapped**: `28` (Flaws successfully intercepted by linter)
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
| `CORP-POE-001` | Kashiram Das (Mahabharata) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-002` | Krittibas Ojha (Ramayana) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-003` | Michael Madhusudan Dutt (Meghnadbadh Kavya) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-004` | Rabindranath Tagore (Sanchayita) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-POE-005` | Kazi Nazrul Islam (Bidrohi) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-001` | Modern Literary Fiction Anthology | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-002-RAW` | Literary Translation Benchmark (Raw LLM) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `2` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'ঝোপের চারপাশে পেটানো' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-FIC-002-GOLD` | Literary Translation Benchmark (Human Gold) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-003` | Riverine Bengal Novel Excerpt | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-004-RAW` | Urban Fiction Dialogue (Raw LLM) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | অস্বাভাবিক ইংরেজি প্যাসিভ ক্যাল্ক: 'খারাপ কর্মী তার সরঞ্জামকে দোষ দেয়' প্রমিত বাংলায় কৃত্রিম শোনায়। |
| `CORP-FIC-004-GOLD` | Urban Fiction Dialogue (Human Gold) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-FIC-005` | Short Story Psychological Monologue | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
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
| `CORP-EDU-001` | NCTB Curriculum Manual | Education & Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-002` | Bangla Wikipedia (উইকিপিডিয়া) | Science & Encyclopedic | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-003` | Classical Poetic Corpus | Poetic Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-004` | Department of Agricultural Extension (DAE) | Agronomy & Crop Protection | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `CORP-EDU-005` | Healthcare Clinical Protocol | Healthcare & Medicine | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141802_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141802_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141802_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141802_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141802_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141802_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141802_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141802_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141803_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141803_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141803_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141803_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141804_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141804_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141804_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141804_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141805_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141805_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141805_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141805_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141807_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141807_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141807_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141807_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141808_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141808_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141808_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141808_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141810_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141810_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141810_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141810_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141812_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141812_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141812_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141812_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141813_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141813_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141813_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141813_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141813-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141813-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141813-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141813-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141821_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141821_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141821_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141821_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141821_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141821_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141821_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141821_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141822_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141822_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141822_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141822_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141823_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141823_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141823_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141823_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141824_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141824_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141824_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141824_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141826_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141826_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141826_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141826_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141827_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141827_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141827_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141827_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141829_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141829_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141829_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141829_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141830_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141830_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141830_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141830_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141832_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141832_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141832_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141832_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141832-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141832-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141832-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141832-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141840_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141840_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141840_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141840_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141840_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141840_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141840_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141840_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141841_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141841_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141841_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141841_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141842_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141842_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141842_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141842_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141843_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141843_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141843_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141843_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141844_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141844_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141844_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141844_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141846_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141846_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141846_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141846_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141848_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141848_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141848_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141848_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141849_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141849_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141849_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141849_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141850_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141850_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141850_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141850_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141851-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141851-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141851-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141851-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141859_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141859_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141859_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141859_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141859_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141859_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141859_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141859_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141900_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141900_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141900_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141900_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141901_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141901_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141901_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141901_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141902_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141902_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141902_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141902_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141904_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141904_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141904_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141904_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141905_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141905_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141905_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141905_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141907_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141907_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141907_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141907_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141908_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141908_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141908_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141908_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141909_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141909_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141909_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141909_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141910-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141910-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141910-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141910-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141918_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141918_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141918_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141918_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141918_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141918_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141918_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141918_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141919_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141919_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141919_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141919_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141920_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141920_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141920_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141920_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141921_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141921_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141921_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141921_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141922_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141922_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141922_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141922_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141924_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141924_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141924_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141924_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141926_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141926_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141926_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141926_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141927_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141927_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141927_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141927_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141928_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141928_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141928_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141928_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141928-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141928-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141928-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141928-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141936_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141936_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141936_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141936_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141936_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141936_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141936_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141936_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141937_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141937_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141937_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141937_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141938_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141938_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141938_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141938_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141940_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141940_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141940_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141940_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141941_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141941_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141941_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141941_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141942_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141942_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141942_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141942_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141945_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141945_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141945_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141945_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141945_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141945_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141945_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141945_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141947_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141947_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141947_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141947_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141947-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141947-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141947-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_141947-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141955_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141955_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141955_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141955_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_141955_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141955_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141955_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141955_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141957_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141957_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141957_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141957_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141958_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141958_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141958_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141958_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141959_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141959_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141959_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_141959_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142000_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142000_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142000_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142000_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142002_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142002_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142002_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_142002_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_142004_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142004_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142004_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142004_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142005_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142005_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142005_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142005_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142006_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142006_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142006_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_142006_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_142006-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_142006-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_142006-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_142006-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
