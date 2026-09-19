# roles/expanded_drug_safety.md — ATD-ANC-R2-Safety（血液科／感染科／藥理學視角）

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

本檔為 run ATD-ANC-R2（expanded review）之獨立產出，僅由本 session（ATD-ANC-R2-Safety）撰寫與擁有，不覆寫 `roles/expanded_case_diagnosis.md`、`roles/expanded_definitive_therapy.md`、`roles/expanded_publication.md`。已讀取 `CLAUDE.md`、`research/case_synopsis.md`；未讀取 `private/*`（MCP config 載入除外）、未讀取任何原始病歷檔。案例一律以 Day-relative 表示，不含病歷號、確切就醫日期或醫護人員姓名。前一輪（ATD-ANC-R1）`roles/hematology.md`、`roles/endocrinology.md`、`roles/methods.md`、`roles/nuclear_surgery.md` 已建立之核實結論（Meyer-Gessner 1989／Otsuka 2012 分子分母、Nakamura 2013 內部不一致、ATA 2016 頁碼、EANM 2023 washout 前提）於本檔採**交叉引用**方式標註來源角色檔，不重複逐字核對，除非本輪有新增查核。

## Role / Scope
血液科／感染科／臨床藥理學視角：(1) 嚴重 agranulocytosis 之鑑別因果（differential causality）；(2) allopurinol 暴露缺口；(3) 發病時序之選擇偏差（selection bias）方法學檢討；(4) 換用 thionamide 之再發證據；(5) G-CSF 之 RCT vs. cohort 端點區分；(6) 肺炎臨床緩解與影像緩解之時間落差；(7) 非 thionamide 橋接選項於 HFrEF／近期 AKI 之禁忌；(8) lithium 監測與交互作用；(9) glucocorticoid 風險；(10) beta-blocker 於低心輸出狀態之警示；(11) cholestyramine 與 therapeutic plasma exchange（TPE）。不做個人化劑量升級建議；所有臨床方向皆為條件式（conditional）。

## 個人可重複工作流程
1. 讀 `CLAUDE.md`＋`research/case_synopsis.md`；讀（唯讀）前一輪四份 `roles/*.md` 作為已核實背景，不重複已完成之逐字 PDF 核對。
2. `ListAgents` 確認同 run 之具名 `ATD-ANC-R2-*` peer（CaseDx／Definitive／Publication），僅對其發送訊息；不對其餘泛用命名 session（如 `atd-anc-14/17/20/f7` 等）發送任何訊息，因無法以命名慣例驗證其角色歸屬。
3. 以去識別化通用臨床詞彙透過 `mcp__paper-search__search_pubmed` 等工具查詢一手文獻，記錄 PMID／DOI、設計、分母、locator，並標示核對層級（本輪僅取得摘要層級者標為「摘要層級，未核對全文 PDF」，不得升級為 CONFIRMED）。
4. 對 CaseDx（storm/infection 判讀或藥物歸因）與 Definitive（感染／心臟／腎功能就緒度）各發送至少一則具體 CHALLENGE，記錄 message_id、傳輸結果；收到之訊息以 RESPONSE＋in_reply_to 回覆，全部逐字存入 `sessions/messages/r2_drug_safety_dialogue.md`。
5. 讀取 peer 正文（若本輪內產出）並撰寫審閱意見；未收到回覆者標記 OPEN，不以沉默推定同意。

---

## 一、嚴重 Agranulocytosis 之鑑別因果（Differential Causality）

### 1.1 因果評估工具與其限制
藥物不良反應因果評估常用工具為 Naranjo Adverse Drug Reaction Probability Scale（Naranjo et al. 1981）與 WHO-UMC causality categories（certain／probable-likely／possible／unlikely／conditional／unassessable）。**方法學警示**：Naranjo scale 在藥物性肝損傷等情境之跨評分者一致性偏低（García-Cortés et al. 2008, *Aliment Pharmacol Ther* 27(9):780–789，PMID 18284654：與 CIOMS/RUCAM 相比，between-observer agreement 45% vs. 72%，敏感度僅 54%），且原作者明確排除將此量表用於 overdose／非治療劑量情境（Seger et al. 2013, *Clin Toxicol* 51(6):612–613，PMID 23777343）。本 session **不對本案病人套用 Naranjo 或 WHO-UMC 計算具體分數**——理由有二：(a) allopurinol 確切起訖時間未知（見第二節），量表中「時序關聯」「停藥後反應」「再暴露」等條目無法評分，任何分數皆為假分數；(b) 即使可評分，上述文獻顯示此類量表本身之信度證據薄弱，套用於單一病例僅會製造虛假精確度（false precision），非新增證據。本節僅作為**方法論框架**陳述，供 CaseDx／Definitive 理解「因果推論」與「時序關聯」的差異，不產出病人個別因果分數。

### 1.2 本案可競爭病因清單（documented vs. inferred vs. absent）
- **Documented（案例摘要直接記載）**：carbimazole 10 mg daily 自 Day 0；Day 43 fever/sore throat；Day 46 外院 WBC ~730/µL；Day 48 WBC 0.8×10³/µL、ANC 0.05×10³/µL（50/µL）、CRP 30.12 mg/dL、chest CT 右中葉 pneumonia。
- **Documented 但起訖不明（部分資訊缺口）**：allopurinol 暴露；case synopsis 明載「曾建議停 allopurinol，實際起訖不明」。
- **Inferred（本 session 依藥理學推論，非病歷直接記載）**：若 allopurinol 為長期慢性用藥（例如 gout／hyperuricemia 之慢性處方），其暴露時間可能遠早於 carbimazole Day 0，此時「carbimazole Day 0→症狀 Day 43」之時序關聯性對 carbimazole 較具特異性（allopurinol 若已長期使用而先前未曾發生血球異常，較不支持其為近期誘因，但不能排除累積或延遲性機轉）；反之若 allopurinol 為近期新加藥物，則時序競爭性升高。**此為推論性方向陳述，非病歷已證實之事實**——這正是「allopurinol 暴露缺口」使因果推論無法進一步收斂的核心原因。
- **Absent（病歷未載、亦查無法定論之外部文獻可填補之項目）**：allopurinol 確切起訖日期／劑量；有無先前 gout 發作紀錄以推測慢性用藥可能性；是否有其他新加藥物（如近期抗生素、其他 OTC/中藥製劑）在 Day 0–43 之間introduced。

### 1.3 已知致病藥物之族群層級證據強度（供比較，非本案風險估算）
- **Thionamide（carbimazole/methimazole）**：機轉相對明確，文獻量大。Nakamura et al. 2013（*J Clin Endocrinol Metab* 98(12):4776–4783, doi:10.1210/jc.2013-2569, PMID 24057289）為 754 例通報系列（見 `roles/hematology.md` E1，已由前輪原始 PDF 核對）；IAAAS 跨國 case-control（經 Curtis 2014 review 轉引，PMID 25247619，362 例 agranulocytosis + 6458 對照）將 antithyroid drugs 列為明確高風險藥物類別。
- **Allopurinol**：本輪新查得之一手 case report 層級證據——
  - Reddy et al. 2022（*Clinical Practice and Cases in Emergency Medicine*，doi:10.56305/001c.39749，PMID 40046802）：n=1，68 歲男性，因 severe neutropenia 併 aseptic meningitis 入院，停 allopurinol 後血球恢復；**摘要層級，本 session 未取得全文核對確切暴露天數**。
  - Schär et al. 1994（*Schweiz Med Wochenschr*，PMID 8171306）：n=1，89 歲男性，「well-documented granulocyte chart」，加用 allopurinol 三週後發生 agranulocytosis，骨髓切片支持藥物性；停藥、隔離、抗生素後白血球恢復，但病人 4 週後死於 progressive renal failure（**此死亡歸因於腎衰竭，非 agranulocytosis 本身，且為 89 歲高齡合併症病人，外推限制大**）。
  - Greenberg & Zambrano 1972（PMID 5046471）、Lee & Kueh 1982（PMID 6216593）：均為 case report 層級，僅摘要可得。
  - **無具分母之世代研究專門針對 allopurinol-induced agranulocytosis 之發生率**，此點與 `roles/hematology.md` E3（PMC11878856）結論一致。三週（Schär 1994）之暴露-發病間隔與本案 carbimazole Day 0→43 天相近，**若 allopurinol 為本案近期新加藥物，此重疊時窗本身不足以區分兩者何者為主因**，需仰賴確切起訖時間（仍為 OPEN）。

