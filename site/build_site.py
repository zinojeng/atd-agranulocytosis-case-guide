from pathlib import Path


OUT = Path(__file__).parent / "dist"
OUT.mkdir(exist_ok=True)

PAGES = [
    ("index.html", "總覽", "先看懂病例與目前結論"),
    ("case.html", "病例與時間線", "已知事實、數字與紀錄歧異"),
    ("diagnosis.html", "診斷問題", "Graves、thyroid storm、nodules、steroid"),
    ("safety.html", "藥物與感染", "Agranulocytosis、換藥、G-CSF、bridge"),
    ("experts.html", "多方專家論點", "角色立場、共識、分歧與交叉質疑"),
    ("i131.html", "Lithium 與 I-131", "可歸因性、停碘與五階段路徑"),
    ("cardiac.html", "HFrEF", "EF 32% 的病因與風險重評"),
    ("evidence.html", "文獻比較", "Guideline、cohort、case report 分層"),
    ("publication.html", "投稿與待補", "CARE、患者觀點與會議問題"),
    ("sources.html", "來源索引", "原始文獻、查核方法與限制"),
]


def sidebar(current: str) -> str:
    links = []
    for filename, label, desc in PAGES:
        active = ' aria-current="page" class="active"' if filename == current else ""
        links.append(
            f'<a href="./{filename}"{active}><strong>{label}</strong><span>{desc}</span></a>'
        )
    return "\n".join(links)


def layout(filename: str, title: str, eyebrow: str, intro: str, toc: str, body: str) -> str:
    return f'''<!doctype html>
<html lang="zh-Hant">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="description" content="去識別化 ATD agranulocytosis 個案研究：{title}。繁體中文易讀版。">
  <meta name="color-scheme" content="light dark">
  <title>{title}｜ATD Agranulocytosis 個案研究</title>
  <link rel="stylesheet" href="./styles.css">
</head>
<body data-page="{filename}">
  <a class="skip-link" href="#main">跳到主要內容</a>
  <header class="topbar">
    <a class="brand" href="./index.html"><span class="brand-mark">ATD</span><span><strong>Agranulocytosis</strong><small>跨專科病例研究</small></span></a>
    <nav class="top-links" aria-label="快捷導覽">
      <a href="./case.html">病例</a><a href="./experts.html">專家論點</a><a href="./i131.html">I-131</a><a href="./cardiac.html">HFrEF</a><a href="./evidence.html">文獻</a>
    </nav>
    <div class="view-tools">
      <button id="fontToggle" type="button" aria-pressed="false">放大文字</button>
      <button id="themeToggle" type="button" aria-pressed="false">切換色彩</button>
      <button id="menuToggle" class="menu-button" type="button" aria-expanded="false">目錄</button>
    </div>
  </header>
  <div class="site-shell">
    <aside class="sidebar" id="sidebar" aria-label="全站內容">
      <div class="sidebar-heading">閱讀地圖</div>
      {sidebar(filename)}
      <div class="legend">
        <span><i class="dot known"></i> 已記錄</span>
        <span><i class="dot inferred"></i> 條件式判讀</span>
        <span><i class="dot open"></i> 尚待補資料</span>
      </div>
    </aside>
    <main class="content" id="main">
      <header class="page-hero">
        <div class="eyebrow">{eyebrow}</div>
        <h1>{title}</h1>
        <p>{intro}</p>
        <div class="page-meta"><span>資料查核至 2026-09-19</span><span>去識別化 relative-day 資料</span><span>臨床討論用途</span></div>
      </header>
      <nav class="on-this-page" aria-label="本頁目錄"><strong>本頁閱讀</strong>{toc}</nav>
{body}
      <section class="page-end">
        <div><strong>解讀原則</strong><p>本文把病歷事實、文獻結果、條件式推論與未解問題分開。它不提供個別處方，也不取代 Endocrinology、Nuclear Medicine、Cardiology、Infection、Anesthesia 與 Surgery 的共同決策。</p></div>
        <a href="./sources.html">查看完整來源與方法 →</a>
      </section>
    </main>
  </div>
  <footer><span>ATD Agranulocytosis 個案研究</span><span>Public de-identified clinical research site</span></footer>
  <script src="./app.js"></script>
</body>
</html>'''


overview = r'''
<section class="key-message" id="summary">
  <div><span class="status open">目前狀態</span><h2>根本治療尚未完成，真正問題是如何安全到達 surgery 或 I-131</h2></div>
  <p>這是一位五十多歲女性，在使用 carbimazole 約六週後發生 severe agranulocytosis，並合併右中葉 pneumonia。ANC 已恢復，但感染、既有 HFrEF、iodine exposure、renal fluctuation 與可疑 thyroid nodules，讓兩條 definitive treatment 路徑都有待滿足的條件。</p>
</section>

<section class="section" id="facts">
  <div class="section-title"><span>01</span><div><h2>八個先知道的重點</h2><p>先分清已記錄事實與目前不能確定的結論。</p></div></div>
  <div class="card-grid four">
    <article class="stat-card"><small>最低 ANC</small><strong>50/µL</strong><p>Day 48，符合 severe agranulocytosis。</p></article>
    <article class="stat-card"><small>發病時序</small><strong>Day 43–48</strong><p>Fever／sore throat 到 ANC 確認，約第六至七週。</p></article>
    <article class="stat-card"><small>既往心功能</small><strong>EF 約 32%</strong><p>沒有較新的 repeat echo。</p></article>
    <article class="stat-card"><small>FT4 走向</small><strong>1.61 → 1.13</strong><p>下降早於 Day 57 門診 lithium。</p></article>
    <article class="info-card known"><span>已記錄</span><h3>ANC 回升很快</h3><p>Day 51 ANC 4.14×10³/µL；多項治療同時進行，不能歸因於單一介入。</p></article>
    <article class="info-card open"><span>仍未知</span><h3>Pneumonia 是否完全清除</h3><p>Day 57 仍記載 necrotizing pneumonia 緩慢改善、接近 abscess。</p></article>
    <article class="info-card inferred"><span>條件式</span><h3>Surgery 與 I-131 都可評估</h3><p>選擇取決於 infection、EF、nodules、iodine washout、RAIU 與病人偏好。</p></article>
    <article class="info-card open"><span>仍未知</span><h3>Day 64 後 outcome</h3><p>沒有 definitive treatment、長期 thyroid、肺部或心臟結局。</p></article>
  </div>
</section>

<section class="section" id="decisions">
  <div class="section-title"><span>02</span><div><h2>目前四個決策核心</h2><p>每個問題都有獨立頁面，可繼續往下讀。</p></div></div>
  <div class="route-grid">
    <a href="./safety.html#causality"><span>藥物安全</span><h3>Carbimazole 是唯一原因嗎？能換 PTU 嗎？</h3><p>時序高度相符，但 allopurinol exposure 未清；換藥百分比常被錯用。</p><b>查看 agranulocytosis 證據 →</b></a>
    <a href="./i131.html#attribution"><span>Lithium</span><h3>FT4 下降能不能歸因於 lithium？</h3><p>門診處方前已下降；level 採血時點與住院實際給藥未知。</p><b>查看可歸因性與監測 →</b></a>
    <a href="./i131.html#pathway"><span>I-131</span><h3>停 iodide 期間如何安全 bridge？</h3><p>用 RAIU、renal function 與末劑確認 readiness，不能只算日曆。</p><b>查看五階段路徑 →</b></a>
    <a href="./cardiac.html#reassessment"><span>HFrEF</span><h3>EF 32% 是否會恢復？</h3><p>Thyrotoxic cardiomyopathy 尚未確立；需要 repeat echo 與病因重建。</p><b>查看風險重評 →</b></a>
  </div>
</section>

<section class="section" id="pathways">
  <div class="section-title"><span>03</span><div><h2>兩條根本治療路徑</h2><p>目前不是選名字，而是確認哪條路的風險可以被控制。</p></div></div>
  <div class="compare-cards">
    <article><div class="compare-head surgery"><span>A</span><h3>Thyroidectomy</h3></div><ul><li>較快移除 hormone source</li><li>可取得 nodule pathology</li><li>需先處理 infection、HF 與 anesthesia risk</li><li>術後需要 thyroid hormone replacement</li></ul><a href="./i131.html#comparison">完整條件比較</a></article>
    <article><div class="compare-head rai"><span>B</span><h3>I-131</h3></div><ul><li>避免手術與 anesthesia</li><li>起效延遲，等待期仍有風險</li><li>Contrast／Lugol 會抑制 uptake</li><li>常以 hypothyroidism 為治療目標或結果</li></ul><a href="./i131.html#pathway">完整停碘與 bridge 流程</a></article>
  </div>
</section>

<section class="section" id="read-map">
  <div class="section-title"><span>04</span><div><h2>依你的問題選擇閱讀路徑</h2><p>不必從頭讀到尾。</p></div></div>
  <div class="reading-map">
    <a href="./case.html"><strong>想先掌握全案</strong><span>病例時間線、重要數字、紀錄歧異</span></a>
    <a href="./diagnosis.html"><strong>想確認診斷</strong><span>Graves、storm、nodules、ACTH</span></a>
    <a href="./safety.html"><strong>想處理用藥安全</strong><span>換 PTU、G-CSF、infection、其他 bridge</span></a>
    <a href="./experts.html"><strong>想比較多方專家論點</strong><span>各角色立場、共識、分歧與交叉質疑</span></a>
    <a href="./i131.html"><strong>想規劃 I-131</strong><span>Lithium、停碘、RAIU、patient preference</span></a>
    <a href="./cardiac.html"><strong>想重評 EF 32%</strong><span>病因、repeat echo、surgery vs waiting risk</span></a>
    <a href="./evidence.html"><strong>想核對文獻</strong><span>研究設計、分母、可外推範圍</span></a>
    <a href="./publication.html"><strong>想準備會議或投稿</strong><span>CARE gaps、問題清單、可寫主軸</span></a>
    <a href="./sources.html"><strong>想看全部來源</strong><span>Guideline、primary studies、official labels</span></a>
  </div>
</section>
'''

