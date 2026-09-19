# roles/expanded_publication_methods.md — ATD-ANC-R2-Publication（evidence methods／case-report reviewer）

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

本檔僅由本 session 擁有並寫入；`sessions/messages/r2_publication_dialogue.md` 同屬本 session。未讀取 `private/*`（MCP config 讀取除外）或任何原始病歷檔；本文件不含病歷號、確切就醫日期或醫護人員／院所名稱，僅用 `research/case_synopsis.md` 之 Day 相對編號。臨床建議一律 conditional，不做個別劑量調整。

## ACK

已讀取：`CLAUDE.md`、`research/case_synopsis.md`、`research/retrieval_report.md`、`research/independent_bridge_audit.md`、前一輪（ATD-ANC-R1）之 `roles/endocrinology.md`、`roles/hematology.md`、`roles/methods.md`、`roles/nuclear_surgery.md`（作為既有研究稽核紀錄，非本輪 peer 正文）、`literature/knight2017.md` 全文。本輪（ATD-ANC-R2）同儕 `roles/expanded_case_diagnosis.md`、`roles/expanded_drug_safety.md`、`roles/expanded_definitive_therapy.md` 於本檔撰寫時尚未存在或尚未完成，故未能讀取其正文；本檔之 Peer Review 部分留待未來讀取後補充，不臆測其內容。已執行 `ListAgents` 並對 `ATD-ANC-R2-Definitive`、`ATD-ANC-R2-CaseDx` 送出 CHALLENGE，逐字紀錄於 `sessions/messages/r2_publication_dialogue.md`。本輪為新查詢，用去識別化通用臨床詞彙（agranulocytosis、heart failure、thyroidectomy、pneumonia、lithium、radioiodine washout 等），未含病人特徵；使用 `mcp__paper-search__search_pubmed`／`search_europepmc`。

## Role / Scope

Evidence methods 與 case-report 可投稿性稽核者：(1) 以實際一手 case report／series 建立 comparator 表，判斷本案是否構成獨立臨床決策問題；(2) 套用 CARE checklist 與同意／隱私要求；(3) 列出投稿前最低限度待補資訊；(4) 提出 case-report thesis 與兩種替代可投稿格式；(5) 對 Definitive／CaseDx 角色送出 CHALLENGE，測試 comparability 與是否過度宣稱新意。不做確定性治療建議、不竄改他人角色檔、不執行 git/config 操作。

---

## 一、Comparator 表：Agranulocytosis + 心臟／肺部器官限制 + non-thionamide bridge + definitive therapy

本表僅納入本 session 已取得摘要或全文、且能列出精確 locator 之一手個案；**本次為目標式檢索（targeted retrieval），非完整 systematic review，不宣稱窮盡所有已發表個案**。

