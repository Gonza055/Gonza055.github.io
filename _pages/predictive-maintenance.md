---
layout: single
title: "Sensor Data to Reliability"
permalink: /projects/predictive-maintenance/
description: "Buenaventura San Gabriel case study: industrial sensor conditioning, reliability feature engineering, asset structuring, and condition-monitoring analysis."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/case-v3.css' | relative_url }}">

<article class="case3" style="--case-accent:#10b981; --case-accent-soft:#ecfdf5;">
  <a class="case3-back" href="/projects/">← Selected Work</a>

  <header class="case3-hero">
    <div class="case3-hero__top">
      <div class="case3-hero__copy">
        <p class="case3-eyebrow" style="color:#6ee7b7!important;">Buenaventura · San Gabriel Unit · 2025</p>
        <h1>From noisy sensor data to a reliability foundation.</h1>
        <p class="case3-hero__lead">I worked with crushing and grinding equipment data to build a cleaner, more structured analytical foundation for condition monitoring and future predictive-maintenance workflows.</p>
        <div class="case3-tags">
          <span class="case3-tag">Industrial Time-Series</span>
          <span class="case3-tag">Feature Engineering</span>
          <span class="case3-tag">Reliability Analytics</span>
          <span class="case3-tag">Asset Structure</span>
        </div>
      </div>
      <div class="case3-hero__image">
        <img src="/assets/images/real/buenaventura-site.webp" alt="Gonzalo Loayza at Buenaventura San Gabriel">
      </div>
    </div>

    <div class="case3-facts">
      <div class="case3-fact"><span>Role</span><strong>Maintenance Data Analyst Intern</strong></div>
      <div class="case3-fact"><span>Organization</span><strong>Compañía de Minas Buenaventura</strong></div>
      <div class="case3-fact"><span>Unit</span><strong>San Gabriel · Peru</strong></div>
      <div class="case3-fact"><span>Period</span><strong>Jun – Aug 2025</strong></div>
      <div class="case3-fact"><span>Domain</span><strong>Crushing &amp; grinding reliability</strong></div>
    </div>
  </header>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">The Problem</p>
      <h2>The data existed. The analytical foundation did not.</h2>
      <p>Equipment and process signals were noisy, irregular, and difficult to use directly for maintenance analysis. Before building any predictive model, the first job was to make the signals more reliable, give them engineering context, and structure the assets consistently.</p>
    </div>

    <div class="case3-problem">
      <div class="case3-copybox">
        <p>The work focused on <strong>building the data foundation</strong> required for predictive maintenance: conditioning sensor histories, engineering reliability-oriented variables, interpreting operating patterns, and organizing asset information so future analysis could be repeatable.</p>
      </div>
      <div class="case3-insight" style="border-color:#a7f3d0;">
        <strong>Important distinction</strong>
        <p>This was not a claim of a production-ready failure-prediction model. It was the engineering and analytical work needed before one could be developed responsibly.</p>
      </div>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Evidence at a Glance</p>
      <h2>Industrial scale, grounded in reliability.</h2>
    </div>

    <div class="case3-results">
      <article class="case3-result"><strong>50k+</strong><p>noisy industrial sensor time-series processed and conditioned.</p></article>
      <article class="case3-result"><strong>15+</strong><p>reliability-focused features engineered for analysis.</p></article>
      <article class="case3-result"><strong>100+</strong><p>assets structured for improved traceability and analytical usability.</p></article>
      <article class="case3-result"><strong>ISO 14224 / 17359</strong><p>standards used to organize asset and condition-monitoring context.</p></article>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Approach</p>
      <h2>An end-to-end reliability analytics workflow.</h2>
      <p>Instead of jumping directly to modeling, I worked through four layers that made the data progressively more useful.</p>
    </div>

    <div class="case3-process">
      <div class="case3-step"><strong>Condition the signals</strong><span>Smoothing, outlier capping, and signal reconstruction to reduce noise and stabilize the histories.</span></div>
      <div class="case3-step"><strong>Engineer reliability features</strong><span>Temperature deltas, load ratios, and transient-spike indicators designed around equipment behavior.</span></div>
      <div class="case3-step"><strong>Interpret operating patterns</strong><span>EDA on crushing and grinding signals to investigate wear behavior, ore variability, and early-warning candidates.</span></div>
      <div class="case3-step"><strong>Structure the assets</strong><span>Organize 100+ assets under reliability-oriented standards to improve consistency and traceability.</span></div>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Technical Workflow</p>
      <h2>Raw signals → trustworthy monitoring variables.</h2>
      <p>The core technical idea was simple: every modeling decision downstream depends on signal quality and context upstream.</p>
    </div>

    <figure class="case3-photo" style="background:#f8fafc;">
      <img src="/assets/images/diagrams/reliability-workflow.svg" alt="Reliability workflow from raw industrial signals through conditioning, feature engineering, and monitoring candidates" style="object-fit:contain;padding:1.5rem;min-height:280px;">
      <figcaption>Reliability workflow from raw equipment signals through conditioning, feature engineering, asset context, and monitoring candidates.</figcaption>
    </figure>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">What the Analysis Looked For</p>
      <h2>Signals that might matter before failure.</h2>
      <p>The objective was not merely to describe the data, but to identify variables and relationships that could later support more useful condition-monitoring logic.</p>
    </div>

    <div class="case3-streams">
      <article class="case3-stream">
        <div class="case3-stream__body">
          <span class="case3-stream__num">01 · Signal Quality</span>
          <h3>Separate noise from behavior.</h3>
          <p>Condition raw histories so that transient noise, outliers, and missing or unstable behavior do not dominate the analysis.</p>
        </div>
      </article>
      <article class="case3-stream">
        <div class="case3-stream__body">
          <span class="case3-stream__num">02 · Equipment Behavior</span>
          <h3>Create interpretable indicators.</h3>
          <p>Build variables that reflect temperature change, relative loading, transient spikes, and other patterns with possible reliability meaning.</p>
        </div>
      </article>
      <article class="case3-stream">
        <div class="case3-stream__body">
          <span class="case3-stream__num">03 · Process Context</span>
          <h3>Relate equipment signals to operation.</h3>
          <p>Use EDA to connect wear-related signals with process behavior and ore variability instead of treating sensors in isolation.</p>
        </div>
      </article>
    </div>
  </section>

  <section class="case3-section">
    <div class="case3-section__head">
      <p class="case3-label">Outcome</p>
      <h2>A stronger basis for condition monitoring and future ML.</h2>
      <p>The internship produced cleaner data, reusable reliability features, more structured asset information, and a clearer analytical basis for early-warning and predictive-maintenance exploration.</p>
    </div>

    <div class="case3-results">
      <article class="case3-result"><strong>Cleaner time-series</strong><p>Sensor histories became more stable and usable for systematic analysis.</p></article>
      <article class="case3-result"><strong>Reusable features</strong><p>Reliability-focused variables created a more consistent basis for comparing equipment behavior.</p></article>
      <article class="case3-result"><strong>Better traceability</strong><p>Asset structuring improved consistency across maintenance and monitoring data.</p></article>
      <article class="case3-result"><strong>Future-ready foundation</strong><p>Prepared datasets and engineering context for later predictive-maintenance prototyping.</p></article>
    </div>
  </section>

  <section class="case3-learn" style="background:linear-gradient(135deg,#052e2b,#064e3b);">
    <p class="case3-label" style="color:#6ee7b7!important;">What I Learned</p>
    <h2>Predictive maintenance starts before the prediction.</h2>
    <p>Good ML for equipment reliability depends on much more than choosing a model. Signal conditioning, asset hierarchy, process context, and engineering interpretation determine whether a prediction can eventually become useful to maintenance and operations teams.</p>
  </section>

  <nav class="case3-next">
    <span>Next Case Study</span>
    <a href="/projects/operational-mode-discovery/">BYU Honors · Process Data → Operating Modes →</a>
  </nav>
</article>