case_body = r'''
<section class="section" id="snapshot">
  <div class="section-title"><span>01</span><div><h2>病例摘要</h2><p>這裡只放病歷目前能支持的內容。</p></div></div>
  <div class="prose-card">
    <p>五十多歲女性，有 thyrotoxicosis、type 2 diabetes 與既有 HFrEF。開始 carbimazole 10 mg daily 後，Day 43 出現 fever／sore throat；Day 46 外院 WBC 約 730/µL；Day 48 入院 ANC 50/µL、CRP 30.12 mg/dL，影像顯示右中葉 pneumonia。</p>
    <p>停 carbimazole 後接受 antibiotics、G-CSF、Lugol、glucocorticoid 與心率控制。Day 51 ANC 已恢復，但出院胸片仍有 infiltrate；Day 57 肺科描述 necrotizing pneumonia 緩慢改善、接近 abscess。血球恢復與感染清除是不同終點。</p>
    <p>FT4 由 Day 48 的 1.61 降至 Day 59 的 1.13 ng/dL。Day 57 才有門診 lithium 150 mg daily 處方；住院是否給藥與 Day 59 level 的採血時點不明。Day 64 仍在討論 thyroidectomy 或 I-131。</p>
  </div>
</section>

<section class="section" id="timeline">
  <div class="section-title"><span>02</span><div><h2>完整 relative-day 時間線</h2><p>避免使用可識別日期，也保留原始紀錄不一致。</p></div></div>
  <ol class="timeline">
    <li><time>Day 0</time><div><h3>開始 carbimazole</h3><p>10 mg daily；沒有完整逐日 dispensing／administration 紀錄。</p></div></li>
    <li><time>Day 43</time><div><h3>Fever／sore throat</h3><p>約第六週，是 agranulocytosis 的警示症狀。</p></div></li>
    <li><time>Day 46</time><div><h3>外院 severe leukopenia</h3><p>WBC 約 730/µL；同次 ANC 未提供。</p></div></li>
    <li><time>Day 47–48</time><div><h3>停藥日有一天差異</h3><p>家屬敘述與住院摘要不同；正式病例應保留兩種紀錄。</p></div></li>
    <li class="critical"><time>Day 48</time><div><h3>ANC 50/µL＋pneumonia</h3><p>WBC 0.8×10³/µL、CRP 30.12 mg/dL。接受 iohexol 75 mL。CT 開立資訊列 Cr 0.94／eGFR 約 65，同日另一筆 Cr 1.53；目前無法確定抽血與注射先後。</p></div></li>
    <li><time>Day 49–55</time><div><h3>住院 non-thionamide bridge</h3><p>Lugol 約 2 mL Q8H；配方濃度、實際每劑與最後一劑未知。另使用 hydrocortisone 與心率控制。</p></div></li>
    <li><time>Day 51</time><div><h3>ANC 恢復</h3><p>ANC 4.14×10³/µL，後續 Cr 0.59 mg/dL。因停藥、G-CSF、抗感染與自然恢復同時發生，單病例不能拆出各自效果。</p></div></li>
    <li><time>Day 54–59</time><div><h3>FT4 持續下降</h3><p>Day 54 1.32、Day 57 1.21、Day 59 1.13 ng/dL；reference 0.70–1.48。</p></div></li>
    <li><time>Day 55–57</time><div><h3>感染尚未等同清除</h3><p>出院胸片仍有 infiltrate；Day 57 記載 necrotizing pneumonia 緩慢改善、接近 abscess。</p></div></li>
    <li><time>Day 57–59</time><div><h3>門診 lithium</h3><p>處方 150 mg daily。Day 59 lithium &lt;0.2，但不知是否已服用、服用幾次、採血距前一劑多久。</p></div></li>
    <li><time>Day 64</time><div><h3>Definitive therapy 未定</h3><p>門診傾向 thyroidectomy，病人仍考慮；尚無 surgery／I-131 執行紀錄。</p></div></li>
  </ol>
</section>

<section class="section" id="labs">
  <div class="section-title"><span>03</span><div><h2>數字怎麼讀</h2><p>避免把不同終點或不同時點混在一起。</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>資料</th><th>已知</th><th>不能推論</th><th>下一個需要</th></tr></thead><tbody>
    <tr><td>ANC</td><td>Day 48 50/µL；Day 51 4.14×10³/µL</td><td>不能把快速恢復全歸因於 G-CSF</td><td>完整 CBC、G-CSF administration 與 infection course</td></tr>
    <tr><td>FT4</td><td>1.61→1.32→1.21→1.13</td><td>不能由曲線證明 lithium 單獨有效</td><td>同步 FT3、每項 bridge 的實際時間</td></tr>
    <tr><td>Renal</td><td>Day 48 有 0.94 與 1.53，後降 0.59</td><td>不能確認 contrast 注射當下已有 AKI，也不能歸因 contrast</td><td>分鐘級採血與注射時間戳、最新 Cr／eGFR</td></tr>
    <tr><td>Inflammation</td><td>CRP 30.12→Day 54 1.61 mg/dL</td><td>CRP 下降不等同 necrotizing lesion 已消失</td><td>症狀、影像、抗生素結束日與肺科／感染科結論</td></tr>
    <tr><td>Lithium</td><td>Day 59 &lt;0.2</td><td>不能判 underdosing、nonresponse 或 absence of toxicity risk</td><td>MAR、adherence、12-hour timing、renal／Na／volume</td></tr>
  </tbody></table></div>
</section>

<section class="section" id="uncertainties">
  <div class="section-title"><span>04</span><div><h2>病例中的關鍵歧異</h2><p>這些不是小細節，會直接改變決策。</p></div></div>
  <div class="issue-list">
    <article><span>01</span><div><h3>Carbimazole 最後一劑</h3><p>Day 47 或 Day 48；需 pharmacy／MAR 確認。</p></div></article>
    <article><span>02</span><div><h3>Contrast 與 Cr 的先後</h3><p>需要精確時間戳，避免錯誤因果敘述。</p></div></article>
    <article><span>03</span><div><h3>Lugol 實際 iodine load</h3><p>2 mL 不能在不知道製劑濃度時換算成 mg。</p></div></article>
    <article><span>04</span><div><h3>BWPS 35→50 的組成</h3><p>缺同時點 temperature、HR、CNS、GI、CHF 與 trigger 分項。</p></div></article>
    <article><span>05</span><div><h3>住院 lithium</h3><p>有建議不等於 medication administration 已完成。</p></div></article>
    <article><span>06</span><div><h3>Day 64 後發生什麼</h3><p>這會決定報告是 teaching analysis 或完整 case report。</p></div></article>
  </div>
</section>
'''

diagnosis_body = r'''
<section class="section" id="etiology">
  <div class="section-title"><span>01</span><div><h2>Thyrotoxicosis 病因仍是工作診斷</h2><p>現有資料支持 Graves，但尚未到高信心確診。</p></div></div>
  <div class="two-col">
    <article class="prose-card"><h3>支持 Graves 的資料</h3><ul><li>TRAb 3.00 IU/L，高於一般 reference &lt;1.99。</li><li>曾以 carbimazole 治療，臨床團隊以 Graves／thyrotoxicosis 處理。</li><li>Glucocorticoid／iodide 後 hormone 下降，方向相容但沒有病因專一性。</li></ul></article>
    <article class="prose-card caution"><h3>降低確定度的資料</h3><ul><li>同一 assay 的 Graves-specific cutoff 為 3.10，數值落在灰區。</li><li>雙側 thyroid nodules 可能與 Graves 並存，也可能涉及 autonomous function。</li><li>Ultrasound 在治療後完成，normal vascularity 不能排除 Graves。</li><li>Contrast 與 Lugol 使近期 scintigraphy／RAIU 可能失真。</li></ul></article>
  </div>
  <div class="next-action"><strong>能縮小不確定性的資料</strong><span>原始 ultrasound 與 Doppler、完整 TRAb assay 說明、適當 washout 後 scintigraphy／RAIU、結節 hot／cold 定位。</span></div>
</section>

<section class="section" id="storm">
  <div class="section-title"><span>02</span><div><h2>Thyroid storm：曾被懷疑並處置</h2><p>目前缺資料，無法把 BWPS 數字當作已確立診斷。</p></div></div>
  <div class="key-message compact"><div><span class="status inferred">最佳用語</span><h3>Possible thyroid storm treated clinically; diagnostic certainty remains limited.</h3></div><p>Thyroid storm 是臨床診斷，hormone level 不必極高；但 BWPS 的 fever、tachycardia、CNS、GI、CHF 與 precipitant 必須用同一時點重建。</p></div>
  <div class="table-wrap"><table><thead><tr><th>項目</th><th>本案可能的混淆</th><th>需要核對</th></tr></thead><tbody>
    <tr><td>Fever</td><td>Pneumonia 本身可造成</td><td>體溫曲線與抗感染反應</td></tr>
    <tr><td>Tachycardia</td><td>Infection、thyrotoxicosis、HF 都可造成</td><td>ECG、rhythm、同時點 HR</td></tr>
    <tr><td>CHF</td><td>既有 EF 32% 不等於當下 pulmonary edema</td><td>rales、oxygen、CXR、JVP、diuretic response</td></tr>
    <tr><td>Trigger</td><td>Pneumonia 可模仿，也可觸發 storm</td><td>不要重複計入而不說明</td></tr>
    <tr><td>CNS／GI</td><td>目前缺原始分項</td><td>護理與 admission notes</td></tr>
  </tbody></table></div>
  <p class="source-note">參考：<a href="https://www.japanthyroid.jp/common/public_comment201605.pdf">JTA/JES criteria</a>、<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13506520/">2026 thyroid-storm joint consensus</a>。</p>
</section>

<section class="section" id="nodules">
  <div class="section-title"><span>03</span><div><h2>Thyroid nodules 可能改變 definitive treatment</h2><p>影像描述需要回看原圖，不能直接等同 cancer。</p></div></div>
  <div class="nodule-grid">
    <article><span>右側</span><strong>1.36 cm</strong><p>Solid、hypoechoic、microcalcification、ill-defined border。若原圖確認高風險特徵，尺寸達常見 FNA 門檻。</p></article>
    <article><span>左側</span><strong>0.80 cm</strong><p>同樣記載 solid、hypoechoic、microcalcification。通常需 suspicious lymph node、extrathyroidal extension 或關鍵位置，才考慮超越常規尺寸門檻。</p></article>
  </div>
  <div class="callout amber"><strong>文字邊界</strong><p>「Ill-defined border」不可自動改寫為「irregular margin」。目前沒有原始影像、完整 cervical lymph-node mapping、FNA 或 cytology。</p></div>
  <div class="decision-chain"><span>原圖確認</span><i>→</i><span>正式 TI-RADS／pattern</span><i>→</i><span>FNA 或 surveillance</span><i>→</i><span>影響 surgery vs I-131</span></div>
  <p class="source-note">參考：<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10448590/">ETA 2023 thyroid nodule guideline</a>。</p>
</section>

<section class="section" id="steroid">
  <div class="section-title"><span>04</span><div><h2>Hydrocortisone、ACTH 與 adrenal 判讀</h2><p>單一低 ACTH 不能診斷永久 central adrenal insufficiency。</p></div></div>
  <div class="prose-card"><p>病歷有 hydrocortisone 使用紀錄，也有 ACTH &lt;5、後續 11.8 pg/mL。外源 glucocorticoid 會抑制 ACTH；acute illness、採血時間與 assay 也會影響解讀。必須先排出末次 hydrocortisone、ACTH 與 paired cortisol 的時間。</p><p>若規劃 surgery，是否需要 perioperative stress coverage 應由 Endocrinology／Anesthesia 依實際 exposure 與後續 testing 決定。Pneumonia 與 diabetes 也使持續 glucocorticoid 的感染與 hyperglycemia 代價更重要。</p></div>
  <p class="source-note">參考：<a href="https://www.endocrine.org/clinical-practice-guidelines/glucocorticoid-induced-adrenal-insufficiency">2024 ESE–Endocrine Society guideline</a>。</p>
</section>
'''

