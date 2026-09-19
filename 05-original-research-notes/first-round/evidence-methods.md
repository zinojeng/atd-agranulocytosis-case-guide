# roles/methods.md — ATD-ANC-Methods（方法學／來源稽核者）final版

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

> **Root 編輯註（2026-09-19）**：以下更正依 root 對原始 PDF 的直接視覺核對，由受託審查者更新；不是角色 session 新增的共識或訊息回覆。Vicente 2017 PDF 第6頁 reference 32 為 Meyer-Gessner 1994，*J Endocrinol Invest* 17:29–36，DOI [10.1007/BF03344959](https://doi.org/10.1007/BF03344959)。1989 原文的 4/29、5/33、11/34 仍經核實，但兩篇文獻之資料關係尚未證實，不推定書目誤植或重複報告。ATA 2016 E6 的 agranulocytosis contraindication 與極窄 storm 短期 PTU 例外位於印刷 p.1357／PDF 第15頁；E7 minor rash 才在 p.1358。Root 已核對 [ATA 原始 PDF](https://www.thermofisher.com/diagnostic-education/dam/clinical/documents/2016-ATA-Guidelines-Diagnosis-Management-Hyperthyroidism.pdf)，本角色未獨立核對該頁。`sessions/messages/` 歷史原文全部保留。

Run ATD-ANC-R1。最終回合更正版，取代先前初稿判斷；歷史措辭保留於 `sessions/messages/methods_dialogue.md`（唯讀對話紀錄，不覆寫）。No raw record filename、chart number、exact age、encounter date 或 clinician 姓名出現於本檔；未讀取 `private/` 或任何原始病歷檔。

## 角色與範圍
Adversarial methods/source reviewer。稽核使用者關切之統計/方法論宣稱來源，對其他三角色（endocrinology、hematology、nuclear_surgery）之引用進行同儕挑戰，要求精確 locator；不做個人化劑量建議，臨床建議一律 conditional。

## 個人可重複工作流程
1. 讀 `research/case_synopsis.md`，列出需外部佐證之數字宣稱。
2. 用 `mcp__paper-search__*` 以去識別化通用臨床查詢搜尋一手文獻；不含病人特徵。
3. 逐筆記錄作者年份/期刊/DOI/PMID/研究設計/確切分母/locator（頁碼、表格）。
4. 交叉比對宣稱數字與一手來源；不一致則標記 UNVERIFIED 並說明落差。
5. `ListAgents` 找同 run 其他 ATD-ANC-* session，`SendMessage` 送 PREFLIGHT／CHALLENGE，含唯一 message_id。
6. 收到回覆以 RESPONSE + in_reply_to 回覆；全部原文存 `sessions/messages/methods_dialogue.md`。
7. 讀其他角色 `roles/*.md`（唯讀），逐一覆核引用，寫入 Peer Review Findings。
8. 收尾更新本檔（證據表、OPEN 清單）；未回覆之挑戰標記 OPEN，不捏造共識。

---

## 證據表（Final）

| # | 宣稱 | 一手來源 / Locator | 研究設計・分母 | 稽核結論 |
|---|---|---|---|---|
| E1 | Nakamura 2013：754 例通報，日本 30 年 | *J Clin Endocrinol Metab* 2013;98(12):4776–4783, doi:10.1210/jc.2013-2569, PMID 24057289。p.4776 Abstract；p.4778 Results/Fig.2 | Retrospective 通報彙整，非連續 cohort。n=754（670 agranulocytosis＋84 pancytopenia/aplastic anemia） | CONFIRMED，本 session 已直接讀取 PDF 全文＋圖表。 |
| E2 | 「84.5% vs 84.6%」90 天內發病比例；n=461 vs 458；4個月後 55 vs 54 | 同上 | 同一論文內部不一致 | **CONFIRMED 為原始文獻本身的不一致**（非 LlamaParse OCR 或同儕誤植）——`research/retrieval_report.md`與`qa/independent_clinical_review.md`已對 PDF 排版頁作視覺核對確認。**警示**：Nakamura 之 LlamaParse 機器轉表（Figure 1/2/3）已知不可靠、Figure 5 尚未核對，任何數字須回到 PDF 正文/圖說，不得引用 LlamaParse 表格。84.5–84.6% 之分母為「時序資料完整之子群」，非全部 754 例。 |
| E3 | Cross-reaction 交叉反應率：13.8%／15.2%／32.4%（Meyer-Gessner 1989）；34.2%／30.0%（Otsuka 2012） | Meyer-Gessner M et al. *Dtsch Med Wochenschr* 1989;114(5):166–171, doi:10.1055/s-2008-1066570, PMID 2464468，**p.169 左欄第一段**；Otsuka F et al. *Clin Endocrinol* 2012;77(2):310–315, PMID 22332800，**p.313 Table 4** | Meyer-Gessner：retrospective cohort n=1256，藥物配對 all-ADR：thiamazole/PTU 4/29=13.8%、carbimazole/PTU 5/33=15.2%、carbimazole/thiamazole 11/34=32.4%。Otsuka：n=449 randomized（391 可分析），換藥子群 71 人：MMI→PTU 14/41=34.2%、PTU→MMI 9/30=30.0% | **CONFIRMED（原文全文已核對，非摘要層級）**。已取得 `literature/meyergessner1989.pdf`、`literature/otsuka2012.pdf` 原始 PDF，經 render 與視覺 QC（見 independent_crossreaction_audit.md、qa/independent_clinical_review.md）。**全部為 all-adverse-reaction 端點，均非 agranulocytosis-specific 之方向別復發率**；Meyer-Gessner 未拆分換藥先後方向，Otsuka 之 30–50%常見引用語境（JAMA 2015 Table 4）在其 Table 4/5 原文中**未能重現成乾淨的 rash-specific 分子分母**，「50%」最初出處仍未釐清。**不可用 13.8–32.4% 或 30–50% 中任一數字估算本案病人若使用 PTU 的 agranulocytosis 風險（既不是 ~15%，也不是 ~50%）**。 |
| E4 | Voci et al. 2026「高達50%」歸因於Vicente2017 | Clin Med Insights Case Rep 2026;19, doi:10.1177/11795476261446355, PMID42078037，Introduction | Case report n=1，引用鏈稽核 | Vicente相關cross-reaction段落為15.2%，不足以支持50%之歸因。**書目已確認**：本角色先前直接讀取之Vicente PDF第6頁ref32為Meyer-Gessner1994，J Endocrinol Invest17:29–36，DOI10.1007/BF03344959，現由root再次視覺確認。1989原文的5/33=15.2%亦經核實；但兩篇資料關係尚未證實，OPEN-M9只保留此問題，不推論年份／期刊誤植或重複報告，不宣稱完整引用鏈已接通。 |
| E5 | G-CSF 對恢復時間之效益 | Fukata S et al. *Thyroid* 1999;9(1):29–31, PMID 10037073（RCT, n=24：14 vs 10） | 前瞻隨機分組研究 | CONFIRMED：中重度病例恢復時間無顯著差異。**用語修正**：此為本 session 已識別到的**一篇小型陰性 RCT**，未證明「G-CSF 對所有情境皆無效」，僅說明「未能在此樣本證實其效益」；本 session 未做窮盡性檢索確認其為唯一 RCT，故不再稱「唯一 RCT」。與觀察性研究（Andrès 2001, PMID 11493719；Wang 2019 統合分析, PMID 31824417）方向相反，屬證據階層張力，非決定性矛盾。 |
| E6 | Lithium 作為橋接：case report 層級 vs. cohort 層級 | JCEM Case Reports 2023;1(4):luad094, PMID 37908984（n=1）；Gao et al. 2026 *Front Endocrinol*, doi:10.3389/fendo.2026.1770772（retrospective cohort, n=146：46 lithium vs 100 standard care） | Case report＋retrospective cohort | **用語修正（不再全稱「無 RCT 或 cohort」）**：確實存在 lithium 比較性 cohort 研究（Gao 2026），非僅 case report。該 cohort 僅排除 severe renal impairment（eGFR<30 mL/min/1.73m²）。**本案病人為近期 AKI 併肌酸酐已回復記錄（自升高值恢復至較低值），非已證實之持續性/現行未解決 AKI**——本 session 先前用語過度暗示「active AKI」，予以修正。針對「肌酸酐已回復軌跡下、lithium 於此類病人之安全性」之證據仍不足：Gao 2026 排除條件為單一 eGFR 切點，未特別驗證「近期 AKI 恢復期」此一動態情境，此點證據不足性維持成立。 |
| E7 | ATA guideline 對換另一 thionamide 之立場 | Ross DS et al. Thyroid2016;26(10):1343–1421, doi:10.1089/thy.2016.0229, PMID27521067；E6印刷p.1357／PDF第15頁；E7 minor rash才在p.1358 | Guideline | 另一thionamide屬contraindicated；保留極窄的危及生命thyroid storm短期PTU考量，非一般換藥策略。Root已直接核對原始PDF；本角色未獨立核對該頁，原OPEN-M6頁碼問題已解決。 |
| E8 | EANM 碘暴露 washout 窗口 | Campennì et al. 2023, doi:10.1007/s00259-023-06274-5, PMID 37395802，Table 1 | Guideline | CONFIRMED：Lugol/SSKI 2–3 週；水溶性含碘顯影劑 6–8 週，**明確以腎功能正常為前提**。本案同日出現腎功能變化，但注射與採血先後未核實；前提是否成立需以連續腎功能／RAIU／尿碘確認，非日曆天數自動達標。**最後一劑 Lugol 濃度與時間、目前心肺腎狀態均為 OPEN；資訊缺口本身不構成自動排除 surgery 或 RAI 任一路徑的理由**，須由多科團隊以到手資料逐項評估。 |

## 核心問題最終結論（精簡版）

1. **Switch to PTU**：不建議常規換藥。交叉反應之量化數字（13.8–32.4% all-ADR、30–50% rash 語境、Voci 2026 之 50%）**均非 agranulocytosis-specific**，不可用於估算本案病人風險（非 ~15%、非 ~50%）。建議之強度來自 guideline 立場與零星個案報告（Chen 1983 PMID 6865827；Ostlere 1988 PMID 3256337）之方向一致性，而非精確復發率。ATA 之「contraindicated」立場保留極窄之 thyroid storm 短期 PTU 例外，非一般換藥策略。
2. **~6–7 週發病時序**：屬典型區間（Meyer-Gessner 1989 中位 45 天；Nakamura 60–90 天窗口內約 85%），非離群值；「約 85%」之分母為時序資料完整子群，非全體 754 例。
3. **G-CSF**：一篇已識別之小型陰性 RCT（Fukata 1999, n=24）未證明效益，但也非證明「普遍無效」；與觀察性證據方向相反，屬證據階層張力。不建議將本案快速恢復單一歸因於 G-CSF。
4. **Lithium 橋接**：現有 cohort 等級證據（Gao 2026, n=146）存在，非僅 case report；但該 cohort 排除條件未針對「近期 AKI 恢復期」此動態情境驗證，證據不足性仍然成立。本案為肌酸酐已見改善之近期 AKI，非已證實持續性 AKI。FT4 於 lithium 前已下降之 before-after 混淆判讀維持不變。
5. **EANM 碘 washout**：contrast 6–8 週前提為腎功能正常，本案該前提未經確認；Lugol 2–3 週為概略區間。缺失資訊（末劑濃度/時間、目前心肺腎狀態）維持 OPEN，但不構成自動排除 surgery 或 RAI 之理由。

## OPEN 清單（最終）

- **RESOLVED-M6（root 原文核對）**：ATA2016 E6印刷p.1357／PDF第15頁已由root直接核對；本角色未獨立核對該頁。
- **OPEN-M8**：Gao et al. 2026 全文之 eligible population／排除條件逐字定義，僅經 `independent_bridge_audit.md` 轉引，未親自核對。
- **OPEN-M9**：Meyer-Gessner1989與1994兩篇資料關係尚未證實；Vicente2017 PDF第6頁ref32的1994書目已確認，不再保留年份爭議，不推論書目誤植或重複報告。
- **OPEN-CLINICAL**：Lugol 末劑濃度/時間、目前 EF／肺部感染／腎功能狀態、甲狀腺結節 FNA 結果——均為多科決策前待補資訊，非本 session 職權範圍。

## CHALLENGE / RESPONSE 狀態（最終）

| ID | 對象 | 結果 |
|---|---|---|
| CHALLENGE-methods-001 | Endocrinology | 已收斂（RESPONSE-endo-to-methods-001）；本輪已加送 FINAL-REVIEW-methods-001，當時記錄 OPEN-M6/M9；現root已核對解決M6，M9僅保留兩篇資料關係。 |
| CHALLENGE-methods-002 | Hematology | 已收斂（RESPONSE-hematology-to-methods-002）；本輪已加送 FINAL-REVIEW-methods-001，修正 G-CSF/AKI 用語。 |
| CHALLENGE-methods-003 | NuclearSurgery | 已收斂（RESPONSE-nuclear_surgery-to-methods-003），無殘留異議。 |
| CHALLENGE-nuclear_surgery-002（收到） | NuclearSurgery→Methods | 已回覆（RESPONSE-methods-to-nuclear_surgery-002）：作者限制文字保留問題於當時尚無角色引用該文獻（N/A）；Day 64 未被誤用為 outcome data（CONFIRMED）。 |

完整逐字原文見 `sessions/messages/methods_dialogue.md`；本輪新增之 FINAL-REVIEW 訊息已送出，peer 之正式 RESPONSE 若在本輪內收到將於對話檔續記，未收到者不視為同意，維持 OPEN。

## Peer Review Findings（最終）

三份 peer 角色檔（endocrinology、hematology、nuclear_surgery）均已完成含證據表、CHALLENGE、OPEN 清單之正文，方法學品質良好，三者對 15.2%/50%/Nakamura 內部不一致之結論與本檔一致，屬多路徑獨立收斂。NuclearSurgery 之 OPEN-VERIFY 透明度最高；Endocrinology 獨立發現 Voci 2026 引用鏈失真為本輪最具體貢獻；Hematology 之 allopurinol 因果歸屬處理審慎，未過度排除加成作用。未發現任何角色將 case report 結論或 Day 64 單次臨床傾向誤植為族群層級 outcome data。

## 最終狀態
本檔為本 session 最終版本，取代先前所有初稿判斷。已依本輪指示：(a) 將 Meyer-Gessner 1989／Otsuka 2012 精確分子分母自「未驗證」升級為 CONFIRMED；(b) Vicente ref32=1994已由root原PDF確認，與本session先前直接讀取相符；OPEN-M9只保留1989與1994資料關係未證實；(c) 已撤回非病歷縮寫；(d) 修正 lithium「無 cohort」與 G-CSF「唯一 RCT」之全稱表述；(e) 明確區分 ATA storm 窄例外與一般換藥；(f) 明確聲明缺失資訊不構成自動排除任一 definitive therapy 路徑；(g) 註明 Nakamura LlamaParse 圖轉表不可信、須以 PDF 正文/圖說為準。已送出 FINAL-REVIEW-methods-001 予 Endocrinology 與 Hematology 兩個同 run peer，訊息回條見上表；未在本輪內收到之新 RESPONSE 不代表同意，維持 OPEN。
