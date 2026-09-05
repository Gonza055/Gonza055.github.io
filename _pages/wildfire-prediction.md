---
layout: single
title: "Wildfire Prediction System"
permalink: /projects/wildfire-prediction/
description: "BYU applied machine-learning project using weather time-series, XGBoost, SHAP interpretability, APIs, and dashboard-style risk visualization."
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
    <h1>Predicting wildfire risk with time-series data and interpretable ML.</h1>
    <p class="case-hero__lead">A prototype risk-scoring workflow combining recent weather conditions, reported wildfire data, model comparison, SHAP interpretability, and API-driven data retrieval to prioritize high-risk locations.</p>
    <div class="case-tags"><span class="pf-tag">XGBoost</span><span class="pf-tag">Time-Series</span><span class="pf-tag">SHAP</span><span class="pf-tag">API Integration</span></div>
  </header>

  <figure class="case-media case-media--wide">
    <img src="/assets/images/social/wildfire-social.jpg" alt="Wildfire prediction system portfolio preview">
    <figcaption>A complete data-to-decision prototype: weather history → risk model → interpretable drivers → priority locations → satellite-image retrieval.</figcaption>
  </figure>

  <section class="case-metric-strip">
    <div><strong>968</strong><span>reported Utah wildfires in the historical dataset</span></div>
    <div><strong>100k</strong><span>random date-location examples for comparison</span></div>
    <div><strong>18×</strong><span>PR-AUC improvement over the random baseline</span></div>
  </section>

  <section style="margin:0 0 2.8rem;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:1rem;">
    <div style="padding:1.2rem;border:1px solid #e2e8f0;border-radius:14px;background:#fff;"><span style="display:block;color:#64748b;font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;">Precision</span><strong style="display:block;font-size:1.9rem;color:#0f172a;margin:.2rem 0;">23%</strong><p style="margin:0;font-size:.82rem;color:#475569;">When the model predicts a fire, about 23% of those alerts correspond to an actual event.</p></div>
    <div style="padding:1.2rem;border:1px solid #e2e8f0;border-radius:14px;background:#fff;"><span style="display:block;color:#64748b;font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;">Recall</span><strong style="display:block;font-size:1.9rem;color:#0f172a;margin:.2rem 0;">9.7%</strong><p style="margin:0;font-size:.82rem;color:#475569;">The prototype detects a small but measurable share of true events in a highly imbalanced dataset.</p></div>
    <div style="padding:1.2rem;border:1px solid #e2e8f0;border-radius:14px;background:#fff;"><span style="display:block;color:#64748b;font-size:.72rem;text-transform:uppercase;letter-spacing:.08em;">PR AUC</span><strong style="display:block;font-size:1.9rem;color:#0f172a;margin:.2rem 0;">0.110</strong><p style="margin:0;font-size:.82rem;color:#475569;">Versus a baseline of 0.006, indicating meaningful lift despite the difficulty of the prediction problem.</p></div>
  </section>

  <section class="case-grid">
    <div class="case-main">
      <section class="case-section"><p class="pf-section__label">The problem</p><h2>Risk prediction needs both performance and interpretability.</h2><p>Wildfire-event data is highly imbalanced, and a useful risk system has to do more than produce a score. It should combine current environmental context with a model whose drivers can be inspected and communicated.</p></section>

      <section class="case-section"><p class="pf-section__label">Data</p><h2>Seven days of weather history around both fire and non-fire examples.</h2><p>The project used reported Utah wildfire locations from June 2020 through October 2025 and paired each event with the previous seven days of weather. A much larger set of randomly sampled Utah dates and locations provided comparison cases. Weather variables included temperature, dewpoint, humidity, precipitation, snow, wind direction, wind speed, wind gust, and air pressure.</p></section>

      <section class="case-section"><p class="pf-section__label">Approach</p><h2>Compare models, explain predictions, and connect live data.</h2><div class="case-points">
        <div><span>01</span><h3>Build the feature context</h3><p>Construct seven-day weather histories for reported fires and comparison locations.</p></div>
        <div><span>02</span><h3>Compare models</h3><p>Train and compare XGBoost, Random Forest, and Naive Bayes on the imbalanced event data.</p></div>
        <div><span>03</span><h3>Explain the model</h3><p>Use SHAP to inspect the weather variables contributing most strongly to risk estimates.</p></div>
        <div><span>04</span><h3>Connect the workflow</h3><p>Combine weather APIs, priority-location mapping, satellite-image retrieval, and dashboard-style presentation.</p></div>
      </div></section>

      <section class="case-section"><p class="pf-section__label">What the result says</p><h2>A useful prototype can show lift without pretending the problem is solved.</h2><p>The model's precision and recall remain limited, which is important to state plainly. At the same time, a PR AUC of 0.110 versus a random baseline near 0.006 shows that the feature set carries predictive signal. The project is therefore best presented as an interpretable prototype and a foundation for better data, spatial features, remote-sensing inputs, and model calibration.</p></section>
    </div>

    <aside class="case-sidebar">
      <div class="case-fact"><span>Context</span><strong>BYU applied ML project</strong></div>
      <div class="case-fact"><span>Year</span><strong>2026</strong></div>
      <div class="case-fact"><span>Models</span><strong>XGBoost · Random Forest · Naive Bayes</strong></div>
      <div class="case-fact"><span>Interpretability</span><strong>SHAP</strong></div>
      <div class="case-fact"><span>Data workflow</span><strong>Weather history · APIs · maps · satellite imagery</strong></div>
      <div class="case-fact"><span>Decision output</span><strong>Prioritized high-risk locations</strong></div>
    </aside>
  </section>

  <nav class="case-next"><span>Back to</span><a href="/projects/">Selected work →</a></nav>
</article>
