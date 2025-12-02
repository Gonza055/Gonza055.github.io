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

<div class="home-card home-card--experience">
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

<div class="home-card home-card--experience">
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

<div class="home-card home-card--experience">
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

<div class="home-card home-card--focus">
<h3>Machine Learning &amp; Data</h3>
<ul>
  <li>Time-series modeling and anomaly detection</li>
  <li>Predictive-maintenance workflows</li>
  <li>Reliability feature engineering (deltas, ratios, transients)</li>
  <li>Noise reduction, smoothing, reconstruction</li>
  <li>Model evaluation and statistical validation</li>
</ul>
</div>

<div class="home-card home-card--focus">
<h3>Software Engineering</h3>
<ul>
  <li>Python, C++, SQL, JavaScript</li>
  <li>Large-scale data wrangling and automation</li>
  <li>Clean, reproducible workflow design</li>
  <li>Jupyter, Git, Linux</li>
</ul>
</div>

<div class="home-card home-card--focus">
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

<div class="home-card home-card--project">
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

<div class="home-card home-card--project">
<h3>TrainOps Simulation Data Optimization (2024)</h3>
<p>
Developed C++ and Python tooling to structure 200k+ simulation records, cutting manual processing time by ~70%.
Merged sensor data with rider-survey logs to validate scenario fidelity and improve planning insights.
</p>
<p class="home-card-meta">
<a href="/projects/">See more details →</a>
</p>
</div>

<div class="home-card home-card--project">
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
/* COLOR SYSTEM */
:root {
  --home-bg-soft: #f5f7fb;
  --home-bg-soft-strong: #e7f0ff;
  --home-border: #e2e6f0;
  --home-border-strong: #c5d0ea;
  --home-text-main: #1f2933;
  --home-text-muted: #6c7a89;
  --home-accent: #3273dc;
  --home-accent-soft: rgba(50, 115, 220, 0.08);
  --home-shadow-soft: 0 16px 40px rgba(15, 23, 42, 0.06);
  --home-shadow-card: 0 8px 20px rgba(15, 23, 42, 0.05);
  --home-radius-lg: 1rem;
  --home-radius-md: 0.85rem;
}

/* Hide the automatic "Home" title that Minimal Mistakes prints */
.page__title {
  display: none;
}

/* SECTION SPACING */
.page__content h2 {
  margin-top: 2.5rem;
  margin-bottom: 0.75rem;
}

/* HERO */
.home-hero {
  text-align: center;
  padding: 3.25rem 1.5rem 2.75rem;
  border-radius: var(--home-radius-lg);
  background:
    radial-gradient(circle at top left, rgba(50, 115, 220, 0.18), transparent 55%),
    linear-gradient(135deg, var(--home-bg-soft) 0%, var(--home-bg-soft-strong) 100%);
  margin: 0 auto 2.75rem auto;
  max-width: 960px;
  box-shadow: var(--home-shadow-soft);
  color: var(--home-text-main);
}

.home-kicker {
  text-transform: uppercase;
  letter-spacing: 0.12em;
  font-size: 0.8rem;
  font-weight: 600;
  color: var(--home-text-muted);
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
  transition: background 0.18s ease, color 0.18s ease, box-shadow 0.18s ease, transform 0.18s ease;
}

.btn--primary {
  background: var(--home-accent);
  border-color: var(--home-accent);
  color: #fff !important;
}

.btn--primary:hover {
  box-shadow: 0 8px 18px rgba(50, 115, 220, 0.35);
  transform: translateY(-1px);
}

.btn:hover {
  background: #f7f8fc;
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
  position: relative;
  border-radius: var(--home-radius-md);
  border: 1px solid var(--home-border);
  padding: 1.3rem 1.4rem;
  background: #ffffff;
  box-shadow: var(--home-shadow-card);
  overflow: hidden;
  transition: transform 0.18s ease, box-shadow 0.18s ease, border-color 0.18s ease, background 0.18s ease;
}

.home-card::before {
  content: "";
  position: absolute;
  inset: 0;
  opacity: 0;
  pointer-events: none;
  transition: opacity 0.18s ease;
}

.home-card h3 {
  margin-top: 0;
  margin-bottom: 0.45rem;
  font-size: 1.06rem;
}

.home-card-sub {
  font-weight: 400;
  font-size: 0.86rem;
  color: var(--home-text-muted);
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
  color: var(--home-text-muted);
}

/* Card variants */
.home-card--experience {
  border-top: 3px solid var(--home-accent);
  background: linear-gradient(135deg, #ffffff 0%, #f6f8ff 100%);
}

.home-card--experience::before {
  background: radial-gradient(circle at top left, var(--home-accent-soft), transparent 60%);
}

.home-card--focus {
  border-top: 3px solid var(--home-border-strong);
  background: linear-gradient(135deg, #ffffff 0%, #f9fbff 100%);
}

.home-card--focus::before {
  background: radial-gradient(circle at top left, rgba(148, 163, 184, 0.15), transparent 60%);
}

.home-card--project {
  border-top: 3px solid #10b981;
  background: linear-gradient(135deg, #ffffff 0%, #f4fdf9 100%);
}

.home-card--project::before {
  background: radial-gradient(circle at top left, rgba(16, 185, 129, 0.12), transparent 60%);
}

/* Hover effects */
.home-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 14px 30px rgba(15, 23, 42, 0.10);
  border-color: var(--home-border-strong);
}

.home-card:hover::before {
  opacity: 1;
}

/* Links inside cards */
.home-card a {
  text-decoration: none;
  border-bottom: 1px solid transparent;
  transition: border-color 0.18s ease, color 0.18s ease;
}

.home-card a:hover {
  border-color: currentColor;
}

/* Mobile tweaks */
@media (max-width: 600px) {
  .home-name {
    font-size: 2.2rem;
  }
  .home-summary {
    font-size: 0.95rem;
  }
  .home-hero {
    padding: 2.6rem 1.25rem 2.3rem;
    border-radius: 0.9rem;
  }
}
</style>
