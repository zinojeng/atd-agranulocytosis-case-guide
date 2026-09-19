# Definitive Therapy 角色紀錄（ATD-ANC-R2-Definitive）

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

> Root 編輯校正（2026-09-19）：兩輪 Claude Code 交叉審查後，root 核對去識別化病史與 [Gao 2026 原文](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1770772/full)，將「Lugol 實際使用超過兩週」改為只寫住院紀錄與未核實的出院用藥，並將 0/46 vs 3/100 thyroid storm 事件改為檢定力不足、不可推論保護效果。歷史對話檔保留角色原始提問與傳輸結果；後編不冒充 peer 已重新同意。


## ACK 與範圍界定
已讀取 `CLAUDE.md`、`research/case_synopsis.md`；未讀取 `private/patient_normalized.txt` 或任何原始病歷、未讀取 `private/*.json`（MCP config 載入除外）。個案一律以 Day-relative 表示，不含病歷號、姓名、院所、醫護人員或確切就醫日期。本檔僅由本 session 寫入，另擁有 `sessions/messages/r2_definitive_therapy_dialogue.md`；不修改其他角色檔案、不執行 git/push/merge/刪除/設定變更。

本備忘為**條件式研究討論**，用於支持多專科會診與病人共同決策，**不構成個別劑量調整或立即執行手術／RAI 之指示**；文獻中出現之劑量、濃度數字僅描述該文獻之作法，不應直接套用為本案處方。

本輪額外讀取（非覆寫）先前 run（ATD-ANC-R1）之 `roles/endocrinology.md`，其中 EANM washout 與 Meyer-Gessner 換藥復發率章節已由 root 對照原始 PDF 逐頁核對；本檔對其中與本案主題重疊之結論（EANM Table 1、Gao 2026 lithium cohort 存在）採信但本 session 另行獨立以 PubMed／Crossref 重新核對書目與摘要內容（見下方引註），不盲目複製其分類判斷。

---

## 個案關鍵事實摘要（僅摘錄與 definitive therapy 決策相關者）

| 相對日 | 與本決策相關之事實 | 解讀限制 |
|---|---|---|
| Day 48 | Chest CT 使用 Omnipaque 350（iohexol）75 mL；ANC 0.05×10³/µL；CT 開立資訊列 Cr 0.94／eGFR 約 65，同日另處記錄 Cr 1.53 mg/dL；RML pneumonia | 兩筆 Cr 數值與顯影劑注射之採檢時刻未分鐘級對齊，**不可推論顯影劑注射當下已存在 AKI，亦不可將 Cr 變化歸因於顯影劑**（原表述有過度推論，已於下方 R2 Peer-Review Addendum 更正） |
| Day 48–49 | 停 carbimazole、避免 PTU；改用 Lugol/KI（濃度、實際劑量、最後一劑未知） | Iodine washout 起算點不明 |
| Day 49–55（門診處方延續至 ≥Day 64） | Lugol 2 mL Q8H → 出院後 2 mL daily | 累積暴露時間已逾 2 週，屬長期而非短期 iodide 準備 |
| Day 51 | ANC 4.14×10³/µL；Cr 降至 0.59 mg/dL | 腎功能已恢復，但 Day 48 顯影劑給藥「當下」腎功能是否正常仍不明 |
| Day 57 | RML necrotizing pneumonia 緩慢吸收、接近 abscess；FT4 1.21；門診加開 lithium carbonate 150 mg daily | 感染未確認清除；lithium 起始時 FT4 已在下降軌跡 |
| Day 59 | FT4 1.13 ng/dL（ref 0.70–1.48）；lithium <0.2 mEq/L | 單次低濃度無法判斷達到治療濃度或僅反映採血時間點 |
| Day 64 | 門診偏向 thyroidectomy，病人仍在考慮；I-131 因近期 contrast／Lugol 暴露需評估延後 | 無 Day 64 新抽血；未見腎功能、CXR、echo 最新資料 |
| 結節 | 右 1.36 cm、左 0.80 cm solid hypoechoic，均有 microcalcification、ill-defined border；taller-than-wide 陰性；vascularity normal；無 FNA、無原始影像複核、無完整頸部淋巴結 mapping | 「ill-defined」不可逕自改寫為 ATA 定義之「irregular margin」 |
| 心臟 | Echo：四腔擴大、global LV hypokinesis，EF ~32%（既往檢查，非最新） | 無更新 EF／volume status |

---

## 一、Iodide／Contrast Washout 與 RAIU 判讀

本案在 RAI 候選路徑上同時有兩種碘暴露：Day 48 水溶性含碘顯影劑（iohexol）與 Day 49–55 住院期間記錄的 Lugol's iodine；出院另有持續處方，但實際服用天數與最後一劑尚未核實。兩者的劑量與清除條件不同，washout 所需時間不能互相替代估算。

