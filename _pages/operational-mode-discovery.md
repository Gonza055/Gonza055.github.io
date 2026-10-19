---
layout: single
title: "Operational Mode Discovery"
permalink: /projects/operational-mode-discovery/
description: "BYU Honors thesis case study applying preprocessing, PCA, DBSCAN, and KPI profiling to identify interpretable operating regimes from industrial process data."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/honors-research-approved.css' | relative_url }}?v=20261018-honors2">

<article class="honors-case">

  <header class="honors-hero">
    <div class="honors-hero__copy">
      <p class="honors-eyebrow">BYU HONORS RESEARCH · COMPUTER SCIENCE · 2025–2026</p>
      <h1>Process Data<br><span>to Operating Modes</span></h1>
      <p class="honors-hero__lead">Unsupervised learning to identify recurring operating regimes in an industrial mineral-processing circuit — and interpret what those regimes mean operationally.</p>
      <div class="honors-hero__tags">
        <span>Industrial Time-Series</span>
        <span>PCA</span>
        <span>DBSCAN</span>
        <span>Operational Analytics</span>
      </div>
    </div>
    <div class="honors-hero__visual">
      <img src="https://proactivo.com.pe/wp-content/uploads/2019/06/miski-mayo-bayovar-800x446.jpg" alt="Industrial phosphate concentrator site view">
    </div>
  </header>

  <main class="honors-body">

    <section class="honors-context">
      <div class="honors-section-head">
        <span>01</span>
        <div><p>RESEARCH CONTEXT</p><h2>Operational-mode discovery from real plant history.</h2></div>
      </div>
      <div class="honors-context__grid">
        <div>
          <h3>Operational Mode Discovery Using Unsupervised Learning</h3>
          <p>The thesis investigates whether a mineral-processing circuit behaves as one broad operating state or as several recurring regimes that can be discovered from minute-level process variables and then interpreted using metallurgical and production KPIs.</p>
        </div>
        <dl class="honors-facts">
          <div><dt>Program</dt><dd>BYU Honors · Computer Science</dd></div>
          <div><dt>Honors Advisor</dt><dd>David Grimsman</dd></div>
          <div><dt>Analytical scope</dt><dd>Concentrator Line 1</dd></div>
          <div><dt>Data</dt><dd>Minute-level process history + daily KPI context</dd></div>
          <div><dt>Methods</dt><dd>StandardScaler · PCA · DBSCAN · KPI profiling</dd></div>
        </dl>
      </div>
    </section>

    <section class="honors-question">
      <div class="honors-section-head">
        <span>02</span>
        <div><p>RESEARCH QUESTION</p><h2>Does the plant operate as one state — or as several recurring operating modes?</h2></div>
      </div>
      <div class="honors-question__grid">
        <p>The process variables define the analytical structure. Recovery, production, and metallurgical KPIs are attached afterward to interpret the regimes — not to generate them.</p>
        <div class="honors-question__rule"><strong>Core analytical rule</strong><span>Discover structure first → interpret performance second.</span></div>
      </div>
    </section>

    <section class="honors-process-context">
      <div class="honors-section-head">
        <span>03</span>
        <div><p>PROCESS CONTEXT</p><h2>The model reflects the active Line 1 configuration studied in the thesis.</h2></div>
      </div>
      <figure class="honors-wide-figure">
        <img src="/assets/images/generated/byu-active-process-context.png" alt="Concentrator Line 1 active process context with feeding, washing and classification, desliming, cyclone classification, and final dewatering">
        <figcaption>Active analytical pathway: feed loading → coarse screening and washing → intermediate classification and desliming → cyclone-based fine classification → final dewatering. Bypassed nominal equipment is excluded from the analytical model.</figcaption>
      </figure>
    </section>

    <section class="honors-methodology">
      <div class="honors-section-head">
        <span>04</span>
        <div><p>METHODOLOGY</p><h2>From process history to interpretable operating regimes.</h2></div>
      </div>
      <figure class="honors-wide-figure honors-wide-figure--method">
        <img src="/assets/images/generated/byu-analytical-workflow.png" alt="Analytical workflow from process and KPI data through integration, imputation, scaling, PCA, epsilon selection, DBSCAN, intervention, export, and interpretation">
        <figcaption>The workflow preserves a separation between structure discovery in process-variable space and later KPI-based operational interpretation.</figcaption>
      </figure>
    </section>

    <section class="honors-results">
      <div class="honors-section-head">
        <span>05</span>
        <div><p>RESULTS</p><h2>Three recurrent operating regimes emerged.</h2></div>
      </div>

      <div class="honors-metrics">
        <div><strong>3</strong><span>retained operating regimes</span></div>
        <div><strong>44%</strong><span>time in Drum Bypass</span></div>
        <div><strong>44%</strong><span>time in Stable</span></div>
        <div><strong>86.86%</strong><span>Stable average recovery</span></div>
        <div><strong>1.85%</strong><span>Stable recovery standard deviation</span></div>
      </div>

      <figure class="honors-wide-figure honors-wide-figure--result">
        <img src="/assets/images/generated/byu-operating-regimes.png" alt="Portfolio reconstruction of the three recurrent operating regimes identified in the thesis">
        <figcaption>Portfolio reconstruction of the thesis result. Percentages and KPI values are thesis results; point positions reproduce the published PCA geometry for presentation, not the original raw coordinates.</figcaption>
      </figure>
    </section>

    <section class="honors-kpis">
      <div class="honors-section-head">
        <span>06</span>
        <div><p>KPI EVIDENCE</p><h2>The regimes differed in both performance and variability.</h2></div>
      </div>
      <div class="honors-kpi-grid">
        <figure>
          <img src="/assets/images/generated/byu-recovery-by-regime.png" alt="Average recovery and recovery standard deviation by operating regime">
          <figcaption>Recovery averages and standard deviations from thesis Table 5.1.</figcaption>
        </figure>
        <figure>
          <img src="/assets/images/generated/byu-production-by-regime.png" alt="Average production and production standard deviation by operating regime">
          <figcaption>Production averages and standard deviations from thesis Table 5.1.</figcaption>
        </figure>
      </div>
    </section>

    <section class="honors-interpretation">
      <div class="honors-section-head">
        <span>07</span>
        <div><p>OPERATIONAL INTERPRETATION</p><h2>A cluster only becomes useful when it has physical and operational meaning.</h2></div>
      </div>
      <div class="honors-regimes">
        <article class="honors-regime honors-regime--red">
          <div class="honors-regime__top"><span></span><h3>Unstable</h3><b>12%</b></div>
          <p>Diffuse operating behavior with the lowest average recovery and the highest recovery variability.</p>
          <dl><div><dt>Recovery</dt><dd>84.89% ± 5.14%</dd></div><div><dt>Production</dt><dd>599.0 ± 44.44 tph</dd></div></dl>
        </article>
        <article class="honors-regime honors-regime--blue">
          <div class="honors-regime__top"><span></span><h3>Drum Bypass</h3><b>44%</b></div>
          <p>A coherent recurrent state associated with a distinct process signature, including drum-speed behavior near zero.</p>
          <dl><div><dt>Recovery</dt><dd>85.96% ± 1.99%</dd></div><div><dt>Production</dt><dd>604.0 ± 50.22 tph</dd></div></dl>
        </article>
        <article class="honors-regime honors-regime--green">
          <div class="honors-regime__top"><span></span><h3>Stable</h3><b>44%</b></div>
          <p>The strongest reference condition: highest average recovery, highest average production, and lowest recovery variability.</p>
          <dl><div><dt>Recovery</dt><dd>86.86% ± 1.85%</dd></div><div><dt>Production</dt><dd>606.8 ± 31.13 tph</dd></div></dl>
        </article>
      </div>
    </section>

    <section class="honors-mentorship">
      <div class="honors-mentorship__photo"><img src="/assets/images/real/honors-yale-original.webp" alt="Gonzalo Loayza with Dr. Yale Zhang during an industrial research discussion in Lima"></div>
      <div class="honors-mentorship__copy">
        <p class="honors-mini-label">RESEARCH MENTORSHIP &amp; INDUSTRIAL CONTEXT</p>
        <h2>Academic rigor connected to real operating questions.</h2>
        <p>The thesis was completed under BYU Honors supervision, while industrial guidance helped frame the concentrator context, the use of real-world process data, and the operational meaning of the analysis.</p>
        <div class="honors-mentorship__notes">
          <div><strong>Honors Advisor</strong><span>David Grimsman</span></div>
          <div><strong>Industrial guidance</strong><span>Plant-performance perspective and applied research context</span></div>
        </div>
      </div>
    </section>

    <section class="honors-close">
      <div>
        <p class="honors-mini-label">WHAT I LEARNED</p>
        <h2>A cluster is not an insight until it has operational meaning.</h2>
        <p>Unsupervised learning can reveal structure in complex process data, but the real value comes from connecting those patterns back to process behavior, KPIs, physical equipment, and operational decisions.</p>
      </div>
      <div>
        <p class="honors-mini-label">TECHNOLOGIES &amp; METHODS</p>
        <div class="honors-tech">
          <span>Python</span><span>Pandas</span><span>StandardScaler</span><span>PCA</span><span>DBSCAN</span><span>KPI Profiling</span><span>Data Visualization</span>
        </div>
      </div>
    </section>

  </main>

  <nav class="honors-nav">
    <a href="/projects/predictive-maintenance/"><small>Previous Project</small><strong>← Buenaventura San Gabriel</strong><span>Sensor Data → Reliability</span></a>
    <a href="/projects/trainops/"><small>Next Project</small><strong>Hatch Urban Solutions →</strong><span>Simulation Data → Operational Insights</span></a>
  </nav>

</article>