---
layout: single
title: "Projects"
permalink: /projects/
---

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

<div class="projects-page">

  <div class="projects-hero">
    <p class="projects-label">Gonzalo Loayza · Portfolio</p>
    <h1 class="projects-title">Selected Projects</h1>
    <p class="projects-tagline">
      Data science and ML projects with a focus on industrial analytics, reliability, and decision support.
    </p>
  </div>

  <p class="projects-intro">
    These projects highlight how I approach noisy, real-world data: from exploratory analysis and cleaning
    to feature engineering and early-stage modeling. The emphasis is on understanding the system and making
    the results actionable for engineers and operators.
  </p>

---

## Featured Projects

<div class="project-block">

  <div class="project-block__header">
    <h3 class="project-block__title">Liner Wear &amp; EDA – Ball Mill at Buenaventura</h3>
    <p class="project-block__meta">2025 · Maintenance Data Analyst Intern · Peru</p>
  </div>

  <div class="project-block__body">
    <p>
      Exploratory analysis of ball-mill liner performance for a polymetallic operation at
      Compañía de Minas Buenaventura. The study quantified wear behaviour, compared liner suppliers,
      and identified the most predictive process variables for future monitoring and ML models.
    </p>

    <ul class="project-block__list">
      <li><strong>Executive summary.</strong> Global linear wear rate ≈ 0.008 mm/kt.
        Vulco: higher throughput but faster wear (~0.010 mm/kt).
        Hofmann: lower throughput but higher durability (~0.006 mm/kt).</li>

      <li><strong>Key correlations.</strong> Thickness vs cumulative tonnage r ≈ −0.63 (global) and
        r ≈ −0.8 (Vulco), confirming “more production → more wear”. MAT 2 vs thickness r ≈ −0.81,
        meaning higher temperature aligns with lower thickness.</li>

      <li><strong>Data cleaning.</strong> Removed nonphysical outliers such as recorded temperatures
        around 6528 °C that would distort any predictive model.</li>

      <li><strong>Operational strategy.</strong> Results supported an alternation plan over four campaigns
        (Vulco–Hofmann–Vulco–Hofmann) to balance throughput, wear rate, and liner cost.</li>

      <li><strong>Next steps.</strong> Thickness, cumulative tonnage, and MAT 2 were highlighted as key
        predictors for future ML-based condition monitoring and dashboards.</li>
    </ul>
  </div>

  <figure class="project-figure project-figure--grid">
    <div class="project-figure-grid">
      <div class="project-figure-grid-item">
        <img src="/assets/images/projects/EDA1.png"
             alt="Liner wear vs cumulative tonnage analysis" />
      </div>
      <div class="project-figure-grid-item">
        <img src="/assets/images/projects/EDA2.png"
             alt="Correlation heatmap for liner wear variables" />
      </div>
      <div class="project-figure-grid-item">
        <img src="/assets/images/projects/EDA4.png"
             alt="Silo and grinding plant construction context" />
      </div>
    </div>
    <figcaption>
      Key EDA outputs and plant context for the Buenaventura ball mill study.
    </figcaption>
  </figure>

</div>

<div class="project-block">

  <div class="project-block__header">
    <h3 class="project-block__title">ML Failure-Mode Prototyping</h3>
    <p class="project-block__meta">2024–2025 · Baseline Models · Maintenance Scenarios</p>
  </div>

  <div class="project-block__body">
    <p>
      Early-stage ML exploration for detecting abnormal equipment behaviour using engineered features
      extracted from industrial time-series. The purpose was not a production model, but a mapping of
      which signals were most informative for distinguishing healthy vs degraded machine states.
    </p>

    <ul class="project-block__list">
      <li><strong>Problem.</strong> Evaluate which failure modes show separable behaviour under noisy plant conditions.</li>
      <li><strong>Data.</strong> Features derived from conditioned pressure, vibration, and load signals,
        labelled using maintenance logs and expert input.</li>
      <li><strong>Approach.</strong> Compared baseline models (Random Forest, SVM, Gradient Boosting),
        using cross-validation and calibration checks to assess model reliability.</li>
      <li><strong>Outcome.</strong> Identified feature families containing real predictive signal and
        highlighted where instrumentation or labeling needed improvement before deployment.</li>
    </ul>
  </div>

</div>

---

<style>
/* Stanford-style palette */
:root {
  --proj-border: #e5e7eb;
  --proj-text-main: #111827;
  --proj-text-muted: #6b7280;
  --proj-accent: #8c1515;  /* Stanford cardinal */
}

/* Ocultar el título automático de Minimal Mistakes */
.page__title {
  display: none;
}

/* Contenedor principal */
.projects-page {
  max-width: 760px;
  margin: 0 auto;
  padding: 1.5rem 0 2.5rem 0;
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

/* Hero */
.projects-hero {
  padding-bottom: 1.3rem;
  border-bottom: 1px solid var(--proj-border);
}

.projects-label {
  text-transform: uppercase;
  letter-spacing: 0.16em;
  font-size: 0.75rem;
  font-weight: 600;
  color: var(--proj-accent);
  margin: 0 0 0.25rem 0;
}

.projects-title {
  margin: 0;
  font-size: 2.0rem;
  font-weight: 700;
  letter-spacing: -0.02em;
  color: var(--proj-text-main);
}

.projects-tagline {
  margin: 0.35rem 0 0 0;
  font-size: 0.95rem;
  color: var(--proj-text-muted);
}

/* Intro */
.projects-intro {
  margin: 1.3rem 0 1.6rem 0;
  font-size: 0.96rem;
  line-height: 1.6;
  color: #374151;
}

/* Alinear el contenido principal con el hero */
.page__content {
  max-width: 760px;
  margin: 0 auto;
}

/* Bloques de proyecto */
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

/* Figuras / imágenes */
.project-figure {
  margin: 0.85rem 0 0 0;
}

.project-figure img {
  max-width: 100%;
  border-radius: 0.4rem;
  border: 1px solid var(--proj-border);
  margin-top: 0.3rem;
}

.project-figure figcaption {
  margin-top: 0.35rem;
  font-size: 0.78rem;
  color: var(--proj-text-muted);
  line-height: 1.45;
  text-align: center;
}

/* Grid reutilizable para Buenaventura */
.project-figure--grid .project-figure-grid {
  display: grid;
  gap: 0.6rem;
  grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
}

.project-figure-grid-item img {
  width: 100%;
  display: block;
  border-radius: 0.4rem;
  border: 1px solid var(--proj-border);
}

/* Mobile tweaks */
@media (max-width: 600px) {
  .projects-title {
    font-size: 1.8rem;
  }
  .projects-intro {
    font-size: 0.94rem;
  }
}
</style>