- **The EANM guideline on radioiodine therapy of benign thyroid disease**（Campennì A et al., *Eur J Nucl Med Mol Imaging* 2023; DOI 10.1007/s00259-023-06274-5；PMID 37395802）— **guideline**。本 session 直接 WebFetch PMC 全文（PMC10542302）Table 1「Thyroid drugs and iodide-containing substances that can reduce radioiodine thyroid uptake」：水溶性 IV 含碘顯影劑建議等待 **6–8 週，前提為腎功能正常**；脂溶性（oil-based）顯影劑建議 **3–6 個月**。此為本 session 直接核對之一手表格內容，非轉引。
- **本案關鍵交織點**：Day 48 CT 開立資訊列 Cr 0.94／eGFR 約 65，同日另處記錄 Cr 1.53 mg/dL；**兩者與顯影劑注射之採檢時刻未分鐘級對齊，不可逕自解讀為「顯影劑給藥當下腎功能軌跡正處於上升段」**（此為本檔前版之過度推論，已於下方 R2 Peer-Review Addendum 更正）。是否符合 guideline 前提「腎功能正常」，現有資料不足以由給藥「當下」瞬時腎功能判斷，僅能確知同一天內存在兩筆數值不同的肌酸酐記錄，且先後順序未知；Day 51 已見 Cr 0.59，但其後（Day 64）無新腎功能數據。**guideline 本身未針對「顯影劑給藥當下腎功能不明或異常」提供替代等待週數**，僅以前提句排除該情境的適用性，這是一個 guideline 未直接覆蓋、需以直接量測（RAIU 或尿碘／肌酸酐比值）取代日曆天數推算的實務缺口。
- **Lugol/SSKI 部分——跨 guideline 分歧（本輪經 ATD-ANC-R2-Safety 全文核對確認）**：`roles/endocrinology.md`（EANM Table 1）記載一般建議等待 2–3 週；但 **Taylor et al. 2026 joint consensus statement on thyroid storm**（*Eur Thyroid J*, DOI 10.1530/ETJ-26-0043, PMID 42554462）之「Iodine/potassium iodide」段落原文明確載：「radioiodine is generally deferred for at least 2–3 months」，**此建議明確針對口服／鼻胃管碘劑（Lugol/SSKI），非 IV 含碘顯影劑**，不可與顯影劑之 washout 數字互相類比。此為 ATD-ANC-R2-Safety 以 WebFetch 直接核對 PMC13506520 全文後確認之**真實跨 guideline 分歧**（2–3 週 vs. 2–3 個月，相差 4–6 倍），非誤讀或轉引錯誤。本案 Lugol 暴露已超過 EANM 之 2–3 週窗口（Day 49 至至少 Day 64，逾 15 天，且門診處方顯示可能仍在使用），**但未必滿足 Taylor 2026 更保守之 2–3 個月標準**；「最後一劑時間」與「實際濃度」在案例底稿中仍明確標註未知。**若採較保守標準，本案 RAI 時機判斷會較本檔前版之推論更為延後**；本檔不代為判斷應採用哪一套 guideline，此屬臨床團隊之判斷，但要求任何後續引用時應並列兩套數字，不可僅採較寬鬆之 EANM 版本而略去 Taylor 2026。
- **建議（條件式，非劑量指示）**：若考慮 RAI 路徑，應以**直接量測**（24 小時 RAIU、必要時尿碘／肌酸酐比值）取代單純日曆天數推算，且應與腎功能同次評估，而非分別解讀。此為與 ATD-ANC-R2-Safety 之交界议题（見後方 CHALLENGE）。

---

## 二、HFrEF、近期 AKI、進行中肺部感染對時機與安全性之影響

### HFrEF（EF ~32%，四腔擴大、global hypokinesis）
- **Kositanurit W et al., "Clinical phenotypes and prognosis of thyrotoxic heart failure and cardiomyopathy in patients hospitalized for acute heart failure"**, *ESC Heart Fail* 2021; DOI 10.1002/ehf2.13347；PMID 33932131 — **cohort**（retrospective，2002–2017，11,109 例 acute HF 住院中 92 例〔0.8%〕thyrotoxic HF，87 例有完整 echo 資料進入分析）。58% 符合 thyrotoxic cardiomyopathy（LVEF<55%）；**definitive therapy 後 LV recovery 率 69%**；thyrotoxic HF 存活率優於一般 acute HF 對照組（HR 4.3, 95% CI 2.1–9.5）。追蹤期長度未見於摘要層級（**OPEN**，需全文查證）。
- **限制與推論分層（interpretation, 非該文獻直接結論）**：此 cohort 未依「RAI vs. 手術」拆分 LV recovery 結果，不能用以主張任一 definitive modality 對心臟恢復較優；僅能支持「thyrotoxicosis 獲控制後 HFrEF 有相當機率可逆」此一方向性推論，且本案病人年齡層、BSA、右心負荷等特徵是否貼合該 cohort（該研究描述之典型表現為 small BSA、middle-age female、HFpEF/right-sided HF 為主）需另核對。
- **手術麻醉風險**：本輪搜尋未取得針對「HFrEF 患者接受 thyroidectomy」之專門 cohort（PubMed 查詢空結果，已記為證據缺口）。Voci et al. 2026（見下）以 right heart catheterization 確認手術適合度，是目前唯一與本案「低 EF＋考慮 thyroidectomy」直接可比的已發表案例，但仍為單一案例，非可推廣結論（詳見第六節比較表）。

### 近期 AKI
- 與顯影劑 washout 前提直接相關（見第一節）；亦與 lithium 安全性直接相關（lithium 經腎清除，腎功能波動會使血中濃度不可預測）——此為對 ATD-ANC-R2-Safety 之核心 CHALLENGE 內容。
- 若走手術路徑，麻醉／液體管理與近期 AKI 病史相關的一般外科風險原則適用，但本輪未取得針對「近期 AKI 恢復期患者接受 thyroidectomy」之專門文獻，亦記為缺口。

