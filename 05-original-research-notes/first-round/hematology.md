# roles/hematology.md — ATD-ANC-Hematology（run ATD-ANC-R1）— 最終版

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

> **Root 編輯註（2026-09-19）**：以下更正依 root 對原始 PDF 的直接視覺核對，由受託審查者更新；不是角色 session 新增的共識或訊息回覆。Vicente 2017 PDF 第6頁 reference 32 為 Meyer-Gessner 1994，*J Endocrinol Invest* 17:29–36，DOI [10.1007/BF03344959](https://doi.org/10.1007/BF03344959)。1989 原文的 4/29、5/33、11/34 仍經核實，但兩篇文獻之資料關係尚未證實，不推定書目誤植或重複報告。ATA 2016 E6 的 agranulocytosis contraindication 與極窄 storm 短期 PTU 例外位於印刷 p.1357／PDF 第15頁；E7 minor rash 才在 p.1358。Root 已核對 [ATA 原始 PDF](https://www.thermofisher.com/diagnostic-education/dam/clinical/documents/2016-ATA-Guidelines-Diagnosis-Management-Hyperthyroidism.pdf)，本角色未獨立核對該頁。`sessions/messages/` 歷史原文全部保留。

本檔取代先前初版之推測性段落；歷史查核過程保留於 `sessions/messages/hematology_dialogue.md` 原始訊息中，不在此重述。未讀取 `private/` 或任何原始病歷；不含病歷號、確切年齡、就醫絕對日期或醫療人員姓名，僅用 case_synopsis.md 之相對 Day 編號。

## Role / Scope
血液科視角文獻查核：agranulocytosis 定義與分層、ATD vs. allopurinol 歸因、G-CSF 治療證據、ATD onset timing 與本案對照、thionamide 交叉反應率數字之 provenance。

## 個人可重複工作流程
1. 讀 `CLAUDE.md`、`research/case_synopsis.md`；不讀 `private/*`。
2. `ListAgents` 確認同 run 之 `ATD-ANC-*`（僅限確實以此樣式命名者，不對通用命名之背景 session 發訊）。
3. 對每個已確認之 peer 送 PREFLIGHT／FINAL-REVIEW 測試，記錄 message_id，逐字保存於 `sessions/messages/hematology_dialogue.md`。
4. 用去識別化通用臨床詞彙查一手文獻（PubMed／Europe PMC／WebFetch），記錄 URL/DOI/PMID＋locator（頁碼/表格）＋研究設計＋分母，區分「已親自核對原文」與「引自他方稽核備忘、待驗證」。
5. 交叉比對 `research/independent_crossreaction_audit.md`、`qa/independent_clinical_review.md` 等獨立稽核備忘之結論，但獨立驗證，不逕行採信。
6. 撰寫本檔正文，標明 OPEN 項目，不捏造共識。
7. 對相關 peer 發至少一則 CHALLENGE／FINAL-REVIEW，回覆收到之 CHALLENGE（RESPONSE + in_reply_to）。
8. 讀 peer `roles/*.md` 正文，寫 reviewer 意見；未獲回應者標記 OPEN。

---

## 一、Agranulocytosis 定義與嚴重度分層

ANC < 500/µL 為公認定義；近期 HLA 關聯研究另將 ANC < 100/µL 列為 severe 亞群（Mao et al. 2026, PMC13494723, retrospective n=24：15 severe／9 typical），severe 亞群恢復時間中位數較長（5 天 vs 3 天）、症狀比例較高，並與 HLA-B*38:02 相關（OR 48.6，95% CI 2.3–1020.7，樣本小、區間寬）。本案 Day 48 ANC 50/µL 屬 severe 分層；Day 48→51（3 天）恢復速度快於該亞群中位數，可能反映個體差異、小樣本效應，或治療介入時序重疊，現有證據無法單獨歸因。

## 二、歸因：ATD（carbimazole）vs. allopurinol

Carbimazole/methimazole 為機轉相對明確、文獻量大之病因（Nakamura et al. 2013 單一系列 754 例通報，估計日本年發生率約 0.1–0.15%）。Allopurinol-induced agranulocytosis 屬罕見（case report 層級，無具分母之世代研究）；IAAAS 跨國 case-control（經 Curtis 2014 review 引用，PMID 25247619；362 例 agranulocytosis + 6458 對照）將 ATD 列為明確高風險藥物類別，allopurinol 未特別突出。

**缺口（維持 OPEN-HEMA-3）**：case_synopsis.md 載明 allopurinol 確切起訖時間未知，無法完成 Naranjo／WHO-UMC 式因果評估。以現有時序（carbimazole Day 0 起始、Day 43 症狀、Day 46–48 確診）而言，此間隔落在多個獨立世代文獻之典型範圍內（見下節），使 ATD 歸因較為簡約可信，但**不構成排除 allopurinol 加成貢獻的證據**。

## 三、G-CSF 治療證據

現有已識別之小型前瞻性 RCT（Fukata et al. 1999, Thyroid, PMID 10037073, n=24：14 G-CSF vs 10 未治療）於中重度病例**未證實顯著效益**——此為單一小樣本試驗之陰性結果，不等同於「證明 G-CSF 普遍無效」，亦不代表已窮盡所有 RCT 證據。多篇回溯性 cohort（Andrès et al. 2001, PMID 11493719, n=20；Tajiri & Noguchi 2005, PMID 15785251, n=109）及 2019 統合分析（Wang et al., PMID 31824417，11 篇研究、474 例，WMD −3.04 天，95% CI −4.38 至 −1.69，Asian 與歐美族群效果量不同）顯示群體層級之恢復縮短，但對「symptomatic 且 ANC<0.1×10^9/L」最嚴重亞群（本案屬此類）效益證據最弱（Tajiri 2005 排除此亞群之效益；Hirsch et al. 1999, PMID 10560960，16 例文獻回顧僅 3 例顯著縮短）。

本案 Day 48→51 之恢復與 G-CSF＋抗生素治療時序相符，但不能排除自發性骨髓恢復——immune-mediated agranulocytosis 本身具「驟降驟升」特徵（Nakamura 2013 Abstract：211 名多次血球監測者中 62%〔Figure 4 圖說則為 52.6%，原文二處不一致，並列標註〕於發病前 2 週仍 >1000/µL）。**結論以 conditional 表述**：時序相符，因果性未經高證據層級證實，此點已與 Methods session 前一輪交叉核對收斂。

## 四、ATD onset timing 與本案 ~6–7 週病程

本案自 carbimazole Day 0 起算，Day 43 症狀、Day 46–48 確診，約 43–48 天（6–7 週）。跨世代文獻比對：
- Meyer-Gessner et al. 1989（Dtsch Med Wochenschr 114(5):166–171, PMID 2464468, p.169，n=1256 世代＋8例轉診）：發病中位數45天（23–60）；1994論文摘要另載33天（23–55）。這是兩篇出版品的不同資料，關係未證實，不能稱1989同一原文內部不一致。
- Andersohn et al. 2007 系統性回顧（經 Vicente 2017 轉引）：PTU/carbimazole/methimazole 平均 36/41/42 天。
- Kobayashi et al. 2014（PMID 24341564, n=81）：首次療程中位 39 天（20–98）、第二次以後療程中位 32.5 天（21–95）——此為「未曾發病者再次用藥後首次發病」，非「已發病者安全 rechallenge」之證據。
- Nakamura et al. 2013（PMID 24057289）：**LlamaParse 對其 Figure 1/2/3 之圖轉數字表已確認不可信（機器生成資料與原圖不符），本節僅採用正文文字與圖說（caption），不引用圖轉表數值。** 正文 Results（p.4778）n=461，71.6% 於 60 天內、84.6% 於 90 天內；Abstract 另載 84.5%；Figure 2 圖說 n=458、84.6%；4 個月後發病者正文 55 例、圖說 54 例。**此 n=461/458、84.5%/84.6%、55/54 之不一致已以原始排版 PDF 視覺核對確認為原文本身之內部差異，非 OCR 或轉錄誤差**，本節如實並列，不擅自擇一版本。

**結論**：本案 43–48 天之發病時間並非離群值，落於上述文獻典型範圍（約 33–45 天中位數）與 Nakamura cohort 60–90 天窗口內，屬典型時序，支持 ATD 之時間關聯性（temporal plausibility），不需以「非典型時程」另作解釋。

## 五、「50%」與「15.2%」交叉反應率之 provenance（本輪已修正、確認版本）

此為使用者核心關切。**下列數字已由原始 PDF 全文（含 LlamaParse 之後之人工視覺核對）確認，非僅摘要層級**：

- **Meyer-Gessner et al. 1989**（p.169 左欄首段）：thiamazole（methimazole）/PTU 配對 **4/29 = 13.8%**；carbimazole/PTU 配對 **5/33 = 15.2%**；carbimazole/thiamazole 配對 **11/34 = 32.4%**。三者均為**藥物配對之整體不良反應（all adverse reactions）復發率**，原文未拆分換藥先後方向，亦未區分 ADR 類型（含皮疹、肝功能異常、關節痛等），**非 agranulocytosis-specific 之復發率**。同一世代（n=1256）中 agranulocytosis 本身發生率僅約 0.14–0.18%。
- **Vicente et al. 2017**（Drugs R D, PMC5318340）於「治療」段落引用 carbimazole／PTU cross-reaction 15.2%；其 PDF 第6頁 reference32 為 **Meyer-Gessner 1994，J Endocrinol Invest 17:29–36，DOI 10.1007/BF03344959**，已由 root 直接視覺核對。先前本檔寫1989有誤，已更正。1989原文確有5/33（15.2%）的 all-ADR 數字，但1989與1994的資料關係尚未證實，不可宣稱此引用鏈已完整接通；尤其不能把1989的 all-ADR 端點當作 agranulocytosis-specific 再發率。
- **Otsuka et al. 2012**（Clin Endocrinol, PMID 22332800, p.313 Table 4）：MMI→PTU **14/41 = 34.2%**、PTU→MMI **9/30 = 30.0%**，同樣為換第二種 ATD 後之**整體不良反應**發生率（因該不良反應而停第二種藥者分別為 11/41、6/30），非 agranulocytosis-specific；此研究之換藥子群本身已排除 diabetes、heart failure、atrial fibrillation 及 severe thyrotoxicosis 患者，不能作為本案（HFrEF 背景）之風險估計。
- **「50%」（含常見的「高達 50%」「30–50%」說法）**：JAMA 2015（Burch & Cooper, PMID 26670972）Table 4 將 30–50% 置於 **rash／皮膚反應**欄位並引用 Otsuka 2012，惟本輪已直接核對 Otsuka 原文 Table 4–5，**無法由原始表格重現 rash-specific 之明確分子分母**，此引用鏈之「原始 rash 分母」本身仍未解決（OPEN）。另一條獨立成因：至少一篇 2026 年 case report（Voci et al., PMC13133480）將「高達 50%」歸因於 Vicente 2017，但 Vicente 全文查無此語句（其唯一「50%」為 ATD 長期緩解率，與 cross-reactivity 無關），屬可查證之引用鏈失真。
- 本輪找到的 agranulocytosis-specific 個案證據為 case report 層級：Chen et al. 1983（PMID 6865827，PTU→agranulocytosis→methimazole→10 週後再次 agranulocytosis）；另有 Ostlere & Apthorp 1988（PMID 3256337，carbimazole 與 PTU 依序使用後再發，方向與本案 carbimazole 暴露更相近）。兩者僅支持「可能發生」，無法提供發生率。

**結論（本輪最終立場）**：**不應以 15.2% 或 50% 之任一數字，估計本案病人若使用 PTU 之 agranulocytosis 復發機率**——前者為不同端點（整體 ADR）之已確認數字，後者原始分母未解決。ATA 2016（Ross et al., PMID 27521067）guideline 方向明確：發生嚴重 ADR（含 agranulocytosis）後，另一 thionamide 應視為 contraindicated；**此建議包含一個範圍極窄的例外——僅限危及生命之 thyroid storm 情境下短期考慮 PTU，並非門診穩定期之常規換藥策略**。此建議之證據基礎為個案報告與 class-wide 免疫機轉之合理性，而非精確量化復發率。

## 六、Definitive therapy 之血液科補充意見

本案 Day 57 曾有 necrotizing pneumonia resolution delayed 之記錄，顯示 ANC 恢復（Day 51 起 4.14×10³/µL）不等同於感染已完全清除。本次查核未找到文獻明確定義「ATD-induced agranulocytosis 恢復後之安全手術感染清除門檻」。**此為缺口，非自動排除任一路徑之理由**——surgery 或 RAI 之選擇仍應由多科團隊依當下臨床穩定度（含心肺、腎功能軌跡、碘暴露 washout）綜合判斷，非本 session 單方面可代為決定。本案已確認之類固醇為 case synopsis 明載的 empiric hydrocortisone。

---

## 證據表（精簡版；完整版見前版本歷史，已由本檔取代）

| # | 主題 | 文獻 | 設計／分母 | Locator | 核對層級 |
|---|---|---|---|---|---|
| E1 | Agranulocytosis 定義；84.5%/84.6%、n=461/458 內部不一致 | Nakamura et al. 2013, PMID 24057289 | Retrospective 通報系列, n=754（時序子群 461/458） | Abstract p.4776；Results/Fig.2 p.4778 | 原始 PDF 視覺核對；圖轉表數值不採用 |
| E2 | Severe（ANC<100）亞群 | Mao et al. 2026, PMC13494723 | Retrospective, n=24 | Results | PMID/PMC 摘要 |
| E3 | Allopurinol 罕見性 | PMC11878856 | Case report + review | Abstract | 摘要層級 |
| E4 | G-CSF：小型 RCT（未證實效益） | Fukata et al. 1999, PMID 10037073 | RCT, n=24 | Abstract | PubMed 摘要 |
| E5 | G-CSF：回溯性 cohort | Andrès et al. 2001, PMID 11493719 | Retrospective, n=20 | Abstract | 二手轉引（Vicente 2017），未獨立取得全文 |
| E6 | G-CSF：統合分析 | Wang et al. 2019, PMID 31824417 | Meta-analysis, n=474 | Abstract | PubMed 摘要 |
| E7 | Meyer-Gessner 1989 交叉反應分子分母 | PMID 2464468 | Retrospective, n=1256 | p.169 | **原始 PDF 全文＋視覺核對，CONFIRMED** |
| E8 | Otsuka 2012 交叉反應分子分母 | PMID 22332800 | RCT 分組後 ADR 分析, n=449（randomized）/391（可分析） | p.313 Table 4 | **原始 PDF 全文＋視覺核對，CONFIRMED** |
| E9 | Vicente 2017 ref32 書目 | PMC5318340 | Narrative review | PDF第6頁 References | Root 已原PDF視覺確認為 Meyer-Gessner 1994，DOI 10.1007/BF03344959；本角色未獨立核對；與1989資料關係未證實 |
| E10 | 「50%」引用鏈失真 | Voci et al. 2026, PMC13133480 | Case report | Introduction | WebFetch 全文核對 |
| E11 | ATA 換藥 contraindication（含 storm 窄例外） | Ross et al. 2016, PMID 27521067 | Guideline | E6，印刷 p.1357／PDF第15頁；E7 minor rash 位於 p.1358 | Root 已直接核對原始 PDF；本角色未獨立核對該頁 |
| E12 | Agranulocytosis-specific case report（n=1×2） | Chen 1983 PMID 6865827；Ostlere & Apthorp 1988 PMID 3256337 | Case report | Abstract | PubMed 摘要 |

---

## 建議（Conditional）

1. 不建議常規於已發生 agranulocytosis 後改用 PTU 或其他 thionamide；此建議依 guideline-level 立場與免疫機轉合理性，**不依賴任何精確交叉反應率數字**，且僅在危及生命之 thyroid storm 情境保留極窄例外，非本案目前狀態之常規選項。
2. 不應將本案 Day 48→51 之 ANC 恢復無條件歸因 G-CSF；建議以「時序相符、因果未證實」表述。
3. Allopurinol 確切用藥時間軸仍為缺口，建議補齊以完成正式因果評估。
4. 手術/RAI 之感染與骨髓雙重就緒門檻查無文獻明確定義，屬多科共同決策事項，不應僅憑此缺口逕行排除任一路徑。

## 跨角色討論狀態

- **CHALLENGE-hematology-001**（→ Endocrinology）：本輪已收到 Endocrinology 直接回覆（`FINAL-REVIEW-endocrinology-001`，in_reply_to=FINAL-REVIEW-hematology-001）：確認「避免 PTU」不依賴量化交叉反應率、僅依 guideline-level 立場；desensitization 文獻僅涵蓋 hypersensitivity、無 agranulocytosis-specific 證據（維持其 OPEN-ENDO-007，非本 session 可關閉之項目）。本 session 已以 ACK-hematology-final-001 確認收訖。**狀態：OPEN-HEMA-1 已解決（RESOLVED，基於本 session 實際收到之逐字 RESPONSE）。**
- **CHALLENGE-hematology-002 / CHALLENGE-methods-002**（與 Methods，前一輪）：雙方已就「不歸因 G-CSF」「Nakamura 內部不一致」「15.2%/50% 端點區分」達成一致並交叉確認，**視為已收斂（非本輪重新開啟）**。
- 完整逐字對話見 `sessions/messages/hematology_dialogue.md`（前一輪記錄保留，本輪新增訊息附加於檔尾）。

## Peer Review（依本輪已讀之 peer roles/*.md 正文）

- `roles/methods.md`：Meyer-Gessner 1989／Otsuka 2012分子分母與本檔一致；其先前保留的Vicente ref32=1994讀取結果，現由root直接原PDF核對確認。修正依據為原始書目，非權威身分或指示本身；1989與1994的資料關係仍未證實。
- `roles/endocrinology.md`：ATA storm窄例外與EANM正常腎功能前提之判讀一致。ATA E6之印刷p.1357／PDF第15頁現由root直接核對；兩角色均未獨立核對該頁，不能再稱無人核對。
- `roles/nuclear_surgery.md`：對「手術/RAI 兩路徑目前皆有未滿足前提，不宣稱其一已無禁忌」之立場與本檔第六節一致，無牴觸。

## OPEN 清單（本輪最終）

- ~~OPEN-HEMA-1~~：已解決，見上方跨角色討論狀態。
- **OPEN-HEMA-3**：Allopurinol 確切用藥時間軸未知。
- **OPEN-HEMA-4**：ATD agranulocytosis 恢復後之安全手術門檻查無文獻定義。
- **OPEN-HEMA-5**：Meyer-Gessner 1989 換藥先後方向別、各類 ADR 個別再發率未拆分（僅有配對層級整體數字）。
- **RESOLVED-HEMA-6（root 原文核對）**：ATA 2016 E6印刷p.1357／PDF第15頁已由root直接核對；本角色未獨立核對該頁。
- **OPEN-HEMA-7**（新增）：JAMA 2015 rash 30–50% 之原始 rash-specific 分子分母，經本輪核對 Otsuka 2012 Table 4–5 仍無法重現，維持未解決。
