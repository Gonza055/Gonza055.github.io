---
layout: single
title: "Sensor Data to Reliability"
permalink: /projects/predictive-maintenance/
description: "Buenaventura San Gabriel case study: HPGR wear analysis, data quality, operational monitoring, and reliability foundations for predictive maintenance."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/buenaventura-approved.css' | relative_url }}?v=20261018-bvn-approved-visuals">

<article class="bvncase">
  <header class="bvn-hero">
    <div class="bvn-hero__content">
      <div class="bvn-brand">
        <span class="bvn-brand__mark">B</span>
        <span class="bvn-brand__name">BUENAVENTURA</span>
        <span class="bvn-brand__divider"></span>
        <span class="bvn-brand__unit">SAN GABRIEL</span>
      </div>
      <h1>Sensor Data to <span>Reliability</span></h1>
      <p class="bvn-hero__lead">HPGR wear and operational data analysis to understand equipment degradation and build a stronger foundation for condition-based maintenance and future predictive analytics.</p>
      <div class="bvn-hero__tags">
        <span>HPGR</span><span>Exploratory Data Analysis</span><span>Reliability</span><span>Predictive Maintenance</span>
      </div>
    </div>
  </header>

  <main class="bvn-sheet">
    <section class="bvn-context">
      <div class="bvn-section-head"><span></span><h2>Context</h2><p>Real maintenance analytics work at San Gabriel.</p></div>
      <div class="bvn-context__grid">
        <div class="bvn-context__copy">
          <h3>HPGR roller wear &amp; operational monitoring</h3>
          <p>During my Buenaventura internship, I analyzed HPGR roller-wear histories together with production, material, and operational sensor data. The goal was to understand degradation patterns, identify data-quality limitations, and determine what information could responsibly support condition monitoring and later predictive-maintenance work.</p>
          <div class="bvn-source-strip">
            <span><b>Wear history</b> thickness · campaigns</span>
            <span><b>Production</b> tonnage · material mix</span>
            <span><b>HPGR sensors</b> temperature · pressure · current · speed · gap</span>
          </div>
        </div>
        <figure class="bvn-context__photo">
          <img src="/assets/images/real/bvn-gonzalo-lima.webp" alt="Gonzalo Loayza at the Buenaventura office in Lima">
          <figcaption>Buenaventura internship — corporate and field context</figcaption>
        </figure>
      </div>
      <div class="bvn-facts">
        <div><b>Role</b><span>Maintenance Intern · Computer Science / ML</span></div>
        <div><b>Organization</b><span>Compañía de Minas Buenaventura</span></div>
        <div><b>Location</b><span>San Gabriel · Peru</span></div>
        <div><b>Core equipment</b><span>HPGR</span></div>
        <div><b>Main focus</b><span>Wear · sensors · reliability data</span></div>
      </div>
    </section>

    <section class="bvn-problem-evidence">
      <div class="bvn-section-head"><span></span><h2>The Data Problem</h2><p>Why the available HPGR data could support exploration, but not yet a responsible predictive model.</p></div>
      <div class="bvn-problem-top">
        <div>
          <h3 class="bvn-kicker">The challenge was not just modeling — it was making the data trustworthy enough to analyze.</h3>
          <p class="bvn-bodycopy">Wear history, campaign records, material information, and HPGR sensor data came from different sources and time windows. The analysis therefore focused first on temporal alignment, data quality, campaign comparability, and the limits of what could be concluded.</p>
        </div>
        <div>
          <div class="bvn-metrics">
            <div><strong>4</strong><span>roller campaigns analyzed</span></div>
            <div><strong>~163k</strong><span>HPGR sensor records documented</span></div>
            <div><strong>16</strong><span>sensor-data columns in the operating dataset</span></div>
            <div><strong>2</strong><span>roller families compared: Vulco/Weir and Hofmann</span></div>
          </div>
          <div class="bvn-quality-card">
            <div class="bvn-quality-card__value">6528°C</div>
            <div><strong>A data-quality issue, not a physical event.</strong><p>Impossible temperature values were explicitly flagged before any predictive interpretation.</p></div>
          </div>
        </div>
      </div>
      <figure class="bvn-problem-visual">
        <img src="/assets/images/generated/bvn-hpgr-data-challenges-approved.png" alt="Key data challenges in the HPGR study: temporal misalignment, sensor anomalies, missing records, and campaign comparability">
        <figcaption>Portfolio visual rebuilt from the documented internship findings.</figcaption>
      </figure>
    </section>

    <section>
      <div class="bvn-section-head"><span></span><h2>Approach</h2><p>The workflow documented in the exploratory analysis.</p></div>
      <div class="bvn-approach bvn-approach--five">
        <article><em>01</em><h3>Clean &amp; validate</h3><p>Convert dates, normalize types, handle missing values, and flag impossible sensor readings.</p></article>
        <b>→</b>
        <article><em>02</em><h3>Integrate datasets</h3><p>Align wear history with comparative campaign data and aggregate sensor information by period.</p></article>
        <b>→</b>
        <article><em>03</em><h3>Explore wear patterns</h3><p>Use distributions, time series, and campaign comparisons to understand degradation behavior.</p></article>
        <b>→</b>
        <article><em>04</em><h3>Test relationships</h3><p>Evaluate tonnage, material mix, correlations, and linear-regression behavior.</p></article>
        <b>→</b>
        <article><em>05</em><h3>Translate to maintenance</h3><p>Separate reliable findings from limitations and identify the data foundation needed for monitoring.</p></article>
      </div>
    </section>

    <section class="bvn-evidence-section">
      <div class="bvn-section-head"><span></span><h2>Technical Evidence</h2><p>Rebuilt directly from the HPGR workbook and report findings.</p></div>
      <article class="bvn-evidence-main">
        <img src="/assets/images/generated/bvn-hpgr-wear-campaigns-approved.png" alt="HPGR roller thickness versus accumulated tonnage for four campaigns">
        <div class="bvn-evidence-main__copy">
          <strong>Wear is highly structured within each campaign.</strong>
          <p>The workbook shows a repeated pattern: roller thickness declines as accumulated tonnage increases, then resets when a new campaign begins. This makes campaign-aware wear estimation possible, while still requiring engineering context before using it as a maintenance rule.</p>
        </div>
      </article>
      <div class="bvn-evidence-grid">
        <article><img src="/assets/images/generated/bvn-hpgr-scatter-approved.png" alt="Scatter plot of HPGR thickness versus accumulated tonnage"><h3>Global wear signal</h3><p>The complete dataset shows a moderate inverse relationship between thickness and accumulated tonnage, with the report documenting <b>r ≈ -0.63</b> and a global linear model with <b>R² ≈ 0.39</b>.</p></article>
        <article><img src="/assets/images/generated/bvn-hpgr-correlations-approved.png" alt="Selected pairwise correlations for HPGR wear analysis"><h3>Material and operating context matter</h3><p>MAT 2 showed a strong inverse association with thickness (<b>r ≈ -0.81</b>). It was treated as an investigation signal — not a causal conclusion — because material definitions and synchronized operating context still needed engineering validation.</p></article>
      </div>
    </section>

    <section class="bvn-framework">
      <div class="bvn-section-head"><span></span><h2>Reliability Framework</h2><p>The maintenance-data manual connected the analytical work to reliability and condition-monitoring standards.</p></div>
      <figure class="bvn-framework-visual">
        <img src="/assets/images/generated/bvn-reliability-framework-approved.png" alt="Reliability data framework connecting ISO 14224, ISO 17359, ISO 13374, and ISO 13381-1">
        <figcaption>Conceptual framework distilled from the internship maintenance-data manual.</figcaption>
      </figure>
    </section>

    <section class="bvn-grid-two bvn-outcome-grid">
      <div>
        <div class="bvn-section-head"><span></span><h2>Outcome</h2></div>
        <h3 class="bvn-kicker">A defensible analytical foundation — not a premature failure model.</h3>
        <div class="bvn-outcomes">
          <div><b>01</b><span><strong>Campaign wear patterns became measurable.</strong> Thickness and tonnage could be compared on a consistent basis.</span></div>
          <div><b>02</b><span><strong>Data-quality risks were made explicit.</strong> Impossible sensor values and missing records were documented instead of hidden.</span></div>
          <div><b>03</b><span><strong>Potential drivers were identified.</strong> Tonnage and material mix became candidates for deeper engineering analysis.</span></div>
          <div><b>04</b><span><strong>Predictive work was scoped more responsibly.</strong> Better temporal overlap and cleaner sensor histories were identified as prerequisites.</span></div>
        </div>
      </div>
      <aside class="bvn-not-model">
        <strong>This was not a production-ready failure-prediction model.</strong>
        <span>The work established the exploratory, data-quality, and reliability foundations needed before one could be developed responsibly.</span>
      </aside>
    </section>

    <section>
      <div class="bvn-section-head"><span></span><h2>Gallery</h2><p>Original internship photographs — no generated substitutes.</p></div>
      <div class="bvn-gallery bvn-gallery--editorial">
        <figure class="bvn-gallery__wide"><img src="/assets/images/real/bvn-gonzalo-field-wide.webp" alt="Gonzalo Loayza at the San Gabriel site"><figcaption>San Gabriel — field context</figcaption></figure>
        <figure><img src="/assets/images/real/bvn-gonzalo-field-portrait.webp" alt="Gonzalo Loayza wearing Buenaventura San Gabriel PPE"><figcaption>Buenaventura San Gabriel — field PPE</figcaption></figure>
        <figure><img src="/assets/images/real/bvn-gonzalo-percy.webp" alt="Gonzalo Loayza with a Buenaventura colleague"><figcaption>Mentorship &amp; collaboration</figcaption></figure>
        <figure><img src="/assets/images/real/bvn-team-culture.webp" alt="Buenaventura team gathering"><figcaption>Team culture</figcaption></figure>
      </div>
    </section>

    <section class="bvn-bottom">
      <div>
        <div class="bvn-section-head"><span></span><h2>What I Learned</h2></div>
        <h3>Predictive maintenance starts before the prediction.</h3>
        <p>The strongest lesson was that modeling is only one layer of the problem. Data quality, asset definitions, operating context, maintenance standards, and engineering judgment determine whether an analytical result can become useful.</p>
      </div>
      <div>
        <div class="bvn-section-head"><span></span><h2>Technologies &amp; Methods</h2></div>
        <div class="bvn-tech"><span>Python</span><span>EDA</span><span>Time Series</span><span>Linear Regression</span><span>Reliability Standards</span></div>
      </div>
    </section>
  </main>

  <nav class="bvn-next">
    <a href="/projects/hatch-digital/"><small>Previous Project</small><strong>← Hatch Digital</strong><span>Mining Data → Decisions</span></a>
    <a href="/projects/operational-mode-discovery/"><small>Next Project</small><strong>BYU Honors Research →</strong><span>Process Data → Operating Modes</span></a>
  </nav>
</article>