safety_body = r'''
<section class="section" id="causality">
  <div class="section-title"><span>01</span><div><h2>Agranulocytosis 的藥物歸因</h2><p>Carbimazole 高度可疑，仍需保留 competing causes。</p></div></div>
  <div class="evidence-line"><span class="level high">強支持</span><div><h3>時序與嚴重度相符</h3><p>Day 0 開始 carbimazole，Day 43 出現症狀，Day 48 ANC 50/µL。約第六至七週落在常見早發分布。</p></div></div>
  <div class="evidence-line"><span class="level medium">尚需核對</span><div><h3>Allopurinol 與其他藥物</h3><p>實際 start／stop、adherence 與完整 medication list 未重建。感染本身也可能影響血球，但如此嚴重 ANC 與典型 ATD timing 使 carbimazole 仍居首位。</p></div></div>
  <div class="evidence-line"><span class="level low">不應進行</span><div><h3>Rechallenge 來證明因果</h3><p>嚴重 agranulocytosis 的再暴露風險不可接受；因果不確定性應靠紀錄與替代病因調查處理。</p></div></div>
</section>

<section class="section" id="cross-reaction">
  <div class="section-title"><span>02</span><div><h2>為什麼不能用「50%」決定換 PTU</h2><p>常見百分比的端點與分母並不是 agranulocytosis recurrence。</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>數字／來源</th><th>真正端點</th><th>可用結論</th></tr></thead><tbody>
    <tr><td>5/33＝15.2%<br><a href="https://pubmed.ncbi.nlm.nih.gov/2464468/">Meyer-Gessner 1989</a></td><td>Carbimazole↔PTU 換藥後的所有 adverse reactions</td><td>不是 agranulocytosis-specific，也不是方向別再發率</td></tr>
    <tr><td>14/41＝34.2%<br><a href="https://pubmed.ncbi.nlm.nih.gov/22332800/">Otsuka 2012</a></td><td>MMI→PTU 的所有 adverse reactions</td><td>不能當作嚴重血液反應機率</td></tr>
    <tr><td>9/30＝30.0%<br><a href="https://pubmed.ncbi.nlm.nih.gov/22332800/">Otsuka 2012</a></td><td>PTU→MMI 的所有 adverse reactions</td><td>仍不是 agranulocytosis rechallenge trial</td></tr>
    <tr><td>n=1<br><a href="https://pubmed.ncbi.nlm.nih.gov/3256337/">Ostlere 1988</a></td><td>Carbimazole 與 PTU 後依序發生 agranulocytosis</td><td>證明交叉再發可能，無法估計機率</td></tr>
    <tr><td>n=1<br><a href="https://pubmed.ncbi.nlm.nih.gov/6865827/">Chen 1983</a></td><td>PTU 後換 methimazole，10 週後再發</td><td>方向與本案相反，也只能證明可能性</td></tr>
  </tbody></table></div>
  <div class="callout red"><strong>臨床結論</strong><p>精確的 agranulocytosis cross-recurrence rate 未知。嚴重 class-related reaction、可能致命感染與已有 definitive alternatives，支持避免例行改用另一種 thionamide。ATA 僅在真正 life-threatening thyroid storm 留有非常窄的短期權衡空間。</p></div>
</section>

<section class="section" id="timing">
  <div class="section-title"><span>03</span><div><h2>發病時序應如何解讀</h2><p>「約 85% 在前 90 天」是病例分布，不是用藥者風險。</p></div></div>
  <div class="prose-card"><p>Nakamura 2013 共收到 754 件 severe hematologic adverse-event reports，其中 670 件 agranulocytosis、84 件 pancytopenia／aplastic anemia。發病時間分析的分母在 Results 與 figure caption 又有 461／458 的差異；摘要與正文報告 84.5%／84.6% 於前 90 天發病。</p><p>正確表述是「在有明確時序且已發病的病例中，約 85% 發生於前 90 天」。它不能變成「85% 的服藥者會發病」，也不能把第 90 天當成安全分界。重新開始療程仍可能在數週內發病，但這不等於曾經 agranulocytosis 的人可以安全 rechallenge。</p></div>
  <p class="source-note"><a href="https://pubmed.ncbi.nlm.nih.gov/24057289/">Nakamura 2013</a>、<a href="https://pubmed.ncbi.nlm.nih.gov/24341564/">Kobayashi 2014 resumed-course cases</a></p>
</section>

<section class="section" id="gcsf">
  <div class="section-title"><span>04</span><div><h2>G-CSF：本案回升快，不等於因果已證明</h2><p>試驗與觀察研究的結果並不完全一致。</p></div></div>
  <div class="two-col"><article class="prose-card"><h3>Randomized evidence</h3><p>Fukata 1999 小型 RCT（n=24）未證實 G-CSF 對中重度 ATD agranulocytosis 有明顯恢復利益；樣本小，嚴重度與 endpoints 限制解讀。</p><a href="https://pubmed.ncbi.nlm.nih.gov/10037073/">查看摘要</a></article><article class="prose-card"><h3>Observational evidence</h3><p>部分 cohort／meta-analysis 指向較快 neutrophil recovery，但 selection、嚴重度與 supportive care 不同，不能從本案 Day 48→51 的改善計算單獨效果。</p><a href="https://pubmed.ncbi.nlm.nih.gov/31824417/">查看 meta-analysis</a></article></div>
</section>

<section class="section" id="infection">
  <div class="section-title"><span>05</span><div><h2>感染恢復要另外追蹤</h2><p>ANC、症狀、CRP 與影像各有不同速度。</p></div></div>
  <div class="progress-track"><div><strong>ANC</strong><span class="done">Day 51 已恢復</span></div><div><strong>Clinical stability</strong><span class="partial">Day 55 較穩定</span></div><div><strong>Inflammation</strong><span class="partial">CRP 下降</span></div><div><strong>Imaging</strong><span class="open">Day 57 仍 near abscess</span></div></div>
  <div class="next-action"><strong>需要的結案資料</strong><span>Antibiotic end date、fever／respiratory symptoms、CRP trend、follow-up CXR／CT、是否需要 drainage、Pulmonology／Infection clearance。</span></div>
</section>

<section class="section" id="bridges">
  <div class="section-title"><span>06</span><div><h2>Non-thionamide bridge 工具箱</h2><p>先決定終點，再選擇能安全到達終點的組合。</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>方法</th><th>作用</th><th>本案限制</th></tr></thead><tbody>
    <tr><td>Lugol／KI</td><td>短期抑制 hormone release；常作術前準備</td><td>配方、總量、末劑未知；escape 與後續 RAI uptake</td></tr>
    <tr><td>Glucocorticoid</td><td>嚴重 thyrotoxicosis／storm 時減少 T4→T3 conversion</td><td>Pneumonia、diabetes、HPA-axis 判讀</td></tr>
    <tr><td>Beta-blocker</td><td>控制 adrenergic symptoms 與 heart rate</td><td>HFrEF 需區分 compensated 與 low-output／shock</td></tr>
    <tr><td>Lithium</td><td>抑制 hormone release；可用於 peri-RAI</td><td>Renal、Na、volume、ARNI／diuretics 交互作用</td></tr>
    <tr><td>Cholestyramine</td><td>減少 enterohepatic recycling</td><td>影響其他口服藥吸收；只能作 adjunct</td></tr>
    <tr><td>Plasma exchange</td><td>快速、暫時降低 circulating hormone</td><td>侵入性、證據多為小型 series；通常銜接 definitive treatment</td></tr>
  </tbody></table></div>
</section>
'''