### 進行中肺部感染（RML necrotizing pneumonia，Day 57 描述接近 abscess）
- 本輪 PubMed 搜尋「thyroidectomy 於未痊癒肺部感染／膿瘍病人之時機」未取得直接文獻（空結果）。**此為推論而非文獻直接支持**：全身麻醉、頸部過伸體位、術後咳嗽排痰能力下降等因素，一般外科教學上會建議延後至急性感染／膿瘍傾向穩定或吸收後再排定非急迫性手術；本案是否符合「必須立即手術」之急迫等級（例如氣道壓迫、惡性確診）目前無資料支持，故此原則性延後建議是否適用仍待 CaseDx／Safety 對感染嚴重度與手術急迫性之判斷整合。
- **RAI 路徑同樣不能忽略感染狀態**：活動性發炎／感染可能干擾當下 RAIU 判讀，且若計畫使用 RAI 仍需確認肺部狀況足以耐受治療後可能的短暫代謝負荷與臥床。

---

## 三、惡性結節疑慮與 Ultrasound／FNA 閾值

### 指引依據
**Haugen BR et al., 2015 American Thyroid Association Management Guidelines for Adult Patients with Thyroid Nodules and Differentiated Thyroid Cancer**, *Thyroid* 2016;26(1); DOI 10.1089/thy.2015.0020；PMID 26462967 — **guideline**（本 session 僅取得摘要層級，未逐頁核對原文 sonographic pattern 表格頁碼，此為locator 限制，標記為 OPEN）。指引核心：具 microcalcification 之 solid hypoechoic 結節屬 high suspicion pattern（不論邊界描述為 irregular 或其他），建議 malignancy risk 70–90%，≥1 cm 建議 FNA；若無 microcalcification／irregular margin／taller-than-wide 之單純 hypoechoic solid 結節屬 intermediate suspicion，risk 10–20%，同樣 ≥1 cm 建議 FNA。

### 對本案兩顆結節的條件式對應（非診斷結論）
- **右側 1.36 cm**：具 microcalcification，符合 size 閾值（≥1 cm），依上述指引屬**建議 FNA** 之類別，不論邊界最終判定為 ill-defined 或 irregular。
- **左側 0.80 cm**：<1 cm；依指引，即使具 high suspicion 特徵，**未達 FNA 建議之 size 閾值**，除非合併其他風險因子（異常頸部淋巴結、家族史、頭頸部放射線暴露史等）——這些因子在案例底稿中均未見記載或明確排除，屬 **OPEN**。
- 案例底稿明確保留「ill-defined 不可逕自改寫為 irregular margin」——此區分在指引風險分層中對「邊界」條件有意義，但因兩顆結節均已有 microcalcification（本身已達 high suspicion 門檻的獨立條件），故此區分對「是否建議 FNA」的結論影響有限；但對於**術前病理預期溝通**（例如向病人說明惡性機率區間）仍有意義，不應忽略。

### 佐證用實證數據（cohort，非本案專屬）
- **Yoon JH et al.**, *Radiology* 2016; DOI 10.1148/radiol.2015150056；PMID 26348102 — **cohort**（retrospective，1293 顆 ≥1cm 結節，2013–2014）：依 2014 ATA pattern 分層之惡性率——very low 2.7%(11/407)、low 3.1%(10/323)、**intermediate 16.7%(39/233)**、**high 58.0%(166/286)**、not-specified 18.2%(8/44)。
- **Chng CL et al.**, *Singapore Med J* 2018; PMID 29774361 — **cohort**（167 顆 >1cm 結節，150 名病人，5.5 年）：惡性結節中 microcalcification 佔 33.3% vs 良性 8.0%（p<0.001）；ATA 分層 sensitivity 98.0%／specificity 17.3%。
- **Valenzuela-Scheker E et al.**, *Endocrinol Eur* 2024; DOI 10.17925/EE.2023.20.1.2；PMID 38812666 — **cohort**（5,040 顆結節資料庫，1,772 顆有手術病理；聚焦 150 顆 2015 ATA 系統無法分類之 solid atypical mixed echogenicity nodules〔SAMEN〕，60 顆手術）：SAMEN 整體 ROM 31%；**惡性 SAMEN 中 70%（28/40）具 microcalcification**，支持 microcalcification 作為獨立高風險特徵之權重。

### 結節與 Graves 共存之惡性風險與行為（與 CaseDx 交界）
- **Mishra A, Mishra SK**, *?* 2001; PMID 11832639 — **cohort**（retrospective，130 例手術治療 Graves 病人，1990–99，碘缺乏地區；追蹤中位數 5.5 年）：35/130（26.9%）有可觸及結節；Graves 合併結節之甲狀腺癌發生率 17.1%（6/35），冷結節惡性率 20%；作者建議此族群「early thyroidectomy」。
- **Cappelli C et al.**, 2006; PMID 16440157 — **cohort**（retrospective，2449 例甲狀腺機能亢進評估病人，1985–2001，義大利）：Graves 合併甲狀腺癌 6.5% vs 單一毒性結節 4.4% vs 多發性毒性結節 3.9%；Graves 合併癌症之淋巴結侵犯率 56%，高於 MTG 之 23%、UTG 之 0%——**作者推論 Graves 合併之甲狀腺癌可能較具侵襲性**（interpretation，非隨機對照證據，且地區碘營養狀態可能為干擾因子，未見以本案地區資料重複驗證）。
- **本案交界問題**：TRAb 3.00 IU/L 落在該 assay 一般參考值與 Graves cutoff 之間，且近期 ATD／iodine 暴露會干擾後續 TRAb 或 uptake 判讀（見 CaseDx 領域）；若病因確為 Graves 而非單純 toxic nodule，上述兩篇 cohort 提示合併結節時之惡性與淋巴結侵犯風險不可依「Graves 通常為良性瀰漫性腫大」的既定印象而降低警覺。**此為送予 CaseDx 之 CHALLENGE 核心之一**。

