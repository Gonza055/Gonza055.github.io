---
layout: single
title: "Predictive Maintenance & Reliability Analytics"
permalink: /projects/predictive-maintenance/
description: "Industrial analytics case study from Buenaventura: sensor-data conditioning, feature engineering, reliability analysis, and condition-monitoring exploration."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/work.css' | relative_url }}">

<article class="portfolio-page case-page">

  <a class="case-back" href="/projects/">← Selected work</a>

  <header class="case-hero">
    <p class="pf-eyebrow">Buenaventura · 2025</p>
    <h1>Turning noisy equipment data into a reliability workflow.</h1>
    <p class="case-hero__lead">
      During my maintenance-data internship, I worked across the reliability-data pipeline: cleaning industrial
      time-series, engineering equipment features, structuring asset information, and analyzing process behavior
      to support condition-monitoring and predictive-maintenance exploration.
    </p>
    <div class="case-tags">
      <span class="pf-tag">Industrial Time-Series</span>
      <span class="pf-tag">Feature Engineering</span>
      <span class="pf-tag">Reliability Analytics</span>
      <span class="pf-tag">Condition Monitoring</span>
    </div>
  </header>

  <section class="case-metric-strip">
    <div><strong>50k+</strong><span>high-noise sensor time-series processed</span></div>
    <div><strong>15+</strong><span>reliability-focused features engineered</span></div>
    <div><strong>100+</strong><span>assets structured under reliability standards</span></div>
  </section>

  <section class="case-grid">
    <div class="case-main">
      <section class="case-section">
        <p class="pf-section__label">The problem</p>
        <h2>The data existed, but it was not yet analysis-ready.</h2>
        <p>
          Equipment and process signals from crushing and grinding systems contained noise, inconsistent behavior,
          outliers, and limited structure. The first challenge was to create a reliable analytical foundation before
          attempting more advanced maintenance models.
        </p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Approach</p>
        <h2>An end-to-end reliability analytics workflow.</h2>
        <div class="case-points">
          <div>
            <span>01</span>
            <h3>Condition the signals</h3>
            <p>Applied smoothing, outlier handling, reconstruction, and preprocessing steps to make noisy time-series more stable and interpretable.</p>
          </div>
          <div>
            <span>02</span>
            <h3>Engineer useful features</h3>
            <p>Created reliability-focused variables including temperature deltas, load ratios, and transient-spike indicators for equipment monitoring.</p>
          </div>
          <div>
            <span>03</span>
            <h3>Connect process and wear behavior</h3>
            <p>Analyzed operating signals linked to equipment wear, ore variability, and process behavior to identify variables worth monitoring.</p>
          </div>
          <div>
            <span>04</span>
            <h3>Structure the asset context</h3>
            <p>Organized 100+ assets using ISO 14224/17359-oriented structures to improve traceability, consistency, and analytical usability.</p>
          </div>
        </div>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Outcome</p>
        <h2>A stronger basis for condition monitoring and future ML.</h2>
        <p>
          The work produced cleaner datasets, a reusable set of reliability features, clearer relationships between
          process behavior and equipment condition, and a more structured asset context for future monitoring workflows.
          The emphasis was not on claiming a production-ready failure model, but on building the data and engineering
          foundation needed for one.
        </p>
      </section>

      <section class="case-section case-section--visual-note">
        <p class="pf-section__label">Visual evidence</p>
        <h2>Real analysis, selectively anonymized.</h2>
        <p>
          The published portfolio intentionally avoids vendor-specific performance comparisons and sensitive operating
          values. Sanitized EDA and signal visuals can be added here where they demonstrate the analytical method without
          exposing confidential operational information.
        </p>
      </section>
    </div>

    <aside class="case-sidebar">
      <div class="case-fact"><span>Role</span><strong>Maintenance Data Analyst Intern</strong></div>
      <div class="case-fact"><span>Organization</span><strong>Compañía de Minas Buenaventura</strong></div>
      <div class="case-fact"><span>Period</span><strong>Jun – Aug 2025</strong></div>
      <div class="case-fact"><span>Domain</span><strong>Crushing &amp; grinding reliability</strong></div>
      <div class="case-fact"><span>Standards</span><strong>ISO 14224 / 17359</strong></div>
      <div class="case-fact"><span>Tools</span><strong>Python · Pandas · NumPy · EDA</strong></div>
    </aside>
  </section>

  <nav class="case-next">
    <span>Next case study</span>
    <a href="/projects/operational-mode-discovery/">Operational Mode Discovery &amp; Business Value Analysis →</a>
  </nav>

</article>