i131_body = r'''
<section class="section" id="attribution">
  <div class="section-title"><span>01</span><div><h2>Lithium 是否有可歸因效果？</h2><p>目前答案是「indeterminate」。</p></div></div>
  <div class="key-message compact"><div><span class="status open">不能歸因</span><h3>門診 lithium 開立前，FT4 已經下降</h3></div><p>Day 48 1.61→Day 54 1.32→Day 57 1.21 ng/dL。Day 57→59 只再下降至 1.13，時間短且有多種 concurrent factors。</p></div>
  <div class="attribution-grid">
    <article><h3>Temporal precedence</h3><p>大部分下降發生在門診 lithium 以前。除非 MAR 證明住院已給藥，不能把前段曲線算入 lithium effect。</p></article>
    <article><h3>Concurrent interventions</h3><p>Lugol、hydrocortisone、beta-blocker、infection recovery 與自然病程同時變化。</p></article>
    <article><h3>Concentration validity</h3><p>Day 59 &lt;0.2 缺少 dose count 與 blood-draw timing；單一數值無法判定 exposure。</p></article>
    <article><h3>Clinical response</h3><p>還需 FT3、HR、rhythm、HF symptoms、temperature 與 mental status。</p></article>
  </div>
  <details><summary>建立可歸因時間線需要哪些欄位？</summary><div class="details-body"><ol><li>每一劑 lithium 的日期、時間、劑型與 adherence。</li><li>每次 level 距前一劑多久，是否已連續使用數日。</li><li>同時點 Cr／eGFR、Na、K、體重、輸入輸出、congestion／dehydration。</li><li>FT4／FT3 與臨床指標；早期不使用仍受抑制的 TSH 當主要反應指標。</li><li>Lugol、glucocorticoid、beta-blocker、cholestyramine、antibiotics 的精確時序。</li></ol></div></details>
</section>

<section class="section" id="monitoring">
  <div class="section-title"><span>02</span><div><h2>Lithium safety 的最低資料集</h2><p>低 dose 或單次低 level 都不足以保證安全。</p></div></div>
  <div class="safety-panel">
    <div><h3>開始／延續前</h3><ul><li>Cr／eGFR、Na、K、Ca</li><li>體重、volume、BP、orthostasis</li><li>Pregnancy status（若適用）</li><li>HF drugs、NSAIDs、antibiotics、diuretics</li></ul></div>
    <div><h3>使用中</h3><ul><li>可解讀的 serum level timing</li><li>Renal／electrolyte trend</li><li>Thirst、polyuria、nausea、diarrhea</li><li>Tremor、ataxia、confusion、slurred speech</li></ul></div>
    <div><h3>本案交互作用</h3><ul><li>Sacubitril/valsartan：可能增加 lithium concentration</li><li>Spironolactone／other diuretics：降低 renal clearance</li><li>Volume depletion、fever、diarrhea：提高 retention／toxicity risk</li><li>NSAIDs：降低 renal lithium clearance</li></ul></div>
  </div>
  <p class="source-note"><a href="https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=803eab29-0d0a-4df0-b504-bcd85ec01ead">Lithium official label</a>、<a href="https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=14bf8041-0b7f-9acb-e063-6294a90a8256">Entresto 7.4</a>、<a href="https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c23b6b9b-aec3-48a8-a518-76e4097f6479">Spironolactone 7.2</a></p>
</section>

<section class="section" id="washout">
  <div class="section-title"><span>03</span><div><h2>停 iodide：三種時間不能混用</h2><p>Guideline 給的是起點，個案 readiness 仍需量測。</p></div></div>
  <div class="washout-scale">
    <article><span>2–3 週</span><h3>Lugol／SSKI</h3><p>EANM 2023 Table 1 的一般 withdrawal interval，依 iodide content 而定。</p></article>
    <article><span>6–8 週</span><h3>Water-soluble IV contrast</h3><p>EANM 的一般框架，明列 assuming normal renal function。</p></article>
    <article><span>至少 2–3 個月</span><h3>大量 iodide／storm treatment</h3><p>2026 multi-society thyroid-storm consensus 採用的較保守框架。</p></article>
  </div>
  <div class="callout amber"><strong>本案做法</strong><p>先確認 Lugol 配方、實際末劑、iohexol 日期與 renal course，再用 RAIU，必要時 urinary iodine，證明 uptake 已恢復。RAIU test 與 I-131 therapy 應在相同 preparation／medication condition 下進行。</p></div>
  <p class="source-note"><a href="https://link.springer.com/article/10.1007/s00259-023-06274-5">EANM 2023</a>、<a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13506520/">2026 joint consensus</a></p>
</section>

<section class="section" id="pathway">
  <div class="section-title"><span>04</span><div><h2>Lithium 支持到 I-131：五階段路徑</h2><p>「Lithium alone」僅指 thyroid-directed bridge；其他器官問題仍需平行治療。</p></div></div>
  <ol class="stage-list">
    <li><span>01</span><div><h3>確認 I-131 適合</h3><p>重建 etiology；評估 eye disease、goiter、pregnancy、radiation precautions、follow-up capacity。先釐清 suspicious nodule 是否需 FNA／cancer work-up。</p><a href="./diagnosis.html#nodules">查看 nodule 判讀</a></div></li>
    <li><span>02</span><div><h3>清除 iodine interference</h3><p>記錄 Lugol 與 contrast，停止不必要的新 iodine exposure；以 RAIU／urinary iodine、renal function 與末劑決定時機。</p></div></li>
    <li><span>03</span><div><h3>建立 lithium safety rails</h3><p>Endocrinology、Cardiology、Pharmacy 共同定義 labs、採血時點、臨床監測與 urgent reassessment thresholds。</p></div></li>
    <li><span>04</span><div><h3>完成 RAIU 與 I-131</h3><p>Nuclear Medicine 決定 activity 與 peri-RAI protocol。研究 dose／serum range 不直接轉成本案處方。</p></div></li>
    <li><span>05</span><div><h3>追蹤 delayed effect</h3><p>I-131 不會立即停止 hormone release。追蹤 FT4／FT3、rhythm、HF、renal、Na、volume 與 lithium toxicity，直到 clinical trajectory 穩定。</p></div></li>
  </ol>
  <div class="callout red"><strong>需要重新評估或改道</strong><p>FT4／FT3 明顯上升、new arrhythmia、worsening congestion／low-output signs、infection relapse、renal／Na 變化、neurologic／GI toxicity，或無法可靠服藥與回診。</p></div>
</section>

<section class="section" id="evidence">
  <div class="section-title"><span>05</span><div><h2>Lithium＋RAI 的研究支持到哪裡</h2><p>有生物學與群體證據，但本案複雜度不同。</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>研究</th><th>設計／結果</th><th>外推限制</th></tr></thead><tbody>
    <tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12364424/">Bogazzi 2002</a></td><td>Randomized n=36；lithium 減少 MMI withdrawal 後 hormone rebound、增加 thyroidal radiation retention；cure rate 差異未顯著</td><td>已用 MMI 控制數月；樣本小，非 agranulocytosis／infection／HFrEF cohort</td></tr>
    <tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/19906789/">Bogazzi 2010</a></td><td>Retrospective n=651；cure 91% vs 85%，median time 60 vs 90 days</td><td>非隨機；newly diagnosed Graves，器官風險較少</td></tr>
    <tr><td><a href="https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1770772/full">Gao 2026</a></td><td>Retrospective n=146；六個月 treatment failure 15.2% vs 10.0%，P=0.345</td><td>未證明降低 rare thyroid storm；protocol target 不是本案處方</td></tr>
    <tr><td><a href="https://academic.oup.com/jes/article/5/Supplement_1/A958/6241039">Fantin 2021</a></td><td>Conference abstract；MMI agranulocytosis，lithium→I-131</td><td>單例、摘要、追蹤一個月</td></tr>
    <tr><td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11454931/">Sazon 2024</a></td><td>Conference abstract；carbimazole、ANC 0，lithium＋prednisone→I-131</td><td>缺完整心肺腎細節與長期追蹤</td></tr>
  </tbody></table></div>
</section>

<section class="section" id="comparison">
  <div class="section-title"><span>06</span><div><h2>Surgery 與 I-131：直接比較</h2><p>兩條路都可能，需加入 patient preference。</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>面向</th><th>Thyroidectomy</th><th>I-131</th></tr></thead><tbody>
    <tr><td>控制速度</td><td>手術完成後快速移除 hormone source</td><td>效果延遲，等待與治療後仍可能波動</td></tr>
    <tr><td>Iodine exposure</td><td>KI 可作短期術前準備</td><td>Lugol／contrast 抑制 uptake，需 washout／RAIU</td></tr>
    <tr><td>Nodules</td><td>可同時取得 pathology</td><td>疑似 cancer 需先完成評估</td></tr>
    <tr><td>HFrEF／infection</td><td>增加 anesthesia／perioperative risk</td><td>避免 anesthesia，但延長 bridge 與 thyrotoxicosis exposure</td></tr>
    <tr><td>Long-term</td><td>Total thyroidectomy 後 lifelong levothyroxine</td><td>Ablative approach 也常以 hypothyroidism 為目標／結果；可能需 repeat treatment</td></tr>
  </tbody></table></div>
  <div class="preference-box"><h3>必須問病人的六件事</h3><ol><li>最重視快速控制，還是避免 surgery／anesthesia？</li><li>能否承受停碘等待、密集抽血與回診？</li><li>是否希望一次取得 nodule pathology？</li><li>是否接受 lifelong levothyroxine？</li><li>能否遵守 radiation precautions？</li><li>是否接受 I-131 可能延遲、失敗或需要 repeat treatment？</li></ol></div>
</section>
'''

cardiac_body = r'''
<section class="section" id="reassessment">
  <div class="section-title"><span>01</span><div><h2>EF 32% 不是完整診斷</h2><p>先重建病因與目前狀態，再談 surgery 或等待 I-131。</p></div></div>
  <div class="key-message compact"><div><span class="status inferred">工作診斷</span><h3>可能含 thyrotoxic 或 tachycardia-mediated cardiomyopathy</h3></div><p>Hyperthyroidism＋低 EF 不能自動確立 thyrotoxic cardiomyopathy。要排除 ischemic、hypertensive、valvular、myocarditis、diabetic 與其他原因，並觀察 thyroid control 後是否恢復。</p></div>
  <div class="workup-grid">
    <article><span>原始 echo</span><ul><li>日期與當時 thyroid／infection state</li><li>LV size、global vs regional motion</li><li>RV function、valves、pulmonary pressure</li><li>Diastolic function</li></ul></article>
    <article><span>Rhythm／etiology</span><ul><li>AF 或其他 tachyarrhythmia burden</li><li>ECG／ambulatory monitor</li><li>是否依一般適應症評估 ischemia</li><li>BP history、myocarditis clues</li></ul></article>
    <article><span>目前 clinical state</span><ul><li>NYHA、orthopnea、exercise tolerance</li><li>BP、orthostasis、weight、edema、JVP</li><li>Renal、Na、K；BNP／troponin 若會改變決策</li><li>GDMT 與 adherence</li></ul></article>
    <article><span>Repeat assessment</span><ul><li>Thyroid 與 infection 較穩定後 repeat echo</li><li>若 clinical status 改變則提前</li><li>確認 compensated 或 decompensated</li><li>記錄 EF trajectory，不只單點</li></ul></article>
  </div>
</section>

<section class="section" id="recovery">
  <div class="section-title"><span>02</span><div><h2>心功能可能恢復，但不能承諾</h2><p>目前最相關的 cohort 有明顯 incomplete follow-up。</p></div></div>
  <div class="number-story"><div><strong>50</strong><span>thyrotoxic cardiomyopathy</span></div><i>→</i><div><strong>32</strong><span>完整 follow-up echo</span></div><i>→</i><div><strong>22</strong><span>恢復 LV systolic function</span></div><i>→</i><div><strong>69%</strong><span>平均追蹤 18 個月</span></div></div>
  <p>這個結果支持 recovery 的可能性，也顯示並非所有人恢復。只有 64% 的 cardiomyopathy subgroup 有完整 echo follow-up，存在 selection bias；不能直接把 69% 當成本案預後。</p>
  <p class="source-note"><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8318454/">Clinical phenotypes and prognosis of thyrotoxic heart failure</a></p>
</section>

<section class="section" id="risk">
  <div class="section-title"><span>03</span><div><h2>結果如何改變兩條路的風險</h2><p>比較當下可控制的風險，而不是只用 EF 一個數字。</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>狀態</th><th>Surgery</th><th>I-131／等待</th></tr></thead><tbody>
    <tr><td><strong>EF 明顯恢復、compensated、感染控制</strong></td><td>Perioperative risk 可能下降，仍需 formal assessment</td><td>等待期 reserve 較佳，仍需 bridge 與 post-RAI monitoring</td></tr>
    <tr><td><strong>EF 約 32%、compensated</strong></td><td>Cardiology、Anesthesia、high-volume thyroid surgeon 共同設計 hemodynamic plan</td><td>避免立即 anesthesia，但承擔較長 thyrotoxicosis、lithium／renal-volume 變化與 delayed effect</td></tr>
    <tr><td><strong>Active／decompensated HF</strong></td><td>通常先暫停 elective surgery並 stabilization</td><td>也不是立即安全出口；若 thyroid excess 驅動 HF，延長等待可能有害</td></tr>
    <tr><td><strong>Uncontrolled arrhythmia／possible ischemia／significant valve disease</strong></td><td>依一般適應症完成會改變管理的評估</td><td>同樣影響 beta-blocker、volume、lithium 與等待安全</td></tr>
  </tbody></table></div>
  <p class="source-note"><a href="https://www.ahajournals.org/doi/full/10.1161/CIR.0000000000001285">2024 AHA/ACC perioperative cardiovascular guideline</a></p>
</section>

<section class="section" id="surgery">
  <div class="section-title"><span>04</span><div><h2>若考慮 thyroidectomy</h2><p>手術風險要以目前狀態重新估計。</p></div></div>
  <div class="check-grid">
    <article><h3>Cardiology</h3><p>Compensation、functional capacity、rhythm、GDMT、需要的 testing。</p></article>
    <article><h3>Anesthesia</h3><p>Hemodynamic plan、airway、volume shifts、術後 monitoring level。</p></article>
    <article><h3>Infection／Pulmonary</h3><p>Necrotizing lesion、antibiotic course、oxygen／respiratory reserve。</p></article>
    <article><h3>Endocrinology／Surgery</h3><p>Hormone control、bridge、high-volume thyroid surgeon、nodule plan。</p></article>
  </div>
  <div class="callout teal"><strong>文獻定位</strong><p>Voci 2026 已報告 agranulocytosis、decompensated HF／EF 35% 經 hemodynamic assessment 後 thyroidectomy。它證明這條路徑曾被實作，不能保證本案安全，也表示此組合不是首次報告。</p><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13133480/">查看 case report</a></div>
</section>

<section class="section" id="waiting">
  <div class="section-title"><span>05</span><div><h2>若等待 I-131</h2><p>避免 anesthesia 不等於沒有 cardiovascular risk。</p></div></div>
  <ul class="risk-list"><li><strong>Thyrotoxicosis exposure：</strong>I-131 起效延遲，停 iodide 與 treatment 後都可能有 hormone fluctuation。</li><li><strong>Lithium exposure：</strong>ARNI、spironolactone／diuretics、renal 與 volume 變化會改變 toxicity risk。</li><li><strong>Arrhythmia：</strong>需持續 ECG／symptom awareness；beta-blockade 依 compensated vs low-output 狀態調整。</li><li><strong>Rescue plan：</strong>若 HF、hormone 或 infection 惡化，要預先知道 admission、其他 adjunct 或 accelerated surgery 的門檻。</li></ul>
</section>
'''

