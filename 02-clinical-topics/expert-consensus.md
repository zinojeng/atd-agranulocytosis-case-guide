# 多方專家完整討論：角色立場、證據、分歧與交叉審查

> 本頁是公開 repo 的完整閱讀版。它把多角色研究稿、交叉質疑及後續 QA correction 依臨床問題重新整理；不是逐字 transcript，也不表示真人專科會診已經舉行。歷史角色全文與修正紀錄保留在[原始研究筆記](../05-original-research-notes/README.md)。

## 如何閱讀這份討論

每個角色的內容分成五層：

1. **角色要保護的臨床終點**。
2. **對現有病例資料的判讀**。
3. **引用的證據與外推限制**。
4. **對其他角色提出的 challenge**。
5. **哪些新資料會改變立場**。

同一項資料可能被不同角色以不同方式使用。例如 EF 32% 對 Surgery 是 perioperative risk，對 Nuclear Medicine 是等待 I-131 期間的 instability risk，對 Cardiology 則先是尚未完成病因與 reversibility 評估的診斷問題。

## 共同病例基準

所有角色最後都應使用以下同一組基準，避免各自選取不同時間點：

| 項目 | 已記錄 | 不應直接推論 |
|---|---|---|
| Agranulocytosis | Day 48 ANC 50/µL | 不能只靠時序證明 carbimazole 是唯一原因 |
| Symptoms | Day 43 fever／sore throat；Day 46 low WBC | 不能把三個日期寫成同一個 onset endpoint |
| Infection | Right middle lobe pneumonia；Day 57 仍記 necrotizing change approaching abscess | ANC／CRP recovery 不等於感染或影像完全清除 |
| Thyroid hormone | FT4 1.61 → 1.32 → 1.21 → 1.13 ng/dL | 不能把下降單獨歸因於 lithium |
| Lithium | Day 57 outpatient prescription；Day 59 level `<0.2` | 缺住院 MAR、服藥次數與抽血 timing，不能判療效或安全 |
| Cardiac | 既往 EF 約 32%、global LV hypokinesis | 不能直接確診 thyrotoxic cardiomyopathy；不知道是否已恢復 |
| Renal／contrast | Day 48 有 Cr 0.94 與 1.53；使用 iohexol | 不知道採血與注射先後，不能稱 contrast caused AKI |
| Iodine | 住院使用 Lugol，另有 iodinated contrast | 缺配方、實際 administration 與 last dose，不能只算日曆決定 RAI readiness |
| Nodules | Right 1.36 cm、left 0.80 cm；文字描述 solid、hypoechoic、microcalcification | 無原始影像、LN mapping、FNA，不能稱 cancer |
| Outcome | Day 64 仍在考慮 thyroidectomy／I-131 | 沒有已完成 definitive treatment 或長期 outcome |

完整 timeline 見[病例摘要](../01-case/case-summary.md)。

---

## 角色一：Case Diagnosis

### 角色立場

先確定哪些是 diagnosis、哪些只是 working diagnosis，避免治療討論建立在過度確定的病名上。

### 對病例的判讀

**Thyrotoxicosis etiology**：Graves disease 是合理的 working diagnosis，但 TRAb 3.00 IU/L 高於一般 reference `<1.99`、低於同一 assay 列示的 Graves-specific cutoff 3.10，位在需要解釋的灰區。雙側 nodules 又保留 toxic nodular disease、autonomous nodule 或 Graves coexistence 的可能。

**Thyroid storm**：病歷出現 BWPS 35→50，但沒有同一時點的 temperature、heart rate、CNS、GI、acute CHF 與 precipitant 分項。Pneumonia 可同時模仿及觸發 storm；既有 EF 32% 也不能自動算成當下 acute CHF。最誠實的表述是「possible thyroid storm, treated clinically; certainty remains limited」。

**Nodules**：若文字描述完全正確，右 1.36 cm nodule 的重建風險可能達 high-suspicion／FNA threshold；左 0.80 cm 通常需額外高風險條件才進入 FNA。這只是條件式重建，不是原影像已正式標為 ACR TI-RADS 5。`Ill-defined` 不等於 `irregular`。

**Steroid／ACTH**：Hydrocortisone exposure 與 ACTH／cortisol 採血 timing 不完整。單一 ACTH `<5` 不能診斷 permanent central adrenal insufficiency。

### 對其他角色的 challenge

- 對 Endocrinology：不要用「正在治療 Graves」反推病因已確診。
- 對 Drug Safety：感染是 agranulocytosis consequence 的可能性高，但 viral／marrow alternatives 是否有足夠資料排除？
- 對 Definitive Therapy：若 thyroid etiology 與 nodule function 未確認，I-131 indication／dose planning 的前提是否完整？
- 對 Publication：標題使用 `ATD-induced` 會不會過早排除 allopurinol？只寫 surgery-versus-RAI 是否忽略 diagnosis uncertainty 本身的教學價值？

