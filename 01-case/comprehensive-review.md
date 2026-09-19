# ATD agranulocytosis 個案：多專科擴充研究與決策地圖

資料查核截至 2026-09-19。以繁體中文撰寫，medical／drug names 保留 English。個案資料出自本機 **UTF-8 Markdown 原始病歷**；只在本機核對，未上傳給文獻或 PDF 解析服務。下文使用去識別化的 [relative-day 底稿](case-summary.md)。本稿整合已發表證據與多角色專科交叉審查；尚缺的病人資料與最終治療結局不能以文獻推定。

## 個案摘要：已知發生了什麼

五十多歲女性，有 thyrotoxicosis、type 2 diabetes 及既有 HFrEF（EF 約 32%）。Carbimazole 10 mg daily 開始後，約 Day 43 出現 fever／sore throat；Day 46 發現嚴重 leukopenia，Day 48 入院 ANC 50/µL、CRP 30.12 mg/dL，影像呈右中葉 pneumonia。停 carbimazole 後接受抗生素、G-CSF、Lugol、glucocorticoid 及心率控制；Day 51 ANC 恢復至 4.14×10³/µL。出院時臨床較穩定，但胸片仍有浸潤，Day 57 肺科又描述右中葉 necrotizing pneumonia 緩慢改善、接近 abscess。ANC 改善與感染完全清除是兩個不同終點。

Thyroid hormone 逐步下降：Day 48 FT4 1.61、Day 54 1.32、Day 57 1.21、Day 59 1.13 ng/dL（參考 0.70–1.48）。Day 57 的門診 lithium 處方為 150 mg daily；住院 lithium 是否實際使用，以及 Day 59 lithium <0.2 的抽血距給藥時間均不明。因此這條曲線不能單獨證明 lithium 有效或無效。Day 64 門診傾向 thyroidectomy、病人仍考慮；所提供病歷沒有手術或 I-131 已執行及後續結局。

| 節點 | 已核對的決策資料 | 尚存的歧異 |
|---|---|---|
| Carbimazole 停藥 | Day 47 家屬敘述 vs Day 48 住院摘要 | 完整實際服藥／停藥時間未取得 |
| Contrast／renal | Day 48 使用 Omnipaque 350 75 mL；同日資料列 Cr 0.94→1.53，後降 0.59 mg/dL | Cr 0.94／eGFR 約 65 出現在 CT 開立資訊；最高 Cr 1.53 不應硬套為顯影劑注射當下數值，需核採血時間 |
| Iodide | 住院 Lugol 約 2 mL Q8H，出院處方 2 mL daily | 配方濃度、實際給藥與最後一劑不明 |
| Thyroid storm | 病程列 BWPS 35→50，住院曾以 hydrocortisone／Lugol 處置 | 缺同時點各項分數；pneumonia 與既有 HFrEF 可影響評分 |
| 根本治療 | 已討論 surgery 與 I-131 | 病人最後決策、術前影像／心肺狀態及實施結果未提供 |

## 臨床問題一：藥物歸因、交叉再暴露與骨髓恢復

