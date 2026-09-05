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
      My Honors thesis explores how unsupervised learning can identify recurring operating patterns in a real
      industrial processing environment and connect those patterns to recovery, production stability, and value drivers.
    </p>
    <div class="case-tags">
      <span class="pf-tag">Python</span><span class="pf-tag">Industrial Time-Series</span><span class="pf-tag">PCA</span><span class="pf-tag">DBSCAN</span><span class="pf-tag">Business Value Analysis</span>
    </div>
  </header>

  <section style="margin:0 0 2.8rem;padding:1.35rem;border:1px solid #e2e8f0;border-radius:18px;background:#fff;">
    <div style="display:grid;grid-template-columns:1.15fr .85fr;gap:1.25rem;align-items:stretch;">
      <div style="min-height:310px;border-radius:14px;background:#f8fafc;position:relative;overflow:hidden;border:1px solid #e2e8f0;">
        <div class="case-visual case-visual--modes" aria-label="Retained operating regimes in reduced-dimensional space" style="margin:0;height:100%;min-height:310px;border:0;border-radius:0;">
          <div class="case-cluster case-cluster--a"><i></i><i></i><i></i><i></i><i></i></div>
          <div class="case-cluster case-cluster--b"><i></i><i></i><i></i><i></i><i></i></div>
          <div class="case-cluster case-cluster--c"><i></i><i></i><i></i><i></i></div>
          <span class="case-axis case-axis--x">principal-component space</span>
          <span class="case-axis case-axis--y">retained structure</span>
        </div>
      </div>
      <div style="display:grid;grid-template-rows:repeat(3,1fr);gap:.75rem;">
        <div style="padding:1rem;border:1px solid #e2e8f0;border-radius:12px;background:#f8fafc;"><span style="display:block;color:#64748b;font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;">Unstable regime</span><strong style="display:block;font-size:1.65rem;color:#0f172a;margin:.15rem 0;">12%</strong><span style="font-size:.82rem;color:#475569;">of operating time · lowest recovery · highest variability</span></div>
        <div style="padding:1rem;border:1px solid #e2e8f0;border-radius:12px;background:#f8fafc;"><span style="display:block;color:#64748b;font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;">Drum-bypass regime</span><strong style="display:block;font-size:1.65rem;color:#0f172a;margin:.15rem 0;">44%</strong><span style="font-size:.82rem;color:#475569;">of operating time · distinct dense operating region</span></div>
        <div style="padding:1rem;border:1px solid #e2e8f0;border-radius:12px;background:#f8fafc;"><span style="display:block;color:#64748b;font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;">Stable regime</span><strong style="display:block;font-size:1.65rem;color:#0f172a;margin:.15rem 0;">44%</strong><span style="font-size:.82rem;color:#475569;">of operating time · highest average recovery · lowest recovery variability</span></div>
      </div>
    </div>
    <p style="margin:.8rem 0 0;color:#64748b;font-size:.78rem;line-height:1.5;">Result summary based on the retained analytical structure in the thesis. Exact partner identity and identifying process details are omitted, while the analytical result is preserved.</p>
  </section>

  <section class="case-metric-strip">
    <div><strong>95%</strong><span>PCA explained-variance target</span></div>
    <div><strong>2.5</strong><span>selected DBSCAN epsilon</span></div>
    <div><strong>3</strong><span>retained operating regimes</span></div>
  </section>

  <section class="case-grid">
    <div class="case-main">
      <section class="case-section">
        <p class="pf-section__label">Research question</p>
        <h2>Can recurring operating patterns reveal where performance changes?</h2>
        <p>Industrial processes do not operate at a single steady state. Throughput pressure, recovery losses, equipment constraints, instrumentation quality, and control-loop behavior can shift how the system behaves. The thesis frames these changes as recurring operational modes that can be discovered and profiled.</p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Method</p>
        <h2>From minute-level process data to interpretable operating modes.</h2>
        <div class="case-points">
          <div><span>01</span><h3>Prepare and align</h3><p>Merge minute-level process data with daily KPI context, handle missing values, and standardize heterogeneous variables before modeling.</p></div>
          <div><span>02</span><h3>Reduce dimensionality</h3><p>Use PCA with a 95% explained-variance target to create a compact latent representation of correlated process behavior.</p></div>
          <div><span>03</span><h3>Find dense structures</h3><p>Apply DBSCAN in principal-component space so dense operating structures can emerge without forcing every observation into a cluster.</p></div>
          <div><span>04</span><h3>Interpret against KPIs</h3><p>Compare retained regimes against recovery, production, variability, and process signatures to connect geometry with operating meaning.</p></div>
        </div>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Result</p>
        <h2>The retained structure was operationally different, not just geometrically different.</h2>
        <p>The thesis identified three recurrent patterns with materially different recovery and production profiles. The unstable regime represented about 12% of operating time and combined the lowest average recovery with the highest recovery variability; the two denser regimes each represented about 44% of operating time, with the stable regime showing the strongest recovery profile.</p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Why it matters</p>
        <h2>Unsupervised learning becomes useful when it explains a real operating state.</h2>
        <p>The value is not the cluster label itself. It is the ability to connect data infrastructure, process signatures, control performance, and machine-learning opportunities to a practical roadmap around throughput, recovery stability, energy optimization, and business value.</p>
      </section>
    </div>

    <aside class="case-sidebar">
      <div class="case-fact"><span>Program</span><strong>BYU Honors</strong></div>
      <div class="case-fact"><span>Period</span><strong>2025–2026</strong></div>
      <div class="case-fact"><span>Setting</span><strong>Real industrial concentrator environment</strong></div>
      <div class="case-fact"><span>Data</span><strong>Minute-level process data + daily KPI context</strong></div>
      <div class="case-fact"><span>Methods</span><strong>StandardScaler · PCA · DBSCAN · KPI profiling</strong></div>
      <div class="case-fact"><span>Goal</span><strong>Interpretable operational insight</strong></div>
    </aside>
  </section>

  <nav class="case-next"><span>Next project</span><a href="/projects/trainops/">TrainOps Simulation Data Engineering →</a></nav>
</article>