### 收到的實質回應

Publication 角色接受因果用語過強的質疑，將主軸改為 severe drug-associated agranulocytosis with uncertain single-agent attribution，並把 Graves／storm certainty 列為與 definitive-treatment choice 同等重要的 teaching point。

### 會改變立場的新資料

TRAb assay details、同時點 BWPS components、原始 ultrasound／Doppler、cervical LN mapping、FNA／cytology，以及適當時機的 scintigraphy／RAIU。

詳細原稿：[Case Diagnosis role](../05-original-research-notes/expanded/case-diagnosis.md)。

---

## 角色二：Endocrinology

### 角色立場

Severe agranulocytosis 後 thionamide 已失去一般安全性。Bridge 的目標是讓病人安全抵達 definitive treatment，而不是成為沒有期限的替代治療。

### 對病例的判讀

**Carbimazole／PTU**：Carbimazole 是 methimazole prodrug，換 methimazole 不能避開 active drug。另一 thionamide 在 severe hematologic reaction 後通常視為 contraindicated；ATA 對 life-threatening thyroid storm 的極窄短期 PTU 例外，不可延伸成一般換藥建議。

**Hormone control**：FT4 的下降方向良好，但缺同步 FT3、完整 medication administration 與 clinical trajectory，不能判定是哪一項 bridge 造成。若病人已 clinically stable，重點是設定下一步 definitive-treatment readiness，而非追逐單一 laboratory target。

**Non-thionamide bridge**：可能 component 包括 beta blockade、iodide、glucocorticoid、cholestyramine、lithium；極端情況可能考慮 therapeutic plasma exchange。每項都需要心、腎、感染與 drug-interaction 條件，不是可以自由疊加的清單。

**Thyroid storm**：Hormone level 不必很高才能有 storm，但 infection、HF 與 medication effects 使本案必須依 organ dysfunction 重新評估。

### 對其他角色的 challenge

- 對 Hematology／Methods：15.2%、34% 與 50% 的分母與 endpoint 是否真的支持 agranulocytosis recurrence？
- 對 Nuclear Medicine：EANM 的一般 washout days 能否直接用於有 contrast、Lugol 與 recent renal fluctuation 的個案？
- 對 Cardiology：若不能等待 thyroid normalization 才做 repeat echo，最低限度如何判定 compensated status？

### 收到的實質回應

Methods 與 Hematology 均確認常見 cross-reaction 數字屬 all-ADR 或 rash context，不提供本案 agranulocytosis-specific probability。Nuclear Medicine 同意用 RAIU／必要時 urinary iodine 與 renal course 檢驗 readiness，不把日曆當唯一條件。

### 會改變立場的新資料

同步 FT4／FT3／TSH、實際 bridge administration、clinical symptoms、hemodynamics、RAIU，以及病人能否完成等待期 monitoring。

詳細原稿：[Endocrinology role](../05-original-research-notes/first-round/endocrinology.md)。

---

## 角色三：Hematology

### 角色立場

先定義嚴重度、完成 competing-drug causality，再把 neutrophil recovery、infection outcome 與 G-CSF efficacy 分開。

### 對病例的判讀

**嚴重度**：ANC 50/µL 明確屬 severe agranulocytosis，合併 pneumonia 使臨床風險更高。

**Causality**：Carbimazole 的 43–48 day latency 與症狀吻合，是最強候選；但 allopurinol 實際開始、停止與 adherence 未知，其他 marrow-toxic drugs 也需從 MAR 核對。正式稿可寫 suspected／associated，不能寫 proven sole cause。

**Onset timing**：約第六至七週屬常見窗口。Nakamura 的約 85% 是已發病病例中前 90 天的比例，不是服藥者的發生率；90 天後也不是零風險。

**PTU re-exposure**：少數 case reports 證明另一 thionamide 後可再發 agranulocytosis，但無法量化個人風險。All-ADR 分母不能冒充 hematologic recurrence rate。

**G-CSF**：Fukata 1999 small randomized trial（n=24）未證明明確 recovery-time benefit；observational cohorts／meta-analysis 常呈較快 recovery，但存在 confounding by indication。Day 48→51 ANC recovery 不能由單病例拆出停藥、G-CSF、infection control 與 spontaneous marrow recovery 的比例。

### 對其他角色的 challenge

- 對 Endocrinology：既然 PTU recurrence rate 無法精確量化，治療建議的依據應明示為 severity、class concern、guideline 與 alternatives，而非假精確百分比。
- 對 Infection：ANC recovery 後仍存在的 lung lesion 應使用哪個 clinical endpoint？
- 對 Publication：若 allopurinol exposure 未知，case title 如何避免因果過度主張？

### 收到的實質回應