### 1.4 感染本身作為競爭解釋
Agranulocytosis 病人之敗血症／肺炎可導致骨髓抑制表現與周邊白血球分布改變，但本案 Day 48 已由骨髓機轉（藥物性）與肺炎（續發於嗜中性球缺乏之伺機感染）兩者並存記載，兩者關係應理解為「agranulocytosis 為肺炎之促成因素（neutropenic host 更易感染／感染更嚴重)」，而非「肺炎導致 agranulocytosis」；case synopsis 未提供支持後者方向之骨髓抑制感染病原（如病毒性骨髓抑制）證據，此為 absent data，本節不臆測。

**結論**：本案 agranulocytosis 之因果推論以 carbimazole 為時序關聯最強、族群層級證據最厚實之候選，**但因 allopurinol 確切暴露時間未知，無法完成正式因果分級（無論 Naranjo 或 WHO-UMC），"不能排除 allopurinol 加成或獨立貢獻"之立場維持不變**（與 `roles/hematology.md` OPEN-HEMA-3 一致）。

---

## 二、Allopurinol 暴露缺口（詳述）
Case synopsis 原文：「另曾建議停 allopurinol，實際起訖不明」。此句本身即為 **documented 但不完整**之資訊——「建議停藥」被記載，但「病人是否遵循、何時開始、何時停止」均為 absent。此缺口對以下三件事造成連鎖限制：
1. 無法完成上述因果分級工具之任一條目評分（暴露時序、停藥後反應時間）。
2. 無法判斷本案是否存在 allopurinol/carbimazole 之**藥物交互作用**（兩者若同時經肝臟或腎臟代謝途徑相互影響清除率，現有病歷資訊不足以評估；本 session 未查得 allopurinol 與 carbimazole 之直接骨髓毒性加成的藥理機轉一手文獻，此為 absent，非否定）。
3. 若病人未來需要 definitive therapy 前之高尿酸血症管理，allopurinol 之 re-challenge 安全性亦因本次事件之歸因不明而增加不確定性——但此為未來假設情境，**不構成本輪個別劑量或用藥建議**，僅標記供多科團隊未來決策參考。

---

## 三、發病時序：選擇偏差（Selection Bias）之方法學檢討

前一輪三份角色檔（`roles/hematology.md` 第四節、`roles/endocrinology.md` 第二節、`roles/methods.md` E2）已詳細核對 Meyer-Gessner 1989（中位 45 天，範圍 23–60）、Nakamura 2013（60 天內 71.6%、90 天內 84.5–84.6%）等時序分布，並已確認本案 43–48 天落於典型範圍。**本節新增之方法學觀點、前一輪未明確展開**：

上述所有時序分布（中位發病天數、90 天內累積比例）之分母皆為「**已經發生 agranulocytosis 的病例**」，即條件機率 P(發病天數 | 已發生 agranulocytosis)，而非 P(agranulocytosis 發生 | 使用 ATD 滿 43–48 天的所有病人)。這是通報系列（reporting series）與世代研究常見的**倖存者/確診者偏差**：只有真正發生事件、且被通報／收案的病例才會出現在分母中，服藥滿相同天數但未發生 agranulocytosis 的廣大族群不在此分布內。因此：
1. 「本案 43–48 天屬典型範圍、非離群值」此一結論**僅能用於支持時序上與已知病例分布相容**（temporal plausibility），**不能反向解讀為「用藥滿 43–48 天者發生 agranulocytosis 的機率特別高」或作為病人個別風險預測**。
2. 此偏差同樣適用於 Kobayashi et al. 2014（PMID 24341564，n=81，首次療程中位 39 天）——該研究之分母為「已發病之病例」，且其「第二次以後療程」子群為「未曾發病者再次用藥後首次發病」的病例，前一輪已正確指出此點（`roles/hematology.md` 第四節），本節從統計方法論角度補充其偏差來源。
3. 對 CaseDx 之因果判讀有直接意涵：不應將「本案時序落在典型窗口內」等同於「典型時序即證實因果」——時序相容性是因果推論之必要而非充分條件，仍須配合族群層級生物合理性（thionamide 骨髓毒性機轉已知）與暴露別排他性（allopurinol 缺口未解）綜合判斷。

---

## 四、換用 Thionamide 之再發證據（交叉引用＋本輪立場）
`roles/hematology.md` 第五節、`roles/endocrinology.md` 第三節、`roles/methods.md` E3/E4 已以原始 PDF 全文核對 Meyer-Gessner 1989（p.169，5/33=15.2% carbimazole/PTU 配對）與 Otsuka 2012（p.313 Table 4，14/41=34.2% MMI→PTU）之精確分子分母，並確認兩者均為 **all-adverse-reaction 端點，非 agranulocytosis-specific 復發率**；「50%」之引用鏈經 Voci et al. 2026（PMID 42078037）追溯至 Vicente 2017（doi:10.1007/s40268-017-0172-1）之誤引，該文獻全文查無 50% 字樣。本 session 交叉核對上述三份角色檔之結論一致，**未發現矛盾，不重複逐字查證**。

本節新增：agranulocytosis-specific 之個案層級再發證據僅有兩則 case report（Chen et al. 1983, PMID 6865827：PTU→agranulocytosis→methimazole→10 週後再次 agranulocytosis；Ostlere & Apthorp 1988, PMID 3256337：carbimazole 與 PTU 依序使用後再發），**兩者樣本數合計 n=2，僅支持「可能發生」，不提供任何可用於估算本案病人風險之發生率**。ATA 2016（Ross et al., PMID 27521067）guideline 之 contraindication 立場（印刷 p.1357／PDF 第15頁，已由 root 直接核對，見前一輪角色檔註記）建立在此類個案報告與 class-wide 免疫機轉合理性之上，而非精確量化復發率——此立場本 session 完全採納，不重新展開。

---

## 五、G-CSF：RCT vs. Cohort 端點區分（本輪聚焦擴充）

| 研究層級 | 文獻 | 設計／分母 | 端點與結果 | 因果推論限制 |
|---|---|---|---|---|
| RCT（efficacy，隨機分組） | Fukata et al. 1999, *Thyroid*, PMID 10037073 | n=24（14 G-CSF vs 10 未治療） | 中重度病例 ANC 恢復時間**未見顯著差異** | 小樣本 RCT 陰性結果——**證明「未能證實效益」，非「證明無效」**；隨機分組可控制適應症混淆（confounding by indication），為現有最高證據層級之陰性結果 |
| Retrospective cohort | Andrès et al. 2001, PMID 11493719 | n=20 | 觀察性研究顯示恢復縮短 | 未隨機分組，**適應症混淆風險高**：臨床上通常對病情較重／ANC 較低者優先給予 G-CSF，若這類病人本身骨髓抑制較輕（immune-mediated 者常「驟降驟升」），會產生反向因果（reverse causation）錯覺，即「用了 G-CSF 才快好」可能只是「本來就會快好的病人剛好被給了 G-CSF」 |
| Retrospective cohort | Tajiri & Noguchi 2005, PMID 15785251 | n=109 | 群體層級恢復縮短；**對 symptomatic 且 ANC<0.1×10⁹/L 之最嚴重亞群，效益證據最弱（此亞群被排除於顯著效益結論外）** | 本案 Day48 ANC 50/µL（0.05×10⁹/L）**恰屬此排除亞群**，故 Tajiri 2005 之群體結論不能直接外推至本案 |
| Meta-analysis（混合設計） | Wang et al. 2019, PMID 31824417 | 11 篇研究，n=474 | WMD −3.04 天（95% CI −4.38 至 −1.69），Asian 與歐美族群效果量不同 | 統合分析主要納入觀察性研究，**適應症混淆未被統合分析之隨機化設計消除**；效果量之異質性（族群差異）進一步限制單一病人外推 |
| Narrative review | Hirsch et al. 1999, PMID 10560960 | 16 例文獻回顧 | 僅 3 例顯著縮短 | 病例層級異質性大，非系統性統合 |