Carbimazole 的 43–48 天暴露時序符合 ATD-induced agranulocytosis 常見早發分布，且 ANC 50/µL 遠低於 500/µL 診斷門檻；這支持「高度懷疑」而非對唯一病因的證明。Allopurinol 的實際處方／服藥日期仍未知，感染、其他藥物及原先 CBC 走向也應併查。Nakamura 2013 的 754 是不良事件通報總數，發病時間分析僅 n=461（Figure 2 圖說 n=458）；正文約 84.6%、摘要 84.5% 在前 90 天發病，是**已發病病例中的時序分布**，不能當成服藥者的絕對風險。[原始研究](https://pubmed.ncbi.nlm.nih.gov/24057289/) 的圖轉表在本機 LlamaParse 有已證實錯誤，本稿僅用原始 PDF 正文／圖說。

若曾發生 agranulocytosis，一般不例行換用另一 thionamide。Meyer-Gessner 1989 的 carbimazole／PTU **5/33=15.2%** 是換藥配對後的**整體 adverse reactions**，並未給出 agranulocytosis-specific、方向別再發機率；Otsuka 2012 的 MMI→PTU **14/41** 同樣為 all-ADR。常見的「50%」並無本案所需的可信 agranulocytosis 再發分母。ATA 2016 的另一藥 contraindication 僅留危及生命的 thyroid storm 情境下極短期權衡例外（[guideline E6，印刷 p.1357](https://www.thermofisher.com/diagnostic-education/dam/clinical/documents/2016-ATA-Guidelines-Diagnosis-Management-Hyperthyroidism.pdf)）。詳見 [原始分母查核](../03-evidence/thionamide-cross-reaction-audit.md)。Vicente 2017 reference 32 實際指 Meyer-Gessner **1994**；1989 數字為另一條獨立直接核對，兩篇資料關係尚未完成查證。

本案 Day 48→51 ANC 快速回升與停藥、抗生素、G-CSF 等介入同時發生，不能單病例歸因。Fukata 1999 小型 RCT（n=24）未證實 G-CSF 對中重度 ATD agranulocytosis 有明顯恢復利益；觀察研究與 meta-analysis 指向部分群體較快恢復，但研究設計、最嚴重 ANC 亞群及 mortality 終點不同。[RCT 摘要](https://pubmed.ncbi.nlm.nih.gov/10037073/)；[統合分析摘要](https://pubmed.ncbi.nlm.nih.gov/31824417/)。臨床改善仍需和持續肺部感染分開監測。

## 臨床問題二：真的是 Graves 與 thyroid storm 嗎？

TRAb 3.00 IU/L 高於檢驗 reference <1.99，卻略低於同一報告的 Graves-specific cutoff 3.10；這不能簡寫為明確陽性或陰性。Ultrasound 顯示雙側結節、正常 vascularity，但它在治療後完成，單憑血流不能排除 Graves。結節自主分泌、Graves 合併結節、其他甲狀腺毒症病因都需以原始影像、抗體、病程與適當時機的功能性檢查重建。近期 contrast／Lugol 會干擾 uptake，低 RAIU 必須放在暴露時序中解讀。

BWPS 35→50 可作急性處置警訊，但病例報告必須重建同一時刻的溫度、心率、CNS、GI、心衰竭與誘因。Day 48 影像證實 pneumonia，既有 EF 32% 並不等於當下 pulmonary edema 或 cardiogenic shock；FT4 只有輕度升高亦不能單獨排除 storm。日本 JTA criteria 對 tachycardia ≥130/min、嚴重急性 CHF 與其他器官症狀有明確組合要求，同時提醒感染既可能模仿症狀，也可能觸發 storm，需要臨床判斷。[JTA/JES guideline 與 Table 3](https://www.japanthyroid.jp/common/public_comment201605.pdf)。目前資料最穩妥的寫法是「曾懷疑並處置可能的 thyroid storm；診斷程度待原始評分資料確認」。

## 臨床問題三：HFrEF、感染與 non-thionamide bridge 如何互相限制？

既往 EF 約 32% 是高風險背景，但沒有後續 echo、心衰竭病因分析或目前心輸出／容量狀態；不能承諾其為可逆的 thyrotoxic cardiomyopathy。Beta-blocker 是否維持、調整或避免疊加，取決於當前 hemodynamics，而非單一心率。Day 57 的 necrotizing pneumonia 描述也使「ANC 已恢復」不足以宣稱麻醉感染風險解除。

| 橋接方法 | 可支持的作用 | 本案要先核實的風險／資料 |
|---|---|---|
| Lugol／KI | 短期抑制 thyroid hormone release，常用於術前準備；停碘後也可評估 I-131 | 製劑濃度、累積 iodide、最後一劑、可能 escape；若轉向 I-131，要重新評估 uptake |
| Glucocorticoid | 在嚴重 thyrotoxicosis／storm 處置中減少 T4→T3 conversion | 已有 pneumonia 與 diabetes；使用時間、停藥與 ACTH／cortisol 抽血時序應核對 |
| Beta-blocker | 控制交感症狀、心率 | HFrEF 是否穩定，是否有 low-output／shock；避免在既有 bisoprolol 上憑單次心率加藥 |
| Lithium | 可短期抑制 hormone release，也可用於特定 RAI 周期 | 近期 AKI、sacubitril/valsartan、spironolactone／利尿劑、Na／volume 變化；門診處方前 FT4 已下降，單次 <0.2 不足以追認療效或目標濃度。見 [lithium 標示](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a12d50fb-2c2f-4105-ad17-adbf90d439d4)、[Entresto 7.4](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?lang=en&setid=000dc81d-ab91-450c-8eae-8eb74e72296f) |
| Cholestyramine | 減少 enterohepatic thyroid hormone recycling，作為 adjunct | 與其他口服藥間隔、不能從組合療法單獨推定效果 |
| Therapeutic plasma exchange | 無法以常規方式控制時的短期 rescue，通常銜接 definitive treatment | 經驗多為小型系列／病例；侵入性、短暫效果及適應性由專科評估 |

## 臨床問題四：可疑 nodules 會否改變根本治療？

原始 ultrasound 敘述右 1.36 cm、左 0.80 cm，均為 solid hypoechoic 並記 microcalcification；「ill-defined border」不能自動改寫為「irregular margin」。若原圖確認 EU-TIRADS 5 高風險特徵，ETA 2023 指引一般在 **>10 mm** 考慮 FNA：右側達尺寸門檻；左側約 8 mm，通常需結合 suspicious lymph node、疑似 extrathyroidal extension 或關鍵位置才考慮超越常規門檻。這是條件式影像判讀，尚非本案已完成的正式 EU-TIRADS 分類。[ETA 2023 guideline：thyroid biopsy](https://pmc.ncbi.nlm.nih.gov/articles/PMC10448590/)。

若 FNA／影像高度支持 malignancy，手術理由增強且可能改變手術範圍；若結節風險低、病因與 uptake 適合，I-131 保留為路徑。病歷沒有原圖、完整頸部淋巴結 mapping 或 cytology，故現在不宜把「雙側結節」等同已確診癌症，也不宜預設兩側都須 FNA。

## 臨床問題五：thyroidectomy 與 I-131 的實際路徑

| 問題 | Thyroidectomy | I-131 |
|---|---|---|
| 起效 | 移除甲狀腺後較快解除分泌來源；需術後 hormone replacement | 起效延後，治療前後可有激素波動；等待期仍需可行的 bridge |
| 現在最大的限制 | 肺炎是否已足夠控制、EF／容量及麻醉風險、術前 hormone 準備、手術團隊經驗 | 持續 Lugol 與 contrast 的 iodine load、實際停碘日、RAIU、最新腎功能與可否安全等待 |
| 結節 | 可同時取 histology，若惡性疑慮成立較有吸引力 | 不可用良性甲亢的 I-131 處置替代疑似癌症的評估 |
| 下一個必要決策 | Infection、Cardiology、Anesthesia、Surgery 共同確認手術可承受性 | Nuclear medicine 確認 uptake／iodine clearance 與停碘後控制計畫 |

EANM 2023 Table 1 提供一般準備框架：Lugol／SSKI 停 **2–3 週**，水溶性含碘 contrast **6–8 週**且明列正常腎功能前提；本案兩種暴露均存在，contrast 當下與後續 Cr 需要分別核實，固定日曆不能取代 RAIU 和臨床狀態。[EANM guideline](https://doi.org/10.1007/s00259-023-06274-5)。另有 [2026 thyroid storm 多學會共識](https://pmc.ncbi.nlm.nih.gov/articles/PMC13506520/) 對大量 iodide 治療後的 RAI 採較保守的 2–3 個月延後框架；這不是本案發病時間，也不能不看製劑、末劑與 uptake 就直接套用。現有紀錄支持「兩條路徑都可評估、各有待滿足條件」，不支持已定手術日期或宣稱 RAI 永久不可行。

## 深入決策一：本案 lithium 有沒有可歸因效果？

### 目前結論：無法歸因，證據是「不確定」而不是「有效」或「無效」

本案 FT4 在門診 lithium 開立前已由 Day 48 的 1.61 降至 Day 54 的 1.32、Day 57 的 1.21 ng/dL，因此這一段下降不能歸因於 Day 57 開始的門診 lithium。Day 57→59 的 1.21→1.13 ng/dL 變化幅度小、時間只有兩天，且同時存在 Lugol 暴露、glucocorticoid、急性感染恢復及檢驗變異。若住院期間 lithium 的 medication administration record 仍未找到，就不能把整條 hormone curve 當作 lithium response。

Day 59 lithium <0.2 也不能獨立回答療效。正式藥品標示的 trough 採血原則是接近下一劑、約前一劑後 12 小時，並在開始後數日再評估；本案缺實際第一劑、最後一劑、服藥遵從性與抽血時點。這些標示來自 bipolar disorder 的 therapeutic drug monitoring，不是本案甲狀腺適應症的直接目標，但可說明為什麼一個時點不明的數值不能判為 underdosing、nonresponse 或「沒有中毒風險」。[DailyMed lithium label](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=803eab29-0d0a-4df0-b504-bcd85ec01ead)。

若要提高可歸因性，至少要重建以下同一條時間軸：

1. **Exposure**：住院與門診每一劑 lithium 的實際給藥時間、劑型、服藥遵從性及停藥時間。
2. **Concentration**：每次 lithium level 距前一劑多久、是否已連續使用數日、抽血時 Cr／eGFR、Na、K 及 volume status。
3. **Thyroid response**：開始前與開始後的 FT4、FT3；早期不要用仍受抑制的 TSH 判斷短期反應。
4. **Concurrent treatment**：Lugol、glucocorticoid、beta-blocker、cholestyramine 與感染改善的精確時序。
5. **Clinical response**：heart rate、rhythm、temperature、HF symptoms、mental status，而非只看 FT4。

本案 lithium 安全性不能只看 dose 低或單次 level 低。Lithium 由腎臟清除；標示列出 impaired renal function、volume depletion／dehydration、Na／K 改變、febrile illness 與 significant cardiovascular disease 均會提高 toxicity 風險。Sacubitril/valsartan 所含 valsartan 可增加 lithium concentration；spironolactone 等 diuretics 會降低 renal lithium clearance。兩個藥品標示都要求併用時監測。[Entresto 7.4](https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=14bf8041-0b7f-9acb-e063-6294a90a8256)、[spironolactone 7.2](https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c23b6b9b-aec3-48a8-a518-76e4097f6479)。因此真正的最低資料集是「最新 Cr／eGFR＋Na／K＋體重／輸入輸出與 congestion／dehydration＋完整 HF／NSAID／antibiotic 用藥」，不能沿用住院早期單一數值。

### 文獻能支持到哪裡

- Bogazzi 2002 的 randomized study（n=36）顯示，在已用 methimazole 控制數月的 Graves patients 中，從停 methimazole 時開始短期 lithium，可避免停藥後 2–5 天的 FT4／FT3 rebound，並提高 thyroidal radiation retention；樣本很小，三組 cure rate 差異未達統計顯著。[PubMed](https://pubmed.ncbi.nlm.nih.gov/12364424/)
- Bogazzi 2010 retrospective cohort（n=651）中，RAI＋lithium 的一年 cure rate 為 91%，RAI alone 為 85%，median time to cure 60 vs 90 days，且 lithium group 沒有 methimazole withdrawal 後的 FT4 rise。這是非隨機研究，且病人是 newly diagnosed Graves，不能直接套用到 agranulocytosis、necrotizing pneumonia、HFrEF 與 renal fluctuation 並存的本案。[PubMed](https://pubmed.ncbi.nlm.nih.gov/19906789/)
- Gao 2026 single-center retrospective cohort 比較 lithium bridge 46 人與 standard preparation 100 人。六個月 treatment failure 沒有顯著差異（15.2% vs 10.0%，P=0.345）；研究 protocol 的 serum target 與時程是群體方法，不是本案處方建議。該研究也不足以證明 lithium 降低罕見 thyroid storm。[Full text](https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1770772/full)

## 深入決策二：不能用 thionamide 時，能否以 lithium 支持到 I-131？

可以把 lithium 視為**可能的 thyroid-directed bridge**，不能把「lithium alone」理解成整個病人只需一種藥。Pneumonia、HFrEF、arrhythmia、volume 與 symptomatic control 仍各自需要處理；beta-blocker 也要依 hemodynamics 判斷。本案若選 I-131，應採條件式流程，而不是先訂一個固定停碘日期。

### Stage 1：先確認 I-131 是適合的根本治療

- 重建 thyrotoxicosis etiology。I-131 的前提是有可治療的 hyperfunctioning thyroid tissue；TRAb 邊界值與 nodules 使病因不能只靠一項檢驗決定。
- 完成眼病、goiter、吞嚥／氣道、pregnancy、radiation-safety 與後續照護可行性評估。
- 右側 suspicious nodule 是否需先 FNA／其他 malignancy work-up 必須釐清；懷疑或確認 thyroid cancer 會改變 benign-disease I-131 路徑。
- 由 Nuclear Medicine 說明目標、可能需 repeat treatment、起效延遲及預期 thyroid replacement。EANM 要求由專科完成適應症、準備、medication review、radiation instructions 與 informed consent。[EANM 2023](https://doi.org/10.1007/s00259-023-06274-5)

### Stage 2：停 iodide，但用「恢復 uptake 的證據」決定何時做 I-131

先查明 Lugol 配方、每日實際量與最後一劑，以及 iohexol 日期與 renal course。EANM Table 1 的一般 withdrawal interval 是 Lugol／SSKI 2–3 週、水溶性 IV contrast 6–8 週（假設 renal function 正常）；同一 guideline 對 contrast exposure 建議 treatment 前 RAIU，urinary iodine 亦可協助。2026 thyroid-storm joint consensus 對大量 iodide 治療後採更保守的「RAI 通常至少延後 2–3 個月」說法。兩者適用情境不同，應由 RAIU（必要時 urinary iodine）、腎功能與實際末劑整合，不宜機械式選最短或最長日曆。

等待期間應避免不必要的新 iodinated contrast、iodine supplements、kelp／高碘產品或含碘藥物；若醫療上確有需要，先治療急症，再重新計算 I-131 路徑。

### Stage 3：若 lithium 是唯一可行的 thyroid-directed bridge，先建立安全欄杆

開始或延續前要有 current Cr／eGFR、Na、K、體重與 volume assessment、完整 medication reconciliation，並由 Endocrinology／Cardiology／Pharmacy 訂定採血時點與臨床監測。Sacubitril/valsartan、spironolactone、其他 diuretics、NSAIDs、脫水、發燒、腹瀉或 renal deterioration 都可能讓原本穩定的 exposure 改變。

同時訂出**重新評估／改道門檻**：FT4／FT3 明顯上升、new arrhythmia、worsening congestion 或 low-output signs、infection relapse、renal／Na 變化、neurologic／GI lithium toxicity symptoms，或無法可靠服藥／回診。此時不能只追加 lithium；要重新討論 monitored admission、其他 adjunct、plasma exchange 或 accelerated surgery 等可控的替代路徑。

### Stage 4：RAIU 與治療日

RAIU testing 與 I-131 therapy 應使用相同 preparation／medication condition。若 uptake 不足，低值可能仍反映 iodine load，不等同真正不適合 I-131。治療時程、activity 與是否將 lithium 延續至 I-131 後數日，應依 Nuclear Medicine／Endocrinology protocol 決定。研究曾採用不同 dose、serum range 與 peri-RAI days；那些數字不應由本文轉成此病人的處方。

### Stage 5：I-131 後仍是高風險期

I-131 不會立即停止 hormone release。EANM 指出 radiation-induced thyroiditis 可使約 10% 病人出現不同程度的 thyrotoxicosis worsening，poorly controlled hyperthyroidism 的風險較高；cardiovascular disease 病人尤其需要 treatment 前後的 symptom／rhythm control 與早期 thyroid-function follow-up。Lithium 若依 protocol 短期延續，也仍要監測 renal、Na、volume、level timing 與 toxicity。成功吞下 I-131 不是 bridge 結束點；等到 hormone trajectory 與 heart failure 穩定才算跨過主要風險期。

## 深入決策三：患者偏好怎麼真正進入 surgery vs I-131？

ATA guideline 要求醫師與病人討論 logistics、benefits、expected speed、drawbacks、side effects 與 costs，最後選擇應納入病人價值與偏好；不能用「門診偏向 surgery」替代 informed preference。[ATA 2016](https://doi.org/10.1089/thy.2016.0229)。本案至少應記錄：

| 要問病人的事 | 若答案偏向 surgery | 若答案偏向 I-131 |
|---|---|---|
| 最在意速度還是避免 procedure？ | 希望較快移除 hormone source、可接受 anesthesia／scar | 希望避免手術，即使效果需等待 |
| 能否承受停碘等待與密集監測？ | 無法安全等待或回診困難會降低 I-131 可行性 | 能按時抽血、回診並接受 bridge safety monitoring |
| 如何看待 nodules 與 pathology？ | 希望一次取得 histology，或 malignancy concern 尚未排除 | 影像／cytology 已足以讓團隊接受非手術路徑 |
| 如何看待 lifelong levothyroxine？ | 接受 total thyroidectomy 後需要 replacement | 理解 ablative I-131 也常以 hypothyroidism 為治療結果，不能把它當「一定不需終身服藥」 |
| 能否遵守 radiation precautions？ | 若家庭／工作安排做不到，I-131 feasibility 下降 | 能理解並執行 Nuclear Medicine 指示 |
| 如何看待失敗或第二次治療？ | 重視一次治療成功率與較快結果 | 接受 I-131 可能延遲、persistent disease 或 repeat treatment |

建議病歷留下病人自己的理由、提問、理解確認，以及目前選擇可否因 EF、infection、RAIU 或 nodule 結果而改變。這也正是 CARE case report 所要求的 patient perspective，而不是額外的敘事裝飾。

## 深入決策四：EF 32% 要怎麼重新診斷與評級？

「Thyrotoxic cardiomyopathy」應視為排除其他病因並觀察治療後 recovery 的工作診斷，不能由 hyperthyroidism＋低 EF 自動成立。住院 thyrotoxic HF cohort 中，50 人被歸類為 thyrotoxic cardiomyopathy，僅 32 人有完整 follow-up echo；在平均 18 個月追蹤中 22/32（69%）恢復 LV systolic function。這證明 recovery 可能發生，也同時表示並非人人恢復，而且有 selection／incomplete-follow-up 限制。[Clinical phenotypes and prognosis cohort](https://pmc.ncbi.nlm.nih.gov/articles/PMC8318454/)。

本案重新評估應回答：

- 原始 echo 的日期、LV size、global 或 regional wall-motion、RV、valves、pulmonary pressure 與 diastolic data。
- 發現 EF 32% 時的 thyroid state、heart rate、AF／other tachyarrhythmia burden、infection 與 volume status。
- 是否依一般適應症評估 ischemic heart disease、hypertension、valvular disease、myocarditis、diabetic cardiomyopathy 或其他原因。
- 最新 symptoms、NYHA class、BP、orthostasis、weight／edema／JVP、ECG／ambulatory rhythm、renal／electrolytes；BNP／troponin 僅在會改變決策時使用。
- Thyroid 與 infection 較穩定後的 repeat echo。若臨床狀態惡化或已改變，不能等待任意固定月數才重做。

### 結果如何改變兩條路的風險

| 重新評估結果 | Surgery 路徑 | I-131／等待路徑 |
|---|---|---|
| EF 明顯恢復、compensated、感染控制 | 麻醉風險可能下降，但仍需 formal perioperative assessment | 等待期 cardiovascular reserve 較佳，仍須 bridge 與 post-RAI monitoring |
| EF 仍約 32% 但 compensated | 低 EF 增加 perioperative risk；由 Cardiology、Anesthesia、high-volume thyroid surgeon 共同設計 hemodynamic plan | 避免立即 anesthesia，但承擔較長 thyrotoxicosis、lithium interaction／renal-volume 變化及 I-131 延遲起效 |
| Active／decompensated HF、hemodynamic instability | 2024 AHA/ACC perioperative guideline 支持先暫停 elective surgery、Cardiology evaluation 與 stabilization | 也不能把 I-131 當立即安全出口；若 thyroid excess 正在驅動 decompensation，延長等待本身可能有害，需 monitored multidisciplinary rescue plan |
| 不能排除 ischemia／significant valve disease／arrhythmia | 依一般臨床適應症完成會改變管理的評估，不為手術而過度檢查 | 同樣會影響 beta-blockade、volume、lithium 與等候安全性 |

2024 AHA/ACC guideline 指出 HF、較低 LVEF 與 active symptoms 都增加 noncardiac surgery risk，clinical decompensation 或 hemodynamic instability 時應考慮延後 elective surgery並尋求 Cardiology 協助；也強調以團隊與病人共同決策。[Full guideline](https://www.ahajournals.org/doi/full/10.1161/CIR.0000000000001285)。但 EF 32% 不是單獨把 surgery 永久排除的數字，也不能自動讓 I-131 成為低風險選項。真正比較的是：在當時 clinical state 下，哪一組風險能被團隊監測、縮短與救援。

## 已發表病例：哪些相似，哪些不能外推？

| 文獻／設計 | 已報告的 bridge 與終點 | 與本案的對照及限制 |
|---|---|---|
| [Knight 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5592706/)，單例 | Thionamide-associated agranulocytosis＋sepsis；Lugol、lithium、cholestyramine、propranolol 9 天後 thyroidectomy，術前 hormone 仍偏高，術後恢復 | 證明感染期仍可能經充分評估後手術；不能直接外推到本案 EF、pneumonia 與結節條件 |
| [Voci 2026](https://pmc.ncbi.nlm.nih.gov/articles/PMC13133480/)，單例 | MMI、PTU 依序 agranulocytosis，EF 35%／decompensated HF；Lugol、G-CSF 與 hemodynamic 評估後 thyroidectomy | 已有 ATD agranulocytosis＋HFrEF＋跨科手術報告，「首例此組合」不可主張；其文中重複的 50% 交叉再發率沒有可接受的專屬分母 |
| [Calissendorff 2017](https://pmc.ncbi.nlm.nih.gov/articles/PMC5434745/)，n=27 | Lugol rescue，26 surgery、1 I-131；9 人因 agranulocytosis 使用 Lugol | 沒有證據顯示 I-131 那一例一定屬 agranulocytosis 子群；Lugol 使用 3 天也不是停碘 3 天 |
| [Fantin et al. 2021](https://academic.oup.com/jes/article/5/Supplement_1/A958/6241039)，conference abstract、單例 | MMI agranulocytosis、ANC 90/µL；lithium 於 I-131 前後短期使用，報告 1 個月 euthyroid | 顯示 lithium→RAI 的已發表摘要個案路徑；僅摘要、追蹤短，且未報告本案的 HFrEF／肺炎／近期雙重碘暴露 |
| [Sazon 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11454931/)，conference abstract | Carbimazole 後 ANC 0；lithium＋prednisone→RAI，短期後 hypothyroidism | 路徑直接相關，惟僅摘要、可核細節與長期追蹤少 |
| [Tamura 2024](https://pubmed.ncbi.nlm.nih.gov/38008728/)，cohort n=185 | KI pretreatment 子群 n=76，停 KI 後再行 I-131 | 說明 KI 並非永久排除 RAI；其整體 outcome 不可稱為 agranulocytosis 個案成功率 |

已有多個「無法用 ATD、用 Lugol／lithium 接上 surgery 或 I-131」的先例。本案潛在價值若成立，應來自**相互衝突的風險如何被實際處理、哪一條根本治療路徑最後被選擇、以及長期結果**；單純同時列出 agranulocytosis、HFrEF、pneumonia、結節尚不足以證明新穎性。

## 其餘值得討論的問題

1. **感染與手術時間**：Day 55 臨床穩定和 Day 57 necrotizing pneumonia 描述如何對照？有無新的 CT、CRP、抗生素療程結束及肺科結論？
2. **Lithium 是否有可歸因效果**：是否有住院實際給藥？採血是固定給藥後多久？最新 Cr／Na／volume 與藥物交互作用如何？
3. **HFrEF 的診斷**：先前 EF 32% 的病因是否另經評估？甲狀腺功能改善後 EF 是否恢復？若未恢復，手術與等待 I-131 的風險如何重新評級？
4. **Steroid／ACTH**：低 ACTH 檢體與 hydrocortisone 給藥的精確時序；是否有理由懷疑獨立 adrenal 病變？短療程 steroid 的檢測／停藥應參照 [2024 ESE–Endocrine Society guideline](https://www.endocrine.org/clinical-practice-guidelines/glucocorticoid-induced-adrenal-insufficiency)，而非單一數值。
5. **個案寫作的因果界線**：ANC 恢復、FT4 下降、腎功能改善都發生在多種介入與自然病程同時變化的時期；任何「某單一藥物造成改善」均須有更強時間證據。
6. **患者偏好與可行性**：偏好 surgery 或 I-131 的理由、是否能承受停碘等待、是否接受手術與 lifelong replacement，不能由醫師意向代替。

## 投稿可行性與資料清單

目前已有足夠資料寫成**多專科教學分析／病例討論初稿**，但所提供病歷截至 Day 64 尚缺已執行的 definitive treatment、後續 FT4／FT3、肺炎與 EF 結局；若主張「成功橋接至手術／I-131」，目前證據不足。最可檢驗的病例報告主軸是：嚴重 ATD agranulocytosis 及 necrotizing pneumonia、HFrEF、結節與 iodine exposure 並存時，團隊如何在兩條 definitive treatment 路徑之間決策，並記錄實際介入與結果。若最終只有討論、沒有實際結局，較合適的是匿名的診斷與決策教學稿，不能寫成成功治療 case report。

依 [CARE checklist](https://www.care-statement.org/checklist)，正式病例稿至少需完整 timeline、診斷挑戰與鑑別、實際介入劑量／期間、患者與臨床追蹤結局、意外事件、患者觀點及 publication consent。ICMJE 對可識別病例資料另要求保護隱私與適當書面同意（[原則](https://www.icmje.org/recommendations/browse/roles-and-responsibilities/protection-of-research-participants.html)）。此 repo 是公開的去識別化研究摘要，**不是已獲投稿同意的公開病例報告**。完整投稿可行性與前例比較另見 [publication assessment](../04-meeting-and-publication/case-report-assessment.md)。

## 證據定位與方法界線

本稿採 [直接原始證據稽核](../03-evidence/thionamide-cross-reaction-audit.md)、[橋接文獻稽核](../03-evidence/bridge-and-definitive-treatment-audit.md) 及四份歷史角色 memo 交叉核對：[診斷](../05-original-research-notes/expanded/case-diagnosis.md)、[用藥安全](../05-original-research-notes/expanded/drug-safety.md)、[根本治療](../05-original-research-notes/expanded/definitive-therapy.md)、[投稿方法](../05-original-research-notes/expanded/publication-methods.md)。Case report 用來證明路徑曾被實作，不能提供本案的平均成功率；cohort 若排除高風險病人，也不能直接宣告本案安全。LlamaParse 解析只作索引材料，Nakamura 圖轉表已知不可靠；關鍵分母以原 PDF 視覺查核為準。