| 個案 | 設計／n | Bridge（非 thionamide） | 器官限制 | Definitive therapy | 結局 | 限制 |
|---|---|---|---|---|---|---|
| **Voci et al. 2026** | Case report, n=1 | Lugol's iodine + G-CSF | Decompensated HFrEF（EF 35%）+ COPD；methimazole 與 PTU 均已致 agranulocytosis（ANC 180／190/µL） | Total thyroidectomy（right heart catheterization 確認手術適合度後） | 未在摘要中載明長期追蹤細節（僅摘要層級，全文未取得） | **本案最接近之 comparator**：涵蓋「agranulocytosis + 低 EF 心衰竭 + surgery」，但**未見肺炎、未見 AKI／含碘顯影劑 washout 交織 RAI 時程之軸線**，亦未使用 lithium。僅讀取摘要，未取得全文，OPEN-PUB-A。 |
| **Knight et al. 2017** | Case report, n=1 | Lugol's iodine + cholestyramine + propranolol + lithium（9 天） | 無心衰竭記錄（ECG 排除 AF，未提供 EF）；有 sepsis（MSSA 頸部潰瘍＋鼻竇炎，非肺炎） | Total thyroidectomy（術中仍 biochemically thyrotoxic：T4 31.9、T3 11.8 pmol/L） | 無併發症；9 個月追蹤 TSH 4.0、T4 13.1 pmol/L，euthyroid on thyroxine | 全文已核對（本 session 直接讀取）。作者自陳「limited available evidence…unique cohort」，**不建立通用生化安全切點**；無肺炎、無 AKI／contrast 軸線。 |
| **Gad et al. 2026** | Case report, n=1 | Steroid／cholestyramine（效果有限）＋ 術前 Lugol 7 天 | 未知（本 session 僅取得二手稽核備忘，未親自讀全文）| Thyroidectomy | 未知 | **作者 learning point 稱 surgery 為唯一選項，經前一輪 nuclear_surgery 稽核判定為過度概括，不應採用**；本 session 未獨立核對全文，OPEN-PUB-B。 |
| **Fredette et al. 2025（pediatric）** | Case report, n=1（17 歲女性） | SSKI 29 天＋β-blockade＋cholestyramine＋G-CSF | Septic shock；無 HF／AKI 記錄 | 摘要未載明最終 definitive therapy（review 型文章，聚焦 bridge 選項本身） | 未知（僅摘要層級） | **兒科族群，不可直接外推成人**；definitive therapy 結局未在摘要呈現，OPEN-PUB-C。 |
| **Rami et al. 2024（Case 2 of series）** | Case report／series 內 case, n=1（引自前一輪稽核備忘） | 多種 bridge 嘗試後 uncontrolled；2 次 TPE | Septic shock；**echo 正常（無心衰竭）** | Thyroidectomy | 未知細節 | 本 session 未親自讀取原文，屬二手轉引，OPEN-PUB-D。與本案不同之處在於此案 echo 正常，非低 EF。 |
| **Guvenc et al. 2004** | Case report, n=1（摘要層級） | 3 次 plasmapheresis | PTU agranulocytosis + **clinical heart failure**（摘要未提供 EF 數值） | 摘要未載明是否完成 thyroidectomy 或 RAI | 「thyroid hormones／clinical findings 改善」（摘要用語，非確定 definitive therapy 結局） | **不可由摘要宣稱已完成任一 definitive therapy**；bridge 為 TPE，非 iodide／lithium，與本案機轉不同。OPEN-PUB-E。 |
| **Calissendorff & Falhammar 2017** | Retrospective series, n=27（agranulocytosis 用 Lugol 者 9 人） | Lugol's solution | 未依病人逐一報告心肺腎狀態（series 層級，本 session 無法拆解個別病人器官限制） | 26/27 thyroidectomy；1/27 RAI（該病人僅用 Lugol 3 天，非 3 天 washout） | 短期 FT4/FT3、HR 下降 | Series 層級資料，**無法作為個別病人器官限制之 comparator**，僅供「Lugol 後仍可 RAI」之方向性佐證。 |
| **Sazon et al. 2024** | **Conference abstract**, n=1 | Lithium + prednisone | 未知（摘要未提供心肺腎狀態） | RAI 24 mCi | 4 週後 hypothyroidism，開始 levothyroxine | **僅會議摘要，非完整同儕審查 case report**；是本 session 找到之少數「lithium bridge → RAI（非 surgery）」個案，但無法核對器官限制細節，亦不能作為完整方法學依據，OPEN-PUB-F。 |
| **Fahmi et al. 2026** | Conference abstract, n=1 | Cholestyramine + lithium | 未知 | 病人選擇 RAI（未確認已完成／結局） | ANC 0.97–1.46×10⁹/L | **此為 neutropenia（未達 agranulocytosis <0.5×10⁹/L 之公認切點），不應與 agranulocytosis 案例並列比較風險等級**，僅供 bridge 藥物組合之方向性參考。 |

### 整合判讀
現有已核對之一手／半核對資料中，**沒有任何單一個案同時涵蓋**：(a) HFrEF、(b) 需要定期影像追蹤之 necrotizing／near-abscess pneumonia、(c) 同日含碘顯影劑暴露與腎功能變化、且注射與抽血先後未核實，因而影響 EANM iodine washout 前提判讀、(d) Lugol 與 lithium 兩種 non-thionamide bridge 的處方紀錄（實際給藥仍待核）、(e) 甲狀腺結節缺 FNA 而需納入 definitive therapy 範圍決策。**此為本次目標式檢索之發現，不等於已進行窮盡性系統性文獻回顧確認之結論**；投稿前需由更廣泛之系統性檢索（見下方 OPEN 清單）驗證是否已有本 session 未檢出之近似個案。

---

## 二、新意（Novelty）評估：獨立臨床決策問題 vs. 既有組合之延伸

**不宣稱 first／unique。** 依上表，本案與 Voci et al. 2026 共享「agranulocytosis + 低 EF 心衰竭 + definitive therapy 決策」此一骨幹，**此組合本身已有至少一篇 2026 年發表之個案報告，故不能以此組合單獨主張新意**。

本案潛在可主張之獨立貢獻，若要成立，應精確定位於：**「當 surgery 與 RAI 兩條路徑同時存在各自未解決之前提條件（surgery 端：低 EF＋肺部感染尚未完全清除；RAI 端：近期 AKI 使含碘顯影劑 6–8 週 washout 前提是否成立無法單純以日曆天數判斷，且甲狀腺結節缺 FNA 增加手術範圍決策之複雜度）時，臨床團隊如何在缺乏兩條路徑皆已就緒的情況下做出決策」**——此為決策時序與多重器官限制交織之問題，而非單一 bridge 藥物或單一 definitive therapy 的成功案例報告。此一框架與 Voci 2026（僅心臟軸線、經 right heart catheterization 確認手術可行後即執行手術，未見路徑間衝突之描述）及 Knight 2017（無心衰竭、無 AKI／contrast 軸線）均不相同。

**此新意主張目前為本 session 之研究判讀，尚未經 ATD-ANC-R2-Definitive 或 ATD-ANC-R2-CaseDx 兩位同儕確認**；已就此送出 CHALLENGE-publication-001（→ Definitive，見對話檔），截至本檔完成時**未收到回覆，維持 OPEN-PUB-001**。在收到跨角色確認前，本檔不將此新意主張視為已收斂之結論。

---

## 三、CARE checklist 套用與同意／隱私要求