**本節結論（與前一輪一致，補充機轉解釋）**：本案 Day 48→51（3 天）之快速恢復，其可能解釋包括：(a) G-CSF＋抗生素治療效果；(b) immune-mediated agranulocytosis 本身之自發性「驟降驟升」自然病程（Nakamura 2013 摘要：211 名多次監測者中 62%／Figure 4 圖說 52.6% 於發病前 2 週仍 >1000/µL，顯示骨髓抑制可迅速逆轉為此類機轉之已知特徵，兩處數字之原文並列差異已由前一輪核對確認）；(c) 兩者疊加、無法個別拆分貢獻度。**因適應症混淆之存在，本案不能將 ANC 恢復之時序相符解讀為 G-CSF 因果效力之證據**，此為本節在既有結論上新增之流行病學方法論理由。

---

## 六、肺炎：臨床緩解與影像緩解之時間落差

### 6.1 本案時序（documented）
| 相對日 | 臨床／血液 | 影像 |
|---|---|---|
| Day 48 | ANC 0.05×10³/µL、CRP 30.12 mg/dL | Chest CT：右中葉 pneumonia |
| Day 51 | ANC 4.14×10³/µL（骨髓恢復） | 未提供同時點影像 |
| Day 54–55 | ANC 3.53×10³/µL、CRP 1.61 mg/dL；出院時**臨床穩定** | 胸片**仍見右中葉浸潤** |
| Day 57 | — | Chest clinic 記右中葉 **necrotizing pneumonia 緩慢吸收、接近 abscess** |

此時序本身已明確顯示：ANC 恢復（Day 51 起）與 CRP 顯著下降（Day 54–55）不等同肺部影像清除；Day 57 之 necrotizing pneumonia／近似 abscess 記錄顯示影像緩解明顯滯後於嗜中性球與發炎指標之恢復。

### 6.2 外部文獻佐證（本輪新查，均為摘要或全文層級 case report/小型 cohort，非本案族群專屬）
- Boucher et al. 2022（*Cureus*, doi:10.7759/cureus.31910, PMID 36579261）：case report n=1，complicated lung abscess 經抗生素＋兩週經皮導管引流後，追蹤影像**近乎完全清除**，臨床症狀（cough／dyspnea）同步改善——**此為免疫功能正常、且接受主動引流病人之個案，非可比較之嗜中性球低下族群**。
- Alshadfan et al. 2026（*PLoS One*, doi:10.1371/journal.pone.0345174, PMID 41886424）：小兒 lung abscess 回溯世代 n=23（非本案之成人／嗜中性球低下族群），平均抗生素療程 4.8 週，療程結束後 1–2 週追蹤影像 91% 完全清除——**僅供影像清除時間尺度之方向性參考（數週至逾一個月），不可作為本案病人之預期時程**。
- Mifsud et al. 2017（*BMJ Case Rep*, PMID 28765482）：case report 提醒「4 週治療後未完全清除之空洞病灶」需考慮非典型病原（該案例最終診斷為 pulmonary echinococcosis），**此為方法學提醒而非直接類比**——若本案 Day 57 之緩慢吸收持續超出預期時間窗，臨床上應保持對非典型病原、阻塞性病灶或膿瘍需介入引流之警覺，而非僅以「等待自然吸收」處理，但**本 session 不對此做出病人個別的介入時機建議**。
- **本 session 查無**專門針對「ATD-induced agranulocytosis 恢復後、continued neutropenic-recovery 期間之 necrotizing pneumonia 影像清除時間常模」之一手文獻，此為與 `roles/hematology.md` OPEN-HEMA-4（安全手術門檻查無文獻）密切相關但範圍更窄之新增缺口，標記 **OPEN-SAFETY-1**。

### 6.3 臨床意涵（條件式）
Day 54–55 出院時「臨床穩定」不應被解讀為感染已清除；Day 57 之影像記錄明確排除此推論。**任何後續 definitive therapy（手術／RAI）之感染就緒度評估，應以最新影像追蹤與臨床感染指標（非僅初期出院時的臨床印象）為準**，此點與 Definitive session 之職權直接相關，本 session 將以 CHALLENGE 提出。

---

## 七、非 Thionamide 橋接選項：於 HFrEF／近期 AKI 之禁忌與注意事項

### 7.1 選項總覽（依 2026 joint consensus 與既有指引）
Taylor et al. 2026（*European Thyroid Journal*, joint consensus statement on thyroid storm, doi:10.1530/ETJ-26-0043, PMID 42554462，摘要層級，本 session 未取得全文 PDF）：thyroid storm 核心治療為 beta-blockade、高劑量 ATD、glucocorticoid、iodide；輔助治療（refractory 情境）包含 cholestyramine、lithium、plasmapheresis（TPE）、ECMO，以及選定病例之 surgical thyroidectomy。此為本輪查得之**最新（2026）guideline-level 彙整來源**，與前一輪 ATA 2016（Ross et al., PMID 27521067）方向一致，本 session 將其列為補充佐證，**摘要層級，未核對全文頁碼，OPEN-SAFETY-2**。

### 7.2 Beta-blocker／calcium-channel blocker 於低心輸出狀態之警示（本輪新增重點）
Subahi et al. 2018（*Am J Ther*, doi:10.1097/MJT.0000000000000739, PMID 29521654）：case report n=1，39 歲女性 thyrotoxic storm 併 atrial fibrillation with rapid ventricular response，予 IV diltiazem drip 後發生低血壓、心搏過緩、進展至 **asystole 心跳停止**。作者摘要明確指出：**calcium channel blocker 與 beta-blocker 在 thyroid storm 合併 decompensated heart failure with reduced ejection fraction 時應「極度謹慎」使用，且現行 thyroid storm guideline 並未提供此情境之具體處置演算法**，此為作者自陳之 guideline gap，非本 session 之推論。

**本案關聯性（條件式，非個別劑量建議）**：本案病人有既往 HFrEF（EF ~32%）背景，且已使用 bisoprolol（beta-blocker）；上述 case report 提示，若未來因 thyroid storm 復發或其他情境需要**升級**心律控制藥物（尤其 IV calcium-channel blocker），應將低心輸出風險與現有 beta-blocker 之疊加效應一併評估，惟本案目前用藥為既有慢性處方而非急性升級情境，**本 session 不對本案是否應調整現行 bisoprolol 劑量提出任何具體建議**，僅標記此一般性警示供臨床團隊參考。

### 7.3 Cholestyramine 與 bile acid sequestrant（本輪新增重點）
機轉：thyrotoxicosis 時 T4/T3 之腸肝循環（enterohepatic circulation）增加，cholestyramine／colestipol 作為陰離子交換樹脂結合腸道內碘甲狀腺胺原酸，加速糞便排除，非抑制甲狀腺合成本身，可與 thionamide／beta-blocker 併用而非取代。

