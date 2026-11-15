# Real-World Corpus Harvesting & Multi-Domain Audit Report

- **Total Ingested Sentences**: `4182`
- **Clean Human Benchmark**: `3795` (Verified authentic native sentences)
- **Canary Trapped**: `384` (Flaws successfully intercepted by linter)
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
| `MISTAKE-LEARN-20261115_113132_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113132_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113132_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113132_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113132_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113132_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113132_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113132_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113159-009` | Deutsche Welle (DW Bangla - Climate & Disaster) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113159-010` | Deutsche Welle (DW Bangla - Climate & Disaster) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113159-011` | Deutsche Welle (DW Bangla - Climate & Disaster) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113159-012` | Bangla Wikipedia Poetry & Classical Verse | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113137_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113137_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113137_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113137_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113140_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113140_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113140_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113140_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113142_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113142_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113142_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113142_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113149_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113149_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113149_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113149_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113155_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113155_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113155_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113155_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113159_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113159_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113159_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113159_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113159-037` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113159-038` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113159-039` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113159-040` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113207_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113207_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113207_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113207_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113207_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113207_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113207_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113207_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113208_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113208_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113208_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113208_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113209_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113209_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113209_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113209_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113210_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113210_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113210_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113210_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113212_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113212_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113212_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113212_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113213_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113213_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113213_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113213_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113215_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113215_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113215_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113215_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113216_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113216_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113216_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113216_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113218_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113218_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113218_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113218_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113218-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113218-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113218-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113218-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113226_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113226_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113226_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113226_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113226_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113226_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113226_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113226_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113227_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113227_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113227_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113227_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113228_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113228_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113228_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113228_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113229_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113229_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113229_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113229_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113230_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113230_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113230_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113230_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113232_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113232_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113232_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113232_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113234_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113234_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113234_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113234_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113235_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113235_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113235_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113235_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113236_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113236_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113236_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113236_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113237-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113237-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113237-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113237-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113245_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113245_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113245_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113245_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113245_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113245_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113245_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113245_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113246_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113246_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113246_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113246_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113247_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113247_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113247_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113247_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113248_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113248_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113248_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113248_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113249_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113249_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113249_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113249_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113251_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113251_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113251_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113251_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113253_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113253_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113253_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113253_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113254_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113254_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113254_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113254_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113255_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113255_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113255_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113255_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113255-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113255-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113255-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113255-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113303_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113303_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113303_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113303_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113303_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113303_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113303_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113303_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113304_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113304_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113304_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113304_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113305_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113305_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113305_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113305_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113306_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113306_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113306_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113306_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113308_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113308_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113308_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113308_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113309_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113309_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113309_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113309_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113311_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113311_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113311_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113311_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113312_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113312_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113312_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113312_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113313_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113313_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113313_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113313_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113314-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113314-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113314-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113314-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113322_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113322_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113322_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113322_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113322_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113322_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113322_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113322_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113323_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113323_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113323_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113323_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113323_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113323_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113323_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113323_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113324_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113324_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113324_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113324_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113326_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113326_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113326_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113326_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113327_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113327_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113327_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113327_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113329_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113329_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113329_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113329_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113330_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113330_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113330_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113330_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113332_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113332_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113332_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113332_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113332-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113332-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113332-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113332-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: nbsp |
| `MISTAKE-LEARN-20261115_113340_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113340_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113340_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113340_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113340_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113340_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113340_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113340_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113341_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113341_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113341_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113341_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113341_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113341_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113341_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113341_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113342_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113342_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113342_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113342_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113344_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113344_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113344_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113344_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113345_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113345_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113345_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113345_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113347_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113347_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113347_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113347_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113348_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113348_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113348_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113348_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113350_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113350_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113350_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113350_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113350-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113350-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113350-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113350-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113358_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113358_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113358_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113358_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113358_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113358_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113358_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113358_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113359_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113359_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113359_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113359_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113400_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113400_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113400_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113400_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113401_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113401_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113401_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113401_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113402_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113402_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113402_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113402_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113404_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113404_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113404_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113404_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113407_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113407_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113407_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113407_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113408_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113408_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113408_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113408_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113409_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113409_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113409_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113409_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113409-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113409-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113409-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113409-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113417_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113417_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113417_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113417_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113417_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113417_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113417_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113417_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113418_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113418_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113418_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113418_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113419_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113419_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113419_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113419_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113420_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113420_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113420_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113420_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113422_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113422_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113422_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113422_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113423_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113423_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113423_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113423_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113425_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113425_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113425_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113425_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113426_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113426_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113426_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113426_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113428_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113428_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113428_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113428_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113428-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113428-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113428-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113428-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113436_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113436_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113436_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113436_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113436_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113436_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113436_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113436_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113437_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113437_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113437_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113437_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113438_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113438_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113438_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113438_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113439_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113439_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113439_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113439_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113440_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113440_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113440_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113440_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113442_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113442_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113442_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113442_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113444_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113444_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113444_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113444_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113445_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113445_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113445_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113445_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113446_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113446_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113446_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113446_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113447-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113447-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113447-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113447-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113455_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113455_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113455_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113455_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113455_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113455_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113455_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113455_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113456_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113456_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113456_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113456_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113457_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113457_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113457_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113457_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113458_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113458_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113458_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113458_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113459_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113459_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113459_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113459_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113501_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113501_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113501_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113501_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113503_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113503_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113503_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113503_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113504_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113504_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113504_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113504_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113505_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113505_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113505_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113505_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113505-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113505-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113505-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113505-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113514_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113514_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113514_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113514_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113514_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113514_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113514_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113514_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113515_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113515_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113515_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113515_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113516_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113516_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113516_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113516_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113517_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113517_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113517_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113517_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113518_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113518_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113518_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113518_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113520_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113520_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113520_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113520_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113522_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113522_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113522_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113522_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113523_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113523_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113523_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113523_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113524_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113524_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113524_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113524_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113524-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113524-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113524-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113524-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113532_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113532_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113532_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113532_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113533_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113533_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113533_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113533_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113534_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113534_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113534_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113534_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113535_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113535_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113535_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113535_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113536_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113536_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113536_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113536_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113537_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113537_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113537_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113537_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113539_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113539_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113539_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113539_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113541_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113541_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113541_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113541_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113542_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113542_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113542_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113542_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113543_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113543_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113543_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113543_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113544-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113544-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113544-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113544-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113552_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113552_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113552_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113552_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113552_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113552_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113552_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113552_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113553_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113553_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113553_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113553_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113554_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113554_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113554_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113554_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113555_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113555_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113555_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113555_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113557_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113557_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113557_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113557_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113558_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113558_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113558_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113558_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113600_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113600_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113600_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113600_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113601_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113601_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113601_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113601_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113602_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113602_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113602_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113602_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113603-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113603-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113603-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113603-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113611_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113611_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113611_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113611_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113611_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113611_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113611_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113611_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113612_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113612_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113612_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113612_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113613_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113613_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113613_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113613_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113614_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113614_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113614_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113614_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113616_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113616_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113616_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113616_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113617_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113617_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113617_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113617_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113619_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113619_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113619_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113619_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113620_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113620_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113620_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113620_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113621_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113621_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113621_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113621_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113622-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113622-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113622-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113622-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113630_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113630_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113630_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113630_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113630_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113630_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113630_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113630_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113631_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113631_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113631_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113631_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113632_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113632_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113632_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113632_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113632_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113632_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113632_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113632_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113634_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113634_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113634_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113634_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113635_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113635_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113635_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113635_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113637_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113637_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113637_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113637_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113638_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113638_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113638_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113638_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113640_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113640_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113640_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113640_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113640-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113640-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113640-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113640-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113648_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113648_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113648_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113648_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113649_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113649_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113649_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113649_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113650_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113650_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113650_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113650_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113651_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113651_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113651_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113651_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113652_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113652_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113652_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113652_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113654_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113654_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113654_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113654_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113655_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113655_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113655_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113655_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113657_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113657_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113657_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113657_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113658_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113658_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113658_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113658_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113700_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113700_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113700_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113700_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113700-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113700-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113700-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113700-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113708_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113708_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113708_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113708_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113708_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113708_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113708_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113708_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113709_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113709_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113709_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113709_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113710_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113710_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113710_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113710_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113711_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113711_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113711_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113711_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113712_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113712_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113712_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113712_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113714_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113714_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113714_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113714_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113716_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113716_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113716_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113716_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113717_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113717_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113717_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113717_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113718_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113718_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113718_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113718_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113719-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113719-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113719-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113719-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113727_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113727_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113727_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113727_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113727_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113727_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113727_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113727_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113728_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113728_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113728_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113728_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113729_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113729_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113729_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113729_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113730_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113730_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113730_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113730_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113731_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113731_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113731_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113731_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113733_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113733_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113733_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113733_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113735_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113735_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113735_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113735_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113736_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113736_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113736_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113736_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113737_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113737_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113737_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113737_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113737-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113737-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113737-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113737-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113745_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113745_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113745_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113745_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113745_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113745_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113745_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113745_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113746_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113746_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113746_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113746_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113747_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113747_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113747_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113747_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113748_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113748_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113748_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113748_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113750_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113750_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113750_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113750_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113752_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113752_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113752_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113752_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113754_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113754_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113754_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113754_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113755_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113755_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113755_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113755_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113756_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113756_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113756_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113756_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113756-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113756-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113756-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113756-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113804_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113804_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113804_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113804_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113804_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113804_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113804_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113804_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113805_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113805_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113805_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113805_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113806_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113806_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113806_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113806_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113807_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113807_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113807_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113807_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113809_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113809_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113809_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113809_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113810_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113810_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113810_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113810_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113812_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113812_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113812_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113812_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113813_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113813_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113813_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113813_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113815_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113815_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113815_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113815_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113815-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113815-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113815-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113815-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113823_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113823_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113823_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113823_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113823_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113823_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113823_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113823_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113824_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113824_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113824_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113824_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113825_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113825_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113825_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113825_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113826_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113826_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113826_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113826_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113827_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113827_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113827_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113827_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113829_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113829_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113829_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113829_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113831_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113831_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113831_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113831_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113832_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113832_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113832_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113832_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113833_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113833_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113833_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113833_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113833-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113833-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113833-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113833-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113841_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113841_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113841_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113841_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113841_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113841_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113841_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113841_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113842_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113842_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113842_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113842_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113843_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113843_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113843_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113843_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113844_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113844_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113844_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113844_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113846_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113846_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113846_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113846_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113847_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113847_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113847_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113847_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113849_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113849_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113849_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113849_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113850_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113850_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113850_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113850_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113851_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113851_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113851_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113851_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113852-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113852-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113852-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113852-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113859_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113859_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113859_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113859_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113900_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113900_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113900_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113900_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113901_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113901_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113901_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113901_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113901_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113901_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113901_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113901_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113902_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113902_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113902_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113902_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113904_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113904_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113904_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113904_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113905_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113905_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113905_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113905_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113907_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113907_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113907_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113907_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113908_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113908_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113908_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113908_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113909_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113909_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113909_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113909_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113910-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113910-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113910-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113910-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113918_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113918_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113918_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113918_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113918_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113918_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113918_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113918_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113919_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113919_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113919_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113919_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113920_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113920_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113920_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113920_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113921_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113921_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113921_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113921_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113922_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113922_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113922_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113922_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113924_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113924_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113924_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113924_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113926_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113926_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113926_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113926_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113927_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113927_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113927_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113927_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113928_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113928_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113928_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113928_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113929-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113929-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113929-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113929-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113937_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113937_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113937_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113937_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113937_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113937_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113937_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113937_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113938_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113938_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113938_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113938_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113939_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113939_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113939_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113939_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113940_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113940_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113940_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113940_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_113941_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113941_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113941_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113941_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113943_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113943_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113943_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113943_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113945_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113945_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113945_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113945_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113946_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113946_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113946_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113946_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113947_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113947_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113947_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113947_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113947-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113947-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113947-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_113947-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113957_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113957_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113957_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113957_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_113957_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113957_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113957_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113957_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113958_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113958_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113958_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113958_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113959_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113959_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113959_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_113959_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114000_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114000_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114000_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114000_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114002_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114002_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114002_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114002_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114003_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114003_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114003_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114003_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114005_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114005_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114005_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114005_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114006_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114006_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114006_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114006_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114007_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114007_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114007_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114007_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114008-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114008-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114008-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114008-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114016_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114016_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114016_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114016_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114016_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114016_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114016_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114016_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114017_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114017_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114017_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114017_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114018_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114018_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114018_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114018_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114019_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114019_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114019_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114019_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114021_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114021_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114021_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114021_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114022_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114022_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114022_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114022_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114024_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114024_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114024_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114024_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114025_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114025_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114025_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114025_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114027_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114027_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114027_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114027_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114027-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114027-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114027-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114027-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114035_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114035_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114035_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114035_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114035_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114035_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114035_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114035_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114037_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114037_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114037_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114037_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114038_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114038_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114038_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114038_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114039_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114039_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114039_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114039_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114040_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114040_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114040_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114040_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114041_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114041_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114041_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114041_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114043_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114043_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114043_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114043_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114044_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114044_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114044_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114044_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114046_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114046_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114046_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114046_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114046-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114046-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114046-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114046-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114054_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114054_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114054_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114054_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114054_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114054_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114054_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114054_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114055_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114055_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114055_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114055_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114056_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114056_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114056_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114056_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114057_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114057_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114057_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114057_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114058_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114058_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114058_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114058_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114100_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114100_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114100_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114100_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114102_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114102_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114102_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114102_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114103_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114103_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114103_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114103_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114104_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114104_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114104_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114104_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114105-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114105-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114105-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114105-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114113_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114113_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114113_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114113_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114113_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114113_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114113_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114113_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114114_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114114_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114114_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114114_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114115_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114115_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114115_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114115_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114116_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114116_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114116_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114116_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114117_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114117_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114117_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114117_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114119_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114119_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114119_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114119_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114120_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114121_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114121_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114121_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114122_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114122_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114122_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114122_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114123_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114123_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114123_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114123_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114123-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114123-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114123-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114123-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114131_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114131_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114131_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114131_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114131_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114131_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114131_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114131_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114132_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114132_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114132_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114132_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114133_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114133_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114133_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114133_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114134_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114134_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114134_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114134_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114135_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114135_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114135_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114135_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114137_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114137_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114137_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114137_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114139_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114139_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114139_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114139_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114141_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114141_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114141_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114141_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114142_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114142_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114142_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114142_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114142-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114142-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114142-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114142-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114150_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114150_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114150_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114150_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114150_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114150_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114150_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114150_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114152_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114152_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114152_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114152_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114153_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114153_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114153_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114153_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114154_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114154_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114154_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114154_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114155_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114155_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114155_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114155_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114157_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114157_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114157_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114157_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114159_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114159_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114159_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114159_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114200_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114200_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114200_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114200_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114201_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114201_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114201_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114201_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114202-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114202-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114202-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114202-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114210_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114210_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114210_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114210_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114210_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114210_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114210_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114210_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114211_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114211_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114211_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114211_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114212_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114212_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114212_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114212_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114213_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114213_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114213_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114213_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114214_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114214_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114214_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114214_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114216_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114216_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114216_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114216_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114217_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114217_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114217_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114217_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114218_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114218_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114218_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114218_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114220_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114220_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114220_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114220_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114220-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114220-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114220-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114220-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114228_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114228_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114228_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114228_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114228_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114228_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114228_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114228_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114230_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114230_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114230_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114230_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114231_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114231_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114231_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114231_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114232_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114232_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114232_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114232_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114233_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114233_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114233_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114233_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114235_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114235_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114235_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114235_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114236_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114236_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114236_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114236_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114237_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114237_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114237_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114237_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114239_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114239_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114239_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114239_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114239-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114239-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114239-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114239-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114247_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114247_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114247_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114247_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114247_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114247_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114247_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114247_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114248_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114248_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114248_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114248_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114249_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114249_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114249_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114249_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114250_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114250_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114250_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114250_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114251_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114251_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114251_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114252_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114253_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114253_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114253_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114253_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114255_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114255_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114255_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114255_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114256_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114256_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114256_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114256_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114258_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114258_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114258_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114258_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114258-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114258-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114258-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114258-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114306_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114306_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114306_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114306_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114306_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114306_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114306_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114306_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114307_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114307_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114307_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114307_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114308_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114308_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114308_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114308_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114309_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114309_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114309_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114309_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114311_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114311_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114311_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114311_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114312_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114312_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114312_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114312_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114314_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114314_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114314_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114314_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114315_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114315_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114315_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114315_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114317_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114317_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114317_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114317_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114317-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114317-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114317-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114317-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114325_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114325_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114325_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114325_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114325_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114325_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114325_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114325_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114326_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114326_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114326_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114326_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114327_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114327_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114327_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114327_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114328_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114328_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114328_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114328_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114330_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114330_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114330_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114330_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114331_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114331_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114331_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114331_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114333_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114333_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114333_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114333_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114334_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114334_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114334_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114334_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114336_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114336_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114336_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114336_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114336-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114336-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114336-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114336-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114344_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114344_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114344_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114344_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114344_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114344_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114344_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114344_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114345_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114345_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114345_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114345_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114346_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114346_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114346_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114346_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114347_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114347_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114347_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114347_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114349_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114349_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114349_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114349_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114350_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114350_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114350_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114350_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114352_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114352_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114352_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114352_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114353_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114353_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114353_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114353_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114355_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114355_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114355_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114355_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114355-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114355-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114355-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114355-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114404_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114404_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114404_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114404_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114404_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114404_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114404_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114404_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114405_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114405_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114405_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114405_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114406_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114406_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114406_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114406_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114407_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114407_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114407_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114407_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114408_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114408_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114408_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114408_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114410_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114410_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114410_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114410_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114412_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114412_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114412_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114412_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114413_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114413_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114413_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114413_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114414_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114414_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114414_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114414_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114415-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114415-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114415-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114415-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114423_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114423_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114423_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114423_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114423_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114423_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114423_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114423_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114424_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114424_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114424_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114424_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114425_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114425_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114425_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114425_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114426_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114426_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114426_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114426_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114428_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114428_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114428_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114428_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114429_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114429_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114429_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114429_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114431_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114431_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114431_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114431_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114432_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114432_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114432_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114432_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114434_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114434_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114434_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114434_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114434-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114434-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114434-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114434-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114442_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114442_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114442_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114442_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114442_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114442_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114442_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114442_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114443_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114443_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114443_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114443_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114444_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114444_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114444_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114444_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114445_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114445_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114445_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114445_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114446_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114446_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114446_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114446_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114448_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114448_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114448_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114448_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114450_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114450_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114450_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114450_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114451_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114451_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114451_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114451_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114452_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114452_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114452_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114452_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114453-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114453-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114453-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114453-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114501_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114501_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114501_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114501_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114501_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114501_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114501_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114501_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114502_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114502_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114502_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114502_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114503_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114503_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114503_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114503_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114504_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114504_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114504_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114504_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114505_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114505_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114505_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114505_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114507_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114507_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114507_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114507_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114509_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114509_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114509_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114509_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114510_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114510_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114510_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114510_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114511_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114511_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114511_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114511_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114512-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114512-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114512-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114512-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114520_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114520_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114520_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114520_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114520_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114520_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114520_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114520_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114521_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114521_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114521_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114521_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114522_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114522_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114522_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114522_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114523_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114523_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114523_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114523_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114524_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114524_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114524_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114524_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114525_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114525_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114525_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114525_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114527_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114527_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114527_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114527_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114528_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114528_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114528_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114528_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114530_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114530_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114530_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114530_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114530-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114530-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114530-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114530-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114538_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114538_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114538_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114538_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114538_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114538_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114538_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114538_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114539_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114539_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114539_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114539_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114540_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114540_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114540_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114540_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114541_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114541_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114541_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114541_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114542_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114542_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114542_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114542_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114544_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114544_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114544_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114544_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114546_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114546_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114546_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114546_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114547_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114547_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114547_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114547_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114548_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114548_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114548_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114548_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114549-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114549-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114549-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114549-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114557_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114557_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114557_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114557_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114557_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114557_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114557_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114557_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114558_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114558_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114558_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114558_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114558_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114558_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114558_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114558_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114559_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114559_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114559_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114559_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114601_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114601_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114601_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114601_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114603_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114603_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114603_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114603_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114605_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114605_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114605_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114605_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114606_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114606_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114606_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114606_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114607_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114607_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114607_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114607_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114607-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114607-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114607-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114607-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114616_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114616_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114616_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114616_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114616_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114616_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114616_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114616_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114617_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114617_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114617_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114617_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114618_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114618_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114618_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114618_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114619_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114619_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114619_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114619_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114621_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114621_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114621_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114621_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114622_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114622_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114622_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114622_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114624_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114624_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114624_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114624_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114625_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114625_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114625_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114625_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114626_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114626_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114626_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114626_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114627-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114627-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114627-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114627-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114635_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114635_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114635_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114635_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114635_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114635_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114635_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114635_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114636_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114636_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114636_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114636_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114637_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114637_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114637_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114637_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114638_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114638_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114638_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114638_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114640_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114640_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114640_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114640_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114641_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114641_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114641_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114641_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114643_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114643_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114643_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114643_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114644_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114644_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114644_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114644_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114646_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114646_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114646_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114646_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114646-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114646-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114646-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114646-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114655_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114655_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114655_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114655_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114656_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114656_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114656_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114656_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114658_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114658_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114658_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114658_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114659_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114659_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114659_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114659_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114659_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114659_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114659_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114659_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114701_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114701_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114701_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114701_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114703_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114703_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114703_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114703_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114705_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114705_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114705_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114705_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114705_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114705_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114705_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114705_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114707_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114707_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114707_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114707_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114708-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114708-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114708-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114708-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114716_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114716_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114716_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114716_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114716_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114716_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114716_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114716_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114717_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114717_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114717_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114717_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114718_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114718_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114718_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114718_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114719_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114719_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114719_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114719_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114721_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114721_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114721_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114721_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114722_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114722_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114722_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114722_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114724_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114724_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114724_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114724_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114726_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114726_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114726_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114726_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114727_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114727_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114727_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114727_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114727-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114727-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114727-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114727-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114736_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114736_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114736_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114736_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114736_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114736_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114736_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114736_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114738_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114738_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114738_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114738_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114738_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114738_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114738_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114738_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114739_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114739_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114739_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114739_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114741_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114741_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114741_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114741_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114742_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114742_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114742_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114742_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114744_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114744_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114744_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114744_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114745_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114745_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114745_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114745_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114747_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114747_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114747_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114747_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114747-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114747-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114747-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114747-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114756_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114756_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114756_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114756_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114756_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114756_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114756_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114756_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114757_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114757_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114757_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114757_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114757_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114757_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114757_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114757_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114759_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114759_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114759_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114759_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114800_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114800_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114800_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114800_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114802_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114802_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114802_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114802_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114804_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114804_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114804_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114804_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114805_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114805_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114805_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114805_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114807_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114807_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114807_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114807_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114807-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114807-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114807-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114807-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114816_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114816_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114816_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114816_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114816_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114816_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114816_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114816_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114817_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114817_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114817_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114817_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114818_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114818_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114818_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114818_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114819_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114819_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114819_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114819_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114820_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114820_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114820_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114820_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114822_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114822_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114822_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114822_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114823_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114823_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114823_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114823_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114824_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114824_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114824_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114824_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114826_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114826_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114826_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114826_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114826-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114826-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: nbsp |
| `SCRAPED-2026_11_15_114826-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114826-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114835_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114835_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114835_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114835_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114835_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114835_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114835_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114835_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114836_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114836_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114836_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114836_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114837_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114837_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114837_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114837_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114838_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114838_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114838_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114838_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114840_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114840_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114840_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114840_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114842_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114842_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114842_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114842_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114844_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114844_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114844_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114844_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114845_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114845_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114845_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114845_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114846_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114846_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114846_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114846_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114847-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114847-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114847-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114847-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114855_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114855_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114855_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114855_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114855_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114855_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114855_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114855_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114856_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114856_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114856_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114856_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114857_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114857_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114857_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114857_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114858_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114858_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114858_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114858_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114900_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114900_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114900_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114900_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114901_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114901_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114901_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114901_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114903_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114903_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114903_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114903_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114904_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114904_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114904_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114904_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114906_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114906_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114906_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114906_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114906-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114906-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114906-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114906-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114915_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114915_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114915_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114915_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114915_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114915_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114915_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114915_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114916_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114916_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114916_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114916_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114917_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114917_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114917_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114917_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114918_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114918_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114918_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114918_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114919_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114919_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114919_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114919_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114921_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114921_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114921_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114921_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114923_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114923_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114923_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114923_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114925_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114925_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114925_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114925_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114926_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114926_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114926_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114926_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114926-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114926-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114926-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'করে' ব্যবহার করা হয়েছে। |
| `SCRAPED-2026_11_15_114926-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114934_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114934_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114934_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114934_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114935_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114935_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114935_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114935_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114936_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114936_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114936_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114936_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114937_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114937_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114937_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114937_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114938_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_114938_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114938_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114938_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114939_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114939_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114939_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114939_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114941_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114941_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114941_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114941_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114942_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114942_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114942_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114942_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114943_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114943_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114943_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114943_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114945_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114945_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114945_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114945_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114945-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114945-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114945-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_114945-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_114954_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114954_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114955_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114955_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114955_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114955_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114957_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114957_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114957_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114957_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114958_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114958_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114958_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114958_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114959_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114959_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114959_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_114959_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115001_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115001_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115001_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115001_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115002_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115002_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115002_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115002_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115004_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115004_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115004_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115004_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115004-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115004-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115004-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115004-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115012_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115012_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115012_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115012_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115012_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115012_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115012_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115012_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115013_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115013_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115013_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115013_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115014_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115014_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115014_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115014_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115015_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115015_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115015_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115015_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115017_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115017_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115017_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115017_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115018_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115018_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115018_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115018_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115020_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115020_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115020_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115020_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115022_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115022_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115022_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115022_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115023_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115023_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115023_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115023_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115023-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115023-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115023-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115023-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115032_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115032_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115032_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115032_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115032_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115032_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115032_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115032_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115033_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115033_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115033_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115033_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115034_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115034_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115034_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115034_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115035_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115035_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115035_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115035_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115037_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115037_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115037_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115037_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115038_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115038_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115038_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115038_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115040_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115040_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115040_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115040_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115042_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115042_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115042_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115042_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115043_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115043_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115043_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115043_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115044-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115044-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115044-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115044-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115052_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115052_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115052_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115052_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115052_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115052_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115052_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115052_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115053_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115053_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115053_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115053_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115054_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115054_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115054_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115054_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115055_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115055_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115055_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115055_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115057_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115057_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115057_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115057_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115058_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115058_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115058_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115058_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115100_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115100_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115100_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115100_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115102_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115102_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115102_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115102_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115102_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115102_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115102_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115102_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115103-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115103-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115103-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115103-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115111_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115111_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115111_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115111_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115112_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115112_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115112_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115112_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115113_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115113_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115113_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115113_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115114_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115114_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115114_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115114_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115115_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115115_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115115_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115115_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115116_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115116_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115116_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115116_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115118_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115118_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115118_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115118_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115120_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115120_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115120_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115120_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115121_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115121_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115121_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115121_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115123_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115123_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115123_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115123_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115123-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115123-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115123-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115123-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115132_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115132_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115132_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115132_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115132_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115132_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115132_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115132_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115133_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115133_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115133_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115133_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115133_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115133_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115133_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115133_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115134_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115134_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115134_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115134_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115136_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115136_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115136_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115136_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115137_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115137_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115137_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115137_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115140_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115140_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115140_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115140_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115141_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115141_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115141_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115141_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115142_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115142_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115142_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115142_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115143-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115143-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115143-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115143-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `ANOMALY_CANDIDATE` | `1` | অস্বাভাবিক কাঁচা ইংরেজি শব্দ পাওয়া গেছে: nbsp |
| `MISTAKE-LEARN-20261115_115151_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115151_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115151_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115151_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115151_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115151_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115151_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115151_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115152_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115152_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115152_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115152_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115153_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115153_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115153_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115153_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115154_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115154_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115154_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115154_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115156_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115156_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115156_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115156_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115157_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115157_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115157_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115157_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115159_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115159_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115159_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115159_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115201_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115201_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115201_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115201_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115202_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115202_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115202_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115202_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115202-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115202-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115202-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115202-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115211_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115211_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115211_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115211_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115212_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115212_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115212_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115212_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115213_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115213_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115213_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115213_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115214_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115214_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115214_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115214_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115215_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115215_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115215_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115215_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115216_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115216_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115216_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115216_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115218_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115218_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115218_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115218_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115219_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115219_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115219_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115219_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115220_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115220_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115220_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115220_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115222_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115222_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115222_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115222_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115223-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115223-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115223-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115223-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115231_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115231_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115231_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115231_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115231_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115231_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115231_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115231_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115232_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115232_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115232_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115232_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115233_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115233_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115233_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115233_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115234_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115234_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115234_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115234_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115236_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115236_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115236_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115236_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115237_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115237_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115237_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115237_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115239_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115239_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115239_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115239_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115240_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115240_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115240_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115240_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115242_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115242_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115242_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115242_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115242-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115242-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115242-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115242-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115251_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115251_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115251_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115251_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115251_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115251_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115251_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115251_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115252_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115252_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115252_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115252_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115253_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115253_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115253_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115253_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115254_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115254_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115254_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115254_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115255_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115255_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115255_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115255_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115256_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115256_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115256_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115256_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115258_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115258_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115258_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115258_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115300_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115300_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115300_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115300_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115301_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115301_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115301_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115301_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115301-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115301-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115301-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115301-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115310_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115310_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115310_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115310_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115310_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115310_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115310_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115310_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115311_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115311_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115311_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115311_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115312_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115312_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115312_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115312_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115313_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115313_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115313_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115313_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115315_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115315_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115315_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115315_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115316_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115316_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115316_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115316_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115318_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115318_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115318_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115318_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115319_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115319_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115319_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115319_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115321_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115321_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115321_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115321_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115321-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115321-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115321-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115321-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115330_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115330_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115330_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115330_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115330_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115330_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115330_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115330_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115331_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115331_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115331_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115331_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115332_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115332_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115332_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115332_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115333_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115333_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115333_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115333_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115334_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115334_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115334_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115334_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115336_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115336_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115336_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115336_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115338_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115338_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115338_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115338_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115339_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115339_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115339_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115339_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115340_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115340_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115340_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115340_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115341-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115341-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115341-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115341-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115349_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115349_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115349_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115349_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115349_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115349_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115349_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115349_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115350_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115350_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115350_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115350_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115351_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115351_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115351_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115351_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115352_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115352_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115352_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115352_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115354_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115354_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115354_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115354_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115355_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115355_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115355_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115355_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115357_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115357_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115357_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115357_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115358_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115358_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115358_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115358_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115359_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115359_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115359_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115359_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115400-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115400-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115400-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115400-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115408_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115408_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115408_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115408_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115408_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115408_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115408_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115408_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115409_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115409_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115409_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115409_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115410_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115410_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115410_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115410_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115411_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115411_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115411_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115411_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115412_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115412_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115412_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115412_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115413_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115413_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115413_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115413_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115415_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115415_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115415_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115415_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115416_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115416_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115416_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115416_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115417_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115417_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115417_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115417_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115418-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115418-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115418-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115418-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115426_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115426_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115426_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115426_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115426_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115426_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115426_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115426_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115427_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115427_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115427_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115427_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115428_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115428_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115428_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115428_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115429_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115429_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115429_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115429_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115430_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115430_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115430_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115430_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115432_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115432_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115432_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115432_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115434_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115434_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115434_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115434_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115435_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115435_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115435_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115435_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115436_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115436_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115436_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115436_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115437-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115437-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115437-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115437-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115445_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115445_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115445_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115445_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115445_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115445_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115445_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115445_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115446_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115446_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115446_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115446_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115447_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115447_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115447_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115447_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115448_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115448_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115448_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115448_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115449_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115449_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115449_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115449_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115451_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115451_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115451_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115451_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115452_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115452_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115452_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115452_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115454_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115454_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115454_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115454_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115455_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115455_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115455_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115455_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115455-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115455-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115455-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115455-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115503_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115503_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115503_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115503_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115503_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115503_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115503_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115503_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115504_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115504_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115504_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115504_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115505_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115505_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115505_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115505_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115506_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115506_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115506_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115506_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115508_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115508_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115508_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115508_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115510_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115510_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115510_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115510_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115511_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115511_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115511_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115511_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115512_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115512_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115512_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115512_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115514_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115514_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115514_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115514_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115514-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115514-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115514-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115514-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115523_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115523_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115523_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115523_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115523_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115523_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115523_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115523_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115524_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115524_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115524_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115524_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115525_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115525_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115525_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115525_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115526_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115526_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115526_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115526_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115527_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115527_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115527_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115527_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115529_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115529_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115529_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115529_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115531_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115531_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115531_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115531_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115532_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115532_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115532_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115532_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115533_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115533_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115533_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115533_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115534-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115534-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115534-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115534-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115543_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115543_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115543_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115543_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115543_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115543_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115543_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115543_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115544_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115544_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115544_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115544_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115545_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115545_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115545_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115545_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115546_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115546_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115546_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115546_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115547_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115547_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115547_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115547_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115549_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115549_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115549_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115549_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115551_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115551_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115551_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115551_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115551_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115551_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115551_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115551_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115553_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115553_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115553_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115553_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115554-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115554-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115554-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115554-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115602_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115602_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115602_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115602_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115602_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115602_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115602_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115602_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115603_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115603_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115603_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115603_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115605_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115605_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115605_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115605_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115606_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115606_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115606_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115606_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115607_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115607_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115607_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115607_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115609_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115609_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115609_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115609_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115611_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115611_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115611_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115611_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115612_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115612_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115612_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115612_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115614_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115614_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115614_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115614_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115614-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115614-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115614-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115614-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115623_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115623_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115623_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115623_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115623_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115623_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115623_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115623_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115624_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115624_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115624_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115624_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115625_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115625_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115625_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115625_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115626_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115626_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115626_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115626_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115628_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115628_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115628_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115628_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115630_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115630_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115630_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115630_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115632_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115632_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115632_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115632_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115633_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115633_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115633_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115633_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115635_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115635_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115635_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115635_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115635-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115635-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115635-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115635-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115644_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115644_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115644_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115644_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115644_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115644_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115644_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115644_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115645_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115645_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115645_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115645_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115646_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115646_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115646_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115646_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115647_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115647_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115647_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115647_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115648_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115648_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115648_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115648_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115650_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115650_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115650_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115650_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115652_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115652_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115652_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115652_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115653_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115653_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115653_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115653_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115655_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115655_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115655_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115655_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115656-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115656-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115656-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115656-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115703_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115703_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115703_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115703_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115703_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115703_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115703_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115703_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115705_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115705_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115705_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115705_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115706_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115706_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115706_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115706_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115707_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115707_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115707_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115707_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115708_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115708_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115708_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115708_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115710_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115710_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115710_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115710_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115712_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115712_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115712_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115712_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115713_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115713_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115713_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115713_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115714_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115714_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115714_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115714_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115715-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115715-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115715-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115715-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115723_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115723_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115723_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115723_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115723_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115723_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115723_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115723_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115724_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115724_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115724_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115724_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115725_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115725_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115725_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115725_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115726_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115726_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115726_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115726_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115727_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115727_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115727_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115727_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115729_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115729_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115729_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115729_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115731_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115731_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115731_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115731_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115732_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115732_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115732_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115732_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115733_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115733_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115733_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115733_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115734-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115734-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115734-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115734-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115742_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115742_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115742_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115742_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115742_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115742_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115742_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115742_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115743_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115743_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115743_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115743_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115744_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115744_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115744_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115744_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115745_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115745_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115745_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115745_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115747_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115747_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115747_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115747_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115748_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115748_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115748_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115748_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115750_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115750_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115750_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115750_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115751_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115751_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115751_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115751_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115753_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115753_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115753_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115753_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115753-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115753-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115753-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115753-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115802_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115802_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115802_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115802_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115802_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115802_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115802_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115802_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115803_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115803_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115803_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115803_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115804_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115804_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115804_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115804_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115805_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115805_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115805_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115805_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115807_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115807_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115807_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115807_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115808_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115808_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115808_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115808_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115810_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115810_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115810_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115810_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115811_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115811_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115811_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115811_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115813_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115813_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115813_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115813_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115813-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115813-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115813-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115813-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115821_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115821_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115821_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115821_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115821_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115821_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115821_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115821_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115822_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115822_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115822_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115822_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115823_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115823_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115823_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115823_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115824_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115824_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115824_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115824_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115826_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115826_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115826_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115826_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115827_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115827_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115827_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115827_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115829_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115829_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115829_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115829_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115830_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115830_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115830_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115830_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115831_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115831_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115831_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115831_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115832-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115832-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115832-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115832-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115840_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115840_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115840_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115840_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115840_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115840_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115840_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115840_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115842_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115842_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115842_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115842_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115843_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115843_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115843_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115843_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115844_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115844_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115844_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115844_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115845_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115845_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115845_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115845_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115847_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115847_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115847_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115847_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115848_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115848_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115848_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115848_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115849_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115849_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115849_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115849_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115851_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115851_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115851_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115851_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115851-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115851-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115851-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115851-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115859_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115859_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115859_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115859_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115859_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115859_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115859_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115859_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115900_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115900_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115900_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115900_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115901_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115901_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115901_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115901_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115902_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115902_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115902_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115902_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115904_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115904_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115904_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115904_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115905_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115905_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115905_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115905_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115907_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115907_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115907_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115907_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115908_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115908_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115908_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115908_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115910_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115910_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115910_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115910_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115910-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115910-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115910-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115910-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115918_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115918_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115918_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115918_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115918_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115918_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115918_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115918_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115919_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115919_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115919_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115919_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115920_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115920_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115920_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115920_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115921_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115921_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115921_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115921_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115923_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115923_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115923_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115923_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115924_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115924_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115924_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115924_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115926_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115926_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115926_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115926_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115927_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115927_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115927_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115927_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115929_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115929_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115929_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115929_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115929-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115929-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115929-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115929-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115937_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115937_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115937_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115937_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115937_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115937_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115937_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115937_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115938_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115938_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115938_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115938_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115940_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115940_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115940_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115940_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115941_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115941_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115941_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_115941_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115942_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115942_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115942_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115942_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115944_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115944_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115944_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115944_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115946_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115946_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115946_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115946_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115947_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115947_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115947_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115947_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115948_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115948_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115948_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115948_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115948-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115948-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115948-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_115948-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115957_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115957_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_115957_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115957_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115957_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115957_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115957_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115957_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115958_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115958_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115958_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115958_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115959_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115959_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115959_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_115959_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120000_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120000_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_120000_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120000_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120001_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120001_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120001_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120001_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120003_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120003_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120003_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120003_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120005_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120005_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120005_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120005_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120006_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120006_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120006_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120006_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120007_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120007_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120007_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120007_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120008-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120008-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120008-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120008-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120016_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120016_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120016_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120016_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120016_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120016_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120016_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120016_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120017_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120017_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120017_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120017_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120018_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120018_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120018_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120018_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120019_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_120019_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120019_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120019_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `CANARY_TRAPPED` | `1` | তৃতীয় পুরুষ সর্বনাম ও ক্রিয়াপদের সঙ্গতিহীনতা: 'তিনি' (সম্ভ্রমাত্মক) এর সাথে সাধারণ ক্রিয়াপদ 'হয়েছে' ব্যবহার করা হয়েছে। |
| `MISTAKE-LEARN-20261115_120020_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120020_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120020_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120020_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120021_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120021_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120021_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120021_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120023_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120023_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120023_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120023_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120024_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120024_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120024_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120024_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120026_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120026_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120026_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120026_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120026-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120026-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120026-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120026-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120034_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120034_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120034_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120034_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120034_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120034_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120034_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120034_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120035_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120035_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120035_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120035_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120036_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120036_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120036_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120036_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120037_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120037_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120037_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120037_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120039_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120039_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120039_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120039_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120040_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120040_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120040_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120040_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120042_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120042_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120042_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120042_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120043_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120043_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120043_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120043_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120045_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120045_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120045_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120045_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120045-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120045-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120045-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120045-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120053_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120053_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120053_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120053_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120053_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120053_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120053_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120053_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120054_7-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120054_7-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120054_7-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120054_7-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120055_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120055_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120055_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120055_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120056_5-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120056_5-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120056_5-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120056_5-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120057_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120057_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120057_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120057_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120059_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120059_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120059_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120059_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120100_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120100_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120100_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120100_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120101_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120101_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120101_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120101_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120103_4-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120103_4-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120103_4-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120103_4-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120103-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120103-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120103-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120103-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120111_8-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120111_8-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120111_8-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120111_8-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Academic Research & Methodology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120111_9-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120111_9-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120111_9-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120111_9-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Administrative Governance & Memos | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120113_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120113_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120113_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120113_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Agronomy & Disaster Management | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120114_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120114_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120114_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120114_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Classical Poetry & Prosody | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120115_2-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120115_2-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120115_2-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120115_2-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Creative Fiction & Dialogue | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120116_6-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120116_6-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120116_6-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120116_6-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Education & NCTB Pedagogy | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120118_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120118_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120118_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `CANARY_TRAPPED` | `1` | গুরুচণ্ডালী দোষ: একই বাক্যে সাধু রূপ ('হইয়াছে') ও চলিত রীতির মিশ্রণ ঘটেছে। |
| `MISTAKE-LEARN-20261115_120118_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Healthcare & Epidemiology | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120120_3-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120120_3-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120120_3-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120120_3-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | ICT & Software Engineering | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120121_0-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120121_0-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120121_0-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120121_0-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Land Registry & Deeds | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120122_1-01` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120122_1-02` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120122_1-03` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `MISTAKE-LEARN-20261115_120122_1-04` | Learning from Mistakes Engine (Offline Autonomous Synthesis) | Constitutional Law & Writs | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120122-041` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120122-042` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120122-043` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
| `SCRAPED-2026_11_15_120122-044` | Prothom Alo (National & Economy) | Macroeconomics & Banking | `BENCHMARK_CLEAN` | `0` | ✓ 100% Clean Authentic Bengali |
