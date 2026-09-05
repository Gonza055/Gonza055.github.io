---
layout: single
title: "Wildfire Prediction System"
permalink: /projects/wildfire-prediction/
description: "BYU applied machine-learning project combining seven-day weather histories, XGBoost risk scoring, Utah maps, and satellite-image retrieval."
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
    <p class="pf-eyebrow">BYU · 2026</p>
    <h1>Prioritizing where to look for wildfires before scanning everywhere.</h1>
    <p class="case-hero__lead">
      A team prototype that combines recent weather data, machine learning, Utah risk maps, and satellite-image
      retrieval to narrow a large search area into locations that deserve attention first.
    </p>
    <div class="case-tags"><span class="pf-tag">XGBoost</span><span class="pf-tag">Time-Series</span><span class="pf-tag">API Integration</span><span class="pf-tag">Docker</span></div>
  </header>

  <figure class="case-media case-media--wide case-media--photo">
    <img src="/assets/images/real/wildfire-team.webp" alt="Gonzalo and two teammates presenting the Wildfire Prediction project at BYU">
    <figcaption>Project showcase at BYU — Gonzalo and teammates with the original physical Wildfire Prediction poster.</figcaption>
  </figure>

  <section class="case-metric-strip">
    <div><strong>7 days</strong><span>of weather history used for each example</span></div>
    <div><strong>3</strong><span>model families compared</span></div>
    <div><strong>18×</strong><span>PR-AUC lift over the random baseline</span></div>
  </section>

  <section class="case-grid">
    <div class="case-main">
      <section class="case-section">
        <p class="pf-section__label">The problem</p>
        <h2>Satellite monitoring becomes more useful when the search area is prioritized.</h2>
        <p>
          Continuously inspecting satellite imagery across a large region is expensive and inefficient. The project
          reframed early wildfire detection as a prioritization problem: use recent weather conditions to estimate
          which Utah locations are most likely to need visual follow-up, then retrieve imagery for those locations first.
        </p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Data &amp; modeling</p>
        <h2>Build weather histories around both fire and non-fire examples.</h2>
        <p>
          The pipeline starts from historical Utah fire dates and locations and retrieves the previous seven days of
          weather using Meteostat. Comparison examples are sampled from non-fire dates and locations. XGBoost,
          Naive Bayes, and Random Forest models were trained on balanced and unbalanced datasets; the unbalanced
          XGBoost model was selected for deployment.
        </p>
      </section>

      <section class="case-media-grid case-media-grid--equal" aria-label="Wildfire model results">
        <figure class="case-media case-media--technical">
          <img src="/assets/images/real/wildfire-risk-map.webp" alt="Utah weather-station locations and wildfire-risk heat map">
          <figcaption>Real project output: weather-station coverage and a Utah risk heat map used to narrow attention to concentrated hotspots.</figcaption>
        </figure>
        <figure class="case-media case-media--technical">
          <img src="/assets/images/real/wildfire-pr-curve.webp" alt="Precision-recall curve for the selected unbalanced XGBoost model">
          <figcaption>Precision-recall curve for the selected unbalanced XGBoost model.</figcaption>
        </figure>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Results</p>
        <h2>The prototype shows predictive lift, with important limitations stated plainly.</h2>
        <p>
          The selected model reached 23% precision, 9.7% recall, and a PR AUC of 0.110 compared with a random
          baseline of 0.006 — about an 18× improvement over random on this rare-event problem. The recall remains
          low, so the result is best understood as a prioritization prototype rather than a complete wildfire detector.
        </p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Product workflow</p>
        <h2>Connect the model to something a user can actually inspect.</h2>
        <div class="case-points">
          <div><span>01</span><h3>Collect current weather</h3><p>Query active Utah weather stations and prepare recent conditions for model scoring.</p></div>
          <div><span>02</span><h3>Rank high-risk locations</h3><p>Apply the deployed XGBoost model and prioritize locations by predicted wildfire risk.</p></div>
          <div><span>03</span><h3>Map the result</h3><p>Display high-risk areas in a browser-based dashboard so users can compare locations and inspect details.</p></div>
          <div><span>04</span><h3>Retrieve imagery</h3><p>Request satellite imagery for prioritized areas as a visual follow-up step rather than scanning the entire region indiscriminately.</p></div>
        </div>
      </section>

      <div class="case-evidence-note"><strong>Implementation:</strong> the final prototype used a Python backend and web-client frontend, with both services containerized for deployment.</div>

      <section class="case-section">
        <p class="pf-section__label">Why it belongs here</p>
        <h2>The same data-to-decision pattern in a different domain.</h2>
        <p>
          Wildfire Prediction broadens the portfolio beyond industrial analytics while preserving the same core idea:
          use imperfect real-world data to reduce a decision space, expose uncertainty, and connect a model to a practical workflow.
        </p>
      </section>
    </div>

    <aside class="case-sidebar">
      <div class="case-fact"><span>Context</span><strong>BYU applied ML team project</strong></div>
      <div class="case-fact"><span>Year</span><strong>2026</strong></div>
      <div class="case-fact"><span>Models</span><strong>XGBoost · Random Forest · Naive Bayes</strong></div>
      <div class="case-fact"><span>Weather data</span><strong>Meteostat + current weather APIs</strong></div>
      <div class="case-fact"><span>Product</span><strong>Python backend · web dashboard · Docker</strong></div>
      <div class="case-fact"><span>Decision output</span><strong>Prioritized high-risk locations</strong></div>
    </aside>
  </section>

  <nav class="case-next"><span>Back to</span><a href="/projects/">Selected work →</a></nav>
</article>