| 研究 | 設計／分母 | 方案 | 結果 |
|---|---|---|---|
| Solomon et al. 1993, PMID 8435884 | Double-blind placebo-controlled crossover RCT, n=15（14 Graves＋1 toxic adenoma） | Cholestyramine 4 g QID＋atenolol 50 mg／methimazole，2 週各期，1 週 washout | Cholestyramine 組甲狀腺素下降更快（F=4–7, P<0.01 vs. 對照 F=2–3.1, P=0.05）；免疫球蛋白濃度不受影響 |
| Kaykhaei et al. 2008, doi:10.1007/s12020-008-9107-5, PMID 18946743 | RCT, n=45（3 組各 15） | Cholestyramine 2 g BID 或 1 g BID＋methimazole 30 mg/d＋propranolol 40 mg/d，4 週 | 高劑量組 4 週末**全數達 euthyroid**；低劑量組亦優於安慰劑 |
| Ha et al. 2016, doi:10.3803/EnM.2016.31.3.476, PMID 27469067 | Retrospective, n=5（cholestyramine+MMI）vs. matched n=12（MMI only） | 高劑量 MMI＋cholestyramine | Free T4／T3 下降更快，**無較多不良事件** |
| Yang et al. 2015, doi:10.3803/EnM.2015.30.4.620, PMID 26394731 | Case report, n=1 | 對兩種 thionamide 及 iodine、beta-blocker 均抵抗／不耐受（含 corticosteroid 過敏史）之 refractory Graves' 病人，2 週高劑量 cholestyramine 後成功施行 thyroidectomy | 直接示範 cholestyramine 可作為**thionamide 與 corticosteroid 均不可用時**之替代橋接 |
| Moreno Watashi et al. 2026（系統性回顧＋統合分析）, doi:10.1177/10507256251409074, PMID 41467975 | 5 RCTs, n=173（93 治療組／80 對照） | Cholestyramine 或 colestipol 併標準治療 vs. 標準治療 | **2 週時 T3/FT4 下降無統計顯著差異；4 週時才達顯著差異**（T3 MD −1.59 nmol/L, CI −2.90 至 −0.27；FT4 MD −1 ng/dL, CI −1.74 至 −0.25）；證據品質低、異質性高 |

**臨床意涵（條件式）**：cholestyramine 之統計顯著效果需時約 4 週方顯現（Moreno Watashi 2026），若本案 definitive therapy 之準備窗口短於此，其邊際效益可能有限；反之若 iodine washout（EANM 6–8 週）或感染／心肺就緒需時較長，cholestyramine 可作為**不需額外碘暴露、不加重腎臟負擔**之併用選項，此為藥理學上與 Lugol／contrast 互斥性最低的橋接選項，**本 session 對是否於本案採用不做決定性建議**，僅提供機轉與時間常模供 Definitive／CaseDx 參考。無腎功能或 HFrEF 特異性禁忌之一手文獻依據被本輪查得；理論上 bile acid sequestrant 可能干擾其他口服藥物（含 thionamide、心臟用藥）之腸道吸收，**建議間隔服用，但本 session 不提供具體間隔時數之個別化建議**。

### 7.4 Therapeutic Plasma Exchange（TPE）
Tian et al. 2024（*Front Endocrinol*, doi:10.3389/fendo.2024.1498014, PMID 39722810）：系統性回顧，MEDLINE/Google Scholar/Embase/CENTRAL 檢索至 2023-12-31，16 篇報告納入，以 Newcastle-Ottawa Scale 評讀品質。病人以女性為主（78.5%）、Graves' disease 為主（89.7%），99.3% 接受 thyroidectomy。以第二線藥物治療 ± TPE 準備者，**術中未見 perioperative thyroid storm 報告**，術前平均 FT4／FT3 下降分別為 52.6±8.2%／68.1±9.3%。**唯一嚴重不良事件**：一篇報告記載病人於治療過程中發生 myocardial infarction 併 tachyarrhythmia 而死亡，**該研究未提供此病例之基礎心功能（是否已有 HFrEF）之摘要層級細節，本 session 未取得全文核對**，故不能確認此死亡與心臟基礎疾病之交互作用細節，僅標記為**TPE／第二線藥物路徑並非零風險，尤其涉及心血管事件**，OPEN-SAFETY-3（待全文核對死亡個案之心臟基礎狀態）。**本案病人有 HFrEF 背景，若考慮 TPE 作為橋接，此死亡個案提示需將心血管監測納入評估，但現有系統性回顧樣本量小（16 篇報告之彙整，非大型 RCT），不足以量化本案病人接受 TPE 之絕對心血管風險**。

---

## 八、Lithium：監測與交互作用（本輪聚焦擴充）

### 8.1 已由前一輪確立之證據層級（交叉引用，不重複核對）
`roles/endocrinology.md` 第四節、`roles/nuclear_surgery.md` 第0節第5點已核實：Gao et al. 2026（*Front Endocrinol*, doi:10.3389/fendo.2026.1770772）為回溯性 cohort，n=146（46 lithium bridging vs. 100 standard care），排除條件僅為 severe renal impairment（eGFR<30 mL/min/1.73m²），對「近期 AKI 恢復期」此動態情境未特別驗證，屬**證據不足而非證據不存在**（OPEN-ENDO-002，本 session 未親自取得該文獻全文，維持二手核對層級）。JCEM Case Reports 2023（PMID 37908984，n=1）為 case report 層級補充。

### 8.2 藥物交互作用機轉（本輪新增，一般藥理學原則，非本案劑量建議）
Lithium 治療窗窄，其腎臟清除高度依賴腎小管對鈉的處理：
- **ACE inhibitor／ARB／ARNI（angiotensin receptor-neprilysin inhibitor，如 sacubitril/valsartan）**：透過降低腎絲球濾過率、影響鈉排除機轉，可減少 lithium 腎臟清除、升高血中濃度，此為 ARB／ACE-I 類藥物之已知類別效應（class effect）；ARNI 之 valsartan 成分屬 ARB，理論上具相同風險方向，但本 session **未查得 ARNI 與 lithium 交互作用之專門發表研究（一手文獻缺口）**，此推論基於 ARB 類別效應之外推，非直接證據，標記 **OPEN-SAFETY-4**。
- **Potassium-sparing diuretic（如 spironolactone）與其他利尿劑**：多數利尿劑（尤其 thiazide）透過促進鈉流失、增加近端腎小管對 lithium 之再吸收，可升高血中濃度；potassium-sparing 類（如 amiloride）之影響據泛用藥物資訊來源（drugs.com／GoodRx 彙整，非原始研究，僅供方向性參考）相對較小，但**本 session 未取得 spironolactone 與 lithium 交互作用之具體隨機試驗或藥物動力學研究之一手文獻**，同屬 OPEN-SAFETY-4。
- 案例摘要記載病人現用藥含 bisoprolol、sacubitril/valsartan、spironolactone；**此為 documented 之當前處方組合**，其與後續 Day 57 門診新加之 lithium carbonate 150 mg daily 之交互作用監測需求，因上述機轉性推論而升高，但**因近期 AKI 已有恢復記錄、且無此特定藥物組合之直接安全性研究，無法量化實際風險幅度**，此點與 `roles/endocrinology.md` OPEN-ENDO-002 完全一致，本節僅補充交互作用機轉細節。

### 8.3 監測建議（條件式、通則層級，非個別劑量指示）
一般 lithium 治療之監測通則（非本案專屬）包括：定期血中 lithium 濃度（需明確記載末次服藥至採血時間，避免峰值/谷值混淆）、腎功能（Cr/eGFR）、電解質（尤其 sodium）、volume status。案例摘要記載 Day 59 lithium <0.2（檢驗參考值未提供 lithium 治療目標區間，且此濃度接近或低於偵測極限），**此單次低濃度不足以判斷療效或安全性，也不可套用精神科治療濃度目標**（此點與 case_synopsis.md 原文限制一致）；若病人腎功能持續恢復但同時併用上述可能降低 lithium 清除之藥物，血中濃度之解讀需格外謹慎，**建議腎科／藥師依當下最新腎功能個別訂定監測頻率，本 session 不提供具體監測間隔天數**。