---

## 四、Preoperative Euthyroidism 爭議：ATD 禁忌下之替代準備方案

### 傳統教學 vs. 本案限制
傳統教學要求 thionamide＋iodine＋beta-blocker 達成生化 euthyroid 後再手術，以降低甲狀腺風暴風險；本案因 agranulocytosis 已排除 carbimazole，且案例底稿明確載明「避免 PTU」，故傳統路徑不可行，必須仰賴替代方案。

### 現有替代方案之證據分層
- **Lithium carbonate 作為橋接**：
  - **Gao X et al., "Lithium carbonate bridging and outcomes of radioiodine therapy in severe Graves' disease: a retrospective cohort study"**, *Front Endocrinol* 2026;17; DOI [10.3389/fendo.2026.1770772](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1770772/full) — **single-center retrospective cohort**（n=146：lithium 組 46 例、標準照護組 100 例）。報告 6 個月 euthyroid 30.4% vs 13.0%，hypothyroid 54.3% vs 77.0%；thyroid storm 事件為 **0/46 vs 3/100**，作者明言樣本對此類罕見事件的檢定力不足，**不能推論 lithium 降低 thyroid storm 風險**。研究排除 severe renal impairment（eGFR<30），且針對 RAI 而非手術前橋接；不能以其濃度或安全性結果直接替本案設定目標。
  - **Rabelo PN et al.**, *Rev Assoc Med Bras* 2019; DOI 10.1590/1806-9282.65.6.755；PMID 31340298 — **case report**（n=1，PTU-induced agranulocytosis）：beta-blocker＋glucocorticoid＋lithium carbonate＋Lugol solution 橋接後 total thyroidectomy，術後無併發症。
  - **Barwinek K et al.**, *Medicina (Kaunas)* 2020; DOI 10.3390/medicina56060290；PMID 32545570 — **case report**（n=1，methimazole-induced agranulocytosis＋giant toxic nodular goiter）：steroid＋beta-blocker＋**propylthiouracil**（！注意：此案在 methimazole 誘發 agranulocytosis 後仍嘗試低風險再引入 PTU，與本案「避免 PTU」之決策方向不同，屬**選定個案的風險耐受策略，非可推廣建議**）＋Lugol＋lithium＋antibiotics＋2 次 plasmapheresis，總甲狀腺切除順利。
  - **Voci A et al., "Dual Antithyroid Drug-Induced Agranulocytosis in Graves' Disease With Decompensated Heart Failure: A Multidisciplinary Approach"**, *Clin Med Insights Case Rep* 2026;19; DOI 10.1177/11795476261446355；PMID 42078037 — **case report**（n=1，54 歲男性，2 年 Graves 病史，MMI 後 PTU 相繼引發 agranulocytosis，合併 decompensated HF EF 35%、COPD）：Lugol's iodine＋G-CSF 橋接後以 right heart catheterization 確認手術適合度，成功 total thyroidectomy。**此為目前與本案最接近之單一案例**（agranulocytosis＋低 EF 心衰竭＋手術路徑），但此案**無 AKI、無惡性結節疑慮、無合併活動性肺部感染**，且性別、年齡、Graves 病程長度均不同——**是選定的成功個案，不是可推廣結論**，本案不能假設相同橋接方案必然同樣安全有效。（此篇由 ATD-ANC-R2-Publication 提出，本 session 已獨立以 PubMed 全文摘要與 Crossref DOI 二次核對，非單方轉引。）
  - 較舊之小型系列／案例（**interpretation 層級較低，僅供背景**）：Tsunoda T et al. 1991（PMID 1713279，case series n=12）、Mochinaga N et al. 1994（PMID 8054820，case report n=2，lithium 單獨使用，濃度 0.43–0.83 mEq/L）、Akin F et al. 2008（PMID 18287805，case series n=6）均描述 lithium 單獨或合併使用之良好結果，但樣本數小、無對照組。
  - **重要反例（counter-evidence，不可省略）**：**Reed J, Bradley EL**, 1985; PMID 3933136 — **case report**（n=1）：lithium 單獨術前準備達到極佳生化控制，但**術後仍發生 thyroid storm**；作者推論手術操作可能促使殘留甲狀腺內已合成賀爾蒙釋放，而 lithium 主要機轉為抑制釋放而非如 thionamide 般長期耗竭合成儲量，故單用 lithium 準備、未搭配足夠時間之碘或其他抑制合成手段時，仍可能因手術操作誘發風暴。此案提示：**RAI 不涉及機械操作腺體，其「免 ATD 前處置仍安全」之推論（見 Vijayakumar 2006，第五節）不能直接外推至手術路徑**，兩種 definitive modality 對「未完全耗竭賀爾蒙儲量」之風暴風險並非等價。
