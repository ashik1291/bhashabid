# Real-World Corpus Harvesting & Multi-Domain Audit Report

- **Total Ingested Sentences**: `4406`
- **Clean Human Benchmark**: `3993` (Verified authentic native sentences)
- **Canary Trapped**: `413` (Flaws successfully intercepted by linter)
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
| `MISTAKE-LEARN-20261115_123146_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123146_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123146_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123146_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123147_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123147_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123147_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123147_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123148_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123148_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123148_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123148_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123148_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123148_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123148_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123148_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123149_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123149_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123149_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123149_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123151_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123151_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123151_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123151_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123152_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123152_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123152_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123152_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123154_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123154_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123154_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123154_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123155_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123155_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123155_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123155_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123157_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123157_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123157_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123157_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123157-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123157-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123157-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123157-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123205_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123205_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123205_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123205_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123205_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123205_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123205_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123205_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123206_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123206_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123206_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123206_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123207_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123207_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123207_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123207_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123208_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123208_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123208_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123208_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123209_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123209_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123209_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123209_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123211_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123211_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123211_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123211_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123213_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123213_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123213_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123213_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123214_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123214_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123214_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123214_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123215_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123215_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123215_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123215_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123215-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123215-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123215-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123215-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123223_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123223_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123223_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123223_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123223_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123223_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123223_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123223_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123224_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123224_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123224_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123224_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123225_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123225_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123225_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123225_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123226_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123226_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123226_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123226_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123227_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123227_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123227_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123227_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123229_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123229_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123229_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123229_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123231_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123231_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123231_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123231_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123232_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123232_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123232_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123232_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123233_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123233_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123233_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123233_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123233-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123233-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123233-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123233-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123241_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123241_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123241_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123241_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123241_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123241_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123241_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123241_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123242_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123242_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123242_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123242_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123243_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123243_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123243_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123243_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123244_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123244_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123244_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123244_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123246_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123246_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123246_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123246_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123247_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123247_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123247_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123247_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123249_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123249_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123249_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123249_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123250_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123250_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123250_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123250_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123252_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123252_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123252_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123252_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123252-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123252-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123252-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123252-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123300_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123300_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123300_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123300_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123300_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123300_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123300_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123300_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123301_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123301_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123301_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123301_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123302_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123302_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123302_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123302_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123303_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123303_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123303_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123303_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123304_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123304_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123304_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123304_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123306_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123306_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123306_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123306_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123308_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123308_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123308_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123308_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123309_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123309_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123309_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123309_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123310_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123310_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123310_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123310_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123310-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123310-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123310-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123310-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123318_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123318_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123318_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123318_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123318_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123318_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123318_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123318_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123319_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123319_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123319_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123319_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123320_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123320_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123320_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123320_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123321_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123321_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123321_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123321_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123323_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123323_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123323_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123323_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123324_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123324_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123324_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123324_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123326_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123326_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123326_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123326_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123327_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123327_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123327_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123327_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123329_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123329_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123329_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123329_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123329-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123329-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123329-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123329-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123337_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123337_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123337_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123337_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123337_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123337_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123337_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123337_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123338_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123338_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123338_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123338_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123339_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123339_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123339_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123339_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123340_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123340_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123340_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123340_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123341_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123341_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123341_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123341_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123343_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123343_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123343_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123343_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123345_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123345_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123345_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123345_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123346_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123346_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123346_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123346_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123347_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123347_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123347_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123347_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123347-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123347-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123347-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123347-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123355_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123355_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123355_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123355_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123355_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123355_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123355_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123355_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123356_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123356_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123356_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123356_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123357_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123357_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123357_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123357_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123358_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123358_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123358_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123358_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123400_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123400_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123400_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123400_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123401_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123401_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123401_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123401_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123403_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123403_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123403_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123403_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123404_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123404_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123404_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123404_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123405_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123405_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123405_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123405_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123406-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123406-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123406-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123406-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123414_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123414_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123414_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123414_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123414_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123414_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123414_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123414_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123415_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123415_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123415_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123415_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123416_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123416_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123416_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123416_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123417_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123417_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123417_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123417_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123418_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123418_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123418_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123418_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123420_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123420_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123420_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123420_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123422_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123422_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123422_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123422_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123423_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123423_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123423_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123423_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123424_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123424_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123424_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123424_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123424-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123424-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123424-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123424-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123432_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123432_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123432_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123432_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123432_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123432_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123432_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123432_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123434_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123434_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123434_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123434_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123434_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123434_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123434_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123434_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123435_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123435_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123435_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123435_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123437_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123437_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123437_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123437_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123438_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123438_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123438_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123438_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123440_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123440_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123440_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123440_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123441_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123441_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123441_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123441_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123443_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123443_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123443_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123443_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123443-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123443-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123443-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123443-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123451_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123451_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123451_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123451_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123451_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123451_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123451_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123451_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123452_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123452_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123452_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123452_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123453_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123453_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123453_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123453_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123454_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123454_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123454_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123454_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123455_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123455_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123455_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123455_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123456_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123456_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123456_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123456_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123458_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123458_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123458_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123458_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123459_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123459_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123459_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123459_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123501_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123501_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123501_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123501_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123501-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123501-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123501-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123501-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123509_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123509_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123509_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123509_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123509_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123509_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123509_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123509_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123510_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123510_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123510_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123510_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123511_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123511_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123511_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123511_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123512_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123512_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123512_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123512_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123513_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123513_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123513_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123513_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123515_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123515_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123515_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123515_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123517_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123517_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123517_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123517_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123518_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123518_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123518_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123518_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123519_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123519_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123519_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123519_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123519-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123519-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123519-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123519-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123527_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123527_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123527_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123527_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123527_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123527_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123527_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123527_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123528_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123528_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123528_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123528_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123529_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123529_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123529_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123529_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123530_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123530_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123530_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123530_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123531_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123531_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123531_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123531_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123533_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123533_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123533_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123533_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123534_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123534_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123534_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123534_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123536_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123536_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123536_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123536_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123537_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123537_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123537_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123537_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123537-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123537-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123537-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123537-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123545_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123545_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123545_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123545_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123545_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123545_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123545_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123545_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123546_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123546_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123546_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123546_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123547_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123547_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123547_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123547_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123548_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123548_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123548_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123548_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123549_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123549_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123549_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123549_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123551_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123551_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123551_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123551_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123553_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123553_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123553_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123553_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123554_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123554_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123554_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123554_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123555_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123555_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123555_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123555_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123555-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123555-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123555-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123555-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123603_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123603_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123603_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123603_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123603_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123603_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123603_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123603_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123604_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123604_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123604_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123604_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123605_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123605_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123605_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123605_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123606_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123606_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123606_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123606_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123608_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123608_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123608_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123608_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123609_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123609_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123609_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123609_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123611_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123611_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123611_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123611_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123612_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123612_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123612_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123612_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123613_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123613_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123613_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123613_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123614-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123614-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123614-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123614-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123621_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123621_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123621_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123621_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123621_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123621_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123621_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123621_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123622_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123622_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123622_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123622_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123623_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123623_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123623_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123623_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123624_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123624_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123624_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123624_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123625_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123625_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123625_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123625_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123627_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123627_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123627_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123627_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123629_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123629_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123629_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123629_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123630_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123630_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123630_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123630_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123631_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123631_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123631_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123631_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123632-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123632-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123632-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123632-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123639_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123639_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123639_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123639_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123639_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123639_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123639_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123639_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123640_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123640_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123640_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123640_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123641_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123641_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123641_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123641_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123642_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123642_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123642_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123642_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123644_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123644_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123644_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123644_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123645_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123645_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123645_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123645_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123647_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123647_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123647_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123647_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123648_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123648_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123648_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123648_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123650_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123650_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123650_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123650_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123650-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123650-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123650-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123650-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123658_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123658_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123658_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123658_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123658_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123658_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123658_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123658_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123700_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123700_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123700_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123700_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123701_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123701_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123701_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123701_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123702_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123702_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123702_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123702_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123703_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123703_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123703_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123703_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123705_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123705_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123705_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123705_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123707_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123707_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123707_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123707_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123708_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123708_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123708_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123708_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123709_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123709_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123709_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123709_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123709-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123709-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123709-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123709-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123717_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123717_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123717_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123717_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123717_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123717_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123717_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123717_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123718_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123718_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123718_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123718_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123719_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123719_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123719_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123719_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123720_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123720_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123720_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123720_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123721_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123721_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123721_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123721_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123723_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123723_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123723_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123723_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123725_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123725_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123725_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123725_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123726_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123726_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123726_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123726_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123727_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123727_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123727_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123727_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123727-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123727-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123727-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123727-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123735_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123735_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123735_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123735_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123735_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123735_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123735_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123735_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123736_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123736_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123736_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123736_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123737_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123737_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123737_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123737_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123738_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123738_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123738_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123738_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123740_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123740_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123740_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123740_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123741_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123741_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123741_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123741_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123743_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123743_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123743_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123743_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123744_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123744_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123744_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123744_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123745_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123745_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123745_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123745_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123746-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123746-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123746-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123746-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123754_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123754_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123754_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123754_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123754_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123754_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123754_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123754_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123755_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123755_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123755_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123755_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123756_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123756_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123756_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123756_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123757_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123757_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123757_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123757_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123758_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123758_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123758_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123758_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123800_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123800_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123800_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123800_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123802_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123802_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123802_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123802_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123803_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123803_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123803_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123803_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123804_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123804_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123804_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123804_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123804-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123804-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123804-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123804-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123812_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123812_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123812_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123812_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123812_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123812_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123812_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123812_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123814_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123814_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123814_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123814_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123815_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123815_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123815_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123815_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123816_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123816_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123816_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123816_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123817_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123817_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123817_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123817_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123818_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123818_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123818_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123818_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123820_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123820_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123820_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123820_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123821_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123821_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123821_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123821_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123823_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123823_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123823_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123823_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123823-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123823-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123823-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123823-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123831_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123831_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123831_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123831_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123831_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123831_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123831_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123831_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123832_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123832_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123832_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123832_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123833_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123833_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123833_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123833_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123834_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123834_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123834_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123834_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123835_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123835_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123835_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123835_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123837_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123837_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123837_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123837_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123839_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123839_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123839_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123839_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123840_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123840_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123840_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123840_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123841_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123841_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123841_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123841_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123841-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123841-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123841-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123841-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123849_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123849_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123849_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123849_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123849_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123849_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123849_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123849_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123850_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123850_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123850_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123850_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123851_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123851_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123851_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123851_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123852_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123852_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123852_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123852_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123854_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123854_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123854_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123854_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123855_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123855_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123855_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123855_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123857_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123857_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123857_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123857_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123858_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123858_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123858_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123858_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123900_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123900_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123900_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123900_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123900-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123900-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123900-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123900-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123908_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123908_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123908_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123908_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123908_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123908_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123908_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123908_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123909_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123909_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123909_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123909_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123910_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123910_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123910_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123910_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123911_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123911_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123911_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123911_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123912_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123912_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123912_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123912_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123914_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123914_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123914_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123914_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123916_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123916_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123916_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123916_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123917_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123917_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123917_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123917_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123918_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123918_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123918_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123918_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123918-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123918-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123918-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123918-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123926_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123926_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123926_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123926_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123926_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123926_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123926_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123926_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123927_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123927_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123927_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123927_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123928_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123928_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123928_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123928_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123929_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123929_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123929_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123929_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123930_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123930_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123930_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123930_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123931_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123931_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123931_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123931_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123933_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123933_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123933_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123933_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123934_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123934_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123934_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123934_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123936_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123936_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123936_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123936_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123936-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123936-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123936-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123936-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123944_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123944_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123944_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123944_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_123944_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123944_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123944_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123944_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123945_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123945_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123945_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123945_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123946_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123946_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123946_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123946_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123947_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123947_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123947_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_123947_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123948_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123948_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123948_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123948_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123950_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123950_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123950_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123950_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123952_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123952_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123952_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123952_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123953_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123953_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123953_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123953_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123954_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123954_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123954_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_123954_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123954-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123954-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123954-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_123954-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124002_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124002_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124002_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124002_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124002_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124002_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124002_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124002_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124003_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124003_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124003_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124003_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124004_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124004_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124004_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124004_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124005_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124005_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124005_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124005_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124006_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124006_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124006_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124006_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124008_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124008_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124008_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124008_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124009_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124009_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124009_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124009_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124011_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124011_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124011_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124011_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124012_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124012_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124012_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124012_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124012-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124012-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124012-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124012-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124020_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124020_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124020_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124020_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124020_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124020_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124020_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124020_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124022_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124022_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124022_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124022_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124022_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124022_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124022_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124022_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124023_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124023_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124023_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124023_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124025_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124025_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124025_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124025_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124026_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124026_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124026_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124026_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124028_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124028_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124028_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124028_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124029_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124029_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124029_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124029_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124031_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124031_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124031_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124031_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124031-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124031-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124031-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124031-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124040_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124040_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124040_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124040_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124040_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124040_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124040_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124040_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124041_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124041_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124041_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124041_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124042_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124042_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124042_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124042_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124043_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124043_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124043_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124043_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124044_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124044_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124044_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124044_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124046_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124046_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124046_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124046_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124048_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124048_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124048_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124048_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124049_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124049_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124049_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124049_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124050_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124050_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124050_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124050_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124050-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124050-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124050-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124050-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124058_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124058_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124058_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124058_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124058_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124058_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124058_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124058_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124059_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124059_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124059_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124059_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124100_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124100_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124100_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124100_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124101_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124101_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124101_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124101_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124103_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124103_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124103_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124103_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124104_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124104_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124104_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124104_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124106_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124106_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124106_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124106_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124107_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124107_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124107_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124107_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124109_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124109_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124109_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124109_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124109-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124109-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124109-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124109-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124118_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124118_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124118_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124118_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124118_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124118_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124118_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124118_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124119_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124119_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124119_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124119_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124120_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124120_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124120_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124120_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124121_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124121_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124121_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124121_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124122_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124122_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124122_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124122_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124124_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124124_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124124_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124124_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124126_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124126_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124126_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124126_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124127_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124127_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124127_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124127_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124128_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124128_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124128_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124128_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124129-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124129-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124129-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124129-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124137_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124137_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124137_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124137_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124137_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124137_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124137_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124137_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124138_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124138_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124138_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124138_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124139_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124139_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124139_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124139_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124140_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124140_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124140_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124140_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124141_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124141_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124141_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124141_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124142_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124142_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124142_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124142_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124144_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124144_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124144_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124144_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124145_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124145_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124145_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124145_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124147_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124147_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124147_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124147_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124147-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124147-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124147-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124147-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124155_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124155_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124155_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124155_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124155_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124155_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124155_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124155_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124156_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124156_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124156_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124156_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124157_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124157_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124157_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124157_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124158_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124158_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124158_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124158_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124159_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124159_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124159_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124159_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124201_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124201_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124201_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124201_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124203_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124203_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124203_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124203_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124204_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124204_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124204_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124204_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124205_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124205_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124205_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124205_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124205-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124205-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124205-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124205-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124213_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124213_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124213_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124213_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124213_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124213_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124213_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124213_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124215_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124215_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124215_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124215_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124216_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124216_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124216_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124216_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124217_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124217_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124217_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124217_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124218_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124218_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124218_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124218_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124219_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124219_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124219_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124219_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124221_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124221_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124221_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124221_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124222_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124222_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124222_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124222_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124223_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124223_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124223_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124223_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124223-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124223-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124223-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124223-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124231_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124231_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124231_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124231_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124232_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124232_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124232_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124232_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124232_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124232_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124232_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124232_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124233_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124233_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124233_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124233_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124234_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124234_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124234_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124234_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124236_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124236_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124236_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124236_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124237_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124237_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124237_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124237_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124239_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124239_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124239_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124239_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124240_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124240_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124240_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124240_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124242_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124242_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124242_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124242_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124242-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124242-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124242-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124242-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124250_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124250_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124250_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124250_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124250_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124250_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124250_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124250_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124251_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124251_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124251_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124251_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124252_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124252_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124252_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124252_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124253_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124253_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124253_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124253_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124254_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124254_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124254_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124254_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124256_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124256_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124256_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124256_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124258_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124258_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124258_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124258_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124259_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124259_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124259_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124259_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124300_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124300_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124300_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124300_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124300-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124300-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124300-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124300-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124308_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124308_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124308_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124308_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124308_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124308_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124308_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124308_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124309_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124309_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124309_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124309_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124310_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124310_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124310_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124310_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124311_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124311_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124311_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124311_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124312_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124312_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124312_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124312_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124314_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124314_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124314_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124314_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124316_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124316_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124316_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124316_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124317_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124317_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124317_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124317_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124319_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124319_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124319_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124319_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124319-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124319-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124319-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124319-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124327_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124327_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124327_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124327_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124327_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124327_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124327_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124327_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124328_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124328_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124328_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124328_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124329_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124329_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124329_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124329_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124330_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124330_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124330_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124330_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124331_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124331_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124331_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124331_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124332_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124332_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124332_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124332_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124334_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124334_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124334_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124334_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124335_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124335_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124335_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124335_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124336_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124336_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124336_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124336_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124337-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124337-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124337-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124337-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124345_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124345_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124345_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124345_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124345_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124345_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124345_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124345_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124346_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124346_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124346_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124346_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124347_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124347_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124347_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124347_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124348_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124348_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124348_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124348_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124349_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124349_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124349_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124349_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124351_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124351_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124351_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124351_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124352_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124352_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124352_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124352_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124353_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124353_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124353_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124353_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124355_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124355_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124355_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124355_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124355-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124355-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124355-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124355-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124403_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124403_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124403_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124403_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124403_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124403_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124403_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124403_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124404_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124404_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124404_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124404_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124405_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124405_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124405_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124405_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124406_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124406_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124406_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124406_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124407_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124407_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124407_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124407_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124409_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124409_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124409_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124409_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124411_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124411_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124411_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124411_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124412_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124412_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124412_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124412_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124413_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124413_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124413_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124413_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124413-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124413-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124413-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124413-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124421_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124421_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124421_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124421_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124421_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124421_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124421_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124421_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124422_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124422_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124422_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124422_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124423_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124423_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124423_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124423_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124424_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124424_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124424_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124424_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124426_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124426_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124426_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124426_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124427_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124427_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124427_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124427_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124429_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124429_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124429_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124429_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124430_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124430_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124430_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124430_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124431_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124431_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124431_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124431_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124431-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124431-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124431-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124431-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124439_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124439_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124439_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124439_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124439_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124439_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124439_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124439_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124440_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124440_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124440_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124440_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124441_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124441_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124441_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124441_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124442_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124442_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124442_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124442_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124444_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124444_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124444_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124444_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124445_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124445_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124445_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124445_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124447_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124447_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124447_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124447_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124448_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124448_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124448_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124448_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124450_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124450_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124450_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124450_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124450-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124450-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124450-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124450-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124458_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124458_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124458_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124458_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124458_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124458_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124458_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124458_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124459_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124459_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124459_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124459_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124459_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124459_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124459_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124459_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124500_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124500_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124500_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124500_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124502_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124502_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124502_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124502_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124503_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124503_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124503_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124503_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124505_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124505_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124505_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124505_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124506_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124506_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124506_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124506_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124508_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124508_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124508_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124508_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124508-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124508-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124508-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124508-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124516_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124516_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124516_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124516_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124516_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124516_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124516_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124516_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124517_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124517_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124517_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124517_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124518_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124518_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124518_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124518_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124519_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124519_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124519_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124519_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124520_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124520_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124520_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124520_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124521_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124521_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124521_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124521_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124523_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124523_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124523_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124523_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124524_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124524_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124524_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124524_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124525_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124525_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124525_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124525_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124526-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124526-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124526-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124526-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124533_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124533_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124533_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124533_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124533_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124533_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124533_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124533_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124535_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124535_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124535_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124535_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124536_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124536_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124536_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124536_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124536_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124536_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124536_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124536_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124538_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124538_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124538_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124538_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124539_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124539_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124539_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124539_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124541_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124541_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124541_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124541_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124542_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124542_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124542_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124542_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124544_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124544_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124544_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124544_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124544-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124544-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124544-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124544-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124552_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124552_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124552_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124552_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124552_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124552_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124552_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124552_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124553_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124553_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124553_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124553_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124554_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124554_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124554_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124554_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124555_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124555_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124555_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124555_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124556_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124556_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124556_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124556_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124558_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124558_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124558_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124558_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124559_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124559_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124559_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124559_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124600_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124600_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124600_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124600_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124602_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124602_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124602_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124602_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124602-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124602-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124602-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124602-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124610_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124610_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124610_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124610_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124610_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124610_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124610_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124610_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124611_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124611_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124611_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124611_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124612_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124612_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124612_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124612_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124613_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124613_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124613_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124613_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124614_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124614_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124614_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124614_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124616_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124616_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124616_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124616_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124618_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124618_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124618_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124618_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124619_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124619_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124619_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124619_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124620_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124620_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124620_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124620_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124621-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124621-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124621-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124621-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124629_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124629_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124629_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124629_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124629_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124629_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124629_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124629_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124631_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124631_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124631_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124631_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124632_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124632_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124632_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124632_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124633_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124633_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124633_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124633_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124634_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124634_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124634_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124634_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124636_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124636_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124636_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124636_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124638_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124638_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124638_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124638_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124639_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124639_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124639_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124639_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124640_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124640_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124640_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124640_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124641-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124641-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124641-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124641-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124649_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124649_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124649_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124649_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124649_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124649_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124649_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124649_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124650_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124650_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124650_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124650_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124651_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124651_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124651_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124651_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124651_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124651_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124651_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124651_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124653_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124653_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124653_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124653_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124654_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124654_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124654_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124654_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124656_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124656_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124656_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124656_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124657_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124657_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124657_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124657_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124659_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124659_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124659_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124659_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124659-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124659-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124659-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124659-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124707_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124707_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124707_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124707_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124707_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124707_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124707_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124707_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124708_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124708_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124708_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124708_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124709_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124709_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124709_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124709_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124710_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124710_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124710_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124710_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124712_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124712_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124712_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124712_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124713_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124713_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124713_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124713_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124715_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124715_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124715_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124715_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124716_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124716_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124716_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124716_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124717_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124717_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124717_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124717_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124718-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124718-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124718-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124718-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124725_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124725_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124725_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124725_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124726_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124726_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124726_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124726_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124727_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124727_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124727_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124727_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124728_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124728_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124728_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124728_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124729_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124729_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124729_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124729_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124730_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124730_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124730_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124730_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124732_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124732_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124732_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124732_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124734_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124734_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124734_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124734_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124735_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124735_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124735_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124735_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124736_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124736_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124736_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124736_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124737-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124737-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124737-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124737-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124745_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124745_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124745_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124745_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124745_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124745_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124745_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124745_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124746_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124746_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124746_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124746_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124747_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124747_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124747_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124747_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124747_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124747_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124747_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124747_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124749_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124749_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124749_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124749_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124750_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124750_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124750_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124750_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124752_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124752_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124752_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124752_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124753_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124753_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124753_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124753_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124754_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124754_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124754_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124754_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124754-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124754-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124754-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124754-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124802_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124802_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124802_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124802_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124802_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124802_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124802_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124802_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124803_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124803_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124803_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124803_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124804_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124804_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124804_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124804_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124805_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124805_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124805_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124805_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124807_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124807_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124807_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124807_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124808_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124808_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124808_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124808_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124810_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124810_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124810_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124810_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124811_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124811_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124811_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124811_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124812_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124812_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124812_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124812_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124812-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124812-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124812-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124812-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124820_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124820_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124820_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124820_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124820_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124820_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124820_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124820_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124821_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124821_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124821_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124821_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124822_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124822_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124822_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124822_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124823_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124823_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124823_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124823_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124824_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124824_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124824_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124824_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124826_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124826_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124826_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124826_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124828_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124828_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124828_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124828_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124829_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124829_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124829_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124829_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124830_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124830_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124830_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124830_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124830-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'করে' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_15_124830-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124830-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124830-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124838_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124838_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124838_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124838_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124838_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124838_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124838_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124838_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124840_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124840_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124840_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124840_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124841_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124841_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124841_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124841_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124842_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124842_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124842_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124842_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124843_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124843_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124843_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124843_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124845_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124845_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124845_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124845_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124847_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124847_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124847_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124847_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124848_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124848_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124848_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124848_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124849_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124849_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124849_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124849_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124849-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124849-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124849-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124849-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124857_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124857_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124857_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124857_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124857_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124857_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124857_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124857_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124858_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124858_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124858_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124858_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124859_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124859_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124859_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124859_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124901_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124901_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124901_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124901_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124902_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124902_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124902_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124902_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124904_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124904_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124904_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124904_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124906_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124906_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124906_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124906_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124907_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124907_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124907_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124907_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124908_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124908_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124908_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124908_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124908-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124908-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124908-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124908-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124916_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124916_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124916_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124916_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124916_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124916_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124916_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124916_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124917_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124917_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124917_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124917_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124918_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124918_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124918_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124918_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124919_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124919_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124919_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124919_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124920_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124920_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124920_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124920_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124921_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124921_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124921_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124921_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124923_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124923_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124923_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124923_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124924_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124924_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124924_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124924_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124926_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124926_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124926_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124926_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124926-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124926-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124926-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124926-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124934_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124934_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124934_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124934_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124934_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124934_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124934_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124934_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124935_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124935_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124935_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124935_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124936_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124936_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124936_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124936_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124937_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124937_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124937_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124937_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124938_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124938_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124938_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124938_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124939_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124939_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124939_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124939_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124941_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124941_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124941_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124941_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124942_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124942_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124942_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124942_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124944_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124944_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124944_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124944_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124944-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124944-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124944-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_124944-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124952_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124952_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124952_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124952_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124952_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124952_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124952_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124952_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124953_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124953_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124953_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124953_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124954_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124954_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124954_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124954_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124955_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_124955_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124955_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124955_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124956_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124956_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124956_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124956_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124958_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124958_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_124958_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_124958_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125000_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125000_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125000_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125000_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125001_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125001_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125001_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125001_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125003_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125003_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125003_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125003_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125003-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125003-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125003-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125003-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125011_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125011_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125011_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125011_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125011_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125011_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125011_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125011_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125012_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125012_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125012_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125012_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125013_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125013_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125013_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125013_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125014_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125014_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125014_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125014_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125015_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125015_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125015_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125015_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125017_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125017_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125017_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125017_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125018_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125018_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125018_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125018_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125019_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125019_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125019_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125019_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125021_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125021_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125021_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125021_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125021-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125021-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125021-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125021-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125029_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125029_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125029_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125029_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125029_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125029_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125029_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125029_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125030_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125030_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125030_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125030_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125031_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125031_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125031_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125031_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125032_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125032_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125032_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125032_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125033_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125033_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125033_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125033_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125035_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125035_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125035_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125035_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125037_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125037_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125037_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125037_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125038_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125038_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125038_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125038_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125039_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125039_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125039_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125039_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125040-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125040-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125040-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125040-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125047_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125047_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125047_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125047_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125048_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125048_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125048_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125048_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125049_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125049_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125049_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125049_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125050_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125050_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125050_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125050_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125051_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125051_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125051_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125051_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125052_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125052_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125052_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125052_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125054_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125054_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125054_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125054_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125056_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125056_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125056_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125056_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125057_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125057_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125057_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125057_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125058_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125058_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125058_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125058_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125058-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125058-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125058-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125058-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125106_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125106_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125106_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125106_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125106_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125106_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125106_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125106_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125107_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125107_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125107_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125107_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125108_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125108_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125108_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125108_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125109_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125109_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125109_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125109_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125111_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125111_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125111_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125111_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125112_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125112_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125112_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125112_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125114_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125114_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125114_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125114_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125115_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125115_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125115_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125115_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125116_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125116_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125116_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125116_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125116-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125116-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125116-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125116-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125124_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125124_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125124_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125124_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125124_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125124_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125124_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125124_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125125_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125125_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125125_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125125_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125126_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125126_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125126_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125126_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125127_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125127_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125127_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125127_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125128_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125128_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125128_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125128_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125130_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125130_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125130_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125130_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125132_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125132_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125132_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125132_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125132_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125132_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125132_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125132_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125134_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125134_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125134_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125134_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125134-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125134-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125134-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125134-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125142_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125142_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125142_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125142_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125142_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125142_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125142_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125142_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125143_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125143_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125143_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125143_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125144_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125144_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125144_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125144_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125144_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125144_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125144_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125144_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125146_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125146_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125146_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125146_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125147_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125147_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125147_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125147_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125149_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125149_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125149_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125149_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125150_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125150_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125150_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125150_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125152_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125152_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125152_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125152_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125152-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125152-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125152-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125152-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125200_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125200_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125200_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125200_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125200_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125200_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125200_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125200_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125201_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125201_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125201_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125201_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125202_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125202_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125202_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125202_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125203_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125203_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125203_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125203_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125204_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125204_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125204_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125204_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125206_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125206_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125206_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125206_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125207_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125207_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125207_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125207_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125208_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125208_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125208_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125208_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125210_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125210_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125210_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125210_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125210-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125210-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125210-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125210-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125218_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125218_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125218_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125218_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125218_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125218_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125218_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125218_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125219_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125219_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125219_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125219_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125220_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125220_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125220_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125220_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125221_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125221_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125221_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125221_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125222_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125222_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125222_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125222_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125223_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125223_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125223_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125223_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125225_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125225_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125225_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125225_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125226_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125226_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125226_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125226_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125228_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125228_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125228_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125228_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125228-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125228-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125228-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125228-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125236_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125236_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125236_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125236_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125236_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125236_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125236_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125236_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125237_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125237_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125237_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125237_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125238_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125238_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125238_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125238_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125239_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125239_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125239_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125239_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125241_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125241_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125241_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125241_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125242_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125242_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125242_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125242_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125244_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125244_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125244_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125244_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125245_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125245_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125245_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125245_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125247_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125247_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125247_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125247_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125247-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125247-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125247-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125247-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125256_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125256_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125256_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125256_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125256_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125256_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125256_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125256_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125257_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125257_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125257_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125257_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125258_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125258_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125258_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125258_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125259_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125259_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125259_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125259_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125300_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125300_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125300_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125300_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125302_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125302_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125302_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125302_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125304_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125304_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125304_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125304_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125305_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125305_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125305_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125305_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125306_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125306_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125306_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125306_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125306-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125306-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125306-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125306-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125314_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125314_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125314_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125314_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125314_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125314_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125314_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125314_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125315_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125315_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125315_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125315_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125316_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125316_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125316_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125316_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125317_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125317_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125317_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125317_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125318_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125318_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125318_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125318_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125320_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125320_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125320_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125320_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125322_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125322_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125322_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125322_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125323_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125323_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125323_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125323_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125324_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125324_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125324_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125324_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125325-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125325-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125325-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125325-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125333_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125333_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125333_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125333_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125333_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125333_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125333_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125333_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125334_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125334_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125334_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125334_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125335_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125335_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125335_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125335_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125336_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125336_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125336_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125336_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125337_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125337_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125337_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125337_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125339_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125339_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125339_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125339_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125340_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125340_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125340_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125340_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125342_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125342_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125342_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125342_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125343_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125343_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125343_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125343_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125343-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125343-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125343-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125343-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125351_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125351_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125351_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125351_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125351_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125351_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125351_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125351_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125353_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125353_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125353_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125353_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125353_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125353_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125353_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125353_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125354_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125354_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125354_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125354_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125356_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125356_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125356_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125356_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125357_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125357_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125357_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125357_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125359_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125359_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125359_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125359_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125400_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125400_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125400_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125400_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125401_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125401_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125401_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125401_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125402-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125402-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125402-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125402-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125410_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125410_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125410_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125410_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125410_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125410_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125410_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125410_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125411_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125411_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125411_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125411_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125412_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125412_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125412_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125412_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125413_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125413_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125413_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125413_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125415_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125415_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125415_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125415_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125416_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125416_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125416_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125416_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125418_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125418_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125418_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125418_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125419_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125419_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125419_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125419_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125420_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125420_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125420_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125420_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125421-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125421-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125421-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125421-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125429_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125430_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125430_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125430_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125430_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125431_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125431_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125431_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125431_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125433_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125433_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125433_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125433_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125434_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125434_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125434_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125434_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125436_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125436_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125436_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125436_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125437_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125437_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125437_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125437_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125439_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125439_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125439_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125439_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125439-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125439-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125439-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125439-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125447_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125447_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125447_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125447_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125447_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125447_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125447_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125447_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125448_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125448_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125448_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125448_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125448_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125448_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125448_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125448_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125449_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125449_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125449_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125449_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125451_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125451_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125451_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125451_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125452_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125452_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125452_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125452_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125454_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125454_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125454_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125454_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125455_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125455_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125455_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125455_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125456_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125456_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125456_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125456_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125457-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125457-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125457-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125457-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125505_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125505_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125505_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125505_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125505_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125505_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125505_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125505_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125506_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125506_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125506_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125506_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125507_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125507_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125507_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125507_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125508_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125508_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125508_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125508_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125509_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125509_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125509_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125509_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125511_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125511_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125511_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125511_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125513_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125513_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125513_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125513_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125514_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125514_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125514_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125514_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125515_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125515_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125515_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125515_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125515-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125515-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125515-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125515-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125523_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125523_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125523_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125523_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125523_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125523_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125523_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125523_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125524_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125524_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125524_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125524_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125525_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125525_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125525_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125525_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125526_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125526_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125526_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125526_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125527_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125527_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125527_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125527_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125529_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125529_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125529_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125529_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125531_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125531_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125531_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125531_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125532_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125532_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125532_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125532_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125533_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125533_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125533_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125533_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125533-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125533-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125533-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125533-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125541_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125541_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125541_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125541_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125541_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125541_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125541_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125541_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125542_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125542_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125542_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125542_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125543_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125543_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125543_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125543_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125544_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125544_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125544_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125544_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125546_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125546_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125546_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125546_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125547_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125547_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125547_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125547_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125549_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125549_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125549_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125549_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125550_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125550_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125550_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125550_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125552_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125552_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125552_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125552_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125552-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125552-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125552-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125552-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125600_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125600_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125600_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125600_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125600_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125600_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125600_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125600_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125601_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125601_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125601_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125601_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125601_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125601_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125601_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125601_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125602_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125602_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125602_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125602_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125604_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125604_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125604_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125604_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125605_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125605_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125605_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125605_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125607_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125607_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125607_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125607_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125608_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125608_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125608_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125608_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125610_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125610_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125610_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125610_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125610-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125610-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125610-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125610-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125618_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125618_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125618_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125618_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125618_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125618_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125618_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125618_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125619_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125619_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125619_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125619_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125620_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125620_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125620_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125620_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125621_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125621_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125621_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125621_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125622_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125622_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125622_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125622_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125624_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125624_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125624_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125624_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125626_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125626_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125626_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125626_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125627_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125627_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125627_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125627_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125628_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125628_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125628_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125628_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125628-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125628-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125628-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125628-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125636_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125636_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125636_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125636_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125636_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125636_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125636_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125636_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125637_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125637_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125637_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125637_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125638_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125638_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125638_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125638_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125639_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125639_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125639_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125639_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125641_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125641_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125641_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125641_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125642_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125642_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125642_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125642_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125644_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125644_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125644_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125644_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125645_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125645_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125645_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125645_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125647_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125647_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125647_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125647_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125647-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125647-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125647-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125647-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125655_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125655_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125655_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125655_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125655_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125655_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125655_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125655_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125656_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125656_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125656_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125656_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125657_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125657_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125657_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125657_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125658_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125658_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125658_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125658_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125700_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125700_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125700_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125700_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125701_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125701_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125701_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125701_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125703_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125703_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125703_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125703_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125704_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125704_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125704_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125704_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125705_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125705_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125705_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125705_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125706-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125706-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125706-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125706-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125714_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125714_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125714_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125714_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125714_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125714_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125714_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125714_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125715_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125715_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125715_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125715_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125716_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125716_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125716_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125716_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125717_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125717_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125717_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125717_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125718_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125718_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125718_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125718_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125720_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125720_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125720_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125720_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125722_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125722_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125722_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125722_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125723_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125723_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125723_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125723_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125724_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125724_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125724_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125724_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125724-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125724-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125724-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125724-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125732_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125732_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125732_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125732_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125732_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125732_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125732_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125732_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125733_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125733_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125733_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125733_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125734_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125734_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125734_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125734_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125735_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125735_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125735_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125735_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125737_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125737_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125737_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125737_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125738_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125738_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125738_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125738_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125740_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125740_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125740_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125740_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125741_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125741_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125741_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125741_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125743_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125743_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125743_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125743_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125743-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125743-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125743-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125743-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125751_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125751_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125751_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125751_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125751_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125751_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125751_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125751_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125752_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125752_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125752_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125752_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125753_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125753_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125753_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125753_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125754_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125754_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125754_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125754_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125755_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125755_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125755_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125755_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125757_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125757_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125757_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125757_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125759_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125759_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125759_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125759_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125800_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125800_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125800_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125800_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125801_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125801_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125801_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125801_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125802-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125802-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125802-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125802-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125810_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125810_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125810_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125810_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125810_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125810_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125810_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125810_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125811_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125811_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125811_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125811_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125812_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125812_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125812_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125812_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125813_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125813_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125813_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125813_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125814_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125814_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125814_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125814_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125816_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125816_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125816_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125816_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125817_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125817_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125817_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125817_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125818_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125818_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125818_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125818_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125820_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125820_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125820_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125820_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125820-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125820-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125820-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125820-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125828_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125828_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125828_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125828_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125828_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125828_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125828_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125828_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125829_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125829_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125829_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125829_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125830_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125830_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125830_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125830_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125831_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125831_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125831_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125831_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125832_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125832_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125832_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125832_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125833_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125833_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125833_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125833_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125835_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125835_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125835_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125835_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125836_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125836_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125836_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125836_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125838_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125838_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125838_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125838_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125838-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125838-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125838-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125838-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125846_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125846_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125846_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125846_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125846_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125846_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125846_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125846_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125847_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125847_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125847_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125847_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125848_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125848_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125848_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125848_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125849_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125849_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125849_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125849_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125851_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125851_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125851_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125851_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125852_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125852_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125852_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125852_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125854_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125854_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125854_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125854_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125855_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125855_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125855_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125855_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125857_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125857_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125857_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125857_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125857-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125857-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125857-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125857-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125905_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125905_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125905_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125905_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125905_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125905_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125905_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125905_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125906_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125906_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125906_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125906_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125907_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125907_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125907_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125907_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125907_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125907_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125907_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125907_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125909_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125909_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125909_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125909_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125910_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125910_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125910_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125910_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125912_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125912_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125912_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125912_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125913_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125913_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125913_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125913_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125915_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125915_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125915_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125915_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125915-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125915-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125915-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125915-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125923_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125923_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125923_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125923_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125923_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125923_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125923_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125923_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125924_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125924_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125924_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125924_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125925_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125925_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125925_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125925_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125926_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125926_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125926_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125926_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125927_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125927_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125927_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125927_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125929_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125929_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125929_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125929_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125931_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125931_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125931_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125931_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125932_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125932_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125932_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125932_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125933_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125933_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125933_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125933_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125934-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125934-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125934-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125934-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125942_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125942_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125942_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125942_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125942_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125942_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125942_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125942_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125943_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125943_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125943_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125943_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125943_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125943_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125943_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125943_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125944_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125944_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125944_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125944_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_125946_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125946_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125946_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125946_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125947_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125947_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125947_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_125947_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125949_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125949_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125949_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125949_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125950_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125950_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125950_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125950_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125951_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125951_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125951_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125951_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125952-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125952-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125952-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_125952-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125959_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125959_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125959_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_125959_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130000_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130000_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130000_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130000_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130001_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130001_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130001_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130001_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130002_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130002_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130002_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130002_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130003_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130003_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130003_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130003_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130004_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130004_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130004_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130004_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130006_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130006_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130006_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130006_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130008_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130008_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130008_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130008_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130009_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130009_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130009_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130009_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130010_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130010_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130010_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130010_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130010-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130010-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130010-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130010-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130018_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130018_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130018_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130018_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130018_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130018_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130018_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130018_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130019_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130019_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130019_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130019_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130020_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130020_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130020_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130020_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130021_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130021_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130021_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130021_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130022_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130022_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130022_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130022_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130024_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130024_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130024_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130024_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130027_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130027_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130027_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130027_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130028_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130028_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130028_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130028_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130030_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130030_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130030_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130030_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130030-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130030-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130030-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130030-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130038_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130038_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130038_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130038_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130038_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130038_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130038_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130038_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130039_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130039_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130039_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130039_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130040_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130040_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130040_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130040_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130041_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130041_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130041_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130041_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130042_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130042_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130042_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130042_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130044_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130044_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130044_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130044_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130045_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130045_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130045_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130045_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130046_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130046_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130046_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130046_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130048_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130048_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130048_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130048_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130048-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130048-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130048-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130048-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130056_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130056_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130056_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130056_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130056_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130056_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130056_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130056_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130057_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130057_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130057_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130057_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130058_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130058_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130058_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130058_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130059_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130059_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130059_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130059_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130101_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130101_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130101_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130101_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130102_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130102_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130102_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130102_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130104_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130104_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130104_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130104_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130105_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130105_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130105_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130105_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130107_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130107_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130107_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130107_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130107-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130107-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130107-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130107-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130115_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130115_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130116_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130116_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130116_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130116_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130117_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130117_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130117_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130117_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130119_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130119_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130119_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130119_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130120_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130120_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130120_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130120_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130122_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130122_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130122_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130122_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130123_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130123_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130123_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130123_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130125_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130125_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130125_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130125_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130125-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130125-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130125-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130125-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130133_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130133_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130133_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130133_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130133_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130133_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130133_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130133_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130134_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130134_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130134_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130134_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130135_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130135_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130135_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130135_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130136_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130136_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_130136_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130136_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130137_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130137_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130137_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130137_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130139_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130139_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130139_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_130139_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130141_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130141_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130141_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130141_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130142_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130142_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130142_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130142_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130143_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130143_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130143_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_130143_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130143-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130143-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130143-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_130143-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