---

## 九、Glucocorticoid 風險

### 9.1 已知機轉與案例現況
Glucocorticoid（本案為 stress-dose 模式之 empiric hydrocortisone）於 thyroid storm 治療中之理論基礎為抑制周邊 T4→T3 轉換、支持可能併存之相對腎上腺功能不足。案例摘要記載 ACTH 一次 <5、後 11.8 pg/mL，惟採血與最後 steroid 劑量間隔不明，**單一低 ACTH 值不足以診斷永久性 central adrenal insufficiency**（與 case synopsis 原文限制一致，本節不重新展開）。

### 9.2 感染共病之疊加風險（本輪新增，藥理學／感染科觀點）
Glucocorticoid 具免疫抑制效應，可能：(a) 減弱發炎反應之臨床徵象（如發燒、CRP 上升幅度），使感染嚴重度之臨床判讀更困難；(b) 理論上可能延緩嗜中性球功能恢復或增加伺機感染風險。**本案關鍵疊加情境**：Day 48–49 病人同時存在（i）severe agranulocytosis（ANC 50/µL）、（ii）documented 右中葉 pneumonia、（iii）empiric hydrocortisone 使用——三者並存時，glucocorticoid 之免疫抑制效應與嗜中性球缺乏之感染易感性可能有加成疑慮。**本 session 查無專門針對「ATD-induced agranulocytosis 併活動性肺炎期間之 glucocorticoid 安全性」之一手研究**（此為窄範圍之 absent data），Chen Cardenas et al. 2022（*J Endocr Soc*, doi:10.1210/jendso/bvac185, PMID 36545644，圍術期 glucocorticoid 管理文獻回顧）僅涉及 HPA axis 抑制與 perioperative adrenal crisis 風險（結論：adrenal crisis 實際發生率低，但研究品質異質性大、樣本數小），**與感染風險疊加無直接對應**，本節僅指出此為一般藥理學合理性推論（plausibility），非已證實之不良結果，**不建議回溯性評論本案 empiric hydrocortisone 使用是否恰當**，因臨床決策當下需權衡 thyroid storm 之立即風險與感染疊加之理論風險，屬多科即時判斷，非本 session 可事後代為評分。標記 **OPEN-SAFETY-5**。

### 9.3 HPA 軸抑制
Chen Cardenas et al. 2022 指出：任何給藥途徑之 glucocorticoid 均可能造成 HPA axis 抑制，但實際 perioperative adrenal crisis 罕見；現有實證對「應補充劑量與療程」之建議仍基於異質性高、樣本小之研究，缺乏高品質 RCT。本案若考慮未來 definitive therapy（尤其 surgery）之圍術期 steroid 覆蓋，此文獻之通則（**維持病人原有慢性劑量、必要時依手術壓力程度給予短期 IV hydrocortisone 25–100 mg/day 為合理範圍**，但此為文獻通則、非本案個別劑量指示）可供多科團隊參考；本案 empiric hydrocortisone 是否已造成足以延長之 HPA 抑制，需待正式腎上腺功能評估，非本 session 可代為判定。

---

## 十、跨角色比較：實際發表案例 vs. 本案（觀察治療與結局，非統計外推）

| 案例 | 設計 | 觀察到的實際處置 | 觀察到的結局 | 與本案異同 |
|---|---|---|---|---|
| Schär et al. 1994（allopurinol，PMID 8171306） | Case report, n=1, 89 歲男性 | 停 allopurinol＋隔離＋抗生素，**未提及 G-CSF** | 白血球恢復正常；4 週後死於 progressive renal failure（非 agranulocytosis 直接致死） | 本案為藥物歸因較不確定之情境（allopurinol 暴露史相近，起訖不明）；本案另加 G-CSF，且本案病人年齡較輕、恢復更快（3 天 vs. 未載明天數但至少數週） |
| Reddy et al. 2022（allopurinol，PMID 40046802） | Case report, n=1, 68 歲男性 | 停 allopurinol＋支持性照護（supportive care） | 血球恢復；摘要未載恢復天數 | 同為停藥＋支持性照護核心策略，本案額外使用 G-CSF、抗生素治療併發肺炎 |
| Chen 1983／Ostlere 1988（thionamide 再發，PMID 6865827／3256337） | Case report, n=1×2 | 換用另一 thionamide 後**再發** agranulocytosis | 支持「換藥有再發風險」之個案層級證據 | 本案**未換用另一 thionamide**（case synopsis：避免 PTU），與此二案例路徑不同，屬遵循 guideline 立場之選擇 |
| Yang et al. 2015（cholestyramine 橋接，PMID 26394731） | Case report, n=1 | 對 thionamide／iodine／beta-blocker／corticosteroid 均抵抗或不耐受，改用 2 週高劑量 cholestyramine 後手術 | 成功施行 thyroidectomy | 本案目前**未記載使用 cholestyramine**；此案例顯示極端不耐受情境下之替代路徑，供本案若未來出現多重藥物不耐受時參考 |
| Tian et al. 2024 系統性回顧（TPE，PMID 39722810） | Systematic review, 16 報告彙整 | 第二線藥物 ± TPE 準備後 99.3% 接受 thyroidectomy | 無 perioperative storm 報告；1 例死於 MI/tachyarrhythmia | 本案未記載使用 TPE；若採 surgery 路徑且藥物橋接不足，此彙整證據顯示 TPE 為可行但非零風險之選項，尤其涉及心血管事件時應留意本案之 HFrEF 背景 |
| Subahi et al. 2018（beta-blocker/CCB 併低心輸出，PMID 29521654） | Case report, n=1 | IV diltiazem 用於 thyrotoxic storm 併 rapid AF | 進展至 asystole 心跳停止 | 本案已有 HFrEF 背景，此案例提示**若未來需要升級心律控制藥物，應對低心輸出族群格外謹慎**；本案目前僅維持既有 bisoprolol，非本節建議變更 |
| Knight et al. 2017（多重橋接後手術，交叉引用 `roles/nuclear_surgery.md` E7） | Case report, n=1 | ANC 0，9 天內多重橋接後 total thyroidectomy | 手術時生化未完全正常化；作者自陳為 unique cohort，無法確立安全時機 | 本案尚未進入此積極橋接後立即手術路徑，Day 64 僅為門診傾向記錄 |

**方法學提醒**：以上均為 case report 或小型系統性回顧層級之個案觀察比較，**不構成統計外推**；此表僅用於呈現「其他文獻中實際觀察到的處置與結局範圍」，供 CaseDx／Definitive 理解可能路徑之既有先例，不作為本案應採取何種路徑之直接建議。

---

## 十一、證據總表（本輪新增查核項目；前一輪已核實項目不重複列出，見交叉引用）

