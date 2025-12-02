---
layout: default
title: Projects
---

<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">

<style>
  body {
    font-family: 'Inter', sans-serif;
    color: #2c3e50;
    line-height: 1.6;
  }

  .projects-page {
    max-width: 860px;
    margin: 0 auto;
    padding: 40px 20px 80px;
  }

  .projects-title {
    font-size: 40px;
    font-weight: 600;
    margin-bottom: 10px;
    color: #002856;  /* Stanford Navy */
  }

  .projects-subtitle {
    font-size: 18px;
    color: #5d6d7e;
    margin-bottom: 40px;
  }

  .project-divider {
    height: 1px;
    background: #dfe6ee;
    margin: 60px 0;
  }

  .project-block__header h3 {
    color: #002856;
    font-size: 26px;
    margin-bottom: 6px;
  }

  .project-block__meta {
    color: #6b7c93;
    font-size: 15px;
    margin-bottom: 18px;
  }

  .project-block__list li {
    margin-bottom: 10px;
  }

  /* Image grid */
  .project-figure {
    margin-top: 25px;
  }

  .project-figure-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
    gap: 18px;
    margin-bottom: 12px;
  }

  .project-figure-grid img {
    width: 100%;
    border-radius: 12px;
    border: 1px solid #e6e9ef;
  }

  figcaption {
    font-size: 14px;
    color: #6b7c93;
    text-align: center;
    margin-top: 6px;
  }
</style>


<div class="projects-page">

  <!-- TITLE -->
  <h1 class="projects-title">Selected Projects</h1>
  <p class="projects-subtitle">Data Science · Machine Learning · Industrial Analytics</p>



  <!-- ========================================================= -->
  <!-- =============== 1. BUENAVENTURA PROJECT ================== -->
  <!-- ========================================================= -->
  <div class="project-block">

    <div class="project-block__header">
      <h3 class="project-block__title">Liner Wear & EDA – Ball Mill at Buenaventura</h3>
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

        <li><strong>Key correlations.</strong> Thickness vs cumulative tonnage r ≈ −0.63 (global) and r ≈ −0.8 (Vulco).
            MAT 2 vs thickness r ≈ −0.81 → higher temperature aligns with lower thickness.</li>

        <li><strong>Data cleaning.</strong> Removed nonphysical outliers such as recorded temperatures ~6528 °C.</li>

        <li><strong>Operational strategy.</strong> Supported an alternation plan over four campaigns
            (Vulco–Hofmann–Vulco–Hofmann) to balance throughput, wear rate, and liner cost.</li>

        <li><strong>Next steps.</strong> Thickness, tonnage accumulation, and MAT 2 highlighted as key
            predictors for future ML-based condition monitoring.</li>
      </ul>
    </div>

    <!-- IMAGES GRID (3 images) -->
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

  <div class="project-divider"></div>



  <!-- ========================================================= -->
  <!-- =========== 2. ML FAILURE-MODE PROTOTYPING ============== -->
  <!-- ========================================================= -->
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
        <li><strong>Problem.</strong> Evaluate which failure modes show separable behaviour under noisy conditions.</li>

        <li><strong>Data.</strong> Derived from conditioned pressure, vibration and load signals, labelled
            using maintenance logs and expert input.</li>

        <li><strong>Approach.</strong> Compared baselines (Random Forest, SVM, Gradient Boosting),
            with cross-validation and calibration checks to determine model reliability.</li>

        <li><strong>Outcome.</strong> Identified feature families containing real predictive signal and
            highlighted where instrumentation or labeling needed improvement.</li>
      </ul>
    </div>

  </div>

</div>