- **Plasmapheresis 作為額外橋接選項**：
  - **Rami I et al.**, *J Med Case Rep* 2024; DOI 10.1186/s13256-024-04480-9；PMID 38553729 — **case series**（n=3，含 1 例 drug-induced agranulocytosis）：plasmapheresis 有效降低循環甲狀腺賀爾蒙，為 total thyroidectomy 爭取準備窗口。
  - 本案目前僅使用 Lugol／lithium，**尚未使用 plasmapheresis**；若現有橋接效果不足（例如需要更快速控制以縮短感染期暴露），plasmapheresis 是文獻上有先例、但本案尚未嘗試的選項，屬「可能改變決策路徑」的證據類別之一（見第七節）。

### 小結（interpretation）
現有文獻支持「ATD 禁忌時，lithium／Lugol／steroid／plasmapheresis 組合可作為手術或 RAI 前之替代準備」的方向，且多數已發表個案結果良好；但（a）多為 case report／小型 series，(b) Reed 1985 顯示 lithium 準備仍有術後風暴之個案風險，(c) 較嚴謹的 cohort 級證據（Gao 2026）是針對 RAI 而非手術前橋接。**本案若走手術路徑，現有證據強度僅達「多篇一致方向之案例報告」層級，非 cohort 級別的手術安全性保證**；此為誠實揭露之證據限制，而非建議停用現行橋接方案。

---

## 五、Perioperative Bridge 與 RAI 治療後 Hormone Release Risk

### 手術路徑之 perioperative bridge（條件式整理，非處方建議）
- Beta-blockade（案例已使用 bisoprolol）：跨文獻一致作為基礎用藥，不論走 RAI 或手術路徑。
- Lugol／lithium 之角色與限制已於第四節詳述；**延長使用 Lugol（本案已逾 2–3 週建議窗口）需留意 iodine escape 現象**（甲狀腺脫離 Wolff-Chaikoff 抑制、FT4 反彈），但本案目前 FT4 仍呈下降軌跡（Day48 1.61→Day59 1.13），暫無 escape 之直接證據；此為需持續追蹤而非現在下結論的項目。
- Adrenal reserve：案例中 ACTH 曾 <5、後 11.8 pg/mL，單次數值不足以判定是否有持續性 central adrenal insufficiency；若手術採全身麻醉，是否需要 stress-dose steroid coverage 屬 Safety／Endocrinology 交界問題，本檔不做劑量建議。
- 術後低血鈣風險（副甲狀腺功能受手術影響）在近期 AKI 病史下，鈣／維生素 D 代謝之基礎狀態不明，屬額外監測考量而非本檔可下結論之項目。

### RAI 路徑之 hormone release／thyroid storm risk
- **Vijayakumar V et al., "Is it safe to treat hyperthyroid patients with I-131 without fear of thyroid storm?"**, *Clin Nucl Med* 2006; PMID 16922465 — **cohort**（retrospective，single center，122 patient-visits，2003年8月–2004年12月）：以 beta-blocker 取代 ATD 前處置直接給予 I-131（370–740 MBq），**0/122 發生 thyroid storm**，含 25% RAIU>65% 之高風險子群同樣未發生風暴。
- **關鍵適用性限制（本案不可忽略）**：該研究之嚴重甲狀腺機能亢進定義**明確排除「合併 complicating intercurrent disease」之病人**（原文用語）。本案同時具有 HFrEF、近期 AKI、進行中肺部感染（近 abscess）——**至少三項均可能構成該研究定義下之 intercurrent disease，故此篇最直接支持「RAI 免 ATD 前處置安全」之證據，其納入條件明確不涵蓋本案病人的臨床複雜度**，不能直接引用其「0% thyroid storm」結論套用於本案。此為對 ATD-ANC-R2-Safety 之 CHALLENGE 核心之二。
- Gao 2026（見第四節）提供 RAI 前 lithium 橋接的回溯比較資料，但 thyroid storm 僅 0/46 vs 3/100，檢定力不足，**不可稱已證明降低風險**；本案的近期腎功能變化與心衰竭用藥也限制安全性外推。
- **RAI 劑量遞送層面的另一風險（非安全性、而是療效不足風險）**：若 washout 未完成即給予 RAI，實際遞送至甲狀腺之輻射劑量可能因競爭性穩定碘而降低，導致治療不足、復發或需重複治療，而非單純「過度風暴」風險——此點常被忽略但與第一節 washout 討論直接相關。

---

## 六、文獻與本案之對照：Guideline／Cohort／Case Report／Series／Interpretation 分層

