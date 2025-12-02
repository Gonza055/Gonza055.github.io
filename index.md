---
layout: single
title: "Home"
permalink: /
---

<div class="home-hero">
  <p class="home-kicker">Machine Learning &amp; Data Science Portfolio</p>
  <h1 class="home-name">Gonzalo Loayza</h1>
  <p class="home-tagline">
    Machine Learning Engineer &mdash; Industrial Time-Series &amp; Predictive Analytics
  </p>
  <p class="home-summary">
    I build ML systems that make sense of noisy industrial sensor data and simulation outputs,
    turning raw signals into reliable, decision-ready pipelines for maintenance, operations,
    and real-world engineering challenges.
  </p>
  <div class="home-actions">
    <a class="btn btn--primary" href="/projects/">View Projects</a>
    <a class="btn" href="/resume/">Resume</a>
    <a class="btn" href="https://github.com/Gonza2055" target="_blank" rel="noopener">GitHub</a>
  </div>
</div>

---

## About

I'm a senior Computer Science student at Brigham Young University (BYU) specializing in machine learning for industrial and engineering applications.  
My work focuses on designing **data-centric ML pipelines** for large-scale time-series, simulation outputs, and operational datasets found in mining, rail systems, and heavy industry.

I work at the intersection of **predictive maintenance**, **reliability analytics**, and **software engineering**, building reproducible workflows that transform complex datasets into structured insights.  
I care about clarity, robustness, and engineering precision in every stage of the ML lifecycle.

---

## Experience

<div class="home-grid home-grid--two">

<div class="home-card">
<h3>Maintenance Data Analyst Intern<br/><span class="home-card-sub">Compañía de Minas Buenaventura &middot; 2025</span></h3>
<p>
Processed and analyzed 50k+ high-noise industrial sensor time-series from crushing and grinding systems. Built
reproducible pipelines for smoothing, outlier capping, and signal reconstruction, and engineered reliability-focused
features used for early-warning indicators and predictive-maintenance prototyping. Structured 100+ assets under
ISO&nbsp;14224/17359 to improve traceability and maintenance workflows.
</p>
<p class="home-card-meta">
Industrial time-series &bull; Predictive maintenance &bull; Reliability feature engineering
</p>
</div>

<div class="home-card">
<h3>Data Analytics Intern<br/><span class="home-card-sub">Hatch Ltd (Urban Solutions, USA) &middot; 2024</span></h3>
<p>
Developed C++ and Python automation utilities to parse and structure 200k+ rail-simulation records, reducing
processing time by ~70%. Integrated rider-survey responses with onboard sensor logs to validate operational scenarios
and analyze network performance for planning teams.
</p>
<p class="home-card-meta">
Simulation data processing &bull; Workflow automation &bull; Scenario analytics
</p>
</div>

<div class="home-card">
<h3>Honors Thesis Researcher<br/><span class="home-card-sub">BYU Honors Program &middot; 2025–2026</span></h3>
<p>
Designing an unsupervised-learning framework to discover operating modes in mineral-processing circuits using
clustering, dimensionality reduction, and statistical validation. The project supports reliability monitoring and
detection of suboptimal operating states in real industrial environments.
</p>
<p class="home-card-meta">
Unsupervised ML &bull; Dimensionality reduction &bull; Mineral-processing analytics
</p>
</div>

</div>

---

## Technical Focus

<div class="home-grid home-grid--three">

<div class="home-card">
<h3>Machine Learning &amp; Data</h3>
<ul>
  <li>Time-series modeling and anomaly detection</li>
  <li>Predictive-maintenance workflows</li>
  <li>Reliability feature engineering (deltas, ratios, transients)</li>
  <li>Noise reduction, smoothing, reconstruction</li>
  <li>Model evaluation and statistical validation</li>
</ul>
</div>

<div class="home-card">
<h3>Software Engineering</h3>
<ul>
  <li>Python, C++, SQL, JavaScript</li>
  <li>Large-scale data wrangling and automation</li>
  <li>Clean, reproducible workflow design</li>
  <li>Jupyter, Git, Linux</li>
</ul>
</div>

<div class="home-card">
<h3>Domains</h3>
<ul>
  <li>Industrial sensor data (vibration, load, pressure, temperature)</li>
  <li>Rail-simulation outputs and operational logs</li>
  <li>Mining, reliability engineering, and heavy-industry analytics</li>