依 Gagnier et al. 2013（CARE guidelines: consensus-based clinical case reporting guideline development，*BMJ Case Reports*，DOI [10.1136/bcr-2013-201554](https://doi.org/10.1136/bcr-2013-201554)，PMID [24155002](https://pubmed.ncbi.nlm.nih.gov/24155002/)；亦同步刊登於其他期刊，如 DOI 10.1016/j.jclinepi.2013.08.003）之 13 項清單，逐項比對本案現有資料：

| CARE Item | 現況 | 缺口 |
|---|---|---|
| 1. Title | 未定案 | 待第五節 thesis 確認 |
| 2. Key words | 未定案 | — |
| 3. Abstract | 未撰寫 | 待其餘項目補齊後撰寫 |
| 4. Introduction | 可依既有文獻脈絡撰寫 | 需先解決第二節新意主張之 OPEN |
| 5. Patient Information | 已去識別化（Day-relative），**性別／年齡層級細節足夠但需最終確認出版前之可識別性審查** | 待病人知情同意 |
| 6. Clinical Findings | 大致可用 case_synopsis.md 現有資料 | BWPS 組成、ACTH 採檢時間點需補 |
| 7. Timeline | **明確缺口**：carbimazole 停藥 Day 47 vs 48 未解決；急診／會診心率體溫不可拼接同一時間點 | 需原始病歷時間戳記逐一核對或如實呈現差異 |
| 8. Diagnostic Assessment | TRAb 3.00 於支持而非確診等級；甲狀腺結節缺 FNA | 需 FNA／病理（若手術）或至少影像科複閱原始影像 |
| 9. Therapeutic Intervention | 現有僅 mL 劑量之 Lugol、無濃度；carbimazole／allopurinol 起訖不明；G-CSF／lithium／steroid 給藥細節不全 | **需完整 medication administration record** |
| 10. Follow-up and Outcomes | **最大缺口**：無最終 definitive therapy 執行紀錄、無出院後 thyroid／heart／lung 結局 | 需等待臨床實際進展 |
| 11. Discussion | 可依本檔 comparator 表與新意評估撰寫（待跨角色確認後） | — |
| 12. Patient Perspective | **完全缺失**：case_synopsis.md 未見病人自述之症狀經驗或治療偏好之正式段落（僅載「病人仍考慮」手術） | 需正式訪談或至少病歷中病人自述段落 |
| 13. Informed Consent | **未確認**：case_synopsis.md 明載「投稿前另需病人知情同意與可識別細節審查」，尚未執行 | 投稿前必要條件，不可省略 |

**同意／隱私額外要求**：(a) 若含任何影像（CT、ultrasound、chest X-ray、histology），需個別確認影像本身不含可識別資訊或已依機構規範去識別；(b) 若病人年齡、性別、地區組合在去識別化後仍具間接可識別風險（小型社區醫院＋罕見複合症候群），需依期刊政策評估是否需額外遮蔽（如僅稱「50 多歲女性」，本 case_synopsis.md 已如此處理）；(c) 需確認機構是否要求 case report 之 IRB exemption 或倫理委員會函；此為機構政策差異，本 session 無法代為確認。

---

## 四、投稿前最低限度待補（CARE 導向，整合 case_synopsis.md 第五節）

1. **Outcome／follow-up**：最終選擇之 definitive therapy（surgery 或 RAI）實際執行結果；術後或 RAI 後 thyroid function 追蹤；肺部影像確認 necrotizing pneumonia 最終吸收或殘留；EF 重新評估。
2. **Image**：原始 thyroid ultrasound（含右側 1.36 cm 結節之完整影像）、頸部淋巴結 mapping、chest CT／X-ray 序列影像、若手術之病理影像或報告。
3. **Drug chart**：carbimazole、allopurinol、G-CSF、lithium、Lugol（**濃度與確切給藥時間，非僅 mL 數字**）、steroid、抗生素之完整逐日給藥紀錄。
4. **Adverse-event causality**：carbimazole vs. allopurinol 對 agranulocytosis 之正式因果評估（如 Naranjo algorithm 或 WHO-UMC 分類），需先補齊 allopurinol 確切起訖時間。
5. **Patient perspective**：正式訪談或病歷中病人自述段落，涵蓋症狀經驗、對手術／RAI 之偏好與理由。
6. **時序矛盾之解決或明確呈現**：Day 47 vs 48 停藥日、BWPS 同時點組成、ACTH 採檢與最後 steroid 劑量間隔——CARE Item 7 要求明確 timeline，若無法解決應在文中如實呈現差異並說明限制，而非擇一忽略另一。

---

## 五、Case-report thesis 建議與兩種替代可投稿格式

### 建議 thesis（暫定，待跨角色與最終結局資料確認）
「Sequential organ-specific constraints on definitive therapy selection following antithyroid-drug-induced severe agranulocytosis complicated by HFrEF, necrotizing pneumonia, and recent iodinated contrast exposure with renal-function changes：a case report illustrating iodine-washout timing uncertainty in the surgery-versus-radioiodine decision under non-thionamide bridging.」

此 thesis 之重點為**決策過程與競爭性器官限制**，而非宣稱任一介入（Lugol、lithium、G-CSF）之療效——依 R1 methods／hematology 角色已確認之證據限制（G-CSF 因果未證實、lithium 於本案族群安全證據不足、交叉反應率數字不可用於估算個人風險），本檔不建議以任何療效宣稱作為 thesis 主軸。

### 替代格式一：Case-based structured review（個案為錨點之結構性文獻回顧）
適合期刊：如 *Endocrinology, Diabetes & Metabolism Case Reports*、*JCEM Case Reports*。優點：可將 comparator 表（第一節）與 EANM／ATA guideline 之交界問題系統性呈現，教育價值高，不需等待最終 definitive therapy 結局即可以「決策階段」為框架撰寫。**限制**：仍需清楚區分「已發表文獻之發現」與「本案未解決之臨床問題」，避免讓讀者誤以為文獻回顧已提供本案答案；且此格式對「新意」之審查門檻通常更高，需更嚴謹地處理第二節之新意主張。

### 替代格式二：Letter to the Editor／brief report（若最終結局資料在投稿時仍不完整）
適合期刊：如 *Thyroid* letters 欄位或 *Clinical Endocrinology* correspondence。優點：對 Follow-up/Outcome（CARE Item 10）與 Patient Perspective（CARE Item 12）之完整度要求較低，可及早分享決策困境本身，且明確定位為「preliminary、決策階段報告」而非完整結局報告。**限制**：篇幅限制使 comparator 表與細節無法完整呈現；多數期刊仍要求註明「outcome pending」並可能要求後續更新或追蹤信；不能以此格式替代最終仍需完整結局資料之正式 case report。

兩種格式均**不能取代**第三、四節所列 CARE 缺口之補齊；若投稿時 definitive therapy 仍未執行，格式二較符合現況，格式一則需等待結局資料方為完整。

---

## 六、證據表（本檔專屬，含 URL/DOI/PMID、設計、分母、locator）

| # | 文獻 | DOI/PMID | 設計 | 分母 | Locator | 核對層級 |
|---|---|---|---|---|---|---|
| P1 | Voci et al. 2026 | DOI [10.1177/11795476261446355](https://doi.org/10.1177/11795476261446355)；PMID [42078037](https://pubmed.ncbi.nlm.nih.gov/42078037/) | Case report | n=1（EF 35%） | PubMed abstract（本 session 直接檢索取得摘要全文，未取得 PDF 全文） | 摘要層級 CONFIRMED；全文未核對，OPEN-PUB-A |
| P2 | Knight et al. 2017 | DOI [10.1530/EDM-17-0071](https://doi.org/10.1530/EDM-17-0071)；PMID [28924483](https://pubmed.ncbi.nlm.nih.gov/28924483/) | Case report | n=1 | 全文（`literature/knight2017.md`） | **本 session 一手全文核對，CONFIRMED** |
| P3 | Gad et al. 2026 | DOI [10.1530/EDM-25-0131](https://doi.org/10.1530/EDM-25-0131)；PMID [41894843](https://pubmed.ncbi.nlm.nih.gov/41894843/) | Case report | n=1 | 引自 `research/independent_bridge_audit.md`（Outcome and follow-up、Figure 2） | 二手轉引，本 session 未親自開啟全文，OPEN-PUB-B |
| P4 | Fredette et al. 2025 | DOI [10.1159/000536508](https://doi.org/10.1159/000536508)；PMID [38295777](https://pubmed.ncbi.nlm.nih.gov/38295777/)；PMC11965825 | Case report + literature review | n=1（17 歲） | PubMed/Europe PMC abstract | 摘要層級，OPEN-PUB-C |
| P5 | Rami et al. 2024 | DOI [10.1186/s13256-024-04480-9](https://doi.org/10.1186/s13256-024-04480-9)；PMC10981326 | Case series（Case 2） | n=1 of series | 引自 `research/independent_bridge_audit.md`（Case presentation → Case 2、Table 2） | 二手轉引，OPEN-PUB-D |
| P6 | Guvenc et al. 2004 | DOI [10.1002/jca.20014](https://doi.org/10.1002/jca.20014)；PMID [15493048](https://pubmed.ncbi.nlm.nih.gov/15493048/) | Case report | n=1 | 摘要（引自 `research/independent_bridge_audit.md`） | 摘要層級，OPEN-PUB-E |
| P7 | Calissendorff & Falhammar 2017 | DOI [10.1530/EC-17-0025](https://doi.org/10.1530/EC-17-0025)；PMID [28325735](https://pubmed.ncbi.nlm.nih.gov/28325735/) | Retrospective series | n=27（agranulocytosis 用 Lugol 9 人） | `literature/lugol2017.md`（Results, LS duration paragraph） | 前一輪已一手核對（見 `research/independent_bridge_audit.md`） |
| P8 | Sazon et al. 2024 | DOI [10.1210/jendso/bvae163.2078](https://doi.org/10.1210/jendso/bvae163.2078)；PMC11454931 | Conference abstract | n=1 | Abstract case narrative | **僅會議摘要**，OPEN-PUB-F |
| P9 | Fahmi et al. 2026 | DOI [10.1093/ejendo/lvag096.1837](https://doi.org/10.1093/ejendo/lvag096.1837) | Conference abstract | n=1（neutropenia，非 agranulocytosis） | Abstract Case Presentation | 摘要層級；端點不符 agranulocytosis 定義，不應與其他個案並列比較 |
| P10 | Gagnier et al. 2013（CARE guidelines） | DOI [10.1136/bcr-2013-201554](https://doi.org/10.1136/bcr-2013-201554)；PMID [24155002](https://pubmed.ncbi.nlm.nih.gov/24155002/) | Consensus guideline | n/a（27 位參與者共識） | 全文摘要（13-item checklist） | 本 session 一手核對摘要 |
| P11 | Riley et al. 2017（CARE explanation & elaboration） | DOI [10.1016/j.jclinepi.2017.04.026](https://doi.org/10.1016/j.jclinepi.2017.04.026)；PMID [28529185](https://pubmed.ncbi.nlm.nih.gov/28529185/) | Explanation document | n/a | 全文摘要 | 本 session 一手核對摘要 |

---

## 七、CHALLENGE／RESPONSE 狀態

| ID | 對象 | 狀態 |
|---|---|---|
| CHALLENGE-publication-001 | → ATD-ANC-R2-Definitive | `SendMessage` 成功排入對方佇列（msg_id [SESSION-ID-REMOVED]），**未收到回覆，OPEN-PUB-001** |
| CHALLENGE-publication-002 | → ATD-ANC-R2-CaseDx | `SendMessage` 成功排入對方佇列（msg_id [SESSION-ID-REMOVED]），**未收到實質回覆，OPEN-PUB-002**（僅收到與此無關之 PREFLIGHT-CASEDX-003，已以 ACK-publication-to-casedx-001 回覆） |

完整逐字往來見 `sessions/messages/r2_publication_dialogue.md`。**未因對方沉默或忙碌狀態推定其同意本檔之新意主張或 diagnostic 完整性判讀。**

---

## 八、OPEN 清單（本檔）

- **OPEN-PUB-001**：新意主張（第二節）尚未經 ATD-ANC-R2-Definitive 確認，CHALLENGE-publication-001 未獲回覆。
- **OPEN-PUB-002**：diagnostic timeline 是否影響 case-report 格式適用性，尚未經 ATD-ANC-R2-CaseDx 確認，CHALLENGE-publication-002 未獲回覆。
- **OPEN-PUB-A至F**：comparator 表中標註之個案，多數僅摘要層級或二手轉引，本 session 未逐一取得全文核對，投稿前需補齊一手全文核對或改標為「未能親自驗證」。
- **OPEN-PUB-系統性檢索**：本檔第一、二節之 comparator 表與新意主張基於目標式檢索，非完整系統性文獻回顧；投稿前應由作者或圖書館協助執行更廣泛之系統性檢索（至少涵蓋 PubMed、Embase、Europe PMC 之 agranulocytosis AND [heart failure OR pneumonia OR contrast] AND [thyroidectomy OR radioiodine]），以排除本 session 未檢出之更接近個案。
- **OPEN-PUB-CARE**：第三、四節列出之 CARE 缺口（尤其 Timeline、Follow-up、Patient Perspective、Informed Consent）均為投稿前之必要條件，非本 session 可代為補齊。
- **未讀取本輪 peer 正文**：`roles/expanded_case_diagnosis.md`、`roles/expanded_drug_safety.md`、`roles/expanded_definitive_therapy.md` 於本檔撰寫時尚未完成，Peer Review Findings 留待後續讀取後另行補充，不臆測其內容。

## 九、交付總結

- 交付檔案：`roles/expanded_publication_methods.md`（本檔）、`sessions/messages/r2_publication_dialogue.md`（完整往來記錄）。
- 已執行 `ListAgents`，確認本輪具名 peer 為 `ATD-ANC-R2-CaseDx`、`ATD-ANC-R2-Safety`、`ATD-ANC-R2-Definitive`。
- 已送出至少兩則 CHALLENGE（`CHALLENGE-publication-001`→Definitive、`CHALLENGE-publication-002`→CaseDx），均為 `SendMessage` 成功排入對方佇列，**非送達或已讀確認**；截至本檔完成時均未收到實質回覆，已如實標記 OPEN，未推定同意。
- 本檔未對 `ATD-ANC-R2-Safety` 送出訊息；若後續讀取其角色正文後發現與本檔證據宣稱（尤其 lithium／Lugol 安全性交界）有出入，將於後續版本補送 CHALLENGE 並更新本檔，不追溯竄改本版本之送出紀錄。

---

## 十、R2 Peer-Review Addendum（跨 session 複審追補，第二輪，本 session 為新啟動之實例）

本節為**明確標示之追補**，不覆寫上方第一至九節原文；上方內容維持為第一輪產出之歷史紀錄。本節記錄第二輪複審之新發現、對第一輪內容之更正，以及本輪新的跨角色往來。已讀取（唯讀）：`reports/expanded_case_review_zh_TW.md`、`reports/case_report_publication_assessment.md`、本輪已完成之 `roles/expanded_case_diagnosis.md`、`roles/expanded_drug_safety.md`、`roles/expanded_definitive_therapy.md` 全文，以及三者對應之 `sessions/messages/r2_*_dialogue.md`（唯讀）。仍未讀取任何原始病歷或 `private/*`。

### 10.1 確認：AKI／顯影劑因果用語已無過度宣稱
逐句檢視第一至九節全文，確認**沒有任何語句宣稱顯影劑導致 AKI，或宣稱顯影劑注射發生於已確立之 AKI 期間**。第一節與第二節現有用語（「近期 AKI 使含碘顯影劑 6–8 週 washout 前提是否成立無法單純以日曆天數判斷」）僅陳述「病人有一段 Cr 上升軌跡」與「washout 前提是否成立待確認」，未對注射與 Cr 變化之時間先後或因果方向下結論，與 `research/case_synopsis.md`（CT 開立資訊列 Cr 0.94／eGFR 約 65，另有同日 Cr 1.53，「分鐘級先後須查採檢時間」）及 `reports/case_report_publication_assessment.md`（「尚不能確定注射時已有 AKI，也不能把 AKI 歸因於 contrast」）之立場一致。此為第二輪核對後之**確認**，非修改。

### 10.2 時序精確化：Day43／Day46／Day48 三個不同節點
第一輪原文未逐一區分這三個節點，本輪明確補充：**Day 43 為症狀起始**（fever／sore throat，屬臨床症狀出現之日，非任何檢驗確診日）；**Day 46 為外院低 WBC 發現日**（約 730/µL，此為白血球總數而非中性球絕對值，尚非嚴重 agranulocytosis 之正式確診）；**Day 48 為入院並確診嚴重 agranulocytosis 之日**（ANC 0.05×10³/µL＝50/µL）。CARE Item 7（Timeline）若僅寫「Day 43–48 診斷 agranulocytosis」會抹除此三階段之臨床意義（症狀出現→異常篩檢→嚴重程度確診），投稿時應保留三個獨立時間點，不可合併為單一「診斷日」。

### 10.3 新增遺漏之 comparator：Fantin et al. 2021（conference abstract，非完整 case report）
依指示補入本輪查核與 `reports/expanded_case_review_zh_TW.md`、`reports/case_report_publication_assessment.md` 已收錄之文獻：

| 個案 | 設計／n | Bridge | 定位 | 限制 |
|---|---|---|---|---|
| **Fantin et al. 2021** | **Conference abstract（非完整同儕審查 case report）**, n=1 | Methimazole agranulocytosis，ANC 90/µL；lithium 於 I-131 前後短期使用 | [academic.oup.com/jes/article/5/Supplement_1/A958/6241039](https://academic.oup.com/jes/article/5/Supplement_1/A958/6241039)，*J Endocr Soc* 2021;5(Suppl 1):A958 | **僅會議摘要**，追蹤僅 1 個月即報告 euthyroid；未報告 HFrEF、肺炎或雙重碘暴露。與 Sazon 2024（本檔第一節 P8）同屬「lithium→RAI（非手術）」路徑之摘要層級個案，兩者合計仍不足以建立此路徑之完整證據層級。 |

此文獻應補入第一節 comparator 表末尾（因表格已於第一輪定案，此處以追補方式呈現，避免覆寫歷史紀錄；若有下一版本重寫，應直接併入原表）。**修正**：本檔第一輪未收錄此文獻，屬遺漏而非錯誤引用；感謝使用者於本輪指令中提供之精確定位。

### 10.4 透過讀取 peer 檔案取得之未送達回覆，及其對本檔論點之影響
詳細傳輸紀錄見 `sessions/messages/r2_publication_dialogue.md`「第二輪」章節。摘要：
- **ATD-ANC-R2-Definitive** 對第一輪 `CHALLENGE-publication-001` 之實質判斷（經檔案讀取取得，非訊息收訖）：本案「AKI-washout 單一軸線」過窄，建議與 HFrEF／肺炎／結節缺 FNA 等軸線合併陳述。本檔第二節原文本已採多軸線框架，此為**確認**而非需重寫；本輪已就此送出 `CHALLENGE-publication-003` 要求對方新實例正式確認，截至本檔完成時**尚未收到新回覆，OPEN-PUB-003**。
- **ATD-ANC-R2-CaseDx** 對第一輪 `CHALLENGE-publication-002` 之實質判斷（同上，經檔案讀取取得）：CARE checklist 容許以不確定性語言呈現診斷段落，不需放棄標準 case report 格式，但須明確標示 BWPS／Graves／停藥日差異／腎上腺軸四項為「未確立」而非「已確診」。**本檔第三節（CARE checklist 表）之 Item 6、7、8 建議應據此加強**：Clinical Findings／Timeline／Diagnostic Assessment 之撰寫應明確使用「經驗性治療」「工作診斷」「並列呈現差異」「現行準則下無法判讀」等措辭，不使用確定性語氣。此點本輪已透過即時送達之訊息（見下 10.5）進一步確認，非僅檔案讀取。

### 10.5 本輪即時（非檔案讀取）跨角色交流：CaseDx 對投稿論點之新挑戰與本 session 之修正

本輪於撰寫本addendum過程中，**即時收到**（非檔案讀取、確認為真正 SendMessage 送達）來自 `ATD-ANC-R2-CaseDx` 之 `CHALLENGE-casedx-to-publication-001`，核心內容：(a) 本檔第五節原建議 thesis 標題使用「antithyroid-drug-induced」，預設了 `research/case_synopsis.md` 與 `roles/expanded_drug_safety.md` 均明確未排除之 allopurinol 加成貢獻，屬因果歸屬之過度宣稱；(b) thesis 副標「surgery-versus-radioiodine decision」隱含病因學（Graves）與 thyroid storm 診斷已足夠穩定，但 CaseDx 第三、四節已論證 TRAb 灰區與 BWPS 缺同時點組成，診斷本身仍不確定；(c) 鑒於 Voci 2026 已使器官限制組合之新穎性打折、Fantin 2021 僅為摘要，「診斷不確定性本身之教學價值」可能才是現階段更站得住腳的投稿賣點。

**本 session 已以 `RESPONSE-publication-to-casedx-003` 完整接受此三點**（`SendMessage` 回報成功排入對方佇列，msg_id `[SESSION-ID-REMOVED]`，非已讀確認），並提出修正後暫定 thesis：

> 「Diagnostic uncertainty (attribution, Graves confirmation, thyroid-storm criteria) and competing, incompletely-resolved organ constraints (HFrEF, unresolved necrotizing pneumonia, dual iodine exposure) shaping the surgery-versus-radioiodine deliberation in severe drug-associated agranulocytosis：a case-based teaching analysis.」

**正式更正第五節**：原建議 thesis（「Sequential organ-specific constraints...antithyroid-drug-induced severe agranulocytosis...」）之「antithyroid-drug-induced」用詞**予以撤回**，改採不預設單一藥物歸因之措辭（如「severe agranulocytosis of uncertain single-agent attribution (carbimazole vs. allopurinol)」）；且「診斷不確定性」應提升為與「definitive therapy 路徑選擇」並列之教學主軸，不應僅列於 Diagnostic Assessment 段落之限制附註中。此更正之理由完全來自 CaseDx 之具體引註（case_synopsis.md 原文＋ expanded_drug_safety.md 第一節），非本 session 自行發現，特此註明來源。

CaseDx 隨後又以 `RESPONSE-casedx-to-publication-002` 回覆本檔原第九節末段之非強制性問題（是否有固定量化門檻觸發改採教學格式），答案為：**無固定門檻，但若「同時點 BWPS 逐項組成」「配對 ACTH+cortisol」「allopurinol 確切起訖」三者於投稿前仍全部缺失，建議改採 diagnostic-uncertainty 教學格式；若僅缺一至二項且能誠實揭露於限制段落，仍可維持標準 case report**。CaseDx 明確聲明此為個人操作性建議，非文獻或機構規範，非已有共識——本檔採納為**參考門檻**，不宣稱其為正式標準。

### 10.6 至少三項超越「換藥／發病時序／橋接」原三大主題之額外個案問題（依指示新增，附各自所需之待補病人資料）

以下問題整合自本輪 CaseDx／Safety／Definitive 三份角色正文，每項附「需要何種病人資料才能解決」：

1. **甲狀腺結節最終病理／FNA 結果**（`roles/expanded_case_diagnosis.md` 第六節、`roles/expanded_definitive_therapy.md` 第三節均已標記缺口）：右側 1.36 cm 結節依 ACR TI-RADS／ATA nodule guideline 均已達建議 FNA 之 size 門檻，但無 FNA 或原始影像複核。**待補資料**：FNA 細胞學報告；原始 ultrasound 影像（供放射科複閱）；若最終接受手術，正式病理報告。
2. **HFrEF 病因與可逆性**（`roles/expanded_case_diagnosis.md` 第五節）：EF ~32% 之病因（thyrotoxic cardiomyopathy vs. tachycardia-mediated vs. 糖尿病相關 vs. 混合）未確立，且 Day 48 之後至 Day 64 均無 repeat echocardiography。**待補資料**：甲狀腺功能穩定後之新 echocardiography；是否曾有 atrial fibrillation 或其他 tachyarrhythmia 之節律病史；冠狀動脈風險評估。
3. **腎上腺軸狀態**（`roles/expanded_case_diagnosis.md` 第七節）：全程無任何 cortisol 數值，僅有兩次 ACTH（<5、11.8 pg/mL），依 Bornstein 2016（PMID 26760044）與 Annane 2017（PMID 28938253）之判準均無法下結論。**待補資料**：配對 ACTH＋cortisol（理想為 cosyntropin 刺激後），並精確記錄與最後一劑 hydrocortisone 之間隔。
4. **TRAb 判讀之技術與時序基礎**（`roles/expanded_case_diagnosis.md` 第三節）：TRAb 3.00 IU/L 抽血相對 carbimazole 暴露之確切時刻未知，且所用 assay 技術平台（TBII vs. TSI）未載明，已治療中病人之 TRAb 濃度本就可能低於未治療病人。**待補資料**：TRAb 檢驗所用之技術平台說明；若臨床上可行，於停藥或治療前重新檢驗之數值。
5. **Necrotizing pneumonia 最終影像清除與是否需介入引流**（`roles/expanded_drug_safety.md` 第六節、`roles/expanded_definitive_therapy.md` 第二節）：Day 57 記錄「緩慢吸收、接近 abscess」，其後無新影像；本輪查無 ATD-agranulocytosis 恢復後此類病灶清除時間常模之專門文獻。**待補資料**：Day 57 之後之胸腔追蹤影像（CT 或 X-ray 序列）；抗生素療程完成與感染科最終結論；若病灶未縮小，是否曾評估經皮引流。
6. **Lithium 是否達具生理意義之橋接濃度**（`roles/expanded_definitive_therapy.md` 第四、七節）：Day 59 單次濃度 <0.2 mEq/L，遠低於 Gao 2026（target 0.6–1.0 mmol/L）或 Mochinaga 1994（0.43–0.83 mEq/L）之文獻濃度區間，且採血距最後服藥時間未知。**待補資料**：重新測量之 lithium 濃度並精確記錄距最後服藥之時間；同次腎功能（Cr/eGFR）與 volume status。

### 10.7 重申：無 Day 64 前已執行 definitive therapy 之宣稱；投稿格式建議不變但補強依據
本檔第五節「兩種替代格式」建議維持不變，但依 10.5 之修正，格式二（Letter to the Editor／brief report）或教學型格式之適用性理由，現同時包含「結局資料缺失」與「診斷本身之不確定性」兩層原因，而非僅前者。**重申**：截至 `research/case_synopsis.md` 記載之 Day 64，病人僅為門診偏向 thyroidectomy、仍在考慮，**沒有任何已執行之 surgery 或 I-131 記錄**，本檔不曾、也不應宣稱 Day 64 前已完成 definitive therapy；此與 `reports/case_report_publication_assessment.md`「Day 64 以前沒有已執行的 definitive therapy 或更長期追蹤」之結論一致。

### 10.8 本輪 OPEN 清單新增／更正
- **OPEN-PUB-001（更正，見上）**：原「未收到回覆」不準確；已透過檔案讀取取得 Definitive 實質判斷並送出 `CHALLENGE-publication-003` 要求新實例正式確認，該訊息本身為新 OPEN。
- **OPEN-PUB-002（更正，見上）**：同上模式，已透過 `RESPONSE-publication-to-casedx-002`／`RESPONSE-publication-to-casedx-003` 兩則訊息與 CaseDx 完成**即時**（非檔案讀取）之實質交流，此項可視為**已收斂**（見 10.5），不再標記 OPEN。
- **OPEN-PUB-003（新增後即時收斂，非 OPEN）**：`CHALLENGE-publication-003`（→ Definitive）已即時收到 `RESPONSE-definitive-to-publication-002`：其逐條檢視第六節文獻分層表（Ross 2016、Haugen 2015、EANM 2023、Kositanurit 2021、Gao 2026／Vijayakumar 2006、結節惡性率 cohort 群、Andrès 2002）後確認**沒有任何一篇以「多重未就緒前提同時存在」為設計或分析框架**；同意本案潛在貢獻應定位為「記錄多軸線同時未解決時團隊如何決策之過程」，而非主張構成新臨床實體，但明確附加條件：此判斷仍取決於 Day 64 後是否真的產生實際 definitive therapy 決策與結局，若始終沒有，則連「決策過程」本身也僅能寫成 teaching discussion 而非 case report；雙方均聲明此為**研究假說層級之收斂，非確定結論**。本 session 已以 `ACK-publication-to-definitive-002` 確認並接受此條件式立場。
- **OPEN-PUB-004（新增後即解決）**：CaseDx 已以 `RESPONSE-casedx-to-publication-002` 回覆非強制性後續問題，提供操作性（非規範性）門檻建議；本項視為已回覆，非 OPEN。
- **OPEN-PUB-B（沿用）**：Fantin et al. 2021 本輪僅依使用者指令與既有 reports 之引註補入，本 session 未親自 WebFetch 該摘要全文核對，維持二手轉引層級。
- **未變更**：第一輪 OPEN-PUB-A、C–F 及 CARE／系統性檢索相關 OPEN 項目依然成立，不因本輪追補而解決。

### 10.9 交付總結（本輪追補）
- 本輪新增交付：本節（第十節 addendum）；`sessions/messages/r2_publication_dialogue.md` 第二輪章節。
- 本輪已送出訊息：`CHALLENGE-publication-003`（→Definitive，OPEN）、`RESPONSE-publication-to-casedx-002`（→CaseDx，已獲回覆）、`RESPONSE-publication-to-casedx-003`（→CaseDx，接受其挑戰並修正 thesis，已送出）。
- 本輪即時收到並處理：`CHALLENGE-casedx-to-publication-001`（已回覆）、`RESPONSE-casedx-to-publication-002`（已知悉，非強制性問題已獲答覆）。
- 未執行 git、push、merge、刪除或設定變更；未修改 `reports/*.md` 或其他角色擁有之檔案；本節之更正一律以「addendum 明確標示」方式呈現，未覆寫第一至九節原文。