Endocrinology 與 Publication 接受不用 15%／50% 量化本案風險；整合稿把因果改為 drug-associated／carbimazole highly suspected。Infection 視角保留 clinical、laboratory 與 imaging recovery 的分離。

### 會改變立場的新資料

完整 MAR、allopurinol exposure、其他 marrow-toxic agents、serial CBC、bone-marrow／viral evaluation（若臨床曾做），以及 G-CSF exact timing／dose。

詳細原稿：[Hematology role](../05-original-research-notes/first-round/hematology.md)。

---

## 角色四：Drug Safety／Clinical Pharmacology

### 角色立場

所有 efficacy 與 toxicity 判讀都必須把 dose、實際 administration、採血 timing、renal clearance、volume／sodium 與 interacting drugs 放在一起。

### 對病例的判讀

**Lithium attribution**：FT4 在 Day 57 outpatient prescription 前已從 1.61 降至 1.21。Day 59 level `<0.2` 缺 first dose、last dose、服藥次數、adherence 與 blood-draw interval，因此既不能證明無效，也不能證明沒有 toxicity risk。

**Lithium monitoring**：最低資料包括 Cr／eGFR、Na／K、volume status、weight、input／output、clinical neurologic／GI symptoms，以及 NSAID、diuretic、renin–angiotensin system drugs 等相互作用。Sacubitril/valsartan 與 spironolactone／diuretic context 特別需要核對。

**Glucocorticoid**：可能降低 peripheral T4→T3 conversion，但 active／recent infection、diabetes、myopathy、delirium 與 HPA suppression 都是代價。ACTH interpretation 也必須知道最後 steroid dose。

**Beta-blocker／calcium-channel blocker**：Thyrotoxic symptom control 的一般效益不能蓋過 low-output／decompensated HF 的 hemodynamic risk。

**Cholestyramine**：可增加 thyroid hormone elimination，但會影響其他 oral drugs absorption，需要 medication-spacing plan。

**Therapeutic plasma exchange**：可作 rescue bridge，主要證據為 case report／series；要評估 procedure、vascular access、hemodynamic 與 resource risk。

### 對其他角色的 challenge

- 對 Case Diagnosis：Glucocorticoid 與 infection 是否改變 thyroid-storm components 和 ACTH 判讀？
- 對 Nuclear Medicine：若要以 lithium bridge 等待 uptake，等待長度與 monitoring burden 是否已量化？
- 對 Cardiology：HF medications 與 volume management 如何改變 lithium clearance？
- 對 Publication：不要把 `lithium level <0.2` 寫成 treatment failure 或 underdosing。

### 收到的實質回應

Definitive Therapy 接受 lithium effect 無法由本案歸因，也接受 I-131 waiting plan 必須包含 renal／Na／volume 與 rescue threshold。Case Diagnosis 將 steroid timing 保留為 HPA-axis 未解資料。

### 會改變立場的新資料

Inpatient／outpatient MAR、adherence、12-hour or actual level timing、serial renal／Na、volume、interacting medication list 與 clinical toxicity assessment。

詳細原稿：[Drug Safety role](../05-original-research-notes/expanded/drug-safety.md)。

---

## 角色五：Infection／Pulmonology

### 角色立場

Bone-marrow recovery、systemic inflammation decline、clinical pneumonia improvement 與 radiographic resolution 是四個不同 endpoint。Definitive-treatment readiness 不能只看 ANC 或 CRP。

### 對病例的判讀

- Day 51 ANC 已恢復，代表 severe neutropenia 的 immediate hematologic phase 改善。
- Day 54 CRP 明顯下降，支持 inflammatory response 改善。
- Discharge chest film 仍有 right-middle-lobe infiltrate。
- Day 57 仍描述 slowly resolving necrotizing pneumonia approaching abscess。

因此不能說「感染已清除」。另一方面，影像異常也可能落後於 clinical recovery，不能只因仍有 opacity 就自動永久排除 surgery。需要把 symptoms、fever、oxygen、culture、antibiotic duration、imaging trend 與 source-control concern 放在一起。

### 對其他角色的 challenge

- 對 Surgery／Anesthesia：你們需要的是完全 radiographic resolution，還是 clinical control 與 acceptable physiologic reserve？
- 對 Nuclear Medicine：延後 I-131 是否會延長 steroid／bridge exposure，反而增加 infection risk？
- 對 Hematology：ANC recovery 後還需要哪些 immune／marrow follow-up 才能支持 procedure？
- 對 Endocrinology：Thyroid hormone rebound 與 infection recurrence 的 rescue plan 是否明確？

### 討論後的共識

沒有找到單一、可普遍套用的 imaging 或 CRP threshold。Readiness 應由 Infection／Pulmonology、Anesthesia、Surgery 與 Cardiology 共同判斷，並清楚寫出接受的 residual risk。

### 會改變立場的新資料