| 類別 | 來源（PMID/DOI） | 設計／分母／追蹤 | 與本案之直接可比性 |
|---|---|---|---|
| Guideline | Ross DS et al. 2016 ATA, PMID 27521067 | 124 條實證建議之整合指引 | 一般性甲狀腺機能亢進治療架構，未特別處理 agranulocytosis 後之橋接細節 |
| Guideline | Haugen BR et al. 2015 ATA nodule guideline, DOI 10.1089/thy.2015.0020 | Sonographic pattern 風險分層 | 直接適用於結節分層，但本 session 未逐頁核對原文頁碼（OPEN） |
| Guideline（本 session 已核對原文表格） | Campennì A et al. 2023 EANM, PMID 37395802, Table 1 | 含碘物質對 RAIU 抑制之等待建議：Lugol/SSKI 2–3 週；水溶性顯影劑 6–8 週 | 直接適用，但未涵蓋「顯影劑給藥當下腎功能不明」之情境 |
| Guideline（ATD-ANC-R2-Safety 已核對原文段落） | Taylor et al. 2026 joint consensus, PMID 42554462, DOI 10.1530/ETJ-26-0043 | Lugol/SSKI 後 RAI 建議延後至少 2–3 個月 | **與 EANM 2–3 週建議相差 4–6 倍，真實跨 guideline 分歧**，本案 Lugol 暴露可能不滿足此較保守標準 |
| Cohort | Kositanurit W et al. 2021, PMID 33932131（n=87/11109，追蹤期未載於摘要） | Thyrotoxic HF 預後 | 支持定性治療後 EF 可能恢復之方向，未拆分 RAI vs 手術 |
| Cohort | Gao X et al. 2026, DOI 10.3389/fendo.2026.1770772（n=146，6 個月追蹤） | Lithium bridging 於 RAI 前之效果 | 適應症為 RAI 前橋接，非手術前橋接；本案已用 lithium，方向一致 |
| Cohort | Vijayakumar V et al. 2006, PMID 16922465（n=122 visits） | RAI 免 ATD 前處置之安全性 | **明確排除 intercurrent disease，本案不完全適用** |
| Cohort | Yoon JH 2016／Chng 2018／Valenzuela-Scheker 2024（結節風險分層，n分別1293/167/150） | 惡性率依 US pattern | 支持右側結節達 FNA 建議門檻 |
| Cohort | Mishra 2001（n=130，追蹤5.5年）／Cappelli 2006（n=2449） | Graves 合併結節之惡性與侵襲性 | 提示不可因病因傾向 Graves 而降低結節警覺 |
| Cohort | Andrès E et al. 2002, PMID 12144912（n=90） | Drug-induced agranulocytosis 一般預後 | ATD 佔病因 23%，G-CSF 縮短恢復期，非手術/RAI 專屬 |
| Case report（選定個案，非可推廣） | Voci 2026／Rabelo 2019／Barwinek 2020／Reed 1985（各 n=1） | Agranulocytosis／低 EF／術後風暴之個案 | 方向不一致（多數成功、Reed 為失敗案例），凸顯個案間異質性 |
| Small series | Rami 2024（n=3）／Tsunoda 1991（n=12）／Akin 2008（n=6）／Mochinaga 1994（n=2） | Lithium／plasmapheresis 橋接 | 樣本小、無對照組，僅供方向性參考 |
| Interpretation | 本檔第一、二節之延伸推論 | 非直接引自單一文獻 | 明確標示為本 session 推論，非文獻結論 |

---

## 七、何種新證據可能改變 Definitive Therapy 決策

1. **直接量測之 RAIU 或尿碘／肌酸酐比值**：取代日曆天數推算，可直接判斷 RAI 路徑目前是否可行，或需要多久之後才可行——目前最欠缺且最可直接執行之關鍵資料。此點因 EANM（2–3 週）與 Taylor 2026（2–3 個月）對 Lugol washout 之建議相差 4–6 倍而更形重要：直接量測可繞開「該採用哪一套 guideline 日曆天數」之爭議。
2. **右側 1.36 cm 結節之 FNA 結果**：依 Haugen 2015 已達建議閾值；若為惡性或高度可疑，將使手術（而非 RAI）成為病因學上必要之選項，且不因心肺風險而被 RAI 取代，只能轉為「如何降低手術風險」而非「是否手術」的問題。
3. **甲狀腺 scintigraphy／功能定位**：釐清結節為 hot 或 cold、病因為 Graves 或合併 toxic nodule，同時影響惡性風險判讀（見 Mishra 2001、Cappelli 2006）與 RAI 劑量反應之可預測性。
4. **最新 echocardiography／EF／volume status**：現有 EF 32% 為既往資料，若最新評估顯示已隨 FT4 下降而部分恢復（呼應 Kositanurit 2021 之 69% LV recovery 方向），會顯著降低手術麻醉風險分級；反之若仍嚴重低下，則會加重對「先控制心臟、延後 definitive therapy」策略之考量。
5. **胸腔影像追蹤（RML 病灶吸收軌跡、是否形成確定 abscess 需引流）**：若確認持續吸收中且無需介入性引流，可支持排定非急迫性手術；若惡化或形成需引流之膿瘍，兩種 definitive modality 皆須重新評估時機。
6. **Lithium 給藥、採血時刻與腎功能之同步追蹤**：核對 150 mg daily 是否確實使用、Day 59 採血距末次給藥多久，並結合 FT4／FT3 與腎功能趨勢評估；他篇研究的濃度區間不能直接當成本案的個別目標（詳見致 Safety 之 CHALLENGE）。
7. **病人自身偏好**：案例底稿明確記載「病人仍考慮」；在兩條路徑均有各自未解決之前提缺口時，病人價值觀本身即是可能改變最終選擇的合法證據來源，非醫療證據不足之替代品。

---

## 致 Peer 之 CHALLENGE（摘要，逐字往來見 dialogue 檔）