evidence_body = r'''
<section class="section" id="hierarchy">
  <div class="section-title"><span>01</span><div><h2>先看證據層級</h2><p>不同設計能回答不同問題。</p></div></div>
  <div class="hierarchy"><article><span>Guideline／consensus</span><p>提供準備、適應症與安全框架；仍需依個案調整。</p></article><article><span>Randomized／cohort</span><p>提供群體平均效果；納入條件常排除高風險複雜病例。</p></article><article><span>Case series／report</span><p>證明某路徑曾做過；無法估計成功率或因果。</p></article><article><span>本案推論</span><p>把外部證據套回病例；必須明確標記不確定性。</p></article></div>
</section>

<section class="section" id="comparators">
  <div class="section-title"><span>02</span><div><h2>最相關的已發表病例與系列</h2><p>每一篇只採用它真正能支持的訊息。</p></div></div>
  <div class="study-list">
    <article><div><h3>Knight et al. 2017</h3><span>完整 case report</span></div><p>Agranulocytosis＋sepsis；Lugol、lithium、cholestyramine、propranolol，約 9 天後 thyroidectomy。未完全 biochemical euthyroid 仍手術。</p><aside><b>可用：</b>感染期經充分評估後手術曾成功。<br><b>限制：</b>不能套用到不同 EF、pneumonia 或 nodules。</aside><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5592706/">全文</a></article>
    <article><div><h3>Voci et al. 2026</h3><span>完整 case report</span></div><p>MMI、PTU 後 agranulocytosis；decompensated HF、EF 35%；Lugol、G-CSF 與 hemodynamic assessment 後 surgery。</p><aside><b>可用：</b>低 EF 並非絕對排除手術。<br><b>限制：</b>「agranulocytosis＋HFrEF＋surgery」已有前例。</aside><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13133480/">全文</a></article>
    <article><div><h3>Calissendorff et al. 2017</h3><span>Retrospective series n=27</span></div><p>9 人因 agranulocytosis 使用 Lugol；整體 26 surgery、1 I-131。</p><aside><b>可用：</b>Lugol rescue 的群體經驗。<br><b>限制：</b>無法證明 I-131 那位屬於 agranulocytosis subgroup；Lugol 使用 3 天不是 washout 3 天。</aside><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5434745/">全文</a></article>
    <article><div><h3>Rami et al. 2024</h3><span>Case series n=3</span></div><p>其中一例 MMI agranulocytosis＋septic shock，TPE 後 thyroidectomy。</p><aside><b>可用：</b>Plasma exchange 作 rescue bridge 有先例。<br><b>限制：</b>同篇其他病例的 HF 不能套到 agranulocytosis case。</aside><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10981326/">全文</a></article>
    <article><div><h3>Fantin et al. 2021</h3><span>Conference abstract</span></div><p>MMI agranulocytosis、ANC 90/µL；lithium 跨越 I-131，短期 euthyroid。</p><aside><b>可用：</b>Lithium→I-131 路徑已有報告。<br><b>限制：</b>摘要、單例、追蹤短。</aside><a href="https://academic.oup.com/jes/article/5/Supplement_1/A958/6241039">摘要</a></article>
    <article><div><h3>Sazon et al. 2024</h3><span>Conference abstract</span></div><p>Carbimazole 後 ANC 0；lithium＋prednisone 後 I-131。</p><aside><b>可用：</b>與本案用藥路徑直接相關。<br><b>限制：</b>缺完整方法、器官狀態與長期 outcome。</aside><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11454931/">摘要</a></article>
    <article><div><h3>Tamura et al. 2024</h3><span>Cohort n=185</span></div><p>KI pretreatment subgroup n=76，兩院停 KI 14／18 天後 I-131。</p><aside><b>可用：</b>KI 不會永久排除 I-131。<br><b>限制：</b>不是 agranulocytosis subgroup outcome，也不是本案 washout shortcut。</aside><a href="https://pubmed.ncbi.nlm.nih.gov/38008728/">摘要</a></article>
  </div>
</section>

<section class="section" id="population">
  <div class="section-title"><span>03</span><div><h2>重要 cohort 與其邊界</h2><p>數字越完整，越要檢查納入條件。</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>研究</th><th>分母／結果</th><th>本案不能直接套用的理由</th></tr></thead><tbody>
    <tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/12364424/">Bogazzi 2002</a></td><td>Randomized n=36；lithium 減少 rebound</td><td>先前以 MMI 控制數月；無本案器官限制</td></tr>
    <tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/19906789/">Bogazzi 2010</a></td><td>n=651；RAI＋lithium cure 91% vs 85%</td><td>Retrospective；newly diagnosed Graves</td></tr>
    <tr><td><a href="https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1770772/full">Gao 2026</a></td><td>n=146；failure difference not significant</td><td>不足以證明 rare-event protection</td></tr>
    <tr><td><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8318454/">Kositanurit 2021</a></td><td>32 complete follow-up；22 recovered LV function</td><td>Incomplete follow-up；mean 18 months，不代表立即恢復</td></tr>
    <tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/16922465/">Vijayakumar 2006</a></td><td>122 RAI visits，0 thyroid storm</td><td>研究排除 complicating intercurrent disease；本案有 HF、pneumonia、renal fluctuation</td></tr>
    <tr><td><a href="https://pubmed.ncbi.nlm.nih.gov/24057289/">Nakamura 2013</a></td><td>約 85% 已發病病例於 90 天內</td><td>病例時間分布，不是服藥者 absolute risk</td></tr>
  </tbody></table></div>
</section>

<section class="section" id="do-not-claim">
  <div class="section-title"><span>04</span><div><h2>目前不能主張的事情</h2><p>這些句子在投稿與會議中都應避免。</p></div></div>
  <div class="claim-grid"><article><strong>「第一例」</strong><p>已有 agranulocytosis＋HFrEF＋surgery，以及 lithium→I-131 前例。</p></article><article><strong>「Lithium 造成 FT4 下降」</strong><p>大部分下降早於門診 lithium，且有多重 concurrent treatment。</p></article><article><strong>「PTU cross-reaction 是 50%」</strong><p>缺 agranulocytosis-specific 分母。</p></article><article><strong>「Contrast 導致 AKI」</strong><p>抽血與注射時間未對齊。</p></article><article><strong>「ANC 恢復等於感染清除」</strong><p>Day 57 仍有 necrotizing lesion。</p></article><article><strong>「I-131 一定較安全」</strong><p>等待、delayed effect 與 bridge toxicity 仍會影響 HFrEF。</p></article></div>
</section>
'''

