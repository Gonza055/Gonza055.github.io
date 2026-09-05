---
layout: single
title: "TrainOps Simulation Data Engineering"
permalink: /projects/trainops/
description: "Hatch Urban Solutions case study: Python and C++ automation for large rail-simulation datasets and scenario analysis."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/work.css' | relative_url }}">

<article class="portfolio-page case-page">

  <a class="case-back" href="/projects/">← Selected work</a>

  <header class="case-hero">
    <p class="pf-eyebrow">Hatch Urban Solutions · 2024</p>
    <h1>Automating simulation data so analysts can focus on the scenario.</h1>
    <p class="case-hero__lead">
      I built Python and C++ tooling to transform large TrainOps simulation outputs into cleaner,
      standardized datasets for scenario evaluation, operational analysis, and planning support.
    </p>
    <div class="case-tags">
      <span class="pf-tag">Python</span>
      <span class="pf-tag">C++</span>
      <span class="pf-tag">Data Engineering</span>
      <span class="pf-tag">Simulation Analytics</span>
    </div>
  </header>

  <figure style="margin:0 0 2.8rem;overflow:hidden;border:1px solid #e2e8f0;border-radius:16px;background:#fff;">
    <img src="/assets/images/projects/trainops-caps-003-2.webp" alt="TrainOps simulation interface and operating profile" style="display:block;width:100%;aspect-ratio:16/7;object-fit:cover;object-position:center;margin:0;">
    <figcaption style="padding:.8rem 1rem .9rem;color:#64748b;font-size:.76rem;line-height:1.5;border-top:1px solid #e2e8f0;">TrainOps simulation environment — the automation work focused on turning large output sets into faster, repeatable scenario analysis.</figcaption>
  </figure>

  <section class="case-metric-strip">
    <div><strong>200k+</strong><span>simulation records processed</span></div>
    <div><strong>~70%</strong><span>reduction in output-processing time</span></div>
    <div><strong>2</strong><span>languages used for automation: Python + C++</span></div>
  </section>

  <section class="case-grid">
    <div class="case-main">
      <section class="case-section">
        <p class="pf-section__label">The problem</p>
        <h2>Large simulation outputs were slowing down the analysis loop.</h2>
        <p>
          Scenario outputs were distributed across large, fragmented files that required repeated manual processing
          before analysts could compare delays, network performance, service assumptions, and operational bottlenecks.
        </p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Approach</p>
        <h2>Standardize the data before interpreting the scenario.</h2>
        <div class="case-points">
          <div>
            <span>01</span>
            <h3>Parse and normalize</h3>
            <p>Built parsers to transform raw simulation outputs into consistent, analysis-ready structures.</p>
          </div>
          <div>
            <span>02</span>
            <h3>Automate repeated processing</h3>
            <p>Reduced manual work by moving recurring cleaning and transformation steps into reusable Python and C++ workflows.</p>
          </div>
          <div>
            <span>03</span>
            <h3>Integrate external context</h3>
            <p>Combined rider-survey information with onboard sensor and simulation data to strengthen interpretation of service-level assumptions.</p>
          </div>
          <div>
            <span>04</span>
            <h3>Support scenario comparison</h3>
            <p>Made it easier to evaluate network performance and operational tradeoffs across multiple simulation cases.</p>
          </div>
        </div>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Outcome</p>
        <h2>Faster iteration and more repeatable analysis.</h2>
        <p>
          The automated workflow reduced simulation-output processing time by about 70% and improved repeatability,
          allowing more attention to shift from data preparation toward interpreting operational scenarios and planning implications.
        </p>
      </section>

      <div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;margin:0 0 2.8rem;">
        <figure style="margin:0;overflow:hidden;border:1px solid #e2e8f0;border-radius:14px;background:#fff;">
          <img src="/assets/images/projects/trainops-caps-004.webp" alt="TrainOps acceleration, resistance, and tractive effort curves" style="display:block;width:100%;height:230px;object-fit:cover;margin:0;">
          <figcaption style="padding:.7rem .85rem;color:#64748b;font-size:.73rem;line-height:1.45;">Performance curves used in simulation interpretation.</figcaption>
        </figure>
        <figure style="margin:0;overflow:hidden;border:1px solid #e2e8f0;border-radius:14px;background:#fff;">
          <img src="/assets/images/projects/trainops-caps-009-2.webp" alt="TrainOps route elevation and speed profile" style="display:block;width:100%;height:230px;object-fit:cover;margin:0;">
          <figcaption style="padding:.7rem .85rem;color:#64748b;font-size:.73rem;line-height:1.45;">Route elevation and speed profile for scenario analysis.</figcaption>
        </figure>
      </div>
    </div>

    <aside class="case-sidebar">
      <div class="case-fact"><span>Role</span><strong>Data Analytics Intern</strong></div>
      <div class="case-fact"><span>Organization</span><strong>Hatch Urban Solutions</strong></div>
      <div class="case-fact"><span>Location</span><strong>Vermont, USA</strong></div>
      <div class="case-fact"><span>Period</span><strong>May – Aug 2024</strong></div>
      <div class="case-fact"><span>Domain</span><strong>Transportation simulation</strong></div>
      <div class="case-fact"><span>Tools</span><strong>Python · C++ · Data automation</strong></div>
    </aside>
  </section>

  <nav class="case-next">
    <span>Next project</span>
    <a href="/projects/wildfire-prediction/">Wildfire Prediction System →</a>
  </nav>

</article>
