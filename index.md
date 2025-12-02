---
layout: single
title: "Home"
permalink: /
---

<div class="home-hero">
  <p class="home-kicker">Machine Learning &amp; Data Science Portfolio</p>
  <h1 class="home-name">Gonzalo Loayza</h1>
  <p class="home-tagline">
    B.S. Computer Science @ BYU &bull; Machine Learning &amp; Predictive Analytics
  </p>
  <p class="home-summary">
    I build machine learning pipelines for noisy industrial time-series, simulations, and operational datasets,
    focusing on predictive maintenance, reliability analytics, and data-driven decision support for real-world engineering problems.
  </p>
  <div class="home-actions">
    <a class="btn btn--primary" href="/projects/">View Projects</a>
    <a class="btn" href="/resume/">Resume</a>
    <a class="btn" href="https://github.com/Gonza2055" target="_blank" rel="noopener">GitHub</a>
  </div>
</div>

---

## About

I'm a senior Computer Science student at Brigham Young University (BYU) with a focus on Machine Learning and data-driven engineering.  
Most of my work sits at the intersection of **time-series analysis**, **predictive maintenance**, and **software engineering** for industrial operations.

I enjoy turning noisy, complex datasets into clean, reliable pipelines that support real-world decisions in maintenance, reliability, and operations.

---

## Technical Focus

<div class="home-grid home-grid--three">

<div class="home-card">
<h3>Machine Learning &amp; Data</h3>
<ul>
  <li>Time-series modeling &amp; anomaly detection</li>
  <li>Predictive maintenance pipelines</li>
  <li>Feature engineering for reliability &amp; maintenance</li>
  <li>Model evaluation and statistical validation</li>
</ul>
</div>

<div class="home-card">
<h3>Software Engineering</h3>
<ul>
  <li>Python, C++, SQL, JavaScript</li>
  <li>Large-scale data wrangling &amp; automation</li>
  <li>Jupyter, Git, Linux</li>
  <li>Power BI, basic AWS/Azure</li>
</ul>
</div>

<div class="home-card">
<h3>Domain Experience</h3>
<ul>
  <li>Industrial sensor data (vibration, load, pressure, temperature)</li>
  <li>Simulation outputs &amp; operations logs</li>
  <li>Predictive maintenance &amp; reliability analytics</li>
  <li>Mining, rail systems, and industrial operations</li>
</ul>
</div>

</div>

---

## Experience

<div class="home-grid home-grid--two">

<div class="home-card">
<h3>Maintenance Data Analyst Intern<br/><span class="home-card-sub">Compañía de Minas Buenaventura &middot; 2025</span></h3>
<p>
Worked with 50k+ high-noise industrial sensor time-series from crushing and grinding systems, building preprocessing
pipelines for smoothing, outlier capping, and signal reconstruction. Performed EDA on equipment behavior and ore-type
patterns, and engineered 15+ reliability-focused features (load ratios, temperature deltas, transient-spike metrics)
to support condition-based maintenance and early-warning indicators.
</p>
<p class="home-card-meta">
Industrial time-series &bull; Predictive maintenance &bull; Reliability feature engineering
</p>
</div>

<div class="home-card">
<h3>Data Analytics Intern<br/><span class="home-card-sub">Hatch Ltd (Urban Solutions) &middot; 2024</span></h3>
<p>
Developed C++ and Python utilities to parse and structure 200k+ TrainOps rail-simulation records, reducing manual
processing time by ~70%. Integrated rider-survey responses with onboard sensor logs to validate operating scenarios,
and provided analysis used by planning teams to compare service configurations and network performance.
</p>
<p class="home-card-meta">
Simulation data processing &bull; Workflow automation &bull; Scenario analytics
</p>
</div>

<div class="home-card">
<h3>Honors Thesis Student Researcher<br/><span class="home-card-sub">BYU Honors Program &middot; 2025–2026</span></h3>
<p>
Designing an unsupervised-learning framework to discover operating modes in mineral-processing circuits. Combines
clustering, dimensionality reduction (e.g., UMAP/PCA), and statistical validation on real plant datasets to support
performance monitoring and early detection of suboptimal operating states.
</p>
<p class="home-card-meta">
Unsupervised ML &bull; Dimensionality reduction &bull; Mineral processing analytics
</p>
</div>