Current symptoms、oxygen requirement、antibiotic end date、culture、repeat chest imaging、abscess／drainage assessment，以及 Infection／Pulmonology 的 procedure-readiness conclusion。

此角色內容主要整合自 [Drug Safety role](../05-original-research-notes/expanded/drug-safety.md) 與[完整病例研究](../01-case/comprehensive-review.md)。

---

## 角色六：Nuclear Medicine

### 角色立場

I-131 是否可做，不能只靠「停 iodide 幾天」決定；必須確認 thyroid uptake、病因、nodule function、renal clearance 與等待期間的控制能力。

### 對病例的判讀

**Dual iodine exposure**：同時有 water-soluble iodinated contrast 與 therapeutic Lugol／KI。Lugol 的 formulation、每劑 iodine amount、實際 administration 與 last dose 不完整。

**Washout discrepancy**：EANM 2023 一般 preparation framework 提及 Lugol／SSKI 約 2–3 weeks、water-soluble contrast 約 6–8 weeks，contrast 項有 normal renal function 前提；2026 thyroid-storm joint consensus 對大量 therapeutic iodide 後 RAI 採至少 2–3 months 的較保守框架。兩者情境不同，是真實 guideline tension。

**Readiness**：應用 updated renal function、urinary iodine（若適用）與 RAIU／scintigraphy 驗證 uptake，而非任選較短或較長的 calendar rule。若 uptake 低，風險包括 delayed scheduling，也包括 insufficient delivered activity／treatment failure。

**Post-RAI period**：I-131 effect 延遲，且可能有 transient hormone release。Vijayakumar 2006 的 122 visits 無 storm，但排除 complicating intercurrent disease，不能直接外推到同時有 pneumonia、HFrEF 與 recent renal fluctuation 的本案。

### 對其他角色的 challenge

- 對 Endocrinology／Drug Safety：停止 iodide 後靠什麼維持 stability？Lithium 的 administration 與 monitoring 是否可信？
- 對 Cardiology：心臟能承受多長等待期與 potential rebound？
- 對 Diagnosis：若 nodules 的 functional status 未知，I-131 planning 是否完整？
- 對 Surgery：如果 uptake 長期不足，手術 readiness 是否可能更早達成？

### 收到的實質回應

Drug Safety 同意 waiting plan 必須把 lithium safety 與 interaction 寫成明確條件。Case Diagnosis 指出 scintigraphy 同時有助於 Graves／autonomy 與 nodule functional assessment。Surgery 視角同意不應把 missing washout data 解讀成永久排除 I-131，但也不應假設一定會恢復到足夠 uptake。

### 會改變立場的新資料

Exact contrast／iodide timeline、Lugol formulation、renal function、urinary iodine、RAIU／scintigraphy、thyroid volume、nodule function、treatment activity plan 與 post-RAI bridge／rescue plan。

詳細原稿：[Nuclear Medicine／Surgery first-round role](../05-original-research-notes/first-round/nuclear-medicine-and-surgery.md)與[Definitive Therapy role](../05-original-research-notes/expanded/definitive-therapy.md)。

---

## 角色七：Thyroid Surgery／Anesthesia

### 角色立場

Thyroidectomy 能快速而確定地移除 hormone source，也能取得 nodule pathology；真正問題是感染、cardiac、airway 與 metabolic risk 是否已控制到可接受程度。

### 對病例的判讀

**可能優勢**：不必等待 iodine uptake；可避免 prolonged lithium／steroid／other bridge；對 suspicious nodules 可取得 pathology；若 RAI readiness 長期不明，時間優勢更明顯。

**主要風險**：Recent necrotizing pneumonia、EF 約 32%、未知 current volume／rhythm、possible thyroid-storm history、glycemic／steroid issues，以及未完成的 airway／nodule／LN evaluation。

**Preoperative euthyroidism**：傳統上希望在可行時改善 biochemical control，但 ATD contraindication 的病例不能把「未達完全 euthyroid」自動視為永遠不能手術。Case reports 顯示在 intensive preparation、experienced team 與 individualized hemodynamic assessment 下曾完成 surgery；這只證明 feasibility，不提供安全率。

**Nodules**：Right 1.36 cm lesion 若原始 high-risk features 成立，可能增加 FNA／surgical pathology 的重要性；但不能以未複核的文字描述直接診斷 malignancy。

### 對其他角色的 challenge

- 對 Infection：clinical control、antibiotic course、follow-up imaging 與 residual abscess concern 到什麼程度？
- 對 Cardiology：現在是 compensated 還是 decompensated HF？需要哪些 preoperative tests／optimization？
- 對 Endocrinology：若無 thionamide，preoperative bridge 的目標、期限與 rescue plan 是什麼？
- 對 Nuclear Medicine：預計多久可確認足夠 uptake；若未恢復，下一個 decision deadline 是什麼？
- 對 Patient／MDT：是否接受 scar、perioperative risk、potential complications 與 lifelong replacement？

