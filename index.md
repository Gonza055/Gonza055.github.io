---
layout: single
title: "Home"
permalink: /
---

<div class="home-hero home-hero--byu">
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

<div class="exp-item">
  <h3 class="exp-title">Maintenance Data Analyst Intern</h3>
  <p class="exp-meta">Compañía de Minas Buenaventura &middot; Peru &middot; 2025</p>
  <p>
    Processed and analyzed 50k+ high-noise industrial time-series from crushing and grinding systems.
    Built reproducible pipelines for smoothing, outlier handling, and signal reconstruction, and engineered
    reliability-focused features used for early-warning indicators and ML failure-mode prototyping.
    Structured 100+ assets under ISO&nbsp;14224/17359 to improve data consistency and traceability.
  </p>
</div>

<div class="exp-item">
  <h3 class="exp-title">Data Analytics Intern</h3>
  <p class="exp-meta">Hatch Ltd (Urban Solutions) &middot; USA &middot; 2024</p>
  <p>
    Developed C++ and Python automation utilities to parse and structure 200k+ rail-simulation records,
    reducing processing time by ~70%. Integrated rider-survey responses with onboard sensor logs to validate
    operational scenarios and analyze network performance for planning teams.
  </p>
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

If you’d like to discuss opportunities for **Spring or Summer 2026 internships**, ML systems work, or data-driven
engineering projects, you can reach me at:

- **Email:** gloayza5@byu.edu  
- **LinkedIn:** <a href="https://www.linkedin.com/in/gonzaloayza" target="_blank" rel="noopener">gonzaloayza</a>

---

<style>
/* BYU-STYLE PALETTE: navy + neutros */
:root {
  --home-border: #e5e7eb;
  --home-text-main: #111827;
  --home-text-muted: #6b7280;
  --home-accent: #002e5d;   /* BYU blue */
  --home-accent-soft: #1d4f91;
}

/* Hide automatic "Home" title */
.page__title {
  display: none;
}

/* HERO – academic, left-aligned, BYU colors */
.home-hero--byu {
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
  color: #374151;
  margin: 0 0 1.3rem 0;
}

.home-actions {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

/* Buttons – simple, BYU blue */
.btn {
  padding: 0.55rem 1.3rem;
  border-radius: 999px;
  font-size: 0.9rem;
  text-decoration: none;
  cursor: pointer;
  transition: background 0.15s ease, color 0.15s ease,
              border-color 0.15s ease;
}

.btn--outline {
  border: 1px solid var(--home-border);
  color: #111827;
  background: #ffffff;
}

.btn--outline:hover {
  border-color: #cbd5e1;
  background: #f9fafb;
}

.btn--solid {
  border: 1px solid var(--home-accent);
  background: var(--home-accent);
  color: #ffffff;
}

.btn--solid:hover {
  background: var(--home-accent-soft);
  border-color: var(--home-accent-soft);
}

/* Section headings */
.page__content h2 {
  margin-top: 2.3rem;
  margin-bottom: 0.9rem;
  font-size: 1.15rem;
  font-weight: 650;
  letter-spacing: -0.01em;
  color: var(--home-text-main);
}

/* Generic paragraphs */
.page__content p {
  font-size: 0.96rem;
  line-height: 1.6;
}

/* Lists */
.page__content ul {
  font-size: 0.95rem;
}

/* Columns – clean for Technical Focus only */
.three-column {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

/* EXPERIENCE – single-column list with left border */
.exp-item {
  border-left: 3px solid rgba(0, 46, 93, 0.5); /* BYU blue, soft */
  padding-left: 0.9rem;
  margin-bottom: 1.4rem;
}

.exp-item--single {
  border-left-color: rgba(148, 163, 184, 0.95);
}

.exp-title {
  margin: 0 0 0.1rem 0;
  font-size: 1.0rem;
  font-weight: 600;
}

.exp-meta {
  margin: 0 0 0.4rem 0;
  font-size: 0.85rem;
  color: var(--home-text-muted);
}

/* TECHNICAL FOCUS */
.focus-block h3 {
  margin-top: 0;
  margin-bottom: 0.3rem;
  font-size: 0.98rem;
  font-weight: 600;
}

.focus-block ul {
  margin: 0.1rem 0 0 1.1rem;
  padding: 0;
}

/* PROJECTS – academic list style */
.project-list {
  display: flex;
  flex-direction: column;
  gap: 1.4rem;
}

.project-item {
  padding-bottom: 0.9rem;
  border-bottom: 1px solid var(--home-border);
}

.project-item:last-child {
  border-bottom: none;
}

.project-title {
  margin: 0 0 0.25rem 0;
  font-size: 1.0rem;
  font-weight: 600;
}

.project-item p {
  margin: 0 0 0.3rem 0;
}

.project-link a {
  font-size: 0.9rem;
  color: var(--home-accent);
  text-decoration: none;
}

.project-link a:hover {
  text-decoration: underline;
}

/* MOBILE */
@media (max-width: 600px) {
  .home-hero--byu {
    padding: 1.6rem 0 1.9rem 0;
  }
  .home-name {
    font-size: 2.0rem;
  }
  .home-summary {
    font-size: 0.95rem;
  }
}
</style>