experts_body = r'''
<section class="key-message" id="orientation">
  <div><span class="status inferred">跨專科判讀</span><h2>每位專家看到的是不同風險；最後決策要把這些風險放在同一張圖上</h2></div>
  <p>本頁保留各角色的原始關切，不把差異壓成單一答案。共識是停止 carbimazole、避免自行改用 PTU，並在 infection、cardiac status、iodine uptake、nodules、renal safety 與 patient preference 都更清楚後，選擇可安全完成的 definitive treatment。</p>
</section>

<section class="section" id="roles">
  <div class="section-title"><span>01</span><div><h2>九個專業角色的核心立場</h2><p>先看每個角色要保護什麼、目前最在意什麼，以及哪個新資料會改變意見。</p></div></div>
  <div class="expert-grid">
    <article class="expert-card"><span class="expert-tag">Case diagnosis</span><h3>先確認診斷強度</h3><p>Graves 仍是 working diagnosis，但 TRAb 位於 assay 灰區；thyroid storm 曾被臨床懷疑並治療，不能只靠無法重建的 BWPS 35→50 寫成確診。</p><dl><dt>最需要</dt><dd>TRAb assay、同時點 BWPS 分項、原始 ultrasound／Doppler、適當時機的 scintigraphy／RAIU。</dd><dt>會改變決策</dt><dd>結節是否 functional、是否有 suspicious lymph node，以及 storm 是否仍在進行。</dd></dl><a href="./diagnosis.html">查看完整診斷分析 →</a></article>
    <article class="expert-card"><span class="expert-tag">Endocrinology</span><h3>控制 hormone，同時走向根本治療</h3><p>ATD 已因 severe agranulocytosis 失去安全性。Bridge 的目的不是無限期維持，而是讓病人安全抵達 thyroidectomy 或 I-131。</p><dl><dt>最需要</dt><dd>同步 FT4／FT3 trend、實際 bridge administration、clinical stability。</dd><dt>會改變決策</dt><dd>Hormone rebound、持續 storm physiology，或出現無法容忍的 bridge toxicity。</dd></dl><a href="./i131.html">查看 definitive therapy 路徑 →</a></article>
    <article class="expert-card"><span class="expert-tag">Hematology</span><h3>嚴重程度已確立，單一藥物歸因尚未完成</h3><p>ANC 50/µL 符合 severe agranulocytosis。Carbimazole 的時序最吻合，但 allopurinol 實際 exposure 未知，因此不宜寫成唯一原因。</p><dl><dt>最需要</dt><dd>完整 medication administration、allopurinol 起訖、其他 marrow-toxic drugs、CBC trajectory。</dd><dt>會改變決策</dt><dd>若存在另一個可疑藥物，未來避免清單與因果表述都要調整。</dd></dl><a href="./safety.html#causality">查看 causality →</a></article>
    <article class="expert-card"><span class="expert-tag">Drug safety</span><h3>不以一個 lithium level 或百分比作結論</h3><p>門診 lithium 處方前 FT4 已下降；Day 59 level &lt;0.2 若缺服藥紀錄與採血距前劑時間，不能判定無效、劑量不足或安全。</p><dl><dt>最需要</dt><dd>MAR／adherence、採血 timing、Cr／eGFR、Na、volume status、ARNI／diuretic／spironolactone 使用。</dd><dt>會改變決策</dt><dd>Renal decline、dehydration、Na 改變或相互作用會快速提高 lithium toxicity risk。</dd></dl><a href="./i131.html#monitoring">查看 lithium 安全監測 →</a></article>
    <article class="expert-card"><span class="expert-tag">Infection</span><h3>ANC 恢復不等於 pneumonia 清除</h3><p>Day 51 ANC 已恢復，Day 54 CRP 明顯下降；但 Day 57 仍記載 necrotizing pneumonia 緩慢改善、接近 abscess。</p><dl><dt>最需要</dt><dd>症狀、oxygen need、antibiotic end date、culture、follow-up imaging 與感染科結論。</dd><dt>會改變決策</dt><dd>未控制 infection 會提高 surgery risk，也會增加等待與 bridge 期間 decompensation 風險。</dd></dl><a href="./safety.html#infection">查看 infection endpoints →</a></article>
    <article class="expert-card"><span class="expert-tag">Nuclear medicine</span><h3>I-131 readiness 要用 uptake 證明</h3><p>Iohexol 與 Lugol 都可能壓低 thyroid uptake。只算「停幾週」不足以確認治療會吸收足夠 activity。</p><dl><dt>最需要</dt><dd>最後 iodide 劑量、配方、urinary iodine、RAIU、renal clearance 與 nodule function。</dd><dt>會改變決策</dt><dd>低 uptake 可能讓 I-131 延後或失敗；可接受 uptake 才支持進入治療。</dd></dl><a href="./i131.html#washout">查看停碘判斷 →</a></article>
    <article class="expert-card"><span class="expert-tag">Thyroid surgery／Anesthesia</span><h3>手術能快速控制來源，但 readiness 不是只有 FT4</h3><p>Thyroidectomy 可快速移除 hormone source，並取得 nodule pathology；代價是 active infection、HFrEF 與 anesthesia 的即時風險。</p><dl><dt>最需要</dt><dd>肺部感染控制、repeat echo、rhythm／volume、airway、原始 nodule imaging、high-volume surgeon 評估。</dd><dt>會改變決策</dt><dd>若 surgery risk 已可控制，而 RAI uptake／等待仍不利，手術優勢增加。</dd></dl><a href="./i131.html#comparison">查看 surgery／I-131 比較 →</a></article>
    <article class="expert-card"><span class="expert-tag">Cardiology</span><h3>EF 32% 需要重新測量與重建病因</h3><p>既往 low EF 可能與 thyrotoxicosis 有關，也可能有 ischemic、arrhythmic、valvular 或其他原因。Thyroid function 改善後是否恢復尚未知。</p><dl><dt>最需要</dt><dd>Repeat echo、ECG／rhythm、volume、functional status、ischemic／valvular workup 與 GDMT tolerance。</dd><dt>會改變決策</dt><dd>Decompensation 會使近期 surgery 危險；持續不穩也會使等待 I-131 與 hormone rebound 危險。</dd></dl><a href="./cardiac.html">查看 HFrEF 風險重評 →</a></article>
    <article class="expert-card"><span class="expert-tag">Evidence／Publication</span><h3>把可行性、效果與本案因果分開</h3><p>Case report 只能證明某路徑曾成功；cohort 的平均結果不一定適用於同時有 pneumonia、HFrEF 與 renal fluctuation 的病人。</p><dl><dt>最需要</dt><dd>Definitive treatment、short／long-term outcome、patient perspective、publication consent。</dd><dt>會改變決策</dt><dd>沒有 outcome 時宜寫 case-based teaching analysis，不宜宣稱 successful case 或「第一例」。</dd></dl><a href="./publication.html">查看投稿與 CARE 缺口 →</a></article>
  </div>
</section>

<section class="section" id="consensus">
  <div class="section-title"><span>02</span><div><h2>目前跨角色共識</h2><p>這些是不同專業從各自角度都能支持的底線。</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>共識</th><th>各角色的理由</th><th>對本案的實際含義</th></tr></thead><tbody>
    <tr><td>Carbimazole 應視為高度可疑並避免再暴露</td><td>時間關係與已知 adverse effect 都吻合；但缺 allopurinol exposure，不能寫成唯一原因。</td><td>過敏／嚴重不良反應紀錄要清楚，同時完成其他藥物因果盤點。</td></tr>
    <tr><td>不要常規改用 PTU</td><td>同類藥後再暴露有嚴重安全疑慮；文獻中的 15.2%、34%、50% 並非 agranulocytosis-specific recurrence rate。</td><td>若任何團隊提出 PTU，必須說明極端理由、替代方案與 risk discussion。</td></tr>
    <tr><td>ANC、CRP、影像是不同終點</td><td>Blood-count recovery 快，不代表 necrotizing pneumonia 已解除。</td><td>Surgery readiness 不能只看 ANC；等待 I-131 也要納入 infection trajectory。</td></tr>
    <tr><td>Lithium 效果尚不可歸因</td><td>FT4 下降早於可確認的門診 lithium exposure，且同時有 iodide、steroid 與其他處置。</td><td>先重建實際給藥與 level timing，再談效果或調整。</td></tr>
    <tr><td>Surgery 與 I-131 都是條件式選項</td><td>手術有立即 perioperative risk；I-131 有 uptake、延遲作用與等待期風險。</td><td>選擇應比較「可以控制的整體風險」，而非只比較 procedure 名稱。</td></tr>
    <tr><td>病人偏好是決策資料</td><td>等待、radiation precautions、手術、scar、終身 replacement 與 follow-up 的負擔不同。</td><td>需要記錄病人的理由、理解與可行性；不能由醫師偏好替代。</td></tr>
    <tr><td>不能聲稱 contrast 造成 renal injury</td><td>Day 48 有兩個 Cr，但採血與注射先後未對齊。</td><td>用「temporal relationship unresolved」描述，並追蹤最新 renal status。</td></tr>
  </tbody></table></div>
</section>

<section class="section" id="debates">
  <div class="section-title"><span>03</span><div><h2>仍有分歧的問題</h2><p>分歧不是錯誤；關鍵是知道要補哪個資料才能收斂。</p></div></div>
  <div class="debate-grid">
    <article><span>Washout</span><h3>停 iodide 2–3 週，還是至少 2–3 個月？</h3><p>EANM 的一般 preparation 與 thyroid-storm consensus 的保守建議適用情境不同。本案同時有 contrast、Lugol 與 renal fluctuation，不宜選一個日曆數字套用。</p><strong>收斂方法：</strong><p>確認末劑與配方，搭配 urinary iodine、RAIU 與 renal recovery。</p></article>
    <article><span>G-CSF</span><h3>快速 ANC recovery 是否支持 G-CSF 有效？</h3><p>小型 randomized trial 未顯示明確 benefit；observational studies／meta-analysis 常見 recovery 加快，但有 indication bias 與 concurrent treatment。</p><strong>收斂方法：</strong><p>只能描述本案接受 G-CSF 後恢復，不能做單病例因果歸因。</p></article>
    <article><span>Timing</span><h3>先等 infection／EF，還是儘快 surgery？</h3><p>沒有單一 EF 或影像門檻能替所有專科決定。過早手術有 perioperative risk；拖延也有 hormone rebound、bridge toxicity 與 HF worsening。</p><strong>收斂方法：</strong><p>用動態 MDT readiness review，逐項說明什麼已改善、什麼仍不可接受。</p></article>
    <article><span>Etiology</span><h3>是否可直接稱為 Graves disease？</h3><p>TRAb 3.00 高於一般 reference，但低於同 assay 的 Graves-specific cutoff 3.10；nodules 與 iodine exposure 又限制近期 functional imaging。</p><strong>收斂方法：</strong><p>保留 working diagnosis，用 assay、影像與適時 scintigraphy 提高確定度。</p></article>
    <article><span>Nodules</span><h3>右 1.36 cm／左 0.8 cm 是否改變治療？</h3><p>文字描述可條件式算到高風險，但原圖、margin 解讀與 lymph-node mapping 不完整；不能把重建分數當正式報告。</p><strong>收斂方法：</strong><p>專家重看原圖、正式 risk classification、FNA indication 與功能定位。</p></article>
    <article><span>Novelty</span><h3>病例是否具有可發表的新意？</h3><p>相似的 agranulocytosis＋HF＋surgery，以及 lithium→I-131 都已有案例。可能的新意在多重限制如何被依序解除。</p><strong>收斂方法：</strong><p>補 treatment outcome、patient perspective 與 consent；避免「第一例」。</p></article>
  </div>
</section>

<section class="section" id="challenges">
  <div class="section-title"><span>04</span><div><h2>專家之間如何互相質疑</h2><p>這些交叉問題用來防止單一專科只看到自己的主要終點。</p></div></div>
  <ol class="challenge-list">
    <li><span>Drug Safety → Diagnosis</span><div><h3>BWPS 的高分有多少來自 infection 與既有 HF？</h3><p>要求用同一時點重建 temperature、HR、CNS、GI、CHF 與 precipitant，不以總分取代臨床證據。</p></div></li>
    <li><span>Infection → Surgery</span><div><h3>「CRP 下降」足以代表 anesthesia risk 已可接受嗎？</h3><p>要求症狀、oxygen、follow-up imaging、抗生素療程與 source-control 評估。</p></div></li>
    <li><span>Cardiology → Nuclear Medicine</span><div><h3>等待 uptake 恢復期間，心臟能否承受 hormone rebound？</h3><p>要求量化等待時間、monitoring frequency、rescue threshold 與 decompensation plan。</p></div></li>
    <li><span>Nuclear Medicine → Drug Safety</span><div><h3>Lithium 是否真的已給、level 是否可解讀？</h3><p>要求 medication administration、前劑時間、renal／Na／volume 與 interacting drugs 同步呈現。</p></div></li>
    <li><span>Surgery → Diagnosis</span><div><h3>Nodules 是否提供選擇 thyroidectomy 的額外理由？</h3><p>要求原始 ultrasound、lymph-node mapping、FNA／cytology，而不是只依文字摘要判 cancer risk。</p></div></li>
    <li><span>Evidence reviewer → 全體</span><div><h3>這個數字的分母是誰？這篇研究排除了誰？</h3><p>要求把 guideline、trial／cohort、case report 與本案推論分層，並說明外推限制。</p></div></li>
    <li><span>Publication reviewer → 全體</span><div><h3>病人最後怎麼選、結果如何？</h3><p>沒有 definitive treatment、outcome、patient perspective 與 consent，就不宜把分析包裝成完整成功病例。</p></div></li>
  </ol>
</section>

<section class="section" id="mdt">
  <div class="section-title"><span>05</span><div><h2>MDT 決策責任表</h2><p>每個問題有主責角色，但資料要能被其他角色檢驗。</p></div></div>
  <div class="table-wrap"><table><thead><tr><th>決策</th><th>主責</th><th>共同參與</th><th>會前最低資料</th></tr></thead><tbody>
    <tr><td>感染是否已達 procedure readiness</td><td>Infection／Pulmonology</td><td>Anesthesia、Surgery、Cardiology</td><td>症狀、oxygen、imaging、antibiotics、culture</td></tr>
    <tr><td>HFrEF 是否 compensated</td><td>Cardiology</td><td>Anesthesia、Endocrinology</td><td>Repeat echo、rhythm、volume、functional status</td></tr>
    <tr><td>I-131 是否有足夠 uptake</td><td>Nuclear Medicine</td><td>Endocrinology、Nephrology／Pharmacy</td><td>Iodide／contrast 時序、RAIU、urinary iodine、renal status</td></tr>
    <tr><td>Lithium 能否安全續用</td><td>Endocrinology／Clinical Pharmacy</td><td>Cardiology、Nephrology</td><td>MAR、level timing、Cr／eGFR、Na、volume、interactions</td></tr>
    <tr><td>Nodules 是否需 FNA／影響路徑</td><td>Thyroid imaging／Endocrinology</td><td>Surgery、Nuclear Medicine</td><td>原圖、正式 risk score、LN mapping、functional status</td></tr>
    <tr><td>選 surgery 或 I-131</td><td>Patient＋MDT</td><td>所有相關專科</td><td>兩路的可行時間、風險、替代方案、病人目標與限制</td></tr>
  </tbody></table></div>
</section>

<section class="section" id="open-items">
  <div class="section-title"><span>06</span><div><h2>尚未解決的高優先問題</h2><p>若只補少量資料，先補最可能改變治療的項目。</p></div></div>
  <div class="issue-list">
    <article><span>01</span><div><h3>Definitive outcome</h3><p>Day 64 後是否接受 surgery／I-131？結果與 complications？</p></div></article>
    <article><span>02</span><div><h3>感染狀態</h3><p>Necrotizing pneumonia 是否已臨床與影像改善到可接受程度？</p></div></article>
    <article><span>03</span><div><h3>Repeat cardiac assessment</h3><p>EF、rhythm、volume 與 functional status 是否改善？</p></div></article>
    <article><span>04</span><div><h3>Iodine／uptake</h3><p>Lugol 配方與末劑、urinary iodine、RAIU 是多少？</p></div></article>
    <article><span>05</span><div><h3>Lithium exposure</h3><p>住院是否實際給藥？Day 59 採血距前劑多久？最新 renal／Na／volume？</p></div></article>
    <article><span>06</span><div><h3>Nodule workup</h3><p>原始 ultrasound、LN mapping、FNA／cytology 與 functional localization？</p></div></article>
    <article><span>07</span><div><h3>Allopurinol exposure</h3><p>實際開始、停止、adherence 與其他 marrow-toxic agents？</p></div></article>
    <article><span>08</span><div><h3>Patient preference</h3><p>病人如何權衡等待、radiation、surgery 與 lifelong replacement？</p></div></article>
  </div>
</section>
'''