### 討論後的共識

沒有單一 EF 或 infection-imaging number 可以自動批准／否決 surgery。需要 high-volume thyroid surgeon、Anesthesia、Cardiology、Infection 與 Endocrinology 共同形成具體 risk statement。

### 會改變立場的新資料

Repeat echo、rhythm、volume、functional status、oxygen／pulmonary course、airway assessment、nodule／LN review、FNA，以及病人的 informed preference。

詳細原稿：[Definitive Therapy role](../05-original-research-notes/expanded/definitive-therapy.md)。

---

## 角色八：Cardiology

### 角色立場

EF 32% 是已記錄 phenotype，不是已完成的 etiology。需要判斷 reversibility 與 current compensation，並比較 surgery 的 immediate risk 與等待 I-131 的 cumulative risk。

### 對病例的判讀

**Etiology**：Thyrotoxicosis 可能造成或加重 cardiomyopathy，但也需考慮 ischemic、arrhythmic、valvular、hypertensive、metabolic、myocarditis／infiltrative 與 tachycardia-mediated causes。Global hypokinesis 不會自行確立 thyrotoxic cardiomyopathy。

**Reversibility**：其他 cohorts 顯示部分 thyrotoxic cardiomyopathy 可恢復，但時間常以 months 計，且 incomplete follow-up／selection 限制很大。不能假設 FT4 接近 reference 後 EF 已經同步恢復。

**Surgery**：Active decompensation、volume overload、unstable rhythm 或 infection 會增加 perioperative risk；若 compensated 且有 intensive plan，low EF 並非絕對禁忌。

**等待 I-131**：避免 anesthesia 不等於沒有心臟風險。Waiting、hormone rebound、tachyarrhythmia、renal／volume fluctuation 與 lithium interaction 可能累積風險。

### 對其他角色的 challenge

- 對 Endocrinology：目前 heart-rate control 的 hemodynamic tolerance 如何？
- 對 Drug Safety：ARNI／spironolactone／diuretic 與 hydration changes 如何影響 lithium？
- 對 Nuclear Medicine：預期等待多久、多久監測一次、什麼情況改變路徑？
- 對 Surgery／Anesthesia：若 EF 未恢復，哪些 optimized conditions 能使 perioperative risk 可接受？

### 討論後的條件式判讀

- 若 EF 明顯恢復、infection controlled、surgery risk acceptable，而 uptake 仍不足，thyroidectomy 的相對優勢增加。
- 若 EF 持續嚴重下降／近期 decompensation，使 anesthesia risk 暫不可接受，但 uptake 已恢復且 bridge 可安全維持，I-131 的相對優勢可能增加。
- 若兩條路的條件都未成熟，應先 stabilization 與補資料，不應強迫選路。

### 會改變立場的新資料

Repeat echo、ECG／telemetry、rhythm history、volume、functional status、ischemic／valvular workup、GDMT administration／tolerance 與 recent decompensation history。

整理頁：[HFrEF 風險重評](cardiac-risk.md)；詳細討論見 [Case Diagnosis role](../05-original-research-notes/expanded/case-diagnosis.md)與[Definitive Therapy role](../05-original-research-notes/expanded/definitive-therapy.md)。

---

## 角色九：Evidence Methods／Publication Review

### 角色立場

每一個數字都要回到正確分母；每一個 conclusion 都要區分 guideline、trial／cohort、case report 與本案 inference。公開病例的 novelty、causality、outcome 與 consent 不能由角色共識替代。

### 對證據的判讀

**Cross-reaction**：Meyer-Gessner 1989、Otsuka 2012 的數字是 all-ADR；50% 常見於 rash context。不得換成 agranulocytosis recurrence probability。

**Nakamura timing**：總 series n=754 與 timing subgroup n=461／458 必須分開；84.5%／84.6% 是原文內部差異。LlamaParse 對 figures 的 machine-converted tables 不可靠，關鍵數字回到原 PDF text／legend。

**G-CSF**：Small negative RCT 是「未證明有效」，不是「證明所有情境無效」；observational signal 也不證明本案因果。

**Lithium**：存在 randomized／cohort evidence，不能說只有 case reports；但研究 population、renal exclusion 與本案 organ constraints 不同。

**Comparator cases**：Knight 2017、Voci 2026 已有 infection／HF 下的 surgery 路徑；Fantin 2021、Sazon 2024 已有 lithium→I-131，但後兩者主要是 conference abstracts。因而不能稱 first／unique。

### 投稿判讀

現階段最可靠的 contribution 是：當 diagnosis、infection、HFrEF、dual iodine exposure、nodules 與 patient preference 同時限制兩條 definitive-treatment path 時，團隊如何定義 observable readiness conditions。

Day 64 前沒有 definitive treatment 或 long-term outcome，故目前適合 case-based teaching analysis。完整 case report 至少需 actual treatment、infection／cardiac／thyroid outcomes、patient perspective、publication consent 與 institution／journal requirements。

