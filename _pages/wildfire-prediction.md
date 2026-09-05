---
layout: single
title: "Wildfire Prediction System"
permalink: /projects/wildfire-prediction/
description: "BYU applied machine-learning project using weather time-series, XGBoost, model comparison, SHAP interpretability, APIs, and dashboard-style risk visualization."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/work.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/visual-v2.css' | relative_url }}">

<article class="portfolio-page case-page">

  <a class="case-back" href="/projects/">← Selected work</a>

  <header class="case-hero">
    <p class="pf-eyebrow">BYU · 2026</p>
    <h1>Predicting wildfire risk with time-series data and interpretable ML.</h1>
    <p class="case-hero__lead">
      A prototype risk-scoring workflow combining recent weather conditions, reported wildfire data,
      model comparison, interpretability, and API-driven data retrieval to prioritize high-risk locations.
    </p>
    <div class="case-tags">
      <span class="pf-tag">XGBoost</span>
      <span class="pf-tag">Time-Series</span>
      <span class="pf-tag">SHAP</span>
      <span class="pf-tag">API Integration</span>
    </div>
  </header>

  <section class="case-evidence">
    <figure class="case-evidence__hero case-evidence--contain">
      <img src="/assets/images/social/wildfire-social.jpg" alt="Wildfire prediction system project cover">
      <figcaption>Project summary: weather time-series, model comparison, SHAP interpretability, and API-connected risk visualization.</figcaption>
    </figure>
  </section>

  <section class="case-grid">
    <div class="case-main">
      <section class="case-section">
        <p class="pf-section__label">The problem</p>
        <h2>Risk prediction needs both performance and interpretability.</h2>
        <p>
          Wildfire-event data is highly imbalanced, and a useful risk system has to do more than produce a score.
          It should combine current environmental context with a model whose drivers can be inspected and communicated.
        </p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Approach</p>
        <h2>Compare models, explain predictions, and connect live data.</h2>
        <div class="case-points">
          <div>
            <span>01</span>
            <h3>Build the feature context</h3>
            <p>Used seven-day weather time-series together with reported fire data to construct a risk-oriented modeling dataset.</p>
          </div>
          <div>
            <span>02</span>
            <h3>Compare baseline approaches</h3>
            <p>Trained and compared XGBoost, Random Forest, and Naive Bayes models on imbalanced wildfire-event data.</p>
          </div>
          <div>
            <span>03</span>
            <h3>Explain the model</h3>
            <p>Applied SHAP interpretability to understand which variables were driving individual and aggregate risk estimates.</p>
          </div>
          <div>
            <span>04</span>
            <h3>Design the workflow</h3>
            <p>Connected weather APIs, satellite-imagery retrieval, and dashboard-style visualization into a prototype decision workflow.</p>
          </div>
        </div>
      </section>

      <section class="case-section">
        <p class="pf-section__label">Why it belongs here</p>
        <h2>A transferable ML problem outside industrial analytics.</h2>
        <p>
          This project broadens the portfolio beyond mining and infrastructure while reinforcing the same core skills:
          time-series data, model evaluation, interpretability, external data integration, and decision-oriented presentation.
        </p>
      </section>
    </div>

    <aside class="case-sidebar">
      <div class="case-fact"><span>Context</span><strong>BYU project</strong></div>
      <div class="case-fact"><span>Year</span><strong>2026</strong></div>
      <div class="case-fact"><span>Models</span><strong>XGBoost · Random Forest · Naive Bayes</strong></div>
      <div class="case-fact"><span>Interpretability</span><strong>SHAP</strong></div>
      <div class="case-fact"><span>Data workflow</span><strong>Weather APIs · fire data · imagery retrieval</strong></div>
    </aside>
  </section>

  <nav class="case-next">
    <span>Back to</span>
    <a href="/projects/">Selected work →</a>
  </nav>

</article>