| # | 主題 | 文獻 | 設計／分母 | Locator | 核對層級 |
|---|---|---|---|---|---|
| S1 | Naranjo scale 信度限制 | García-Cortés et al. 2008, PMID 18284654 | 225 例雙評分者比較 | Results | 摘要層級 |
| S2 | Naranjo scale 不適用於 overdose | Seger et al. 2013, PMID 23777343 | Narrative review | Abstract | 摘要層級 |
| S3 | Allopurinol agranulocytosis case report | Reddy et al. 2022, PMID 40046802 | Case report n=1 | Abstract | 摘要層級 |
| S4 | Allopurinol agranulocytosis case report（死亡歸因腎衰竭） | Schär et al. 1994, PMID 8171306 | Case report n=1 | Abstract | 摘要層級 |
| S5 | G-CSF 適應症混淆之方法學推論 | 本 session 綜合 S/Andrès 2001／Tajiri 2005／Wang 2019（已由 `roles/hematology.md` E4–E6 核實） | Meta-methodological | — | 本 session 論證，非新文獻 |
| S6 | Necrotizing pneumonia／abscess 影像清除時間常模（方向性） | Boucher 2022 PMID 36579261；Alshadfan 2026 PMID 41886424；Mifsud 2017 PMID 28765482 | Case report／retrospective n=23 | Abstract | 摘要層級，非嗜中性球低下族群，僅供方向性參考 |
| S7 | 2026 Thyroid storm joint consensus（含 cholestyramine/lithium/TPE/ECMO） | Taylor et al. 2026, PMID 42554462, doi:10.1530/ETJ-26-0043 | Guideline/consensus | Abstract | 摘要層級，未核對全文頁碼 |
| S8 | Cholestyramine RCT/cohort/case report 全系列 | Solomon 1993 PMID 8435884；Kaykhaei 2008 PMID 18946743；Ha 2016 PMID 27469067；Yang 2015 PMID 26394731；Moreno Watashi 2026 PMID 41467975 | RCT×2、retrospective n=17、case report、meta-analysis(5 RCT n=173) | Abstract（各篇） | 摘要層級 |
| S9 | TPE 系統性回顧 | Tian et al. 2024, PMID 39722810, doi:10.3389/fendo.2024.1498014 | Systematic review, 16 報告 | Abstract | 摘要層級 |
| S10 | Beta-blocker/CCB 於低心輸出 thyroid storm 之警示 | Subahi et al. 2018, PMID 29521654, doi:10.1097/MJT.0000000000000739 | Case report n=1 | Abstract | 摘要層級 |
| S11 | Lithium-ACEI/ARB/diuretic 交互作用機轉（類別效應，非專門研究） | 泛用藥物資訊來源（drugs.com／GoodRx，彙整性二手來源） | 非研究，藥物資訊彙整 | 一般敘述 | **二手、非同儕審閱一手文獻，僅供機轉方向參考，不可作為決定性證據** |
| S12 | Glucocorticoid 圍術期管理與 HPA 抑制 | Chen Cardenas et al. 2022, PMID 36545644, doi:10.1210/jendso/bvac185 | Narrative review | Abstract | 摘要層級 |
| S13 | Lithium bridging cohort（交叉引用，不重複核對） | Gao et al. 2026, doi:10.3389/fendo.2026.1770772 | Retrospective cohort n=146 | 見 `roles/endocrinology.md`／`roles/nuclear_surgery.md` | 二手核對層級，本 session 未親自取得全文 |

**重要限制聲明**：本輪因時間與工具限制，S1–S12 之新增文獻均**僅達 PubMed 摘要層級**，未如前一輪 Meyer-Gessner 1989／Otsuka 2012／EANM 2023 Table 1 般取得原始 PDF 進行視覺核對。本檔對此類文獻之引用**一律以「摘要層級」標註，不宣稱 CONFIRMED**，亦不將摘要結論直接套用為本案病人之個別化風險數字。

---

## 十二、CHALLENGE／訊息狀態
本節記錄本 session 發出與收到之訊息 ID、傳輸結果與回覆內容，完整逐字記錄見 `sessions/messages/r2_drug_safety_dialogue.md`。截至本檔本版完成時：
- 已收到 **PREFLIGHT-CASEDX-001**（← ATD-ANC-R2-CaseDx）。
- 已發送 **CHALLENGE-safety-to-casedx-001**（→ ATD-ANC-R2-CaseDx，storm 判讀與 allopurinol 歸因）、**CHALLENGE-safety-to-definitive-001**（→ ATD-ANC-R2-Definitive，感染影像就緒度與 lithium/glucocorticoid 殘留效應）；傳輸結果與後續回覆詳見對話檔，**未收到之回覆不視為同意**。

## 十三、OPEN 清單（本輪）
- **OPEN-SAFETY-1**：查無 ATD-induced agranulocytosis 恢復後、necrotizing pneumonia／near-abscess 影像清除時間常模之專門文獻。
- ~~OPEN-SAFETY-2~~：**已於本輪跨 session review pass 升級為 CONFIRMED**（見第15.5節）。Taylor et al. 2026（PMC13506520）全文「Iodine/potassium iodide」段落明確載明：口服/鼻胃管碘劑（Lugol/SSKI）之 RAI 建議延後 **2–3個月**（原文："radioiodine is generally deferred for at least 2–3 months"），**不適用於 IV 含碘顯影劑**。此與 EANM 2023（Campennì et al., PMID 37395802）Table 1 之 Lugol/SSKI 2–3 **週**建議相差一個數量級，構成新發現之跨 guideline 分歧，詳見第15.5節與致 Definitive 之 RESPONSE。
- **OPEN-SAFETY-3**：Tian et al. 2024 TPE 系統性回顧中之心因性死亡個案，其基礎心功能（是否合併 HFrEF）未核對全文。
- **OPEN-SAFETY-4**：ARNI（sacubitril/valsartan）與 spironolactone 對 lithium 清除率之專門交互作用研究缺乏一手文獻，現有推論僅基於 ARB／利尿劑類別效應之外推。
- **OPEN-SAFETY-5**：Glucocorticoid 於「agranulocytosis 併活動性肺炎」此特定疊加情境之安全性，查無專門研究；本節僅為藥理學合理性推論，非已證實之風險量化。
- **延續 OPEN-HEMA-3（allopurinol 起訖時間未知）、OPEN-HEMA-4（安全手術門檻無文獻）、OPEN-ENDO-002（本案藥物組合下 lithium 監測排程無直接文獻對應）**：本 session 完全認同前一輪結論，不重複開啟，僅於相關章節交叉引用。

## 十五、R2 Peer-Review Addendum（跨 session 複審輪，本節新增，不修改上方原文）

本節為本 session 於跨 session review pass 新增之附錄，用於：(a) 讀取三份 peer 完整正文（`roles/expanded_case_diagnosis.md`、`roles/expanded_definitive_therapy.md`、`roles/expanded_publication_methods.md`）及共享報告 `reports/expanded_case_review_zh_TW.md`、`reports/case_report_publication_assessment.md` 後之審閱意見；(b) 對本檔（僅本檔，不修改前述其他檔案）之既有內容作明確標示之補充與更正。**上方第一至十四節原文不刪改，任何更正均以本節「更正」字樣獨立標出。**

### 15.1 自我核對結果（compliance self-audit）
- 已重新檢視本檔全文：未使用任何非病歷本身之縮寫代稱，未將本案描述為「three-month late-onset」或任何等同措辭；Day 43（fever/sore throat 症狀出現）、Day 46（外院 WBC ~730/µL）、Day 48（住院、ANC 0.05×10³/µL=50/µL 確診）三個時間點於第 1.2 節已分別列出，未合併或混淆。**確認合規，無需更正**。
- 已重新檢視本檔是否對 Day 48 顯影劑（Omnipaque 350）給藥時腎功能狀態做出因果推論：本檔第七節、第八節聚焦於 lithium／glucocorticoid／beta-blocker／cholestyramine／TPE，**未曾對 CT 顯影劑與 AKI 之時序關係做出推論**，此議題屬 `roles/expanded_case_diagnosis.md`／`roles/expanded_definitive_therapy.md` 之主責範圍（兩份文件均已正確處理：CT 醫囑面 Cr 0.94／eGFR~65 與同日另記 Cr 1.53 為採檢時刻未對齊之兩筆數字，不可推論顯影劑給藥「當下」腎功能異常或顯影劑為 AKI 病因）。**本檔確認未曾逾越此界線，無需更正**。
- 已確認本檔未曾宣稱 Day 64 已執行任何 definitive therapy（本檔第 10 節表格與第 6 節僅引用 case synopsis 既有之「門診偏向 thyroidectomy，病人仍考慮」，未改寫為已執行）。**確認合規**。