### 對其他角色的 challenge

- 你的百分比是誰的分母？
- 研究排除了哪些與本案相似的 high-risk patients？
- Case report 是證明 feasibility，還是被錯用成成功率？
- Outcome 尚未發生時，是否把 planned treatment 寫成 completed treatment？
- Peer 沉默或 message queued 是否被誤寫成 consensus？

### 收到的實質回應與修正

Case Diagnosis 成功促使 publication thesis 移除過度確定的 `ATD-induced`，並把 diagnostic uncertainty 納入主軸。QA 後續修正了 Vicente reference year、ATA page locator、AKI wording、G-CSF certainty 與 lithium evidence-level statements。

### 會改變立場的新資料

Definitive treatment、procedure／I-131 details、complications、serial thyroid／cardiac／infection outcome、patient perspective、consent，以及更廣泛的 novelty search。

詳細原稿：[Evidence Methods](../05-original-research-notes/first-round/evidence-methods.md)、[Publication Methods](../05-original-research-notes/expanded/publication-methods.md)與[Case-report assessment](../04-meeting-and-publication/case-report-assessment.md)。

---

## 已收斂的跨角色共識

| 共識 | 為什麼能收斂 | 對決策的意義 |
|---|---|---|
| Carbimazole 高度可疑並應避免再暴露 | 時序、known adverse effect 與 severity 一致 | Allergy／severe ADR record 應清楚；仍要補 allopurinol／MAR |
| 不常規改用 PTU | Guideline、severity、class concern 與 case reports 方向一致 | 不能用未驗證百分比支持試換 |
| 6–7 week onset 屬常見時序 | 多角色回到 Nakamura／Meyer-Gessner 的正確分母 | Timing 支持 suspicion，不單獨證明 causality |
| G-CSF 效果不可由本案歸因 | 多項 intervention 同時發生；trial／observation 有張力 | 描述 treatment exposure 與 recovery，不寫單一因果 |
| ANC／CRP／影像是不同 endpoint | Day 57 lung lesion 仍存在 | Surgery／waiting readiness 需獨立 infection assessment |
| Lithium 效果不可由本案歸因 | FT4 decline 早於可確認 prescription；level timing 未知 | 先重建 exposure，再談 efficacy／dose |
| Surgery 與 I-131 均為條件式選項 | 兩邊各有 immediate／delayed risk | 比較可控制的整體風險，不以 procedure 名稱決定 |
| Contrast 不能被宣稱造成 AKI | Cr 與 injection 的分鐘級順序未核對 | 保留 temporal uncertainty，使用最新 renal data |
| Nodules 尚未等於 cancer | 無原圖、LN mapping、FNA／pathology | 影像／細胞學可能改變 treatment path |
| Patient preference 是核心資料 | 兩條路的負擔、速度與 follow-up 不同 | 需要記錄理由與可行性，不能由醫師意向替代 |
| 目前不能宣稱 first／successful case | 已有 comparator；本案缺 definitive outcome | 定位為 teaching analysis，等待 outcome／consent |

## 尚未完全收斂的爭議

| 爭議 | 觀點 A | 觀點 B | 如何收斂 |
|---|---|---|---|
| Lugol washout | EANM 一般框架約 2–3 weeks | 2026 storm consensus 至少 2–3 months | Exact exposure＋renal＋urinary iodine／RAIU |
| G-CSF | Small RCT 未顯著 | Observational／meta-analysis 常見 recovery 加快 | 不以本案作因果；依 severity 與 clinical judgment |
| Surgery timing | 延後至 infection／cardiac optimization | Prolonged delay 有 hormone／bridge／HF risk | Dynamic MDT readiness review，不設單一 threshold |
| I-131 without ATD | Cohort 顯示可執行且 rare storm | High-risk intercurrent disease 常被排除 | Uptake、organ stability、bridge／rescue plan |
| Graves certainty | TRAb 高於 general reference | 低於 disease-specific cutoff 且有 nodules | Assay details＋適時 functional imaging |
| Nodule implication | Recorded descriptors 可達 high-risk direction | 無原圖，ill-defined 不等於 irregular | Expert image review＋LN mapping＋FNA when indicated |
| Lithium target | Trials／labels可提供 monitoring context | Thyroid indication不能直接套 psychiatry range | 以目的、timing、clinical response、renal safety個別評估 |
| Publication novelty | 多重 competing constraints 有教學價值 | 相似 disease combinations 已發表 | 強調 decision process，不宣稱 first／unique |

## 交叉 challenge／response 完整摘要

