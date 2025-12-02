---
layout: single
title: "Home"
permalink: /
---

<div class="home-hero">
  <p class="home-kicker">Machine Learning &amp; Data Science Portfolio</p>
  <h1 class="home-name">Gonzalo Loayza</h1>
  <p class="home-tagline">
    Machine Learning Engineer &mdash; Data-Centric Modeling &amp; Applied Analytics
  </p>
  <p class="home-summary">
    I design and build data-centric ML systems, working with large datasets, time-series signals,
    and complex real-world problems. I enjoy turning messy data into clear, reliable pipelines that
    support modeling, experimentation, and intelligent decision-making.
  </p>
  <div class="home-actions">
    <a class="btn btn--primary" href="/projects/">View Projects</a>
    <a class="btn" href="/resume/">Resume</a>
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
/* PALETTE – Apple-style, soft and minimal */
:root {
  --home-bg-band: #f9fafb;
  --home-border: #e5e7eb;
  --home-text-main: #020617;
  --home-text-muted: #6b7280;
  --home-accent: #4f46e5;  /* soft indigo */
}

/* Hide automatic "Home" title from Minimal Mistakes */
.page__title {
  display: none;
}

/* SECTION HEADINGS WITH SMALL DOT */
.page__content h2 {
  position: relative;
  margin-top: 2.4rem;
  margin-bottom: 1rem;
  padding-left: 1.1rem;
  font-weight: 650;
  letter-spacing: -0.01em;
}

.page__content h2::before {
  content: "";
  position: absolute;
  left: 0;
  top: 0.9em;
  width: 0.45rem;
  height: 0.45rem;
  border-radius: 999px;
  background: var(--home-accent);
  box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.12);
  transform: translateY(-50%);
}

/* HERO – clean Apple-like band */
.home-hero {
  text-align: center;
  padding: 3rem 1.5rem 2.6rem;
  margin: 0 -1.5rem 2.5rem -1.5rem;
  background:
    radial-gradient(circle at top left, rgba(79, 70, 229, 0.12), transparent 55%),
    linear-gradient(180deg, #ffffff 0%, var(--home-bg-band) 100%);
  border-bottom: 1px solid var(--home-border);
}

.home-kicker {
  text-transform: uppercase;
  letter-spacing: 0.14em;
  font-size: 0.78rem;
  font-weight: 600;
  color: var(--home-text-muted);
  margin-bottom: 0.55rem;
}

.home-name {
  font-size: 3.1rem;
  margin: 0.1rem 0 0.4rem 0;
  font-weight: 750;
  letter-spacing: -0.03em;
  color: var(--home-text-main);
}

.home-tagline,
.home-summary {
  max-width: 650px;
  margin-left: auto;
  margin-right: auto;
}

.home-tagline {
  font-size: 1.06rem;
  color: #4b5563;
  margin-bottom: 0.85rem;
  font-weight: 500;
}

.home-summary {
  color: #374151;
  font-size: 1.02rem;
  line-height: 1.55;
  margin-bottom: 1.6rem;
}

/* HERO BUTTONS */
.home-actions .btn {
  display: inline-block;
  margin: 0.25rem 0.45rem;
}

.btn {
  padding: 0.62rem 1.5rem;
  border-radius: 999px;
  border: 1px solid #d4d4f0;
  font-size: 0.9rem;
  text-decoration: none;
  transition: background 0.15s ease, color 0.15s ease,
              box-shadow 0.15s ease, transform 0.15s ease,
              border-color 0.15s ease;
}

.btn--primary {
  background: var(--home-accent);
  border-color: var(--home-accent);
  color: #ffffff !important;
}

.btn--primary:hover {
  box-shadow: 0 12px 28px rgba(79, 70, 229, 0.35);
  transform: translateY(-1px);
}

.btn:hover {
  background: #eef2ff;
  border-color: #c7d2fe;
}

/* LAYOUT – editorial columns, no cards */
.two-column {
  display: grid;
  gap: 1.8rem;
}

.two-column--stack {
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
}

.three-column {
  display: grid;
  gap: 1.5rem;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

/* EXPERIENCE */
.exp-item {
  border-left: 3px solid rgba(79, 70, 229, 0.35);
  padding-left: 1rem;
}

.exp-item--single {
  margin-top: 1.5rem;
  border-left-color: rgba(148, 163, 184, 0.8);
}

.exp-title {
  margin: 0 0 0.1rem 0;
  font-size: 1.02rem;
  font-weight: 600;
}

.exp-meta {
  margin: 0 0 0.35rem 0;
  font-size: 0.86rem;
  color: var(--home-text-muted);
}

.exp-item p {
  font-size: 0.94rem;
  line-height: 1.55;
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
  font-size: 0.93rem;
}

/* PROJECTS – editorial style, no boxes */
.project-list {
  display: flex;
  flex-direction: column;
  gap: 1.6rem;
}

.project-item {
  padding-bottom: 1.1rem;
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
  font-size: 0.94rem;
  line-height: 1.55;
  margin: 0 0 0.35rem 0;
}

.project-link a {
  font-size: 0.9rem;
  color: var(--home-accent);
  text-decoration: none;
  border-bottom: 1px solid transparent;
}

.project-link a:hover {
  border-color: var(--home-accent);
}

/* MOBILE */
@media (max-width: 600px) {
  .home-name {
    font-size: 2.4rem;
  }
  .home-summary {
    font-size: 0.97rem;
  }
  .home-hero {
    margin: 0 -1rem 2rem -1rem;
    padding: 2.6rem 1.1rem 2.2rem;
  }
}
</style>
