---
layout: single
title: "Operational Mode Discovery & Business Value Analysis"
permalink: /projects/operational-mode-discovery/
description: "BYU Honors thesis case study applying time-series preprocessing, PCA, clustering, and business-value analysis to a real industrial processing environment."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">

<article class="portfolio-page case-page">

  <a class="case-back" href="/projects/">← Selected work</a>

  <header class="case-hero">
    <p class="pf-eyebrow">BYU Honors Program · 2025–2026</p>
    <h1>Discovering operating modes and connecting them to business value.</h1>
    <p class="case-hero__lead">
      My Honors thesis explores how unsupervised learning can identify recurring operating patterns in a real
      industrial processing environment and connect those patterns to performance, stability, and value drivers.
    </p>
    <div class="case-tags">
      <span class="pf-tag">Python</span>
      <span class="pf-tag">Industrial Time-Series</span>
      <span class="pf-tag">PCA</span>
      <span class="pf-tag">Clustering</span>
      <span class="pf-tag">Business Value Analysis</span>
    </div>
  </header>

  <section class="case-visual case-visual--modes" aria-label="Illustration of operating modes in reduced-dimensional space">
    <div class="case-cluster case-cluster--a"><i></i><i></i><i></i><i></i><i></i></div>
    <div class="case-cluster case-cluster--b"><i></i><i></i><i></i><i></i><i></i></div>
    <div class="case-cluster case-cluster--c"><i></i><i></i><i></i><i></i></div>
    <span class="case-axis case-axis--x">reduced dimension 1</span>
    <span class="case-axis case-axis--y">reduced dimension 2</span>
  </section>

  <section class="case-grid">
    <div class="case-main">
      <section class="case-section">
        <p class="pf-section__label">Research question</p>
        <h2>Can recurring operating patterns reveal where performance changes?</h2>
        <p>
          Industrial processes do not operate at a single steady state. Throughput pressure, recovery losses,
          equipment constraints, instrumentation quality, and control-loop behavior can all shift how the system
          behaves. The thesis frames these changes as recurring operational modes that can be discovered and profiled.
        </p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Method</p>
        <h2>From minute-level process data to interpretable operating modes.</h2>
        <div class="case-points">
          <div>
            <span>01</span>
            <h3>Preprocess the process data</h3>
            <p>Align minute-level process information with daily KPI context, scale features, and prepare comparable observations for multivariate analysis.</p>
          </div>
          <div>
            <span>02</span>
            <h3>Reduce complexity</h3>
            <p>Use principal component analysis to compress correlated process variables while retaining interpretable patterns in the operating data.</p>
          </div>
          <div>
            <span>03</span>
            <h3>Discover recurrent modes</h3>
            <p>Apply clustering to identify recurring operating states and evaluate whether those modes correspond to meaningful process behavior.</p>
          </div>
          <div>
            <span>04</span>
            <h3>Connect modes to value</h3>
            <p>Profile operating modes against recovery, losses, throughput, stability, instrumentation gaps, and improvement opportunities.</p>
          </div>
        </div>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Why it matters</p>
        <h2>Analytics is more useful when it connects to an operational roadmap.</h2>
        <p>
          The thesis goes beyond clustering for its own sake. Its goal is to connect data infrastructure,
          control performance, instrumentation quality, and machine-learning opportunities to a staged roadmap
          around throughput, recovery stability, energy optimization, and business value.
        </p>
      </section>
    </div>

    <aside class="case-sidebar">
      <div class="case-fact"><span>Program</span><strong>BYU Honors</strong></div>
      <div class="case-fact"><span>Period</span><strong>2025–2026</strong></div>
      <div class="case-fact"><span>Data</span><strong>Industrial process time-series + KPI context</strong></div>
      <div class="case-fact"><span>Methods</span><strong>PCA · Clustering · Performance profiling</strong></div>
      <div class="case-fact"><span>Goal</span><strong>Interpretable operational insight</strong></div>
      <div class="case-note">
        <strong>Confidentiality</strong>
        <p>The industrial partner and identifying process details are intentionally not disclosed in this public portfolio.</p>
      </div>
    </aside>
  </section>

  <nav class="case-next">
    <span>Next project</span>
    <a href="/projects/trainops/">TrainOps Simulation Data Engineering →</a>
  </nav>

</article>