1. **→ ATD-ANC-R2-CaseDx**：TRAb 3.00 IU/L 落於一般參考值與 Graves cutoff 之間，且結節惡性風險判讀（Mishra 2001、Cappelli 2006 顯示 Graves 合併結節之惡性率與淋巴結侵犯率不低）與病因學判斷（Graves vs. toxic nodule）互相影響；請問是否有進一步病因學資訊（如是否曾安排 scintigraphy、頸部淋巴結描述完整度）可用以縮小此不確定性？另請確認「ill-defined border」與 ATA「irregular margin」定義是否等同，此區分雖不影響右側結節之 FNA 建議（已因 microcalcification 達 high suspicion），但會影響左側 0.80 cm 結節是否有除 size 外之額外風險因子需考慮 FNA。
2. **→ ATD-ANC-R2-Safety**：(a) Lithium 150 mg daily 處方後於 Day59 測得濃度 <0.2 mEq/L，但末次給藥至採血間隔未知；加上近期 AKI 病史與心衰竭用藥，是否足以判斷有效性或安全性？(b) Vijayakumar 2006（RAI 免 ATD 前處置安全性 cohort）之結論以沒有 complicating intercurrent disease 為條件，本案 HFrEF／近期 AKI／進行中肺部感染如何限制外推？請提供 Safety 角度對感染吸收軌跡的判讀，以協助辨認手術與 RAI 的時機限制。

---

## R2 Peer-Review Addendum（跨會期複審，本輪新增；不覆寫上方原始正文，僅在此追加更正與新內容）

### A. 範圍聲明
本輪為 root 指示之 cross-session review pass，延續同一 ATD-ANC-R2-Definitive 角色身分（非新人格）。本輪額外讀取：`reports/expanded_case_review_zh_TW.md`、`reports/case_report_publication_assessment.md`、以及本輪三份已完成之 peer 角色檔（`roles/expanded_case_diagnosis.md`、`roles/expanded_drug_safety.md`、`roles/expanded_publication_methods.md`）。此輪偵測到底層 session 之 socket／PID 與先前一輪不同（peer 名稱相同但為新啟動之實例），故上方「致 Peer 之 CHALLENGE」與 `sessions/messages/r2_definitive_therapy_dialogue.md` 中標記為「傳輸失敗」之訊息，其原始收件對象已確認結束；本輪已收到三方以新實例重新送達或透過讀檔取得之回覆，詳見對話檔更新。

### B. 更正本檔自身之過度推論（erratum）
上方「個案關鍵事實摘要」表格 Day 48 列與第一節「本案關鍵交織點」原表述為「Day 48 顯影劑給藥當下腎功能軌跡正好處於 Cr 0.94→1.53 上升段」，並在表格中標註「Cr 0.94→1.53 mg/dL（AKI 軌跡）」。**此為本檔前版之過度推論，已於本輪直接修正原文**：case synopsis 實際記載為 CT 開立資訊列 Cr 0.94／eGFR 約 65，另一處記錄同日 Cr 1.53 mg/dL，兩者與顯影劑注射之採檢時刻**未經分鐘級對齊**，因此**不能推論顯影劑注射當下已存在 AKI，也不能將後續 Cr 變化歸因於顯影劑**——原表述隱含之時序因果為本檔之錯誤，非 case synopsis 原文之限制被本檔正確傳達。此更正與 `roles/expanded_case_diagnosis.md` 第一節（Day 48 小節）之表述方式一致，本輪對齊之。同時明確區分三個不同時間點，避免任何潛在混淆：**Day 43 症狀發作（fever／sore throat）、Day 46 外院低 WBC（約 730/µL）、Day 48 入院確認 ANC 50/µL 併顯影劑注射／CT**——此三者為不同事件，不可合併敘述或互相取代。

### C. 對齊 Voci et al. 2026 之新意定位（避免誤讀）
本檔第四節稱 Voci 2026（PMID 42078037）為「目前與本案最接近之單一案例」，此描述本身不變，但本輪明確補充：`roles/expanded_publication_methods.md` 第二節已明確結論「不宣稱 first／unique」——**Voci 2026 已是一篇發表之 agranulocytosis＋低 EF 心衰竭＋手術個案報告，此組合本身不構成本案的新意來源**。本檔完全採納此立場，避免讀者誤以為本檔第四、六節之比較分析暗示本案在「agranulocytosis+HFrEF+surgery」此骨幹組合上有原創性；若本案有potential 貢獻，僅可能在於多軸線（AKI-washout、未確認清除之肺部感染、未活檢結節）同時交織之決策過程本身（詳見與 Publication 之最新往來，section D、E）。

### D. 新增文獻定位澄清：Fantin et al. 2021（conference abstract）
`reports/case_report_publication_assessment.md` 第二節引用 Fantin et al. 2021（*J Endocr Soc* Supplement，MMI-induced agranulocytosis、ANC 90/µL，短期 lithium 跨越 I-131、報告 1 個月後 euthyroid）——**此為 conference abstract，非完整同儕審查之 case report**，本檔第四、五節原未納入此篇，本輪予以補充列入 lithium→RAI 路徑之證據清單，與 Gao 2026（cohort）、Sazon 2024（conference abstract，同樣為 lithium＋prednisone→RAI 路徑）並列：三者共同顯示「lithium 橋接後走向 RAI（而非手術）」已有先例存在，但 Fantin／Sazon 兩篇僅達會議摘要層級，追蹤短、器官限制（HFrEF／AKI／肺炎）細節均未見於摘要，**不可比照 cohort 或完整 case report 之證據強度使用**。