| 發問角色 → 回應角色 | Challenge | 回應／目前狀態 |
|---|---|---|
| Hematology → Endocrinology | 精確 cross-reaction rate 不明，為何仍避免 PTU？ | 依 severe class-related event、guideline 與 definitive alternatives，而非假精確數字；已收斂 |
| Methods → Hematology | G-CSF small RCT 是否被過度解讀成 universally ineffective？ | 改為「此樣本未證明效益」；保留 observational tension；已修正 |
| Endocrinology → Methods | 15.2%／50% 是否有 agranulocytosis-specific denominator？ | 沒有可用分母；all-ADR／rash context 已釐清；已收斂 |
| Case Diagnosis → Publication | `ATD-induced` 是否過早排除 allopurinol？ | Thesis 改為 uncertain single-agent attribution；已採納 |
| Case Diagnosis → Publication | Surgery-versus-RAI 主軸是否忽略 diagnosis uncertainty？ | 將 Graves／storm／causality uncertainty 提升為主軸；已採納 |
| Drug Safety → Case Diagnosis | Infection、glucocorticoid 如何混淆 BWPS／ACTH？ | 保留同時點資料與 steroid timing 缺口；已收斂 |
| Definitive Therapy → Drug Safety | Lithium level 與 clinical effect 是否可解讀？ | 缺 MAR／timing／renal context，不能判；已收斂 |
| Drug Safety → Definitive Therapy | Taylor 2026 的 2–3 months 與 EANM 2–3 weeks 是否真衝突？ | 兩個原文情境皆存在；並列，使用 uptake／iodine data 收斂 |
| Case Diagnosis ↔ Definitive Therapy | Right／left nodules 是否達 FNA threshold？ | 兩種 guideline framework 方向一致：right 可能達門檻，left 通常未達；仍需原圖 |
| Definitive Therapy → Publication | Voci 2026 是否已降低 `agranulocytosis＋HFrEF＋surgery` novelty？ | 是；不再使用 first／unique，改寫成 decision-process contribution |
| Cardiology → Nuclear Medicine | 等待 uptake 時心臟能承受多久？ | 尚無病人特定答案；需 repeat echo、monitoring interval、rescue／switch threshold；OPEN |
| Infection → Surgery | CRP decline 是否足以進手術？ | 否；需 clinical、oxygen、imaging、antibiotic course 與 multidisciplinary judgment；OPEN |
| Surgery → Nuclear Medicine | 若 uptake 未恢復，何時停止等待？ | 需預先設定 decision deadline；本案未記錄，OPEN |
| Publication → 全體 | Day 64 後 outcome、patient perspective、consent 在哪裡？ | 目前資料沒有；正式 case report 仍未完成，OPEN |

## MDT 決策責任矩陣

| 決策 | 主責角色 | 共同參與 | 會前最低資料 |
|---|---|---|---|
| Agranulocytosis causality／avoidance list | Hematology／Drug Safety | Endocrinology、Pharmacy | Complete MAR、allopurinol、CBC course |
| Infection procedure readiness | Infection／Pulmonology | Anesthesia、Surgery、Cardiology | Symptoms、oxygen、imaging、antibiotics、culture |
| HFrEF compensation／perioperative risk | Cardiology | Anesthesia、Endocrinology | Echo、rhythm、volume、functional status、GDMT |
| Graves／storm diagnostic wording | Endocrinology／Case Diagnosis | Infection、Cardiology | TRAb assay、BWPS components、thyroid tests |
| Nodule FNA／surgical implication | Thyroid imaging／Endocrinology | Surgery、Nuclear Medicine | Original images、LN mapping、FNA／cytology |
| I-131 uptake readiness | Nuclear Medicine | Endocrinology、Pharmacy／Nephrology | Iodide／contrast timeline、renal、urinary iodine／RAIU |
| Lithium continuation／monitoring | Endocrinology／Clinical Pharmacy | Cardiology、Nephrology | MAR、level timing、Cr／eGFR、Na、volume、interactions |
| Thyroidectomy readiness | Surgery／Anesthesia | Endocrinology、Cardiology、Infection | Infection＋cardiac＋airway＋nodule assessment |
| Surgery versus I-131 | Patient＋MDT | 所有相關角色 | Feasible timing、risks、alternatives、patient goals |
| Case publication | Treating team／Publication reviewer | Patient、institution | Outcome、perspective、consent、privacy review |

## 目前 OPEN registry

### 會直接改變治療路徑

1. Day 64 後是否實際接受 thyroidectomy 或 I-131？
2. Necrotizing pneumonia 現在的 symptoms、oxygen、imaging 與 antibiotic outcome？
3. Repeat EF、rhythm、volume 與 functional status？
4. Lugol formulation、actual dose、last dose 與全部 iodine exposure？
5. Urinary iodine／RAIU 是否顯示足夠 uptake？
6. Right nodule 的 original images、LN mapping、FNA／cytology？
7. Patient preference 的理由與生活可行性？

### 會改變 drug-safety 判讀

