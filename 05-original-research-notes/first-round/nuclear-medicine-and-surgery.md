# Role: nuclear_surgery（核醫／外科視角）— ATD-ANC-NuclearSurgery — 最終版

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

> **Root 編輯註（2026-09-19）**：以下更正依 root 對原始 PDF 的直接視覺核對，由受託審查者更新；不是角色 session 新增的共識或訊息回覆。Vicente 2017 PDF 第6頁 reference 32 為 Meyer-Gessner 1994，*J Endocrinol Invest* 17:29–36，DOI [10.1007/BF03344959](https://doi.org/10.1007/BF03344959)。1989 原文的 4/29、5/33、11/34 仍經核實，但兩篇文獻之資料關係尚未證實，不推定書目誤植或重複報告。ATA 2016 E6 的 agranulocytosis contraindication 與極窄 storm 短期 PTU 例外位於印刷 p.1357／PDF 第15頁；E7 minor rash 才在 p.1358。Root 已核對 [ATA 原始 PDF](https://www.thermofisher.com/diagnostic-education/dam/clinical/documents/2016-ATA-Guidelines-Diagnosis-Management-Hyperthyroidism.pdf)，本角色未獨立核對該頁。`sessions/messages/` 歷史原文全部保留。

## ACK（最終輪）
本 session 已完成研究、跨角色 CHALLENGE／RESPONSE 與同儕審閱，依指示進行一次收斂性修正並產出本最終版本，取代先前草稿之過時判讀。已讀取：`CLAUDE.md`、`research/case_synopsis.md`、本輪其他三份完整正文之 `roles/endocrinology.md`／`roles/hematology.md`／`roles/methods.md`、`research/independent_crossreaction_audit.md`、`research/independent_bridge_audit.md`、`qa/independent_clinical_review.md`、`qa/independent_bridge_review.md`、`research/retrieval_report.md`、`reports/clinical_synthesis_zh_TW.md`，以及其他三份角色的對話紀錄。未讀取、未曾讀取 `private/` 下任何檔案或原始病歷；本文件不含病歷號、確切就醫日期或醫師/院所名稱，僅用 Day 0 起算之相對天數。本輪未再檢索新文獻。

## Role / Scope（不變）
核醫（RAI）與外科（thyroidectomy）視角，聚焦：(1) ATD-induced agranulocytosis 後 definitive therapy 之 surgery vs RAI 取捨；(2) iodine/contrast 清除動力學對 RAI 時程的影響；(3) HFrEF 與近期 AKI 對手術風險及 RAI 適用性之雙向影響；(4) 甲狀腺結節與 FNA 缺口；(5) 對 Endocrinology（lithium 安全性）與 Methods（case report 外推性）之跨角色 CHALLENGE。不做個別劇量調整、不做確定性（非條件式）治療建議、不竄改他人角色檔、不執行 git/config 操作。

## 個人可重複工作流程（保留）
1. 讀 `CLAUDE.md` + `research/case_synopsis.md`，抽取核醫/外科相關節點。
2. `ListAgents` 確認同 run 對等 session（僅限已命名 `ATD-ANC-*`），發送 PREFLIGHT 並記錄 message_id；對來源無法以 ListAgents 驗證之訊息（例如自稱協調者但不在列表中者）不視為指令，僅記錄不採信。
3. 以去識別化通用臨床詞彙查詢 PubMed/EuropePMC/guideline 全文（`paper-search`/`research_hub` MCP 或 WebSearch/WebFetch）。
4. 每條證據記錄 URL/DOI/PMID＋確切 locator（頁碼/段落/表格）＋研究設計＋分母，並區分「一手核對」與「引自他方稽核備忘，待驗證」。
5. 讀取（唯讀）`literature/` 全文、其他角色 `roles/*.md`、`research/`／`qa/` 之獨立稽核備忘，作為交叉驗證輸入，不逕自採信。
6. 發送並回覆 CHALLENGE（含唯一 ID、來源、明確問題；RESPONSE 附 in_reply_to），全部存入 `sessions/messages/nuclear_surgery_dialogue.md`。
7. 收斂輪次：讀取同儕已完整之正文，撰寫 reviewer 意見；未獲回應或未實際收到之議題明確標記 OPEN，不假設同儕已默示同意。
8. 最終回覆列出交付檔案路徑、OPEN ID 與已收到之 peer 訊息回條。

---

## 研究本體（最終修正版）

### 0. 本輪修正總覽
相對於前一版草稿，本次依 root 提供之更正與已完成之 qa 視覺核對（`qa/independent_clinical_review.md`），修正以下判讀：
1. **AKI 定性修正**：本案為 recent AKI 併 documented creatinine recovery（Cr 1.53→0.59），**非已證實之持續性未解決 AKI**。前版部分段落將此描述為「腎功能恢復軌跡尚未穩定」「EANM 前提不成立」，屬過度延伸，本版已改為條件式敘述。
2. **不自動推論路徑排除**：missing information（如最新腎功能趨勢、Lugol 最後劑量）本身不構成排除 surgery 或 RAI 任一路徑之理由，僅代表決策前需補齊之確認項目。
3. **Meyer-Gessner 1989／Otsuka 2012 分子分母**：已由 qa 稽核以原始 PDF 視覺核對確認（見下方證據表 E2/E3），非僅摘要層級，故不再標註「全文未取得」。
4. **Vicente2017 ref[32]書目已確認**：root現已直接視覺核對PDF第6頁，確認為Meyer-Gessner1994，J Endocrinol Invest17:29–36，DOI10.1007/BF03344959，與Endocrinology／Methods先前讀取一致；先前root誤指1989，本檔隨之採用亦有誤，現更正。這項修正依據是原始PDF，不是指示者身分。本角色未獨立核對Vicente該頁；1989的5/33=15.2%仍真，但1989與1994資料關係尚未證實，不宣稱完整引用鏈已接通。
5. **Lithium 證據層級修正**：不應全稱「僅 case report、無 RCT/cohort」。Gao et al. 2026（回溯性 cohort，doi:10.3389/fendo.2026.1770772，n=146：46 lithium bridging vs 100 standard care）為 cohort 層級證據，惟其排除條件僅為 severe renal impairment（eGFR<30），不能反向證明「eGFR≥30 即安全」，且未針對 active/recent-AKI-recovery 族群之安全性提供直接證據——**此為證據不足，而非證據不存在**。
6. **Nakamura 2013 圖表解析警示**：依 `research/retrieval_report.md`，LlamaParse 對 Nakamura Figure 1/2/3 之機器轉表數字已知不可靠，Figure 5 尚未視覺核對，**本文件所有 Nakamura 數字均取自原文正文/圖說文字，不取自機器轉表**。
7. **G-CSF 因果強度**：Fukata et al. 1999（n=24 RCT）顯示中重度病例未見顯著效益，此為「未證明有效」，不等同「證明無效」；本文件對 Day48→51 ANC 恢復不歸因於任何單一介入。

### 1. 核心問題逐項回應（修正版）

**(a) 換用 PTU 與交叉反應率**：不建議常規換藥。ATA guideline 之 contraindication 立場**僅在危及生命的 thyroid storm 情境留有極有限之短期 PTU 例外討論，不是門診期或穩定期之換藥策略**。常引用之數字經多方核對如下（均非 agranulocytosis-specific 之復發率，**本文件不對本案病人估算任何精確之 agranulocytosis 交叉反應風險數字**，無論 15% 或 50%）：
- Meyer-Gessner 1989（p.169，qa 已視覺核對）：thiamazole(methimazole)↔PTU 4/29=13.8%；carbimazole↔PTU 5/33=15.2%；carbimazole↔thiamazole 11/34=32.4%——**三組為不同藥物配對，非同一配對之雙向數字**，端點為換藥後任一種不良反應復發（all-ADR），非 agranulocytosis-specific。
- Otsuka 2012（p.313 Table 4，qa 已視覺核對）：MMI→PTU 14/41=34.2%；PTU→MMI 9/30=30.0%，同為 all-ADR 端點（其中因副作用停第二種 ATD 者分別為 11/41、6/30）。
- 「50%」查無 agranulocytosis-specific 之可靠一手出處；多篇下游文獻（如 Voci et al. 2026）之引用鏈可追溯至與 rash cross-reactivity（Burch & Cooper 2015 JAMA 引用 Otsuka 2012）或 Vicente 2017 之混淆，非獨立新證據。

**(b) 常見發病時間與本案約 6–7 週病程**：本案 carbimazole Day 0 起始，Day 43 出現 fever/sore throat，Day 46–48 確認嚴重 agranulocytosis，約當療程第 43–48 天。Nakamura et al. 2013（正文 n=461／Figure 2 圖說 n=458，兩者皆為原文內部既存之不同分母，並列呈現不擇一）：71.6% 於 60 天內、84.5%（Abstract）／84.6%（Results/Fig.2）於 90 天內發病。Meyer-Gessner 系列中位發病時間約 33–45 天（不同出版品分別記載，未強行調和）。本案時序落於典型窗口內，非離群值，**但此為「已發病病例中之時間分布」，不代表「所有 ATD 使用者中約 85% 會於 90 天內發病」——分母意涵不同，須避免混用**。

**(c) Non-ATD bridge 到 surgery 或 RAI**：ATA 2016 支持 thionamide 無法使用時以 beta blockade、KI/Lugol、glucocorticoids、必要時 cholestyramine 作為短期術前準備。EANM 2023 guideline 之等待窗口：Lugol/SSKI 2–3 週；water-soluble IV contrast（如本案 Omnipaque）6–8 週，**此 6–8 週前提為腎功能正常**。本案關鍵修正：Day 48 曾用含碘 contrast 時腎功能為 AKI 狀態，隨後 Cr 已恢復至 0.59——**此為 recent AKI 併恢復，不是持續性未解決 AKI**；6–8 週前提是否已滿足，取決於最新一次腎功能檢驗（此為 OPEN，非已知違反），且應以 RAIU／必要時尿碘實測輔助判斷時機，而非僅算日曆天數。此資訊缺口不自動推論 RAI 或手術任一路徑受排除。

### 2. Surgery vs RAI：直接原始資料（表格精簡，去除冗長逐字引用）

| 文獻 | 設計／n | 要點 | 外推限制 |
|---|---|---|---|
| Tamura et al. 2024 | Retrospective, 2 中心 n=185（KI 亞組 76） | 整體 1 年成功率 160/185（86.5%）；KI 亞組兩中心分別 65.0%／88.9% | 非隨機、非 agranulocytosis/AKI 專屬族群，不可稱為「agranulocytosis 病人成功率」 |
| Okamura et al. 2022 | Observational, n=104 | 停 KI 4–7 天後 median RAIU 60.0% | 碘充足地區特定 protocol，非本案族群 |
| Calissendorff & Falhammar 2017 | Retrospective, n=27（agranulocytosis 用 Lugol 者 9 人） | 26 人 thyroidectomy、1 人 RAI（僅用 Lugol 3 天，非停碘 3 天） | 單一 RAI 案例，樣本過小無法比較 |
| Knight et al. 2017 | Case report, n=1 | ANC 0；9 天內多重橋接後 total thyroidectomy，手術時生化未完全正常化 | 作者自陳此為「unique cohort」、無法確立安全時機，單例不建立生化門檻 |
| 2026 dual-ATD-agranulocytosis＋decompensated HF 案例（PMC13133480） | Case report, n=1, EF 35% | 曾接受 RAI 效果不完全；選擇 thyroidectomy 而非重複 RAI，考量低 EF 下重複 RAI 可能誘發心臟事件 | 作者自陳單中心、資源有限情境之外推需謹慎；與本案 EF~32% 情境方向相關但仍為 n=1 敘述 |
| Amiodarone-thyrotoxicosis thyroidectomy MACE by EF（多中心，n=101） | EF<40%組26人／EF≥40%組75人 | 5年MACE 61.4% vs 24.0%；心因性死亡 30.8% vs 1.3% | 病因為 amiodarone-induced thyrotoxicosis，非 Graves'，機轉不同，僅作方向性佐證（低 EF 增加手術心血管風險），非直接外推 |
| Gad et al. 2026 | Case report, n=1 | 術前 Lugol 7 天後 thyroidectomy | 作者稱 surgery 為唯一選項，與 guideline 及上列 RAI 系列不符，屬過度概括，不採用 |

**整合判讀（修正版）**：本案同時存在 EF~32%（方向上提示手術心血管風險升高）、recent-AKI-with-recovery（非持續性 AKI）、iodine/Lugol 暴露史、Day 57 記錄之感染尚未完全清除。**兩條路徑（surgery／RAI）在現有資訊下皆非已知禁忌，亦皆非已知安全就緒**；決策應待最新腎功能、感染影像、EF、結節 FNA 結果補齊後，由麻醉／心臟科／感染科／核醫／外科／內分泌共同評估，本 session 不代替臨床團隊做最終選擇。Day 64 門診「傾向 surgery」為單次臨床決策記錄，不是療效或安全性之 outcome data。

### 3. 甲狀腺結節與 FNA
依 ATA 2015 nodule guideline（Haugen et al., Thyroid 2016;26(1):1–133, DOI 10.1089/thy.2015.0020, PMID 26462967）通則：high suspicion pattern（solid hypoechoic + microcalcification，惡性風險約70–90%）建議 FNA 門檻 ≥1 cm；low suspicion ≥1.5 cm；very-low suspicion ≥2 cm。本案右側 1.36 cm 併 microcalcification——microcalcification 本身即足以歸入 high suspicion，且尺寸達標，理論上符合 FNA 適應症，但無 FNA/病理記錄，為 definitive therapy（尤其手術範圍）決策前之缺口。左側 0.80 cm 未達任何切點尺寸門檻，非因雙側皆有結節即自動需雙側 FNA。案例摘要保留「ill-defined border」而非改寫為「irregular margin」為正確作法——兩者在 guideline 分類意涵上不完全對應，缺乏原始影像前不應自行升級判讀；因 microcalcification 已獨立成立 high suspicion，仍建議影像科／外科複閱原始影像並考慮 FNA。

### 4. 缺失資訊清單（不作為排除任一路徑之理由）
1. 最新（非單次）腎功能連續趨勢，用以確認 EANM 6–8 週前提是否已滿足。
2. Omnipaque／Lugol's solution 確切濃度與最後一劂時間。
3. 右側結節原始影像、頸部淋巴結評估、FNA 細胞學結果。
4. 最新 EF 值與心臟科／麻醉科正式術前風險分層。
5. Necrotizing pneumonia／near-abscess 之最新影像追蹤。
6. 本案已確認使用之 glucocorticoid 為 empiric hydrocortisone；依給藥紀錄與感染狀態核對療程。

### 5. 條件式建議
在上述缺失資訊補齊前，本 session 僅提出條件式方向：**若**最新腎功能確認穩定、EANM 前提可成立、患者傾向非手術路徑，RAI 為可行選項，時機應以 RAIU 而非日曆天數決定；**若**肺部感染已達可耐受全身麻醉、EF 經心臟科/麻醉科正式評估可接受、右側結節已完成 FNA，surgery 亦為合理路徑。兩條路徑之選擇應由多學科共同決定；現有資訊不足以排除或確立任一路徑之單獨優先性。

---

## 證據總表（精簡版，含 URL/DOI/PMID、locator、設計、核對層級）

| # | 文獻 | DOI/PMID | 設計 | 分母/n | Locator | 核對層級 |
|---|---|---|---|---|---|---|
| E1 | Ross et al.2016（ATA guideline） | 10.1089/thy.2016.0229；PMID27521067 | Guideline | n/a | E6印刷p.1357／PDF第15頁：另一thionamide contraindicated及storm短期PTU極窄例外；E7 minor rash位於p.1358 | Root已直接核對原始PDF；本角色未獨立核對該頁 |
| E2 | Meyer-Gessner 1989 | 10.1055/s-2008-1066570；PMID 2464468 | Retrospective cohort n=1256 | 換藥子分析：4/29、5/33、11/34 | p.169 | **qa 已視覺核對原始 PDF，CONFIRMED** |
| E3 | Otsuka 2012 | 10.1111/j.1365-2265.2012.04365.x；PMID 22332800 | RCT n=449（MMI15/MMI30/PTU300） | 換藥子分析：14/41、9/30 | p.313 Table 4 | **qa 已視覺核對原始 PDF，CONFIRMED** |
| E4 | Nakamura et al. 2013 | 10.1210/jc.2013-2569；PMID 24057289 | Retrospective 通報系列 n=754 | 時序子群 n=461（正文）／458（Fig.2） | Abstract p.4776；Results/Fig.2 p.4778 | 正文/圖說文字已核對；**Figure 1/2/3 機器轉表數字不可信，Figure 5 未核對，不引用轉表數字** |
| E5 | Campennì et al. 2023（EANM guideline） | 10.1007/s00259-023-06274-5；PMID 37395802 | Guideline | n/a | Table 1（Lugol 2–3週；water-soluble contrast 6–8週，前提腎功能正常） | qa 已核對 PDF 第3頁 Table 1，CONFIRMED |
| E6 | Tamura et al. 2024 | 10.1007/s00259-023-06523-7；PMID 38008728 | Retrospective cohort n=185 | KI 亞組 76 | Patient preparation section | 引自稽核備忘 |
| E7 | Knight et al. 2017 | 10.1530/EDM-17-0071；PMID 28924483 | Case report | n=1 | 全文 | 本 session 前輪已 WebFetch 全文核對 |
| E8 | 2026 dual-ATD-agranulocytosis + HF 案例 | PMC13133480 | Case report | n=1, EF 35% | 全文 | 本 session 前輪已 WebFetch 全文核對 |
| E9 | Gao et al. 2026 | 10.3389/fendo.2026.1770772 | Retrospective cohort | n=146（46 lithium/100 standard） | Methods，排除 eGFR<30 | 引自稽核備忘，未親自取得全文，OPEN |
| E10 | Haugen et al. 2016（ATA nodule guideline） | 10.1089/thy.2015.0020；PMID 26462967 | Guideline | n/a | 摘要已核對，FNA 尺寸切點為二手來源交叉印證通則 | 部分核對，OPEN |
| E11 | Vicente2017 ref[32]書目 | 10.1007/s40268-017-0172-1 | Narrative review | n/a | PDF第6頁ref32=Meyer-Gessner1994，J Endocrinol Invest17:29–36，DOI10.1007/BF03344959 | Root原PDF視覺確認；本角色未獨立核對。OPEN僅限1989／1994資料關係 |
| E12 | DailyMed Lithium carbonate label | setid [SESSION-ID-REMOVED] | Official label | n/a | Sections 2.5, 7, 8.6 | 本 session 前輪已 WebFetch 全文核對 |

---

## CHALLENGE／RESPONSE 最終狀態
- **CHALLENGE-nuclear_surgery-001**（→ Endocrinology，lithium＋ARNI/spironolactone＋AKI 監測邊界）：Endocrinology 之 RESPONSE-endo-to-nucsurg-001 於原輪 SendMessage **傳輸失敗**，本 session 從未實際收到；本輪收到 FINAL-REVIEW-endocrinology-001 為本 session 實際收到之首則實質回覆，內容已接受（見 dialogue log）。**視為已回應，非因沉默推定同意**。
- **CHALLENGE-nuclear_surgery-002**（→ Methods，case report 外推性）：已收到 RESPONSE-methods-to-nuclear_surgery-002（(1) N/A 待任何角色正式引用；(2) CONFIRMED 無 Day64 誤用）。**已回應**。
- 收到並回覆 **CHALLENGE-methods-003**（橋接治療證據層級）：已於本版更正為「lithium 有 cohort 層級證據但對 active-AKI 安全性仍不足，非全稱無 cohort」。**已回應，本版更新**。
- Endocrinology 之 **CHALLENGE-ENDO-002**（iodine bridge vs RAI 時機）：原輪從未送達本 session；本輪由 Endocrinology 重送後本 session 實際收到，並嘗試回覆（核心立場：EANM「腎功能正常」前提應理解為涵蓋清除期間，非僅暴露當下；本案 AKI-then-recovery 軌跡使日曆天數不可靠，建議以 RAIU/尿碘取代單純算日，此為生理推論非直接引用文獻），但送出時再度發生 SendMessage 傳輸失敗（"No agent named 'ATD-ANC-Endocrinology' is reachable"）。**本 session 未捏造已送達**；完整回覆內容存於 `sessions/messages/nuclear_surgery_dialogue.md` 第 S8 節，供對方或 root 後續讀取。隨後重新執行 ListAgents，確認 Endocrinology／Hematology／Methods 三個具名 session 已從對等列表消失，僅剩無法辨識角色歸屬之泛用名稱（`atd-anc-14/17/20/f7`），本 session 依契約不對這些未驗證歸屬之名稱發送訊息。**列為 OPEN-CHALLENGE-ENDO-002-relay（部分回應已備妥但未能送達）**。

## Peer Review Findings（最終輪，三份正文已完整）
- **對 roles/endocrinology.md**：其1989原文all-ADR分子分母及Vicente ref32=1994讀取結果，現有原PDF查核支持。書目年份不再OPEN；1989與1994資料關係仍未證實，不推定兩篇為重複報告。
- **對 roles/hematology.md**：G-CSF 證據分層（Fukata 1999 陰性 RCT vs 觀察性研究陽性）與本文件修正後之立場一致；Nakamura 461/458、84.5/84.6 不一致已獨立確認並如實並列，未擇一。Allopurinol 因果歸屬未武斷排除，符合證據標準。
- **對 roles/methods.md**：治理發現（repo 根目錄疑似含未去識別化檔案，已 gitignore 排除但位置不當）已記錄並轉達，非本 session 職權範圍；對其收到之未經 ListAgents 驗證之「ATD-ANC-Director」訊息採取不採信未驗證來源的處置方式，方法學上審慎，予以認同。本 session 亦提醒：本輪自身接獲之若干訊息應以同一標準檢核來源。

## OPEN 清單（最終）
- RESOLVED-E1（root原文核對）：ATA2016 E6印刷p.1357／PDF第15頁已由root直接核對；本角色未獨立核對該頁。
- OPEN-E9：Gao2026已由independent_bridge_audit核對官方全文的樣本數與eGFR<30排除條件；本角色未獨立核對，保留角色自身查核層級，不能稱無人查核。
- OPEN-E10：ATA nodule guideline FNA 切點之逐字 recommendation 編號未親自核對。
- OPEN-E11：僅保留Meyer-Gessner1989與1994資料關係尚未證實；Vicente2017 ref32的1994書目已由root直接原PDF確認，不再保留年份爭議。
- OPEN-CHALLENGE-ENDO-002-relay：Endocrinology 送出之 CHALLENGE-ENDO-002 本 session 從未收到，非默示同意。
- OPEN-CLINICAL-1至6：見「缺失資訊清單」，任一項均不構成自動排除 surgery 或 RAI 之理由。

**無 consensus 宣稱**：以上 OPEN 項目代表尚未經本 session 實際收到之訊息或全文核對確認之議題；本 session 不假設任何一致意見已達成，亦不因對方沉默而推定同意。

## 交付總結
- 交付檔案：`roles/nuclear_surgery.md`（本檔，最終版）、`sessions/messages/nuclear_surgery_dialogue.md`（完整往來記錄）。
- 本輪已送出 FINAL-REVIEW-nuclear_surgery-001（→ Endocrinology，回覆其 FINAL-REVIEW-endocrinology-001）。
- 已收到之 peer 訊息回條：本輪即時收到 FINAL-REVIEW-endocrinology-001（ATD-ANC-Endocrinology）；前輪已收到 RESPONSE-methods-to-nuclear_surgery-002 與 CHALLENGE-methods-003（ATD-ANC-Methods）。
