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

<article class="case3 case3-honors-hero" style="--case-accent:#60a5fa; --case-accent-soft:#eff6ff;">
  <a class="case3-back" href="/projects/">← Selected Work</a>

  <header class="case3-hero">
    <div class="case3-hero__top" style="background:radial-gradient(circle at 72% 20%,rgba(96,165,250,.14),transparent 34%),linear-gradient(135deg,#061526,#0c2a4d);">
      <div class="case3-hero__copy">
        <p class="case3-eyebrow" style="color:#93c5fd!important;">BYU Honors · Computer Science · 2025–2026</p>
        <h1>Process Data to Operating Modes.</h1>
        <p class="case3-hero__lead">Using minute-level historian data from Line 1 of the Miski Mayo phosphate concentrator, I investigated whether recurring operating regimes could be discovered without supervision and then explained in operational terms.</p>
        <div class="case3-tags">
          <span class="case3-tag">Industrial Time-Series</span>
          <span class="case3-tag">PCA</span>
          <span class="case3-tag">DBSCAN</span>
          <span class="case3-tag">Operational Analytics</span>
        </div>
      </div>
      <div class="case3-hero__image">
        <img src="/assets/images/diagrams/honors-regimes.svg" alt="Three retained operating regimes in PCA space">
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
      <p>The thesis tests whether process history can reveal distinct operating regimes and whether those regimes differ meaningfully in recovery, production, variability, and process behavior.</p>
    </div>

    <div class="case3-problem">
      <div class="case3-copybox">
        <p><strong>Core question:</strong> can unsupervised learning reorganize high-dimensional process data into recurring states that engineers can recognize and discuss?</p>
      </div>
      <div class="case3-insight" style="border-color:#bfdbfe;">
        <strong>Why the distinction matters</strong>
        <p>Recovery and production were used to interpret the clusters after discovery — not to define them.</p>
      </div>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Method</p>
      <h2>Discover structure first. Interpret performance second.</h2>
    </div>

    <figure class="case3-photo" style="background:#f8fafc;">
      <img src="/assets/images/diagrams/honors-method.svg" alt="Honors thesis workflow from process data through preprocessing PCA DBSCAN and KPI interpretation" style="object-fit:contain;padding:1.6rem;min-height:285px;">
      <figcaption>Process data → preprocessing and scaling → PCA → DBSCAN → retained regimes → KPI and process-signature interpretation.</figcaption>
    </figure>

    <div class="case3-process" style="margin-top:1rem;">
      <div class="case3-step"><strong>01 · Prepare</strong><span>Clean, align, and scale multivariate process data.</span></div>
      <div class="case3-step"><strong>02 · Reduce</strong><span>Use PCA to retain components explaining 95% of variance.</span></div>
      <div class="case3-step"><strong>03 · Discover</strong><span>Apply DBSCAN using a k-distance-supported ε = 2.5.</span></div>
      <div class="case3-step"><strong>04 · Interpret</strong><span>Compare regimes against KPIs and underlying process signatures.</span></div>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Results</p>
      <h2>Three recurrent regimes emerged.</h2>
    </div>

    <div class="case3-honors-summary">
      <div class="case3-honors-summary__main">
        <strong>Stable became the strongest reference state.</strong>
        <p>It combined the highest average recovery, the lowest recovery variability, and the strongest average production among the retained regimes.</p>
      </div>
      <div class="case3-honors-summary__metric">
        <div><strong>3</strong><span>retained operating regimes</span></div>
        <div><strong>44%</strong><span>time in the stable regime</span></div>
        <div><strong>86.86%</strong><span>stable average recovery</span></div>
        <div><strong>1.85%</strong><span>stable recovery standard deviation</span></div>
      </div>
    </div>

    <div class="case3-results" style="margin-top:1rem;">
      <article class="case3-result"><strong>12% · Unstable</strong><p>Diffuse behavior, lowest average recovery, and highest recovery variability.</p></article>
      <article class="case3-result"><strong>44% · Drum Bypass</strong><p>A coherent recurrent condition with drum-speed values near zero.</p></article>
      <article class="case3-result"><strong>44% · Stable</strong><p>Highest average recovery and production with the lowest recovery variability.</p></article>
      <article class="case3-result"><strong>Operational meaning</strong><p>Labels were assigned only after geometry, KPIs, and process signatures agreed.</p></article>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Operating-Regime Comparison</p>
      <h2>The clusters were different in both process signature and performance.</h2>
    </div>

    <table class="case3-regime-table">
      <thead>
        <tr>
          <th>Regime</th>
          <th>Share of Time</th>
          <th>Recovery (avg)</th>
          <th>Process Interpretation</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td><strong style="color:#ef4444;"><span class="case3-regime-dot"></span>Unstable</strong></td>
          <td>12%</td>
          <td>84.89%</td>
          <td>Diffuse, variable operating behavior.</td>
        </tr>
        <tr>
          <td><strong style="color:#2563eb;"><span class="case3-regime-dot"></span>Drum Bypass</strong></td>
          <td>44%</td>
          <td>85.96%</td>
          <td>Distinct condition associated with drum speed near zero.</td>
        </tr>
        <tr>
          <td><strong style="color:#10b981;"><span class="case3-regime-dot"></span>Stable</strong></td>
          <td>44%</td>
          <td>86.86%</td>
          <td>Highest recovery, lowest variability, and strongest production.</td>
        </tr>
      </tbody>
    </table>

    <div class="case3-callout" style="background:#eff6ff;border-color:#bfdbfe;color:#1e40af;">The KPI comparison comes after clustering. The regimes were discovered from process behavior, then interpreted using recovery, production, variability, and equipment signatures.</div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Why It Matters</p>
      <h2>Historian data becomes more useful when operating states are explicit.</h2>
    </div>

    <div class="case3-results">
      <article class="case3-result"><strong>Reproducible</strong><p>PCA outputs, cluster labels, summaries, and KPI comparisons can be regenerated and audited.</p></article>
      <article class="case3-result"><strong>Interpretable</strong><p>Regimes are tied back to physical process signatures rather than arbitrary cluster names.</p></article>
      <article class="case3-result"><strong>Comparable</strong><p>Recovery, variability, and production can be evaluated by operating state instead of only by global averages.</p></article>
      <article class="case3-result"><strong>Actionable later</strong><p>The framework can support future regime-aware monitoring and process-improvement analysis.</p></article>
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
      <div class="case3-tech__item"><strong>KPI Profiling</strong><span>Recovery, production, and variability</span></div>
    </div>
  </section>

  <section class="case3-learn" style="background:linear-gradient(135deg,#082f49,#0c4a6e);">
    <p class="case3-label" style="color:#93c5fd!important;">What I Learned</p>
    <h2>A cluster is not an insight until it has operational meaning.</h2>
    <p>The value came from connecting mathematical structure back to the process: recurring states had to make sense in the underlying variables and show meaningful differences in metallurgical and production performance.</p>
  </section>

  <nav class="case3-next">
    <span>Next Case Study</span>
    <a href="/projects/trainops/">Hatch Urban Solutions · Simulation Data → Operational Insights →</a>
  </nav>
</article>