### E. Peer-Review Findings（不修改對方檔案，僅記錄本檔之審閱意見）
- **CaseDx**（`roles/expanded_case_diagnosis.md`）：獨立以 ACR TI-RADS（Tessler 2017, PMID 28372962）計算兩顆結節之 composition+echogenicity+echogenic foci 已達 7 分（TR5 門檻），與本檔採用之 Haugen 2015 ATA size 閾值判讀（右側 1.36cm 建議 FNA、左側 0.80cm 除非額外風險因子否則落在追蹤區間）**方向收斂但依據系統不同**——兩套指引各自的 FNA size 門檻與風險分層邏輯不完全相同，本檔採信此收斂結果，但提醒後續正式引用時應分別標明所依循之指引（ACR TI-RADS vs. ATA 2015），不可混用點數與 pattern 分類。CaseDx 對 TRAb 病因信心層級之判斷（「中等偏弱，非高信心」，因 assay cutoff 灰區＋治療中濃度衰減效應）本檔採納，已於第三節之病因學前提中反映此不確定性。
- **Drug Safety**（`roles/expanded_drug_safety.md`）：其 OPEN-SAFETY-1（necrotizing pneumonia 影像清除時間常模查無專門文獻）、OPEN-SAFETY-4（lithium 與 ARNI／spironolactone 交互作用僅能以類別效應外推）均與本檔第二、四、五節直接重疊，本輪相互確認結論一致，未發現矛盾。本檔新增之 CHALLENGE-definitive-to-safety-002（見對話檔）針對其 OPEN-SAFETY-2（Taylor et al. 2026 joint consensus 僅摘要層級）提出更具體之查證請求：共用報告中一則「大量 iodide 後 RAI 應延後 2–3 個月」之量化聲稱缺乏本檔或 Safety 檔案中任何一手全文核對之明確定位，此為**本輪新識別之潛在未經證實之量化聲稱**，已正式提出查證請求，尚未獲答覆。
- **Publication**（`roles/expanded_publication_methods.md`）：其第二節「新意評估」與本檔第四節 Voci 2026 之定位互相一致（均不宣稱 first/unique）；經本輪 CHALLENGE-publication-003 往來確認，雙方同意：現有 guideline／cohort 均未以「多重未就緒前提同時存在」為分析框架，本案潛在貢獻（若最終有 definitive therapy 執行與結局可記錄）應定位為決策過程紀錄，而非新臨床實體；此為雙方研究假說層級之共識，非最終定論，且明確以 Day 64 前無已執行 definitive therapy 為前提限制。

### F. 額外案例問題（本輪新增，超出原「換藥／發病時序／橋接」三大主題）

1. **顯影劑注射與兩筆 Cr（0.94／1.53）之精確時間戳記關係為何？** 若能取得原始給藥紀錄與採血時間戳，可直接判斷顯影劑注射當下之瞬時腎功能，進而確認 EANM 2023 guideline「腎功能正常」前提是否成立於暴露當下，取代目前僅能以「未知」處理此前提的狀態。**可解決之資料**：完整 medication administration record 與檢驗採檢時間戳（分鐘級）。
2. **本案兩顆結節之功能定位（hot vs. cold）為何？** 目前無 thyroid scintigraphy 或其他 uptake 影像；此結果將同時影響（a）RAI 之劑量反應可預測性（toxic nodule vs. Graves 之攝取型態不同）、（b）結節惡性風險判讀（cold nodule 依 Mishra 2001 有 20% 惡性率，hot nodule 通常良性可能性較高）。**可解決之資料**：thyroid scintigraphy／radionuclide uptake scan（需先確認近期碘暴露是否已足夠 washout 以避免影像失真）。
3. **Day 64 之後是否已安排或執行右側 1.36 cm 結節之 FNA？** 本檔第三節已依 Haugen 2015 ATA 與 CaseDx 之 ACR TI-RADS 兩套系統收斂判定達 FNA 建議門檻，但案例底稿之資料截止於 Day 64 門診記錄，尚未見任何後續影像或細胞學結果。**可解決之資料**：後續 ultrasound／FNA 報告與 cytology 結果。
4. **目前（Day 64 以後）之腎功能、lithium trough 濃度與心臟功能（repeat echocardiography）為何？** 這三者同時決定手術麻醉風險分層、RAI washout 前提是否成立、以及現行 lithium 橋接劑量是否足夠或過量。**可解決之資料**：Day 64 以後之新 Cr／eGFR、至少 2–3 次 lithium trough level（含末次服藥至採血間隔記錄）、repeat echocardiography／EF。
5. **若走手術路徑，是否已由麻醉科／心臟科依現有 EF 32%（既往數值）與現行肺部感染狀態完成正式術前風險分級（如 ASA class 或等效之心肺風險評估工具）？** 本檔第二節僅能以一般外科原則做方向性推論，因查無「HFrEF 患者接受 thyroidectomy」或「近期 AKI 恢復期接受 thyroidectomy」之專門文獻。**可解決之資料**：正式麻醉科術前評估紀錄／心臟科手術適合度會診意見（可類比 Voci 2026 案例中之 right heart catheterization 角色）。

### G. 通訊狀態更新
本輪已收到並回覆：`RESPONSE-safety-to-definitive-001`（→ 已回覆 `CHALLENGE-definitive-to-safety-002`，msg_id=[SESSION-ID-REMOVED]，已排入佇列，非已讀確認）、`RESPONSE+CHALLENGE-publication-003`（→ 已回覆 `RESPONSE-definitive-to-publication-002`，msg_id=[SESSION-ID-REMOVED]）、`RESPONSE-CASEDX-002`（→ 已回覆 `ACK-definitive-to-casedx-002`，msg_id=[SESSION-ID-REMOVED]）。**「已排入佇列」不等於對方已讀或已同意**，完整逐字記錄與後續是否收到確認，見 `sessions/messages/r2_definitive_therapy_dialogue.md` 本輪新增章節。
