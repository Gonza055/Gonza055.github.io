---
layout: single
title: "Home"
permalink: /
---

<div class="home-hero home-hero--stanford">
  <p class="home-label">Gonzalo Loayza</p>
  <h1 class="home-name">Machine Learning Engineer</h1>
  <p class="home-tagline">
    Data-Centric Modeling &amp; Applied Analytics
  </p>
  <p class="home-summary">
    I design and build data-centric ML systems, working with large datasets, time-series signals,
    and complex real-world problems. I enjoy turning messy data into clear, reliable pipelines that
    support modeling, experimentation, and intelligent decision-making.
  </p>
  <div class="home-actions">
    <a class="btn btn--outline" href="/projects/">View Projects</a>
    <a class="btn btn--solid" href="/resume/">Resume</a>
  </div>
</div>

---

## About

I'm a senior Computer Science student at Brigham Young University (BYU) focusing on applied machine learning,
large datasets, and data-centric modeling.  
My work centers on designing end-to-end ML workflows that connect clean data pipelines with robust models and
clear evaluation.

I enjoy working on problems where data is messy, structure is not obvious, and good engineering makes the
difference between a one-off notebook and a reliable system.

---

## Experience

<div class="two-column two-column--stack">

  <div class="exp-item">
    <h3 class="exp-title">Maintenance Data Analyst Intern</h3>
    <p class="exp-meta">Compañía de Minas Buenaventura &middot; 2025</p>
    <p>
      Processed and analyzed 50k+ high-noise industrial time-series from crushing and grinding systems.
      Built reproducible pipelines for smoothing, outlier handling, and signal reconstruction, and engineered
      reliability-focused features used for early-warning indicators and ML failure-mode prototyping.
      Structured 100+ assets under ISO&nbsp;14224/17359 to improve data consistency and traceability.
    </p>
  </div>

  <div class="exp-item">
    <h3 class="exp-title">Data Analytics Intern</h3>
    <p class="exp-meta">Hatch Ltd (Urban Solutions, USA) &middot; 2024</p>
    <p>
      Developed C++ and Python automation utilities to parse and structure 200k+ rail-simulation records,
      reducing processing time by ~70%. Integrated rider-survey responses with onboard sensor logs to validate
      operational scenarios and analyze network performance for planning teams.
    </p>
  </div>

</div>

<div class="exp-item exp-item--single">
  <h3 class="exp-title">Honors Thesis Researcher</h3>
  <p class="exp-meta">BYU Honors Program &middot; 2025–2026</p>
  <p>
    Designing an unsupervised-learning framework to discover operating modes in mineral-processing circuits
    using clustering, dimensionality reduction, and statistical validation. The project supports monitoring and
    early detection of suboptimal operating states in real industrial environments.
  </p>
</div>

---

## Technical Focus

<div class="three-column">

  <div class="focus-block">
    <h3>Machine Learning</h3>
    <ul>
      <li>Modeling and evaluation (classification, regression)</li>
      <li>Time-series and sequential data</li>
      <li>Representation and feature engineering</li>
      <li>Model validation and monitoring</li>
    </ul>
  </div>

  <div class="focus-block">
    <h3>Software &amp; Tools</h3>
    <ul>
      <li>Python, C++, SQL, JavaScript</li>
      <li>NumPy, Pandas, scikit-learn</li>
      <li>Jupyter, Git, Linux</li>
    </ul>
  </div>

  <div class="focus-block">
    <h3>Data &amp; Systems</h3>
    <ul>
      <li>Data pipelines and automation</li>
      <li>Large-scale datasets and experimentation</li>
      <li>Simulation and analytics workflows</li>
      <li>Reproducible research and documentation</li>
    </ul>
  </div>

</div>

---

## Selected Projects

<div class="project-list">

  <div class="project-item">
    <h3 class="project-title">Sensor Data Conditioning for ML (2025)</h3>
    <p>
      Built end-to-end preprocessing workflows for 50k+ industrial time-series, implementing noise reduction,
      outlier handling, and signal reconstruction. Created reliability-focused feature sets for downstream
      modeling and failure-mode analysis.
    </p>
    <p class="project-link"><a href="/projects/">See more details →</a></p>
  </div>

  <div class="project-item">
    <h3 class="project-title">TrainOps Simulation Data Optimization (2024)</h3>
    <p>
      Developed C++ and Python tooling to structure 200k+ simulation records, cutting manual processing time
      by ~70%. Merged sensor data with rider-survey logs to validate scenario fidelity and improve planning
      insights.
    </p>
    <p class="project-link"><a href="/projects/">See more details →</a></p>
  </div>

  <div class="project-item">
    <h3 class="project-title">ML Failure-Mode Prototyping (2024–2025)</h3>
    <p>
      Exploratory ML pipeline inspired by industrial maintenance settings, including EDA, feature engineering,
      and baseline models (Random Forest, SVM, Gradient Boosting) to detect early abnormal behavior in equipment.
    </p>
    <p class="project-link"><a href="/projects/">See more details →</a></p>
  </div>

</div>

---

## Contact

If you’d like to talk about internships, ML systems, or data-driven projects, you can reach me via:

- **Email:** gloayza5@byu.edu  
- **LinkedIn:** (add your LinkedIn URL)

---

<style>
/* STANFORD-STYLE PALETTE: muy sobrio */
:root {
  --home-border: #e5e7eb;
  --home-text-main: #111827;
  --home-text-muted: #6b7280;
  --home-accent: #8c1515; /* Stanford cardinal */
}

/* Ocultar título automático "Home" */
.page__title {
  display: none;
}

/* HERO – layout académico, alineado izquierda */
.home-hero--stanford {
  max-width: 760px;
  margin: 0 auto 2.5rem auto;
  padding: 1.8rem 0 2rem 0;
  border-bottom: 1px solid var(--home-border);
  display: flex;
  flex-direction: column;
}

.home-label {
  text-transform: uppercase;
  letter-spacing: 0.16em;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--home-accent);
  margin: 0 0 0.35rem 0;
}

.home-name {
  font-size: 2.3rem;
  margin: 0 0 0.2rem 0;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--home-text-main);
}

.home-tagline {
  font-size: 1.0rem;
  color: var(--home-text-muted);
  margin: 0 0 0.9rem 0;
}

.home-summary {
  max-width: 720px;
  font-size: 0.98rem;
  line-height: 1.6;
