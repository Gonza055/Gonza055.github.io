---
layout: single
title: "Operational Mode Discovery"
permalink: /projects/operational-mode-discovery/
description: "BYU Honors thesis case study applying preprocessing, PCA, DBSCAN, and KPI profiling to identify interpretable operating regimes in Line 1 of the Miski Mayo phosphate concentrator."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/case-v3.css' | relative_url }}">

<article class="case3" style="--case-accent:#60a5fa; --case-accent-soft:#eff6ff;">
  <a class="case3-back" href="/projects/">← Selected Work</a>

  <header class="case3-hero">
    <div class="case3-hero__top" style="background:radial-gradient(circle at 72% 20%,rgba(96,165,250,.14),transparent 34%),linear-gradient(135deg,#061526,#0c2a4d);">
      <div class="case3-hero__copy">
        <p class="case3-eyebrow" style="color:#93c5fd!important;">BYU Honors · Computer Science · 2025–2026</p>
        <h1>Process Data to Operating Modes.</h1>
        <p class="case3-hero__lead">My Honors thesis investigates whether minute-level historian data from Line 1 of the Miski Mayo phosphate concentrator can reveal recurrent operating regimes that are analytically separable, operationally interpretable, and meaningfully different in performance.</p>
        <div class="case3-tags">
          <span class="case3-tag">Industrial Time-Series</span>
          <span class="case3-tag">PCA</span>
          <span class="case3-tag">DBSCAN</span>
          <span class="case3-tag">Operational Analytics</span>
        </div>
      </div>
      <div class="case3-hero__image" style="background:#f8fafc;display:grid;place-items:center;">
        <img src="/assets/images/diagrams/honors-regimes.svg" alt="Three retained operating regimes in PCA space" style="object-fit:contain;padding:2rem;min-height:420px;">
      </div>
    </div>

    <div class="case3-facts">
      <div class="case3-fact"><span>Program</span><strong>BYU Honors</strong></div>
      <div class="case3-fact"><span>Study</span><strong>Line 1 · Miski Mayo Concentrator</strong></div>
      <div class="case3-fact"><span>Data</span><strong>Minute-level process history + daily KPI context</strong></div>
      <div class="case3-fact"><span>Methods</span><strong>PCA · DBSCAN · KPI profiling</strong></div>
      <div class="case3-fact"><span>Goal</span><strong>Interpretable operating regimes</strong></div>
    </div>
  </header>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Research Question</p>
      <h2>Does the plant operate as one state — or as several recurring modes?</h2>
      <p>Industrial mineral-processing plants operate under persistent variability. Changes in ore characteristics, feed composition, equipment behavior, and operating conditions can create recurrent patterns that disappear when the process is viewed only through averages.</p>
    </div>

    <div class="case3-problem">
      <div class="case3-copybox">
        <p>The thesis asks whether <strong>minute-level process data can be reorganized into recurring operating regimes</strong> and whether those regimes can then be interpreted using recovery, production, tailings behavior, and underlying process signatures.</p>
      </div>
      <div class="case3-insight" style="border-color:#bfdbfe;">
        <strong>Important distinction</strong>
        <p>This is an unsupervised structure-discovery problem, not a supervised prediction problem. The goal is to discover and interpret recurrent behavior without using performance KPIs to define the clusters.</p>
      </div>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Method</p>
      <h2>Discover structure first. Interpret performance second.</h2>
      <p>The methodology keeps process behavior and KPI context conceptually separate during regime discovery, then reconnects them afterward to determine whether the retained structures have operational meaning.</p>
    </div>

    <figure class="case3-photo" style="background:#f8fafc;">
      <img src="/assets/images/diagrams/honors-method.svg" alt="Honors thesis analytical workflow from process data through scaling PCA DBSCAN and KPI interpretation" style="object-fit:contain;padding:1.6rem;min-height:300px;">
      <figcaption>Minute-level process data → preprocessing and scaling → PCA → DBSCAN → retained structures → KPI and process-signature interpretation.</figcaption>
    </figure>

    <div class="case3-process" style="margin-top:1rem;">
      <div class="case3-step"><strong>01 · Prepare & align</strong><span>Organize process history and preserve daily metallurgical and operational KPI context for later interpretation.</span></div>
      <div class="case3-step"><strong>02 · Reduce dimensionality</strong><span>Use PCA to retain enough components to explain 95% of variance while compressing correlated process variables.</span></div>
      <div class="case3-step"><strong>03 · Discover dense structures</strong><span>Apply DBSCAN with a k-distance-supported epsilon of 2.5 and a neighborhood rule tied to retained PCA dimensions.</span></div>
      <div class="case3-step"><strong>04 · Interpret the regimes</strong><span>Compare retained structures against recovery, production, tailings behavior, and process signatures.</span></div>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Results</p>
      <h2>Three recurrent regimes emerged.</h2>
      <p>The final retained analytical structure showed that Line 1 did not behave as one homogeneous operating state.</p>
    </div>

    <div class="case3-results">
      <article class="case3-result"><strong>12% · Unstable</strong><p>Diffuse, less coherent behavior with the lowest average recovery and the highest recovery variability.</p></article>
      <article class="case3-result"><strong>44% · Drum Bypass</strong><p>A coherent recurrent condition distinguished by drum-speed values near zero.</p></article>
      <article class="case3-result"><strong>44% · Stable</strong><p>The strongest combination of average recovery, recovery consistency, and production performance.</p></article>
      <article class="case3-result"><strong>3 regimes</strong><p>Operational meaning was assigned after examining PCA geometry, KPIs, and underlying process signatures together.</p></article>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Performance Contrast</p>
      <h2>The regimes were different in more than geometry.</h2>
      <p>Recovery and production profiles provided evidence that the retained clusters corresponded to materially different operating behavior.</p>
    </div>

    <div class="case3-results">
      <article class="case3-result"><strong>84.89%</strong><p>Average recovery in the unstable regime.</p></article>
      <article class="case3-result"><strong>85.96%</strong><p>Average recovery in the drum-bypass regime.</p></article>
      <article class="case3-result"><strong>86.86%</strong><p>Average recovery in the stable operating regime.</p></article>
      <article class="case3-result"><strong>1.85%</strong><p>Recovery standard deviation in the stable regime — the lowest of the three retained regimes.</p></article>
    </div>

    <div class="case3-callout" style="background:#eff6ff;border-color:#bfdbfe;color:#1e40af;">These KPI differences were used for interpretation after clustering. They were not used to create the regimes themselves.</div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Operational Interpretation</p>
      <h2>Clusters become useful only when engineers can explain them.</h2>
      <p>The analysis moved from mathematical separation to process meaning by checking whether each regime had a coherent operational signature.</p>
    </div>

    <div class="case3-streams">
      <article class="case3-stream">
        <div class="case3-stream__body">
          <span class="case3-stream__num">01 · Unstable Regime</span>
          <h3>Diffuse and variable.</h3>
          <p>Lower recovery, higher recovery variability, and weaker production performance were consistent with a less coherent operating condition.</p>
        </div>
      </article>
      <article class="case3-stream">
        <div class="case3-stream__body">
          <span class="case3-stream__num">02 · Drum Bypass Regime</span>
          <h3>A distinct equipment configuration.</h3>
          <p>Drum-speed values near zero provided a direct process signature supporting interpretation of this dense regime as a recurrent bypass-related condition.</p>
        </div>
      </article>
      <article class="case3-stream">
        <div class="case3-stream__body">
          <span class="case3-stream__num">03 · Stable Regime</span>
          <h3>The strongest reference state.</h3>
          <p>This regime combined the highest average recovery, the lowest recovery variability, and the highest average production among the retained structures.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Why It Matters</p>
      <h2>From historian data to a more structured understanding of plant behavior.</h2>
      <p>The contribution is not simply that DBSCAN found clusters. The contribution is the reproducible path from noisy high-dimensional process history to regimes that can be discussed in operational terms and compared against metallurgical performance.</p>
    </div>

    <div class="case3-results">
      <article class="case3-result"><strong>Reproducible workflow</strong><p>Stored PCA outputs, cluster labels, summary tables, and KPI artifacts make the analysis auditable and repeatable.</p></article>
      <article class="case3-result"><strong>Process interpretability</strong><p>Regime labels emerge from geometry plus underlying process signatures rather than from arbitrary naming.</p></article>
      <article class="case3-result"><strong>Performance context</strong><p>Recovery, variability, production, and tailings behavior make the analytical structures operationally meaningful.</p></article>
      <article class="case3-result"><strong>Future monitoring basis</strong><p>The regime framework can support later regime-aware monitoring and process-improvement analysis.</p></article>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Technologies &amp; Methods</p>
      <h2>Methods served interpretation, not the other way around.</h2>
    </div>

    <div class="case3-tech">
      <div class="case3-tech__item"><strong>Python</strong><span>Reproducible analytical workflow</span></div>
      <div class="case3-tech__item"><strong>StandardScaler</strong><span>Comparable multivariate feature space</span></div>
      <div class="case3-tech__item"><strong>PCA</strong><span>95% variance target</span></div>
      <div class="case3-tech__item"><strong>DBSCAN</strong><span>Density-based regime discovery</span></div>
      <div class="case3-tech__item"><strong>KPI Profiling</strong><span>Recovery, production, tailings, variability</span></div>
    </div>
  </section>

  <section class="case3-learn" style="background:linear-gradient(135deg,#082f49,#0c4a6e);">
    <p class="case3-label" style="color:#93c5fd!important;">What I Learned</p>
    <h2>A cluster is not an insight until it has operational meaning.</h2>
    <p>The most important part of the thesis was not choosing PCA or DBSCAN. It was connecting the mathematical structure back to the process — asking whether the regimes were recurrent, whether their signatures made physical sense, and whether their performance differences were meaningful enough to help engineers understand how the plant operates.</p>
  </section>

  <nav class="case3-next">
    <span>Next Case Study</span>
    <a href="/projects/trainops/">Hatch Urban Solutions · Simulation Data → Operational Insights →</a>
  </nav>
</article>