### 15.2 對本檔內容之更正（新增，非刪除原文）

**更正 1：Voci et al. 2026 應同時列為直接治療結局比較個案（原檔僅用於「50%」引用鏈失真之討論，遺漏其作為 HFrEF＋agranulocytosis＋surgery 直接比較個案之角色）**

原檔第四節、第五節僅將 Voci et al. 2026（*Clin Med Insights Case Rep*, PMID 42078037, DOI 10.1177/11795476261446355, PMC13133480）用於追溯「50%」交叉反應率之錯誤引用鏈。經本輪讀取 `reports/case_report_publication_assessment.md`（第15–18行）與 `reports/expanded_case_review_zh_TW.md`（第67–68行）確認：**Voci 2026 為已完整發表之 case report（非摘要），描述 MMI 與 PTU 依序引發 agranulocytosis、合併 decompensated HF（EF 35%）與 COPD，經 Lugol's iodine＋G-CSF 橋接、以 right heart catheterization 確認手術適合度後成功施行 total thyroidectomy**。此為與本案（agranulocytosis＋HFrEF EF~32%＋考慮 surgery）**目前已知最直接可比之單一已發表案例**，本檔第十節比較表原未納入此案例作為治療路徑比較項，**特此補列**：

| 案例（更正後新增） | 設計 | 觀察到的實際處置 | 觀察到的結局 | 與本案異同（更正版） |
|---|---|---|---|---|
| Voci et al. 2026（PMID 42078037，完整 case report，非摘要） | Case report, n=1，54歲男性，2年Graves病史，MMI後PTU相繼引發agranulocytosis，合併decompensated HF（EF 35%）、COPD | Lugol's iodine＋G-CSF橋接，以right heart catheterization確認手術適合度後 | 成功施行total thyroidectomy | 目前與本案最接近之單一已發表個案；但此案**無AKI、無惡性結節疑慮、無合併活動性肺部感染**，性別、年齡、Graves病程長度亦不同——**是選定的成功個案，不構成可推廣之安全性保證**，不能假設本案採相同橋接方案必然同樣安全有效（此點與 `roles/expanded_definitive_therapy.md` 第四節之判讀一致，本檔獨立確認後補列） |

**更正 2：新增 Fantin et al. 2021 與 Sazon et al. 2024 作為 lithium／glucocorticoid 橋接之額外比較個案（本輪新查，原檔未收錄）**

依使用者本輪指示與 `reports/case_report_publication_assessment.md`（第18–19行）、`reports/expanded_case_review_zh_TW.md`（第70–71行）之交叉核對：
- **Fantin et al. 2021**（*J Endocr Soc* 5(Suppl 1):A958, https://academic.oup.com/jes/article/5/Supplement_1/A958/6241039）：**明確為 conference abstract，非完整 case report**——本檔在此明確標註其證據層級低於 case report（無完整方法/追蹤細節可核）。內容：MMI-induced agranulocytosis，ANC 90/µL；短期 lithium 跨越 I-131 治療前後使用，報告 1 個月後達 euthyroid。**與本檔第八節 lithium 橋接主題直接相關**：此為本輪新查得之「lithium 橋接至 RAI（而非手術）」之個案層級先例，惟僅摘要層級、追蹤僅 1 個月，無法提供本案 lithium 於 HFrEF／近期 AKI 恢復期＋ARNI／spironolactone 併用情境下之安全性佐證。
- **Sazon et al. 2024**（conference abstract，PMC11454931）：carbimazole 後 ANC 0；**lithium＋prednisone 合併使用**後接受 I-131，短期後出現 hypothyroidism。**此為本輪新查得、與本檔第八、九節（lithium 與 glucocorticoid 合併橋接）最直接相關之個案**，但同樣僅摘要層級，缺完整心肺腎時序與長期結局，無法核對其 prednisone 之確切劑量/療程與 lithium 之交互作用監測方式。

**兩者均應標註為「conference abstract 層級，非完整 case report」，不可與 Knight 2017、Voci 2026 等完整 case report 並列為同等證據力**，此為本檔更正後之明確立場，避免未來引用時證據層級混淆。

**更正 3：第十節比較表標題澄清**——原表格標題「觀察治療與結局，非統計外推」保持不變，但依更正1、2，表格應理解為**不完整清單**，本輪已知至少 Fantin 2021、Sazon 2024 兩則 lithium／glucocorticoid 橋接摘要層級個案未列入原表，現於本節補充，不重寫原表以保留版本歷史可追溯性。

### 15.3 對 Peer 正文之審閱意見（讀畢三份完整正文）

- **對 `roles/expanded_case_diagnosis.md`**：第三節 TRAb assay cutoff 灰區分析（Theodoraki 2011、Smit 2020）與本檔第三節「選擇偏差」之方法論精神一致——兩者均強調「單一數值/單一時間點之判讀，脫離其產生情境（治療中 vs. 治療前；已發病 vs. 未發病之分母）即可能失真」，屬獨立收斂而非互相引用之巧合。第七節 ACTH／cortisol 判讀（引用 Bornstein 2016、Annane 2017）方法學嚴謹，明確指出「本案無任何 cortisol 數值，故無法套用任何國際準則判讀」，此結論本檔完全採納，並據此發出新 CHALLENGE-safety-to-casedx-002（見下）以補其未觸及之「glucocorticoid 起始時間相對 ANC 最低點之先後」議題。
- **對 `roles/expanded_definitive_therapy.md`**：第四節之 Reed & Bradley 1985（PMID 3933136，case report n=1：lithium 單獨術前準備達良好生化控制，但**術後仍發生 thyroid storm**）為極重要之反例，且該檔案誠實地將其列為「counter-evidence，不可省略」而非略去不利個案——此與本檔方法學立場一致（本檔第八節同樣強調 lithium 監測不能僅憑單次數值判定安全）。本檔認為 Reed 1985 進一步支持本檔 OPEN-SAFETY-4 之立場：**lithium 之機轉為抑制釋放而非耗竭合成儲量**，若術前準備時間不足或監測不到位，即使某一時間點生化正常，仍可能於手術操作時釋放殘留賀爾蒙——此為本檔在 Definitive 既有發現基礎上之藥理機轉補充，非新增獨立文獻。第一節 EANM guideline「腎功能正常」前提於「顯影劑給藥當下腎功能不明」情境之缺口辨識與本檔第八節 lithium／ARNI 交互作用之「一手文獻缺口」性質相同，均屬「guideline 未覆蓋之實務情境」，方法學上互相印證。
- **對 `roles/expanded_publication_methods.md`**：（見下方 15.4，本檔已讀取其正文用於確認 Fantin/Sazon/Voci 之書目與定位一致性，內容與 `reports/case_report_publication_assessment.md`、`reports/expanded_case_review_zh_TW.md` 交叉核對後未見矛盾。）

### 15.4 本輪 CHALLENGE／RESPONSE 更新（詳見 `sessions/messages/r2_drug_safety_dialogue.md`）
- 已透過讀取 `sessions/messages/r2_definitive_therapy_dialogue.md`、`sessions/messages/r2_case_diagnosis_dialogue.md` 得知：Definitive 與 CaseDx 均曾嘗試對本 session（前一實例）送出實質 CHALLENGE／RESPONSE，但因本 session 前一實例已結束，`SendMessage` 傳輸失敗，**本 session 從未直接收到**。本輪已以新實例透過 `SendMessage` 正式回覆兩者，並對 CaseDx 新發送 **CHALLENGE-safety-to-casedx-002**（glucocorticoid 起始時間相對 Day48 ANC 最低點之先後、與 neutropenia／感染疊加風險，引用 Annane et al. 2017 CIRCI guideline, doi:10.1097/CCM.0000000000002737, PMID 28938253 為具體 locator），要求明確回覆。**傳輸回報為成功排入佇列，非確認已讀或已同意**；截至本節完成時尚未收到任一方之新 RESPONSE。

