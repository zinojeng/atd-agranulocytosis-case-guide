# Endocrinology 角色紀錄（ATD-ANC-Endocrinology / run ATD-ANC-R1）— 最終版

> **公開版註**：以下保留的是去識別化歷史研究稿，可能包含已被後續 QA 更正的判讀與原 repo 的舊路徑。請以 `01-case/comprehensive-review.md` 與主題整理稿為 final synthesis；session identifiers 與逐字 transport logs 已移除。

> **Root 編輯註（2026-09-19）**：以下更正依 root 對原始 PDF 的直接視覺核對，由受託審查者更新；不是角色 session 新增的共識或訊息回覆。Vicente 2017 PDF 第6頁 reference 32 為 Meyer-Gessner 1994，*J Endocrinol Invest* 17:29–36，DOI [10.1007/BF03344959](https://doi.org/10.1007/BF03344959)。1989 原文的 4/29、5/33、11/34 仍經核實，但兩篇文獻之資料關係尚未證實，不推定書目誤植或重複報告。ATA 2016 E6 的 agranulocytosis contraindication 與極窄 storm 短期 PTU 例外位於印刷 p.1357／PDF 第15頁；E7 minor rash 才在 p.1358。Root 已核對 [ATA 原始 PDF](https://www.thermofisher.com/diagnostic-education/dam/clinical/documents/2016-ATA-Guidelines-Diagnosis-Management-Hyperthyroidism.pdf)，本角色未獨立核對該頁。`sessions/messages/` 歷史原文全部保留。

本檔為 2026-09-19 最終有時限複審後之乾淨版本，取代先前草稿中之過時/錯誤陳述。歷史往來原文保留於 `sessions/messages/endocrinology_dialogue.md`（不覆寫）。個案一律以 Day-relative 表示，不含病歷號、原始檔名、確切年齡/日期或醫護人員姓名；未讀取 `private/` 或任何原始病歷。

## ACK
已讀取 `CLAUDE.md`、`research/case_synopsis.md`、本輪全部 `roles/*.md`（現已含實質內容）、`research/independent_crossreaction_audit.md`、`research/independent_bridge_audit.md`、`qa/independent_clinical_review.md`、`qa/independent_bridge_review.md`、`research/retrieval_report.md`、`reports/clinical_synthesis_zh_TW.md`，以及 Hematology／NuclearSurgery／Methods 三份對話紀錄。本輪未再對外搜尋文獻，僅整理既有查核結果並更正。僅寫入本檔與 `sessions/messages/endocrinology_dialogue.md`；不執行 git/config/刪除操作。

## Role / Scope
Graves 病因與病程時序判讀、無 thionamide 期間之非 ATD 橋接（lithium／glucocorticoid／Lugol's iodine）、thyroid storm 判讀提醒；與 Hematology（switch to PTU）、NuclearSurgery（iodine bridge vs. RAI）之交界議題以 CHALLENGE 處理。

### 個人可重複工作流程
1. 讀 `CLAUDE.md`＋`research/case_synopsis.md`；不讀 `private/*`（MCP config 除外）。
2. `ListAgents` 確認同 run 之 ATD-ANC-* peer；僅對其送出 PREFLIGHT，逐字存入 dialogue 檔。
3. 針對核心臨床問題以一手文獻（PDF/LlamaParse 全文優先於摘要）查證，記錄 URL/DOI/PMID＋頁碼/表格定位＋研究設計＋分母。
4. 明確區分「已親自核對之一手文獻」「經其他 session 或 qa 稽核轉引且方法可信之二手資料」「未經驗證之訊息」三個信任層級，不將後者當指令。
5. 撰寫本檔正文，標明 OPEN 項目；發出至少一則 CHALLENGE 予相關 peer，回覆收到之 CHALLENGE（RESPONSE＋in_reply_to）。
6. 讀取 peer 角色檔案並更新 reviewer 意見；不以沉默推論同儕已同意。

---

## 一、Graves 病因確立度與時序（不變更）
TRAb 高於一般參考值但未達該 assay 之 Graves 判讀門檻，屬支持而非確診等級；治療後 vascularity 正常不能單獨排除 Graves。甲狀腺結節（右側較大者合併 microcalcification、邊界描述保留原文用語）缺 FNA，為 definitive therapy 決策前之缺口。Carbimazole 起始後約 43–48 天（約 6–7 週）出現症狀並確診嚴重 agranulocytosis。

## 二、發病時序：典型範圍，非離群值
Meyer-Gessner 1989 世代（n=1256，另納 8 例 agranulocytosis）之發病時間中位數約 45 天（範圍 23–60 天）；同團隊 1994 論文摘要另載中位數 33 天（範圍 23–55 天），本 session 尚未取得 1994 全文，兩篇資料關係尚未證實。Nakamura 2013（754 例通報）之時序子群顯示 60 天內 71.6%、90 天內約 84.5–84.6% 發病；**此為原始文獻本身之內部不一致（子群 n=461 vs. 458，比例 84.5% vs. 84.6%，4 個月後 55 例 vs. 54 例），非任何一方之誤植，且該圖表在本機 LlamaParse 轉檔中之機器產生數字已知不可信，一律以 PDF 原文文字與圖說為準，不得用轉檔表格重新運算**。本案 43–48 天落在上述所有文獻報告之典型區間內，時序上不構成排除 ATD 因果之理由。

## 三、交叉反應率「15.2%／50%」溯源（本輪最終版）

**已確認之一手數字**（本 session 直接讀取 `literature/meyergessner1989.md` 全文，並與 `qa/independent_clinical_review.md` 之原始 PDF 視覺核對結果一致）：Meyer-Gessner 1989（Dtsch Med Wochenschr 114(5):166–171，doi:10.1055/s-2008-1066570，PMID 2464468）p.169：thiamazole/PTU 換藥後任一不良反應復發 4/29（13.8%）、carbimazole/PTU 5/33（15.2%）、carbimazole/thiamazole 11/34（32.4%）。**三者均為換藥後任何不良反應之整體復發率，非特定方向、非 agranulocytosis-specific**；原文本身提醒此數字可能因多數不良反應會自發緩解而被低估。同一原始文獻之討論段落，另有明確立場（大意，非逐字引用）：發生嚴重不良反應後不建議在 thiamazole／carbimazole 間互換，改用 PTU 亦非無虞、需嚴密監測，此情境應優先安排 definitive therapy——此為本 session 找到最直接支持「不建議換藥、轉向 definitive therapy」立場之一手文獻依據，且與精確百分比無關。

Otsuka 2012（Clin Endocrinol 77(2):310–315，PMID 22332800）p.313 Table 4（經 `qa/independent_clinical_review.md` 視覺核對 PDF 原文，本 session 未親自開啟，故列為經核實之二手來源）：MMI→PTU 換藥後任一不良反應 14/41（34.2%）、PTU→MMI 9/30（30.0%），同樣為 all-ADR，非 agranulocytosis-specific。

**「50%」查無可靠、明確分母之 agranulocytosis-specific 原始研究支持**。本 session 已具體指認一則 2026 案例報告（Voci et al., Clin Med Insights Case Rep, PMID 42078037）將「高達 50%」歸因於 Vicente et al. 2017（Drugs R D, doi:10.1007/s40268-017-0172-1），但 Vicente 全文（本 session 已逐頁讀畢）僅載 15.2%，並無 50% 字樣；30–50% 之另一可能源頭是 rash／cutaneous 交叉反應語境（經 Burch & Cooper 2015 JAMA review 轉引 Otsuka 2012），亦非 agranulocytosis。

**已確認之書目與尚未證實之資料關係**：本 session 與 Methods 先前直接讀取 Vicente 2017 PDF 第6頁 References 所見的 ref[32] 為 Meyer-Gessner 1994，*J Endocrinol Invest* 17:29–36（DOI 10.1007/BF03344959；PMID 7516356），現由 root 再次直接視覺核對確認。先前 root 指向1989的說法有誤，已更正；**Vicente 的書目年份不再是 OPEN**。另已核實1989原文載有15.2%（5/33），但1989與1994資料的關係尚未證實，不宣稱已接通完整引用鏈，不推論年份／期刊誤植或同世代重複報告（OPEN-ENDO-009僅保留此資料關係）。

**臨床意涵**：15.2%／13.8%／32.4%／34.2%／30.0% 均為整體不良反應換藥復發率，不應解讀為本案病人若使用 PTU 之 agranulocytosis 復發機率；「50%」不應在對外溝通中使用。儘管精確比率不可靠，ATA 2016 guideline 方向與 Meyer-Gessner 1989 之一手臨床立場一致——發生 agranulocytosis 後不建議換用另一 thionamide，應轉向 definitive therapy。**ATA 之例外僅限於真正危及生命的 thyroid storm 短期使用 PTU，屬極窄之急救情境，不是門診常規換藥策略**，本節先前版本未充分強調此界線，特此更正。

## 四、非 ATD 橋接：lithium／glucocorticoid／Lugol's iodine（本輪更正）

- **Lithium**：現有證據包含 case report（JCEM Case Reports 2023, PMID 37908984，n=1，非 agranulocytosis 適應症）**與**回溯性 cohort（Gao et al. 2026, Front Endocrinol, doi:10.3389/fendo.2026.1770772，n=146：46 例 lithium bridging vs. 100 例 standard care，排除 severe renal impairment 即 eGFR<30 mL/min/1.73m²）。**更正**：不應全稱陳述「無 RCT 或 cohort」；準確表述為「存在 cohort 等級證據，但其對 active/近期 AKI 情境之安全性證據仍不足」。本案病人為**近期 AKI 併後續肌酸酐恢復**（非持續未解之現行 AKI），此為本輪更正之重要澄清——先前版本用語曾暗示腎功能持續不穩定，過度強調不確定性，特此修正；Gao 2026 的 severe renal impairment 排除門檻為 eGFR<30；不能僅由 recent AKI 已恢復或併用 ARNI（sacubitril/valsartan）與 potassium-sparing diuretic（spironolactone）推定本案被該研究排除或不屬其典型納入族群。針對本案這種近期 AKI 恢復期及特定併用藥物組合的安全資料仍不足，需依最新腎功能、volume/sodium、交互作用與 serum lithium levels 個別監測；既不能由該 cohort 宣告安全，也不直接判定不安全。案例摘要記載之單次低 lithium 濃度與 FT4 於門診 lithium 前已下降之時序，屬 before-after 設計混淆（regression to mean、自然病程改善、Lugol 殘留效應等競爭解釋未排除），不能作為療效證據。**OPEN-ENDO-002**：本案特定藥物組合（ARNI＋potassium-sparing diuretic＋近期 AKI 恢復期）之 lithium 監測排程，文獻無直接對應族群，建議腎科／藥師另訂。
- **Glucocorticoid**：案例已確認使用 hydrocortisone（stress-dose 模式）；其療程與臨床必要性應依感染與甲狀腺狀況核對。
- **Lugol's iodine**：確切濃度與最後一劑時間不明，直接限制 iodine washout 起算基準之精確度；此為與 NuclearSurgery 交界之 OPEN 議題（最後一劑 Lugol、目前心肺腎狀態均為 OPEN），**不應僅因這些資訊缺口就自動推論排除手術或 RAI 任一路徑**，此為本輪需明確澄清之原則。

## 五、Thyroid storm 判讀提醒（不變更）
BWPS 由 impending storm 區間上升至 highly suggestive 區間，但屬機率評分而非確診工具；已給予 storm 等級治療不能反向推論診斷已確認。

## 六、EANM 碘暴露 washout 與 definitive therapy（本輪更正強調）
依 `qa/independent_bridge_review.md`（已核實 EANM 2023 guideline 原文 Table 1 與 preparation 段落）：Lugol/SSKI 建議等待 2–3 週；含碘顯影劑（水溶性）建議 6–8 週，**前提為腎功能正常**。本案顯影劑開立紀錄列 Cr 0.94 mg/dL／eGFR 約 65；同日稍後紀錄有 Cr 1.53 mg/dL，但注射與採血時間尚未逐筆核對，不能斷定注射當下已有 AKI，也不能歸因於顯影劑。其後是否穩定恢復仍須以連續資料確認，不能單純以「已過 6–8 週」宣告 iodine clearance 完成，可由 Nuclear medicine 評估 RAIU 或尿碘實測。此為本 session 對 NuclearSurgery 之 CHALLENGE 核心，維持 OPEN。**手術與 RAI 兩條路徑目前均有各自未滿足之前提（surgery：肺部感染清除度、EF 最新評估、結節 FNA；RAI：碘暴露 washout 確認、RAIU 適合度），不能僅因資訊缺口本身就推論任一路徑已被排除。**

## 七、證據表（精簡版，完整版本見對話紀錄與各稽核備忘）

| 主張 | 來源 | 設計／分母 | 定位 | 核對層級 |
|---|---|---|---|---|
| CBZ/PTU all-ADR 復發 15.2%(5/33)；MMI/PTU 13.8%(4/29)；CBZ/MMI 32.4%(11/34) | Meyer-Gessner 1989, DOI 10.1055/s-2008-1066570, PMID 2464468 | Retrospective cohort n=1256，換藥子分析 | p.169 | **本 session 一手核對**＋qa 視覺核對一致 |
| MMI→PTU all-ADR 34.2%(14/41)；PTU→MMI 30.0%(9/30) | Otsuka 2012, PMID 22332800 | 隨機分組研究之換藥子分析 | p.313 Table 4 | qa 視覺核對（本 session 未親自開啟原文，二手但已核實） |
| Agranulocytosis 84.5–84.6% 於 90 天內發病 | Nakamura 2013, doi:10.1210/jc.2013-2569, PMID 24057289 | 回溯性通報病例系列 n=754，時序子群 n=461/458（原文內部不一致） | Abstract p.4776；Results/Fig.2 p.4778 | 本 session 一手核對；圖轉表數字不可信，已排除使用 |
| 發病時間中位數 45 天(23–60) | Meyer-Gessner 1989（同上） | 同上 cohort，8 例 agranulocytosis | 全文 | 本 session 一手核對 |
| 「50%」查無 agranulocytosis-specific 一手來源 | Voci 2026, PMID 42078037 → 誤引 Vicente 2017 | Case report n=1 | Introduction；Vicente 全文核對後未見此數字 | 本 session 一手核對兩篇原文 |
| ATD agranulocytosis 後另一 thionamide 應避免；極窄 life-threatening storm 短期 PTU 例外 | ATA 2016 (Ross et al.), doi:10.1089/thy.2016.0229, PMID 27521067 | Guideline | E6，印刷 p.1357／PDF第15頁；E7 minor rash 位於 p.1358 | Root 已直接核對原始 PDF；本角色未獨立核對該頁 |
| Lugol/SSKI 2–3 週；含碘顯影劑 6–8 週（需腎功能正常） | EANM 2023 (Campennì et al.), doi:10.1007/s00259-023-06274-5 | Guideline | Table 1 | 經 `qa/independent_bridge_review.md` 核實 |
| Lithium bridging：case report＋回溯性 cohort n=146（排除 eGFR<30） | JCEM Case Reports 2023 PMID 37908984；Gao et al. 2026 doi:10.3389/fendo.2026.1770772 | Case report＋retrospective cohort | 各文獻 Results | 二手核對（經 `independent_bridge_audit.md` 轉引），本 session 未親自開啟 Gao 2026 全文 |
| G-CSF：已識別之小型 RCT 未證實顯著效益 | Fukata et al. 1999, PMID 10037073 | RCT, n=24 | Abstract | 二手核對（Hematology/Methods 一手核對），**非「唯一 RCT 證明無效」之全稱結論** |

## 八、條件式建議
1. 不建議以任何精確交叉反應率數字作為是否嘗試 PTU 之判斷依據；依據為 guideline 方向與一手文獻之臨床立場。ATA 之 PTU 例外僅限危及生命之 storm，非門診換藥策略。
2. Lithium 若作為橋接選項，其於本案（近期 AKI 恢復期＋ARNI＋potassium-sparing diuretic）之安全監測排程無直接文獻對應，建議腎科／藥師個別訂定，不套用穩定腎功能病例之方案。
3. Surgery 與 RAI 兩條 definitive therapy 路徑目前均有未滿足之前提條件，不應僅因資訊缺口（結節 FNA、EANM washout 確認、最後 Lugol 劑量）就推論排除任一路徑；待補齊後由多科團隊決定。
4. Thyroid storm 治療強度應依連續臨床評估調整，不應僅依單次 BWPS 分數變化決定停藥時機。

## 九、OPEN 清單
- **RESOLVED-ENDO-001（root 原文核對）**：ATA 2016 E6 印刷 p.1357／PDF第15頁之 contraindication 與 storm 窄例外已由 root 直接核對；本角色未獨立核對，不再宣稱無人核對。
- **OPEN-ENDO-002**：本案特定藥物組合下 lithium 監測排程無直接文獻對應。
- **OPEN-ENDO-004**：EANM 2023 Table 1 已由 qa 核實，本 session 自身未逐頁核對原文，殘留為次要缺口。
- **OPEN-ENDO-006**：甲狀腺結節缺 FNA。
- **OPEN-ENDO-007**：Agranulocytosis-specific thionamide desensitization 證據缺乏。
- **OPEN-ENDO-009**：僅保留 Meyer-Gessner 1989 與1994兩篇資料關係尚未證實；Vicente ref[32] 的1994書目已確認，不再列年份爭議。
- **OPEN-REVIEW**：本次已完整讀取三份 peer 正文並於下方給出審閱意見，不再是骨架階段。

## 十、Reviewer Findings（本輪，讀畢三份完整正文）
- **Hematology**：G-CSF 證據矛盾（Fukata 1999 RCT 陰性 vs. 觀察性研究正向）、allopurinol 因果缺口、15.2%/50% 溯源與本 session 結論高度收斂，方法學透明。
- **NuclearSurgery**：EANM「腎功能正常」前提與本案 AKI 之衝突已被獨立指出，OPEN-VERIFY 系列標註誠實；Knight 2017／PMC13133480 之作者自陳限制被完整保留，未見過度概括。
- **Methods**：對「ATD-ANC-Director」身分未經 ListAgents 驗證一事保持審慎、不盲從，與本 session 對同一問題（Vicente ref[32] 年份）之處理方式一致；E3/E4 端點區分（all-ADR vs. agranulocytosis-specific）表述精確。

## 十一、跨 session 通訊摘要
本 session 之 PREFLIGHT、CHALLENGE-ENDO-001/002、RESPONSE(×3)、本輪 FINAL-REVIEW（送予 Hematology／Methods／NuclearSurgery，含對 Hematology 之 RESPONSE 內容重送、對 Methods 之 Vicente ref[32] 立場確認、對 NuclearSurgery 之近期 AKI／非現行 AKI 澄清）均逐字存於 `sessions/messages/endocrinology_dialogue.md`。CHALLENGE-ENDO-002（→NuclearSurgery，iodine washout 前提）截至本檔完成時仍為 OPEN，未獲該角色本輪 RESPONSE，不假設同意。

## 十二、交付總結
- 交付檔案：`roles/endocrinology.md`（本檔，最終版）、`sessions/messages/endocrinology_dialogue.md`。
- 本輪已送出訊息：FINAL-REVIEW-endocrinology-001 ×3（Hematology／Methods／NuclearSurgery），均為 SendMessage 回報成功、進入對方佇列，非確認送達。
- 已收到並回覆：FINAL-REVIEW-hematology-001、FINAL-REVIEW-methods-001。
- 尚未收到本輪回覆：NuclearSurgery（CHALLENGE-ENDO-002／本輪 FINAL-REVIEW 均待其回應）。
