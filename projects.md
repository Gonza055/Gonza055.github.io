---
layout: single
title: "Projects"
permalink: /projects/
---

<p class="projects-intro">
  A selection of projects that show how I work with data, build ML pipelines, and connect models to
  real-world decisions. This page is focused on end-to-end thinking rather than just model accuracy:
  how data is collected, cleaned, modeled, and evaluated.
</p>

---

## Featured Projects

<div class="project-block">

  <div class="project-block__header">
    <h3 class="project-block__title">Predictive Maintenance – Sensor Data Conditioning</h3>
    <p class="project-block__meta">2025 · Industrial Time-Series · Reliability Analytics</p>
  </div>

  <div class="project-block__body">
    <p>
      Preprocessing and feature-engineering pipeline for 50k+ high-noise industrial sensor time-series
      from crushing and grinding equipment. The goal was to turn raw vibration, load, and pressure signals
      into stable inputs for ML failure-mode models and early-warning indicators.
    </p>

    <ul class="project-block__list">
      <li><strong>Problem.</strong> Raw sensor feeds were noisy, inconsistent, and difficult to use directly for reliability analysis or ML models.</li>
      <li><strong>Data.</strong> 50k+ tagged time-series segments (multi-channel) plus equipment metadata and maintenance events.</li>
      <li><strong>Approach.</strong> Implemented smoothing, outlier handling, resampling, and basic signal reconstruction; engineered window-based reliability features (trend, volatility, envelope statistics).</li>
      <li><strong>Outcome.</strong> Delivered a reproducible preprocessing flow and feature set that fed into failure-mode prototyping and reliability dashboards.</li>
    </ul>
  </div>

  <!-- Placeholder figure – replace src with your actual diagram/image later -->
  <figure class="project-figure">
    <img src="/assets/images/projects/sensor-pipeline-placeholder.png"
         alt="Placeholder diagram of the sensor data conditioning pipeline" />
    <figcaption>Placeholder diagram – to be replaced with the actual pipeline figure.</figcaption>
  </figure>

</div>


<div class="project-block">

  <div class="project-block__header">
    <h3 class="project-block__title">TrainOps Simulation Data Optimization</h3>
    <p class="project-block__meta">2024 · C++ &amp; Python Tooling · Transportation Analytics</p>
  </div>

  <div class="project-block__body">
    <p>
      Data-engineering utilities for 200k+ rail-simulation records combining operational logs and
      passenger survey information. The main objective was to eliminate manual processing and make
      simulation outputs usable for planning and “what-if” analysis.
    </p>

    <ul class="project-block__list">
      <li><strong>Problem.</strong> Simulation outputs were large, fragmented text files that required manual cleaning before any analysis.</li>
      <li><strong>Data.</strong> 200k+ simulation records across multiple scenarios, plus structured survey responses from riders.</li>
      <li><strong>Approach.</strong> Built C++ and Python parsers to normalize schemas, validate fields, and produce analysis-ready tables; joined survey data to simulated trips.</li>
      <li><strong>Outcome.</strong> Cut processing time by ~70% and enabled analysts to run scenario comparisons directly from standardized datasets.</li>
    </ul>
  </div>

  <figure class="project-figure">
    <img src="/assets/images/projects/trainops-placeholder.png"
         alt="Placeholder visualization of TrainOps scenario comparison" />
    <figcaption>Placeholder visualization – future space for scenario plots or schema diagrams.</figcaption>
  </figure>

</div>


<div class="project-block">

  <div class="project-block__header">
    <h3 class="project-block__title">ML Failure-Mode Prototyping</h3>
    <p class="project-block__meta">2024–2025 · Baseline Models · Maintenance Scenarios</p>
  </div>

  <div class="project-block__body">
    <p>
      Early-stage ML exploration for detecting abnormal equipment behavior using engineered features from
      industrial time-series. The goal was not to ship a production model, but to map what signal was
      available for different types of failure modes.
    </p>

    <ul class="project-block__list">
      <li><strong>Problem.</strong> Understand how well simple models can separate “healthy” vs. degraded behavior under noisy conditions.</li>
      <li><strong>Data.</strong> Feature matrices derived from conditioned sensor signals, with labels from maintenance logs and domain expertise.</li>
      <li><strong>Approach.</strong> Compared baseline models (Random Forest, SVM, Gradient Boosting); used cross-validation and simple calibration checks to benchmark signal quality.</li>
      <li><strong>Outcome.</strong> Identified which feature families carried most signal and which modes required better instrumentation or labeling.</li>
    </ul>
  </div>

  <figure class="project-figure">
    <img src="/assets/images/projects/failure-mode-placeholder.png"
         alt="Placeholder ROC / feature-importance plots for failure-mode models" />
    <figcaption>Placeholder plots – intended for ROC curves, feature importance, or confusion matrices.</figcaption>
  </figure>

</div>


---

## Additional Work & Coursework

<ul class="project-small-list">
  <li>
    <strong>Course Projects (BYU CS &amp; ML).</strong>
    Implemented classical ML algorithms, data-structure libraries, and web applications as part of
    the Computer Science curriculum. Representative work includes search and optimization algorithms,
    clustering and classification, and data-centric web services.
  </li>
  <li>
    <strong>Analytics &amp; Visualization Exercises.</strong>
    Smaller notebooks focused on EDA, hypothesis testing, and communicating uncertainty using real-world datasets.
  </li>
</ul>

<p class="projects-note">
  Code repositories and notebooks for these projects will be linked here as they are cleaned up and published.
</p>

---

<style>
/* Reuse Stanford palette from Home for consistency */
:root {
  --proj-border: #e5e7eb;
  --proj-text-main: #111827;
  --proj-text-muted: #6b7280;
  --proj-accent: #8c1515;
}

/* Intro paragraph */
.projects-intro {
  max-width: 760px;
  font-size: 0.96rem;
  line-height: 1.6;
  color: #374151;
  margin-bottom: 1.6rem;
}

/* Project blocks */
.project-block {
  padding: 1.4rem 0 1.6rem 0;
  border-bottom: 1px solid var(--proj-border);
}

.project-block:last-of-type {
  border-bottom: none;
}

.project-block__header {
  margin-bottom: 0.4rem;
}

.project-block__title {
  margin: 0;
  font-size: 1.05rem;
  font-weight: 650;
  color: var(--proj-text-main);
}

.project-block__meta {
  margin: 0.15rem 0 0.6rem 0;
  font-size: 0.85rem;
  color: var(--proj-text-muted);
}

.project-block__body p {
  margin: 0 0 0.5rem 0;
  font-size: 0.95rem;
  line-height: 1.6;
}

.project-block__list {
  margin: 0.4rem 0 0 1.1rem;
  font-size: 0.93rem;
}

.project-block__list li {
  margin-bottom: 0.25rem;
}

/* Figures / images (placeholders for now) */
.project-figure {
  margin: 0.85rem 0 0 0;
  padding-left: 0.2rem;
}

.project-figure img {
  max-width: 100%;
  border-radius: 0.4rem;
  border: 1px solid var(--proj-border);
}

.project-figure figcaption {
  margin-top: 0.35rem;
  font-size: 0.8rem;
  color: var(--proj-text-muted);
}

/* Smaller projects / coursework */
.project-small-list {
  font-size: 0.94rem;
  line-height: 1.6;
}

.project-small-list li {
  margin-bottom: 0.4rem;
}

/* Note text */
.projects-note {
  margin-top: 0.8rem;
  font-size: 0.85rem;
  color: var(--proj-text-muted);
  font-style: italic;
}
</style>