### 15.5 本輪即時往來（跨 session review pass 進行中收到之實質回覆，逐項記錄）

本節記錄本檔第15.4節送出訊息後，於本 session 撰寫過程中**實際收到**之回覆（非讀檔得知，是 SendMessage 直接送達）：

1. **收到 RESPONSE-CASEDX-001（重送，內容與前一實例相同）**：CaseDx 確認其 storm 判讀已將感染列為 BWPS 混淆因子、未視為獨立確診，並重申 G-CSF 因果貢獻之提問——**此問題已於本檔第15.4節送出之 RESPONSE-safety-to-casedx-002 中回覆**（Nakamura 2013 驟降驟升佐證、不建議以 ANC 恢復佐證感染負荷同步下降），視為已處理，不重複回覆。
2. **收到 RESPONSE-casedx-to-safety-003**：CaseDx 已重新核對 `research/case_synopsis.md` 第16行，確認原文僅載 hydrocortisone 與其他藥物「相繼使用」，**未提供其相對 ANC 最低點之精確先後**，同意新增 OPEN-CASEDX-008 於其檔案，並同意將「glucocorticoid 免疫抑制與 severe neutropenia+active pneumonia 疊加風險」列為跨角色共同 OPEN 項。**本 session 確認一致，此為雙方獨立核對後之真實收斂，非單方宣稱**。
3. **收到 CHALLENGE-definitive-to-safety-002**：Definitive 指出共用報告 `reports/expanded_case_review_zh_TW.md` 第61行引用「2026 thyroid storm 多學會共識」（連結 PMC13506520）聲稱大量 iodide 治療後 RAI 應採 **2–3個月**延後框架，遠大於 EANM 2023 之 2–3 週建議，要求本 session（既已引用 Taylor 2026）協助核對全文。**本 session 已以 WebFetch 直接核對 PMC13506520 全文，確認**：(a) 該文獻確為 Taylor et al. 2026 joint consensus（*Eur Thyroid J*, doi:10.1530/ETJ-26-0043, PMID 42554462），書目無誤；(b) 「Iodine/potassium iodide」段落原文明確載："radioiodine is generally deferred for at least 2–3 months"，**此建議明確針對口服/鼻胃管碘劑（Lugol/SSKI），非 IV 含碘顯影劑**；(c) 此為**跨 guideline 之真實分歧**（Taylor 2026 之 2–3 個月 vs. EANM 2023 之 2–3 週，相差約 4–6 倍），非任一方誤讀，**應於共用報告與雙方檔案中明確並列兩者，不可只採較寬鬆之 EANM 2–3 週而忽略較保守之 Taylor 2–3 個月**，尤其本案 Lugol 暴露已持續超過 2–3 週但未必滿足 2–3 個月。已將此發現升級本檔 OPEN-SAFETY-2 為 CONFIRMED（見上方 OPEN 清單），並已透過 SendMessage 回覆 Definitive（見交付總結）。**此為本輪最具體之全文核對貢獻，過程逐字保留於 `sessions/messages/r2_drug_safety_dialogue.md`**。

4. **收到 ACK-definitive-to-safety-003**：Definitive 確認收訖 RESPONSE-safety-to-definitive-002，並自述已將其 `roles/expanded_definitive_therapy.md` 第一節、第六節文獻表、第七節同步更新為並列 EANM 2023（2–3週）與 Taylor 2026（2–3個月）兩套數字。**本 session 未讀取、未核對 Definitive 檔案之實際修改內容**（依契約不編輯亦不需親自複核他人擁有檔案），僅如實記錄對方訊息中自述之處置結果，不代為背書其修改品質。

## 十六、本輪新增之額外案例問題（超出原始「換藥／發病時序／橋接」三大主題）

以下問題聚焦血液科／感染科／藥理學視角，每項均註明可解決此問題所需之病人資料：

1. **Day 48 肺炎之微生物學工作檢查（痰液／血液培養、非典型病原檢測）為何？** 若有明確病原體（如 *Klebsiella pneumoniae*、*Staphylococcus aureus* 或厭氧菌，常見於 necrotizing pneumonia／abscess 形成），將直接影響抗生素選擇是否為病原導向而非純經驗性、以及 Day 57 near-abscess 是否需要介入性引流而非僅延長抗生素療程。**可解決此問題之資料**：Day 48 痰液/血液培養報告與藥敏、Day 57 是否曾會診感染科或胸腔外科評估引流。
2. **G-CSF 之實際給藥規格（劑型、劑量、起訖日期）為何？** Filgrastim 之藥理效應通常於給藥後 24–72 小時內出現 ANC 上升；若本案 G-CSF 給藥時間點與 Day48→51 之 ANC 恢復曲線在藥理學上吻合，則因果歸因之合理性會提高（雖仍無法完全排除自發性驟升，見本檔第五節）；若給藥時間遠早於或晚於此曲線，則自發性恢復之解釋權重應提高。**可解決此問題之資料**：完整 medication administration record 中 G-CSF 之劑型／劑量／給藥時刻。
3. **Day 46 外院 WBC ~730/µL 當時是否有白血球分類計數（differential）或周邊血液抹片（peripheral smear）？** 現有資料僅載 WBC 總數，未載 ANC 或形態學發現（如 toxic granulation、blast forms、absolute lymphocytosis）。此資訊可協助區分「Day 46 已是藥物性 agranulocytosis 之早期階段」與「其他導致 WBC 下降之過程（如敗血症消耗性淋巴球增多相對比例改變、假性白血球低下）」，並可與 Day 48 之正式 ANC 50/µL 確診做形態學層面的連續性比對，而非僅有兩個時間點的絕對數字。**可解決此問題之資料**：Day 46 CBC differential 與（若有留存）周邊血液抹片報告。
4. **Lithium carbonate 150 mg daily 起始前後，是否有心電圖（ECG／QTc）監測？** Lithium 可能造成竇房結功能異常、T 波改變，且本案病人同時使用 bisoprolol（beta-blocker，本身可能造成心搏過緩）與近期曾有 AKI（電解質波動風險）；兩者疊加可能放大 lithium 對心臟傳導之潛在影響，此為本檔第七節（beta-blocker 於低心輸出狀態警示）與第八節（lithium）交界之新議題，先前兩節均未觸及心電圖監測面向。**可解決此問題之資料**：lithium 起始前後之 ECG／QTc 記錄，以及是否有相關心律不整症狀記載。

---

## 十四、交付總結
- 交付檔案：`roles/expanded_drug_safety.md`（本檔，含本輪新增第十五、十六節）、`sessions/messages/r2_drug_safety_dialogue.md`。
- 本輪未修改、未讀寫任何其他角色或報告之擁有檔案（`reports/*.md`、`roles/expanded_case_diagnosis.md`、`roles/expanded_definitive_therapy.md`、`roles/expanded_publication_methods.md` 均僅讀取，未編輯）；未執行 git/config/刪除操作。
- 本檔之臨床意涵段落均為條件式（conditional），不含個別劑量升級建議，不臆測病人現行藥物之絕對禁忌或已證實安全性。
- 本輪已透過 SendMessage 對 ATD-ANC-R2-Definitive 送出 RESPONSE-safety-to-definitive-001、對 ATD-ANC-R2-CaseDx 送出 RESPONSE-safety-to-casedx-002＋新 CHALLENGE-safety-to-casedx-002；均為成功排入佇列，**非確認已讀或已同意**，實際回覆狀態與未回覆 OPEN 項目詳見 `sessions/messages/r2_drug_safety_dialogue.md`。