8. Allopurinol 的開始、停止、adherence 與 indication？
9. 住院 lithium 是否真的 administration？
10. Day 59 level 距最後一劑多久？
11. 最新 Cr／eGFR、Na／K、weight、congestion／dehydration？
12. NSAID、diuretic、ARNI、spironolactone 與 antibiotic 的實際 concurrent use？
13. G-CSF exact administration 與 CBC trajectory？

### 會改變 diagnosis／publication 判讀

14. BWPS 35／50 的同時點原始 components？
15. TRAb assay platform、reference 與 Graves-specific cutoff？
16. Hydrocortisone 最後一劑與 ACTH／cortisol 採血 timing？
17. Long-term thyroid、cardiac、infection outcomes？
18. Patient perspective、publication consent 與 institution policy review？

## 如果新資料到位，各角色如何更新立場

| 新資料 | 可能使 Surgery 相對有利 | 可能使 I-131 相對有利 | 仍不足以單獨決定 |
|---|---|---|---|
| Infection 明顯控制 | 降低 perioperative risk | 也降低等待期 systemic risk | 仍需 cardiac／uptake／preference |
| EF 明顯恢復／compensated | 降低 anesthesia risk | 也提高等待耐受性 | 不能單獨選路 |
| RAIU 足夠 | 不直接排除 surgery | 解除 I-131 技術性障礙 | 仍需 delayed-effect／bridge plan |
| RAIU 持續很低 | 等待的機會成本增加 | I-131 failure risk 增加 | 需確認 exposure／renal 原因與可逆性 |
| Right nodule FNA suspicious／malignant | Pathology／definitive surgery 優勢增加 | I-131 for Graves 不能取代 cancer pathway | 需正式 cytology／staging |
| Lithium intolerable／unsafe | 避免 prolonged bridge 的優勢增加 | 等待 I-131 更困難 | 仍可能有其他 bridge／rescue |
| 病人拒絕 surgery | 手術不可行 | 若 uptake／safety 達標則相對有利 | 需確認 informed refusal 與替代可行性 |
| 病人無法承受長期等待／頻繁追蹤 | 較快 definitive control 可能較合適 | I-131 pathway feasibility 降低 | 仍需 perioperative acceptability |

## 原始角色稿與 QA 對照

| 內容 | 完整原稿 |
|---|---|
| Endocrinology | [first-round/endocrinology.md](../05-original-research-notes/first-round/endocrinology.md) |
| Hematology | [first-round/hematology.md](../05-original-research-notes/first-round/hematology.md) |
| Nuclear Medicine／Surgery | [first-round/nuclear-medicine-and-surgery.md](../05-original-research-notes/first-round/nuclear-medicine-and-surgery.md) |
| Evidence Methods | [first-round/evidence-methods.md](../05-original-research-notes/first-round/evidence-methods.md) |
| Case Diagnosis | [expanded/case-diagnosis.md](../05-original-research-notes/expanded/case-diagnosis.md) |
| Drug Safety／Infection | [expanded/drug-safety.md](../05-original-research-notes/expanded/drug-safety.md) |
| Definitive Therapy | [expanded/definitive-therapy.md](../05-original-research-notes/expanded/definitive-therapy.md) |
| Publication Methods | [expanded/publication-methods.md](../05-original-research-notes/expanded/publication-methods.md) |
| 第一輪 reconciliation | [quality-review/reconciliation.md](../05-original-research-notes/quality-review/reconciliation.md) |
| 擴充輪 reconciliation | [quality-review/expanded_reconciliation.md](../05-original-research-notes/quality-review/expanded_reconciliation.md) |
| Independent clinical review | [quality-review/independent_clinical_review.md](../05-original-research-notes/quality-review/independent_clinical_review.md) |
| Independent bridge review | [quality-review/independent_bridge_review.md](../05-original-research-notes/quality-review/independent_bridge_review.md) |

## 建議下一次 MDT 的輸出格式

會議不應只留下「傾向 surgery」或「考慮 I-131」。每一條路至少填完：

| 欄位 | Thyroidectomy | I-131 |
|---|---|---|
| 已滿足條件 |  |  |
| 尚未滿足條件 |  |  |
| 負責補資料的人 |  |  |
| 預計完成時間 |  |  |
| 等待期間 bridge |  |  |
| Monitoring frequency |  |  |
| Rescue／switch threshold |  |  |
| 病人主要顧慮 |  |  |
| 最終共同決策 |  |  |

相關閱讀：[完整病例研究](../01-case/comprehensive-review.md)、[Diagnosis](diagnosis.md)、[Drug Safety／Infection](drug-safety-and-infection.md)、[Definitive Treatment](definitive-treatment.md)、[HFrEF](cardiac-risk.md)、[Literature map](../03-evidence/literature-map.md)與[公開網站專家頁](https://atd-agranulocytosis-case-guide.zinojeng.chatgpt.site/experts.html)。