</div>

---

## Selected Projects

<div class="home-grid home-grid--three">

<div class="home-card">
<h3>Predictive Maintenance – Sensor Data Conditioning (2025)</h3>
<p>
Built reproducible preprocessing workflows for 50k+ high-noise industrial sensor time-series
(noise reduction, outlier capping, reconstruction) and engineered reliability-focused
features for downstream ML failure prediction and maintenance analytics.
</p>
<p class="home-card-meta">
<a href="/projects/">See more details →</a>
</p>
</div>

<div class="home-card">
<h3>TrainOps Simulation Data Optimization (2024)</h3>
<p>
Developed C++/Python utilities to parse and structure 200k+ rail-simulation records,
cutting manual processing time by ~70% and integrating survey data with sensor logs
to validate operating scenarios and network performance.
</p>
<p class="home-card-meta">
<a href="/projects/">See more details →</a>
</p>
</div>

<div class="home-card">
<h3>ML Failure-Mode Prototyping (2024–25)</h3>
<p>
Designed an academic ML pipeline inspired by industrial settings, including EDA, noise reduction,
feature engineering, and exploratory labeling of time-series. Benchmarked baseline models
(Random Forest, SVM, Gradient Boosting) for early detection of abnormal equipment behavior.
</p>
<p class="home-card-meta">
<a href="/projects/">See more details →</a>
</p>
</div>

</div>

---

## Contact

If you'd like to talk about internships, ML projects, or data-driven maintenance work,  
you can reach me via:

- **Email:** gloayza5@byu.edu  
- **GitHub:** <a href="https://github.com/Gonza2055" target="_blank" rel="noopener">Gonza2055</a>  
- **LinkedIn:** (add your LinkedIn URL)

---

<style>
/* Hide the small automatic "Home" title that Minimal Mistakes prints */
.page__title {
  display: none;
}

/* Layout */
.home-hero {
  text-align: center;
  padding: 3rem 1.5rem 2.5rem;
  border-radius: 0.9rem;
  background: linear-gradient(135deg, #f5f7fb 0%, #e7f0ff 100%);
  margin: 0 auto 2.75rem auto;
  max-width: 960px; /* keeps the hero nicely centered */
}

.home-kicker {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.8rem;
  font-weight: 600;
  color: #6c7a89;
  margin-bottom: 0.35rem;
}

.home-name {
  font-size: 2.8rem;
  margin: 0.1rem 0;
  font-weight: 700;
}

.home-tagline {
  font-size: 1.1rem;
  color: #555;
  margin-bottom: 0.8rem;
}

.home-summary {
  max-width: 720px;
  margin: 0 auto 1.6rem auto;
  color: #444;
  font-size: 1rem;
}

.home-actions .btn {
  display: inline-block;
  margin: 0.25rem 0.4rem;
}

/* Buttons */
.btn {
  padding: 0.55rem 1.3rem;
  border-radius: 999px;
  border: 1px solid #d0d4e4;
  font-size: 0.9rem;
}

.btn--primary {
  background: #3273dc;
  border-color: #3273dc;
  color: #fff !important;
}

/* Cards & grid */
.home-grid {
  display: grid;
  gap: 1.5rem;
  margin: 1rem 0 0 0;
}

.home-grid--three {
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}

.home-grid--two {
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

.home-card {
  border-radius: 0.75rem;
  border: 1px solid #e2e6f0;
  padding: 1.25rem 1.3rem;
  background: #fff;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
}

.home-card h3 {
  margin-top: 0;
  margin-bottom: 0.35rem;
  font-size: 1.05rem;
}

.home-card-sub {
  font-weight: 400;
  font-size: 0.85rem;
  color: #6c7a89;
}

.home-card p {
  margin-bottom: 0.5rem;
  font-size: 0.9rem;
}

.home-card ul {
  margin: 0.35rem 0 0.5rem 1.1rem;
  font-size: 0.9rem;
}

.home-card-meta {
  font-size: 0.85rem;
  color: #6c7a89;
}

/* Mobile tweaks */
@media (max-width: 600px) {
  .home-name {
    font-size: 2.1rem;
  }
  .home-summary {
    font-size: 0.95rem;
  }
}
</style>