publication_body = r'''
<section class="section" id="status">
  <div class="section-title"><span>01</span><div><h2>目前適合的發表形式</h2><p>已有教學價值，尚未具備完整 successful case report 的 outcome。</p></div></div>
  <div class="compare-cards"><article><div class="compare-head surgery"><span>可</span><h3>Case-based teaching analysis</h3></div><ul><li>完整 relative-day timeline</li><li>診斷不確定性與多科風險衝突</li><li>Surgery／I-131 readiness 比較</li><li>說明文獻不可外推之處</li></ul></article><article><div class="compare-head rai"><span>待</span><h3>完整 case report</h3></div><ul><li>實際 definitive therapy</li><li>Short- and long-term outcomes</li><li>Patient perspective</li><li>Publication consent</li></ul></article></div>
</section>

<section class="section" id="thesis">
  <div class="section-title"><span>02</span><div><h2>最有價值的文章問題</h2><p>新意在可追蹤的決策過程，不在疾病組合本身。</p></div></div>
  <blockquote>當 severe ATD-associated agranulocytosis 發生後，surgery 與 I-131 同時受到 infection、HFrEF、iodine exposure 與 suspicious nodules 限制時，團隊如何用可觀察條件選擇並完成 definitive treatment？</blockquote>
  <p>理想文章應在同一張 timeline 呈現 ANC、CRP、FT4／FT3、Cr、iodide exposure、影像、EF、實際 administration 與真正 decision points。Outcome 至少涵蓋 definitive treatment、infection、cardiac function 與 thyroid function。</p>
</section>

<section class="section" id="care">
  <div class="section-title"><span>03</span><div><h2>CARE checklist 缺口</h2><p>依重要性排序的補件清單。</p></div></div>
  <ol class="stage-list compact-list">
    <li><span>01</span><div><h3>治療與 outcome</h3><p>最後選擇、執行日期、實際 procedure／I-131 activity、complications、follow-up。</p></div></li>
    <li><span>02</span><div><h3>完整 medication administration</h3><p>Carbimazole、allopurinol、G-CSF、antibiotics、Lugol、hydrocortisone、lithium 與 HF drugs。</p></div></li>
    <li><span>03</span><div><h3>Timeline reconciliation</h3><p>停藥日、contrast／Cr、Lugol last dose、lithium level timing。</p></div></li>
    <li><span>04</span><div><h3>Diagnostic evidence</h3><p>BWPS components、TRAb assay、ultrasound images、lymph-node mapping、FNA／pathology。</p></div></li>
    <li><span>05</span><div><h3>Organ outcomes</h3><p>Follow-up pulmonary imaging、infection course、repeat echo、rhythm、renal function。</p></div></li>
    <li><span>06</span><div><h3>Patient perspective／consent</h3><p>病人的理由、理解、選擇變化與正式 publication consent。</p></div></li>
  </ol>
  <p class="source-note"><a href="https://www.care-statement.org/checklist">CARE checklist</a>、<a href="https://www.icmje.org/recommendations/browse/roles-and-responsibilities/protection-of-research-participants.html">ICMJE privacy／consent</a></p>
</section>

<section class="section" id="questions">
  <div class="section-title"><span>04</span><div><h2>跨專科會議的 15 個問題</h2><p>每一題都對應一個可能改變治療的資料。</p></div></div>
  <ol class="question-grid">
    <li><span>01</span><div><h3>完整用藥時序？</h3><p>所有實際給藥與最後一劑。</p></div></li>
    <li><span>02</span><div><h3>Allopurinol exposure？</h3><p>開始、停用、adherence 與其他 neutropenia drugs。</p></div></li>
    <li><span>03</span><div><h3>Contrast 與 Cr 先後？</h3><p>分鐘級時間戳。</p></div></li>
    <li><span>04</span><div><h3>Lugol 配方與末劑？</h3><p>計算 iodine load 與 RAI readiness。</p></div></li>
    <li><span>05</span><div><h3>BWPS 35／50 分項？</h3><p>同時點器官症狀。</p></div></li>
    <li><span>06</span><div><h3>Etiology 能否更確定？</h3><p>TRAb、scintigraphy／RAIU。</p></div></li>
    <li><span>07</span><div><h3>Pneumonia 是否清除？</h3><p>影像、症狀、antibiotic end date。</p></div></li>
    <li><span>08</span><div><h3>EF 是否恢復？</h3><p>Repeat echo、rhythm、volume。</p></div></li>
    <li><span>09</span><div><h3>右側 nodule FNA？</h3><p>原圖、LN mapping、cytology。</p></div></li>
    <li><span>10</span><div><h3>左側 nodule 如何追蹤？</h3><p>位置、LN／ETE 與正式分類。</p></div></li>
    <li><span>11</span><div><h3>Lithium 是否真的使用？</h3><p>MAR、adherence、level timing。</p></div></li>
    <li><span>12</span><div><h3>最新 renal／Na／volume？</h3><p>決定 lithium 與等待安全。</p></div></li>
    <li><span>13</span><div><h3>ACTH 如何解讀？</h3><p>Hydrocortisone 與 paired cortisol timing。</p></div></li>
    <li><span>14</span><div><h3>病人真正偏好？</h3><p>速度、surgery、radiation、replacement、follow-up。</p></div></li>
    <li><span>15</span><div><h3>Day 64 後 outcome？</h3><p>決定能否形成完整 case report。</p></div></li>
  </ol>
</section>

<section class="section" id="meeting">
  <div class="section-title"><span>05</span><div><h2>建議會議順序</h2><p>先確認事實，再做選擇。</p></div></div>
  <div class="decision-chain wrap"><span>1. 核對 timeline／MAR</span><i>→</i><span>2. 更新 infection／HF</span><i>→</i><span>3. 確認 etiology／nodules</span><i>→</i><span>4. 判斷兩路 readiness</span><i>→</i><span>5. 納入 patient preference</span><i>→</i><span>6. 設定 rescue／follow-up</span></div>
</section>
'''