</ul>
</div>

</div>

---

## Selected Projects

<div class="home-grid home-grid--three">

<div class="home-card">
<h3>Predictive Maintenance &mdash; Sensor Data Conditioning (2025)</h3>
<p>
Built end-to-end preprocessing workflows for 50k+ industrial time-series, implementing noise reduction, outlier
handling, and signal reconstruction. Created reliability-focused feature sets for downstream ML failure prediction
and maintenance analytics.
</p>
<p class="home-card-meta">
<a href="/projects/">See more details →</a>
</p>
</div>

<div class="home-card">
<h3>TrainOps Simulation Data Optimization (2024)</h3>
<p>
Developed C++ and Python tooling to structure 200k+ simulation records, cutting manual processing time by ~70%.
Merged sensor data with rider-survey logs to validate scenario fidelity and improve planning insights.
</p>
<p class="home-card-meta">
<a href="/projects/">See more details →</a>
</p>
</div>

<div class="home-card">
<h3>ML Failure-Mode Prototyping (2024–2025)</h3>
<p>
Exploratory ML pipeline inspired by industrial maintenance settings, including EDA, feature engineering, and baseline
models (Random Forest, SVM, Gradient Boosting) to detect early abnormal behavior in equipment.
</p>
<p class="home-card-meta">
<a href="/projects/">See more details →</a>
</p>
</div>

</div>

---

## Contact

If you’d like to talk about internships, ML systems, or industrial data projects, you can reach me via:

- **Email:** gloayza5@byu.edu  
- **GitHub:** <a href="https://github.com/Gonza2055" target="_blank" rel="noopener">Gonza2055</a>  
- **LinkedIn:** (add your LinkedIn URL)

---

<style>
/* Hide the automatic "Home" title that Minimal Mistakes prints */
.page__title {
  display: none;
}

/* HERO */
.home-hero {
  text-align: center;
  padding: 3.25rem 1.5rem 2.75rem;
  border-radius: 1rem;
  background: linear-gradient(135deg, #f5f7fb 0%, #e7f0ff 100%);
  margin: 0 auto 2.75rem auto;
  max-width: 960px;
  box-shadow: 0 16px 40px rgba(15, 23, 42, 0.06);
}

.home-kicker {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.8rem;
  font-weight: 600;
  color: #6c7a89;
  margin-bottom: 0.4rem;
}

.home-name {
  font-size: 2.8rem;
  margin: 0.1rem 0;
  font-weight: 700;
}

.home-tagline {
  font-size: 1.1rem;
  color: #505967;
  margin-bottom: 0.9rem;
}

.home-summary {
  max-width: 720px;
  margin: 0 auto 1.7rem auto;
  color: #414856;
  font-size: 1rem;
  line-height: 1.6;
}

.home-actions .btn {
  display: inline-block;
  margin: 0.25rem 0.45rem;
}

/* Buttons */
.btn {
  padding: 0.6rem 1.4rem;
  border-radius: 999px;
  border: 1px solid #d0d4e4;
  font-size: 0.9rem;
  text-decoration: none;
}

.btn--primary {
  background: #3273dc;
  border-color: #3273dc;
  color: #fff !important;
}

/* GRID & CARDS */
.home-grid {
  display: grid;
  gap: 1.6rem;
  margin: 1.2rem 0 0 0;
}

.home-grid--three {
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
}

.home-grid--two {
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

.home-card {
  border-radius: 0.85rem;
  border: 1px solid #e2e6f0;
  padding: 1.3rem 1.4rem;
  background: #ffffff;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.04);
}

.home-card h3 {
  margin-top: 0;
  margin-bottom: 0.45rem;
  font-size: 1.06rem;
}

.home-card-sub {
  font-weight: 400;
  font-size: 0.86rem;
  color: #6c7a89;
}

.home-card p {
  margin-bottom: 0.55rem;
  font-size: 0.9rem;
  line-height: 1.55;
}

.home-card ul {
  margin: 0.4rem 0 0.6rem 1.1rem;
  font-size: 0.9rem;
}

.home-card-meta {
  font-size: 0.84rem;
  color: #6c7a89;
}

/* Mobile tweaks */
@media (max-width: 600px) {
  .home-name {
    font-size: 2.2rem;
  }
  .home-summary {
    font-size: 0.95rem;
  }
}
</style>
