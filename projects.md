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
          and decision-support workflows — with an emphasis on making engineering information more reliable,
          interpretable, and useful for operational decisions.
        </p>
        <div class="work-feature__tags">
          <span class="pf-tag">Data Engineering</span>
          <span class="pf-tag">Automation</span>
          <span class="pf-tag">Digital Mining</span>
          <span class="pf-tag">Decision Support</span>
        </div>
        <span class="work-feature__link">Read case study →</span>
      </div>
      <img src="/assets/images/social/hatch-digital-social.jpg" alt="Hatch Digital data engineering and decision support portfolio preview" style="display:block;width:100%;height:100%;min-height:430px;object-fit:cover;border-left:1px solid #e2e8f0;">
    </a>

    <a class="work-feature" href="/projects/predictive-maintenance/">
      <img src="/assets/images/projects/EDA4.png" alt="Mining operation where reliability analytics work was performed" style="display:block;width:100%;height:235px;object-fit:cover;object-position:center;border-bottom:1px solid #e2e8f0;">
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
      <img src="/assets/images/social/operational-mode-social.jpg" alt="Operational mode discovery and business value analysis portfolio preview" style="display:block;width:100%;height:235px;object-fit:cover;border-bottom:1px solid #e2e8f0;">
      <div class="work-feature__content">
        <p class="work-feature__meta">BYU Honors · 2025–2026 · Industrial Time-Series</p>
        <h2>Operational Mode Discovery &amp; Business Value Analysis</h2>
        <p>
          Honors research using time-series preprocessing, PCA, clustering, and performance context
          to identify recurrent operating modes in a real industrial processing environment.
        </p>
        <div class="work-feature__tags">
          <span class="pf-tag">Python</span>
          <span class="pf-tag">PCA</span>
          <span class="pf-tag">Clustering</span>
          <span class="pf-tag">Business Value</span>
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
      <a class="work-small-card" href="/projects/trainops/" style="overflow:hidden;">
        <img src="/assets/images/projects/trainops-caps-009-2.webp" alt="TrainOps route elevation and speed profile" style="display:block;width:calc(100% + 2.8rem);height:150px;margin:-1.4rem -1.4rem 1.1rem;object-fit:cover;border-bottom:1px solid #e2e8f0;">
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

      <a class="work-small-card" href="/projects/wildfire-prediction/" style="overflow:hidden;">
        <img src="/assets/images/social/wildfire-social.jpg" alt="Wildfire prediction system portfolio preview" style="display:block;width:calc(100% + 2.8rem);height:150px;margin:-1.4rem -1.4rem 1.1rem;object-fit:cover;border-bottom:1px solid #e2e8f0;">
        <div class="work-small-card__top">
          <p class="work-feature__meta">BYU · 2026</p>
          <span class="work-small-card__number">02</span>
        </div>
        <h3>Wildfire Prediction System</h3>
        <p>
          A wildfire-risk prototype using weather time-series, XGBoost, model comparison, SHAP interpretability,
          APIs, and dashboard-oriented visualization.
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