sources_body = r'''
<section class="section" id="guidelines">
  <div class="section-title"><span>01</span><div><h2>Guidelines 與 official sources</h2><p>用來界定標準框架與藥物安全。</p></div></div>
  <div class="source-library">
    <a href="https://doi.org/10.1089/thy.2016.0229"><span>ATA 2016</span><strong>Hyperthyroidism and thyrotoxicosis guideline</strong><p>治療選擇、patient preference、ATD adverse reaction、surgery。</p></a>
    <a href="https://link.springer.com/article/10.1007/s00259-023-06274-5"><span>EANM 2023</span><strong>Radioiodine therapy of benign thyroid disease</strong><p>RAIU、iodine withdrawal、patient preparation、contraindications。</p></a>
    <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13506520/"><span>Multi-society 2026</span><strong>Management of thyroid storm</strong><p>Lithium、iodide、definitive therapy 與較保守 washout。</p></a>
    <a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10448590/"><span>ETA 2023</span><strong>Thyroid nodule management</strong><p>Ultrasound risk、FNA threshold 與 follow-up。</p></a>
    <a href="https://www.ahajournals.org/doi/full/10.1161/CIR.0000000000001285"><span>AHA/ACC 2024</span><strong>Perioperative cardiovascular management</strong><p>HF、LVEF、decompensation 與 shared decision-making。</p></a>
    <a href="https://www.endocrine.org/clinical-practice-guidelines/glucocorticoid-induced-adrenal-insufficiency"><span>ESE／Endocrine Society 2024</span><strong>Glucocorticoid-induced adrenal insufficiency</strong><p>HPA-axis assessment framework。</p></a>
    <a href="https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=803eab29-0d0a-4df0-b504-bcd85ec01ead"><span>DailyMed</span><strong>Lithium carbonate label</strong><p>Level timing、renal／electrolytes、toxicity 與 interactions。</p></a>
    <a href="https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=14bf8041-0b7f-9acb-e063-6294a90a8256"><span>DailyMed</span><strong>Entresto label</strong><p>Section 7.4 lithium interaction。</p></a>
    <a href="https://dailymed.nlm.nih.gov/dailymed/lookup.cfm?setid=c23b6b9b-aec3-48a8-a518-76e4097f6479"><span>DailyMed</span><strong>Spironolactone label</strong><p>Section 7.2 reduced lithium clearance。</p></a>
  </div>
</section>

<section class="section" id="primary">
  <div class="section-title"><span>02</span><div><h2>Primary studies 與 case comparators</h2><p>可依主題直接跳到原始來源。</p></div></div>
  <div class="link-groups">
    <article><h3>Agranulocytosis timing／cross-reaction</h3><a href="https://pubmed.ncbi.nlm.nih.gov/24057289/">Nakamura 2013</a><a href="https://pubmed.ncbi.nlm.nih.gov/24341564/">Kobayashi 2014</a><a href="https://pubmed.ncbi.nlm.nih.gov/2464468/">Meyer-Gessner 1989</a><a href="https://pubmed.ncbi.nlm.nih.gov/22332800/">Otsuka 2012</a><a href="https://pubmed.ncbi.nlm.nih.gov/3256337/">Ostlere 1988</a></article>
    <article><h3>G-CSF</h3><a href="https://pubmed.ncbi.nlm.nih.gov/10037073/">Fukata 1999 randomized trial</a><a href="https://pubmed.ncbi.nlm.nih.gov/31824417/">G-CSF meta-analysis</a></article>
    <article><h3>Lithium／RAI</h3><a href="https://pubmed.ncbi.nlm.nih.gov/12364424/">Bogazzi 2002 randomized study</a><a href="https://pubmed.ncbi.nlm.nih.gov/19906789/">Bogazzi 2010 cohort</a><a href="https://www.frontiersin.org/journals/endocrinology/articles/10.3389/fendo.2026.1770772/full">Gao 2026 cohort</a><a href="https://pubmed.ncbi.nlm.nih.gov/38008728/">Tamura 2024 KI→RAI</a></article>
    <article><h3>Case reports／series</h3><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5592706/">Knight 2017</a><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC13133480/">Voci 2026</a><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC5434745/">Calissendorff 2017</a><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC10981326/">Rami 2024</a><a href="https://academic.oup.com/jes/article/5/Supplement_1/A958/6241039">Fantin 2021 abstract</a><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC11454931/">Sazon 2024 abstract</a></article>
    <article><h3>HFrEF／thyrotoxic cardiomyopathy</h3><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC8318454/">Kositanurit 2021</a><a href="https://pmc.ncbi.nlm.nih.gov/articles/PMC3780617/">Determinants of recovery</a></article>
    <article><h3>Publication standards</h3><a href="https://www.care-statement.org/checklist">CARE checklist</a><a href="https://www.icmje.org/recommendations/browse/roles-and-responsibilities/protection-of-research-participants.html">ICMJE privacy／consent</a></article>
  </div>
</section>

<section class="section" id="method">
  <div class="section-title"><span>03</span><div><h2>研究與查核方法</h2><p>來源與本案資料採不同層級處理。</p></div></div>
  <div class="method-grid"><article><span>01</span><h3>Case reconstruction</h3><p>原始 UTF-8 Markdown 病歷只在本機核對；公開內容改用 relative days 並去識別化。</p></article><article><span>02</span><h3>Multi-role review</h3><p>Diagnosis、Endocrinology、Hematology、Drug Safety、Infection、Nuclear Medicine、Surgery、Cardiology 與 publication methods 分別判讀，再互相 challenge。</p></article><article><span>03</span><h3>Primary-source audit</h3><p>重要分母回到 guideline、original paper、official label；解析 Markdown 只作索引。</p></article><article><span>04</span><h3>Evidence boundary</h3><p>Case report 證明可行路徑，cohort 提供群體結果，兩者都不能直接替本案下結論。</p></article></div>
</section>

<section class="section" id="limitations">
  <div class="section-title"><span>04</span><div><h2>主要限制</h2><p>網站內容再完整，也不能補出尚未存在的 patient data。</p></div></div>
  <ul class="risk-list"><li>資料截止 Day 64，缺 definitive treatment 與長期 outcome。</li><li>Medication administration、iodine formulation、最後一劑與 lithium level timing 不完整。</li><li>沒有原始 ultrasound images、完整 cervical LN mapping、FNA／pathology。</li><li>沒有 updated echo、infection clearance 與完整 renal／volume follow-up。</li><li>本次是 targeted literature review，不是 systematic review；不主張 first 或 exhaustive novelty。</li><li>公開網站只提供去識別化研究摘要；原始病歷不公開。正式投稿仍需 patient consent 與 institution policy review。</li></ul>
</section>
'''

pages = {
    "index.html": ("病例總覽與閱讀地圖", "ATD AGRANULOCYTOSIS · CASE HUB", "從病歷事實開始，逐步走到 Lithium、I-131、HFrEF、nodules、文獻證據與投稿缺口。每個結論都標明它是已記錄、條件式判讀，或仍待補資料。", '<a href="#summary">目前結論</a><a href="#facts">關鍵事實</a><a href="#decisions">決策核心</a><a href="#pathways">兩條路徑</a><a href="#read-map">閱讀地圖</a>', overview),
    "case.html": ("病例與完整時間線", "CASE RECONSTRUCTION", "以 relative days 重建病程，保留停藥、renal、iodide 與 lithium 紀錄中的不一致，避免把不同時點合併成錯誤因果。", '<a href="#snapshot">摘要</a><a href="#timeline">時間線</a><a href="#labs">數字判讀</a><a href="#uncertainties">紀錄歧異</a>', case_body),
    "diagnosis.html": ("診斷問題：Graves、Storm、Nodules", "DIAGNOSTIC VIEW", "把工作診斷、替代解釋與會改變治療的影像問題分開。", '<a href="#etiology">病因</a><a href="#storm">Storm</a><a href="#nodules">Nodules</a><a href="#steroid">Steroid／ACTH</a>', diagnosis_body),
    "safety.html": ("藥物安全、感染與替代 Bridge", "DRUG SAFETY · HEMATOLOGY · INFECTION", "從 causality、cross-reaction、G-CSF 到 infection recovery，說明為什麼嚴重 agranulocytosis 後不能用簡單百分比決定換藥。", '<a href="#causality">藥物歸因</a><a href="#cross-reaction">換 PTU</a><a href="#timing">發病時間</a><a href="#gcsf">G-CSF</a><a href="#infection">感染</a><a href="#bridges">Bridge</a>', safety_body),
    "experts.html": ("多方專家論點與交叉審查", "MULTIDISCIPLINARY VIEW", "逐一保留九個專業角色的主要立場、需要的資料與可能改變意見的條件，再把跨角色共識、分歧與互相質疑放在同一頁。", '<a href="#orientation">導讀</a><a href="#roles">角色立場</a><a href="#consensus">共識</a><a href="#debates">分歧</a><a href="#challenges">交叉質疑</a><a href="#mdt">責任表</a><a href="#open-items">未解問題</a>', experts_body),
    "i131.html": ("Lithium、停碘與 I-131 路徑", "DEFINITIVE THERAPY VIEW", "回答 lithium 是否真的有效、如何在不能使用 thionamide 時管理停碘等待，以及 patient preference 如何進入 surgery／I-131 選擇。", '<a href="#attribution">可歸因性</a><a href="#monitoring">安全監測</a><a href="#washout">停碘</a><a href="#pathway">五階段</a><a href="#evidence">Lithium evidence</a><a href="#comparison">治療比較</a>', i131_body),
    "cardiac.html": ("HFrEF：EF 32% 的病因與風險重評", "CARDIOLOGY VIEW", "不把 low EF 自動稱為 thyrotoxic cardiomyopathy，也不把 I-131 自動視為低風險；先確認是否恢復、是否 compensated，以及哪一組風險可以被控制。", '<a href="#reassessment">重新診斷</a><a href="#recovery">恢復證據</a><a href="#risk">風險矩陣</a><a href="#surgery">手術</a><a href="#waiting">等待 I-131</a>', cardiac_body),
    "evidence.html": ("文獻比較與外推界線", "EVIDENCE MAP", "依 guideline、randomized／cohort、case report 與本案推論分層，讓每個數字回到正確分母。", '<a href="#hierarchy">層級</a><a href="#comparators">病例比較</a><a href="#population">Cohort</a><a href="#do-not-claim">不可主張</a>', evidence_body),
    "publication.html": ("投稿評估、CARE 缺口與會議問題", "PUBLICATION · MDT MEETING", "整理目前可以誠實撰寫的主軸、還缺的 outcome、patient perspective，以及跨專科會議要回答的問題。", '<a href="#status">形式</a><a href="#thesis">主軸</a><a href="#care">CARE</a><a href="#questions">15 題</a><a href="#meeting">會議順序</a>', publication_body),
    "sources.html": ("來源索引與研究方法", "SOURCE LIBRARY", "集中列出 guideline、primary studies、official drug labels、case comparators 與研究限制。", '<a href="#guidelines">Guidelines</a><a href="#primary">研究／病例</a><a href="#method">方法</a><a href="#limitations">限制</a>', sources_body),
}

for filename, (title, eyebrow, intro, toc, body) in pages.items():
    (OUT / filename).write_text(layout(filename, title, eyebrow, intro, toc, body), encoding="utf-8")

print(f"generated {len(pages)} pages in {OUT}")
