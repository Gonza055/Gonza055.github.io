---
layout: single
title: "Operational Mode Discovery & Business Value Analysis"
permalink: /projects/operational-mode-discovery/
description: "BYU Honors thesis case study applying time-series preprocessing, PCA, DBSCAN clustering, and business-value analysis to a real industrial processing environment."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/work.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/visual-pass-2.css' | relative_url }}">

<article class="portfolio-page case-page">
  <a class="case-back" href="/projects/">← Selected work</a>

  <header class="case-hero">
    <p class="pf-eyebrow">BYU Honors Program · 2025–2026</p>
    <h1>Discovering operating modes and connecting them to business value.</h1>
    <p class="case-hero__lead">
      My Honors thesis investigates whether minute-level industrial process data can reveal recurring operating
      regimes that are analytically distinct, operationally interpretable, and meaningfully different in performance.
    </p>
    <div class="case-tags">
      <span class="pf-tag">Python</span><span class="pf-tag">Industrial Time-Series</span><span class="pf-tag">PCA</span><span class="pf-tag">DBSCAN</span><span class="pf-tag">Operational Analytics</span>
    </div>
  </header>

  <figure class="case-media case-media--wide case-media--technical">
    <img src="/assets/images/real/thesis-regimes.webp" alt="PCA visualization showing three retained operating regimes">
    <figcaption>Real thesis result: the retained PCA structure reveals three recurring operating regimes rather than one homogeneous operating state.</figcaption>
  </figure>

  <section class="case-metric-strip">
    <div><strong>95%</strong><span>PCA explained-variance target</span></div>
    <div><strong>2.5</strong><span>selected DBSCAN epsilon</span></div>
    <div><strong>3</strong><span>retained operating regimes</span></div>
  </section>

  <section class="case-grid">
    <div class="case-main">
      <section class="case-section">
        <p class="pf-section__label">Research question</p>
        <h2>Can noisy process history be reorganized into operating states that engineers can interpret?</h2>
        <p>
          Industrial processes rarely behave as one steady state. Feed conditions, equipment configurations,
          hydraulic behavior, and control conditions shift over time. The thesis asks whether those changes leave
          recurring multivariate patterns in the process data — and whether those patterns relate to performance.
        </p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Method</p>
        <h2>Separate process behavior from performance context, then connect them again for interpretation.</h2>
        <p>
          Minute-level process observations form the unsupervised-learning feature space, while daily operational
          and metallurgical KPIs are preserved as interpretive context. The workflow prepares and aligns both layers,
          standardizes the process features, reduces dimensionality with PCA, applies DBSCAN, and then profiles the
          retained structures against operational evidence.
        </p>
      </section>

      <figure class="case-media case-media--wide case-media--technical">
        <img src="/assets/images/real/thesis-workflow.webp" alt="Analytical workflow from process and KPI data through preprocessing, PCA, DBSCAN, refinement, and exported outputs">
        <figcaption>Analytical workflow from the thesis: data integration → preprocessing → scaling → PCA → DBSCAN → analytical refinement → reproducible outputs.</figcaption>
      </figure>

      <div class="case-points">
        <div><span>01</span><h3>Prepare and align</h3><p>Merge minute-level process history with daily KPI context while preserving the difference in time scale.</p></div>
        <div><span>02</span><h3>Reduce dimensionality</h3><p>Use PCA with a 95% explained-variance target to compress correlated industrial variables into a latent feature space.</p></div>
        <div><span>03</span><h3>Find dense structures</h3><p>Apply DBSCAN so recurring dense regions can emerge without forcing every observation into a cluster.</p></div>
        <div><span>04</span><h3>Interpret the regimes</h3><p>Compare retained structures against recovery, production, variability, and process signatures to assign operating meaning.</p></div>
      </div>

      <section class="case-section">
        <p class="pf-section__label">Result</p>
        <h2>The three regimes differed in both geometry and operating performance.</h2>
        <p>
          The retained result contains one diffuse unstable regime representing about 12% of operating time and two
          denser recurring regimes representing about 44% each. Within the analyzed period, the stable regime showed
          the strongest combination of average recovery, recovery consistency, and production, while the unstable
          regime showed the weakest and most variable profile. A separate dense regime was distinguished by a clear
          equipment-configuration signature.
        </p>
      </section>

      <section class="case-media-grid case-media-grid--equal" aria-label="Thesis result interpretation">
        <figure class="case-media case-media--technical">
          <img src="/assets/images/real/thesis-regimes.webp" alt="Operating regimes in PCA space with their share of operating time">
          <figcaption>Structure in PCA space: 12% diffuse/unstable, 44% configuration-specific, and 44% stable operation.</figcaption>
        </figure>
        <figure class="case-media case-media--technical">
          <img src="/assets/images/real/thesis-temporal.webp" alt="Daily operating-regime contribution plotted alongside a daily performance KPI">
          <figcaption>Temporal view: regime prevalence changes day by day and can be compared with operational KPI behavior.</figcaption>
        </figure>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Why it matters</p>
        <h2>Unsupervised learning becomes useful when the structure can be explained in process terms.</h2>
        <p>
          The contribution is not simply finding clusters. It is building a reproducible path from noisy historian data
          to operating regimes that can be discussed with engineers, compared against performance, and eventually used
          as a foundation for regime-aware monitoring and process-improvement work.
        </p>
      </section>
    </div>

    <aside class="case-sidebar">
      <div class="case-fact"><span>Program</span><strong>BYU Honors</strong></div>
      <div class="case-fact"><span>Period</span><strong>2025–2026</strong></div>
      <div class="case-fact"><span>Setting</span><strong>Real industrial concentrator environment</strong></div>
      <div class="case-fact"><span>Data</span><strong>Minute-level process data + daily KPI context</strong></div>
      <div class="case-fact"><span>Methods</span><strong>StandardScaler · PCA · DBSCAN · KPI profiling</strong></div>
      <div class="case-fact"><span>Goal</span><strong>Interpretable operational modes</strong></div>
    </aside>
  </section>

  <nav class="case-next"><span>Next project</span><a href="/projects/trainops/">TrainOps Simulation Data Engineering →</a></nav>
</article>
