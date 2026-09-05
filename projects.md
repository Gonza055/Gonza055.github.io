---
layout: single
title: "Work"
permalink: /projects/
description: "Selected work by Gonzalo Loayza across machine learning, data engineering, industrial analytics, and decision support."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/work.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/visual-pass-2.css' | relative_url }}">

<div class="portfolio-page work-page">

  <header class="work-hero">
    <p class="pf-eyebrow">Selected work</p>
    <h1>Data, ML, and software applied to real systems.</h1>
    <p>
      I am most interested in technical work where the data is imperfect, the physical system matters,
      and the analysis needs to support a real engineering or operational decision.
    </p>
  </header>

  <section class="work-featured">
    <a class="work-feature work-feature--hero" href="/projects/hatch-digital/">
      <div class="work-feature__content">
        <p class="work-feature__meta">Hatch Digital · 2026 · Mining &amp; Industrial Operations</p>
        <h2>Data Engineering &amp; Decision Support</h2>
        <p>
          Applied digital work spanning tailings-data automation, drone-based measurement concepts,
          and shift-level decision support — with an emphasis on making engineering information reliable,
          interpretable, and useful for action.
        </p>
        <div class="work-feature__tags">
          <span class="pf-tag">Data Engineering</span>
          <span class="pf-tag">Automation</span>
          <span class="pf-tag">Digital Mining</span>
          <span class="pf-tag">Decision Support</span>
        </div>
        <span class="work-feature__link">Read case study →</span>
      </div>
      <img class="work-feature__media" src="/assets/images/real/hatch-presentation-hitm.webp" alt="Gonzalo presenting a Hatch Digital data-validation workflow">
    </a>

    <a class="work-feature" href="/projects/predictive-maintenance/">
      <img class="work-feature__media" src="/assets/images/real/buenaventura-site.webp" alt="Gonzalo at the mining operation where reliability analytics work was performed">
      <div class="work-feature__content">
        <p class="work-feature__meta">Buenaventura · San Gabriel · 2025 · Reliability Analytics</p>
        <h2>Predictive Maintenance &amp; Reliability Analytics</h2>
        <p>
          An end-to-end industrial analytics experience spanning noisy sensor data, feature engineering,
          equipment behavior, asset structure, and condition-monitoring exploration.
        </p>
        <div class="work-feature__metrics">
          <strong>50k+</strong><span>time-series</span>
          <strong>15+</strong><span>engineered features</span>
          <strong>100+</strong><span>structured assets</span>
        </div>
        <span class="work-feature__link">Read case study →</span>
      </div>
    </a>

    <a class="work-feature" href="/projects/operational-mode-discovery/">
      <img class="work-feature__media" src="/assets/images/real/thesis-regimes.webp" alt="PCA operating-regime visualization from the BYU Honors thesis">
      <div class="work-feature__content">
        <p class="work-feature__meta">BYU Honors · 2025–2026 · Industrial Time-Series</p>
        <h2>Operational Mode Discovery &amp; Business Value Analysis</h2>
        <p>
          Honors research using minute-level process data, PCA, DBSCAN, and KPI context
          to identify recurrent operating modes in a real industrial processing environment.
        </p>
        <div class="work-feature__tags">
          <span class="pf-tag">Python</span>
          <span class="pf-tag">PCA</span>
          <span class="pf-tag">DBSCAN</span>
          <span class="pf-tag">Operational Analytics</span>
        </div>
        <span class="work-feature__link">Read case study →</span>
      </div>
    </a>
  </section>

  <section class="pf-section work-more">
    <div class="pf-section__head">
      <div>
        <p class="pf-section__label">More work</p>
        <h2>Software, simulation, and applied ML.</h2>
      </div>
    </div>

    <div class="work-small-grid">
      <a class="work-small-card" href="/projects/trainops/">
        <img class="work-small-card__media" src="/assets/images/projects/trainops-caps-009-2.webp" alt="TrainOps route elevation and speed profile">
        <div class="work-small-card__top">
          <p class="work-feature__meta">Hatch Urban Solutions · 2024</p>
          <span class="work-small-card__number">01</span>
        </div>
        <h3>TrainOps Simulation Data Engineering</h3>
        <p>
          Python and C++ automation for 200k+ rail-simulation records, reducing processing time by about 70%
          and improving repeatability for scenario analysis.
        </p>
        <span class="work-feature__link">View project →</span>
      </a>

      <a class="work-small-card" href="/projects/wildfire-prediction/">
        <img class="work-small-card__media" src="/assets/images/real/wildfire-team.webp" alt="Gonzalo and teammates presenting the Wildfire Prediction project">
        <div class="work-small-card__top">
          <p class="work-feature__meta">BYU · 2026</p>
          <span class="work-small-card__number">02</span>
        </div>
        <h3>Wildfire Prediction System</h3>
        <p>
          A wildfire-risk prototype using seven-day weather histories, model comparison,
          XGBoost, maps, and satellite-image retrieval to prioritize high-risk locations.
        </p>
        <span class="work-feature__link">View project →</span>
      </a>
    </div>
  </section>

  <section class="work-principle">
    <p class="pf-section__label">How I work</p>
    <blockquote>
      Understand the system first. Make the data trustworthy. Build the simplest analysis that answers the
      decision. Then add modeling where it creates real value.
    </blockquote>
  </section>

</div>
