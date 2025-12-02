---
layout: single
title: "Home"
permalink: /
---

<div class="home-hero">
  <p class="home-kicker">Machine Learning &amp; Data Science Portfolio</p>
  <h1 class="home-name">Gonzalo Loayza</h1>
  <p class="home-tagline">
    B.S. Computer Science @ BYU • Machine Learning &amp; Predictive Analytics
  </p>
  <p class="home-summary">
    I build data-centric ML systems and predictive-maintenance pipelines for real-world engineering problems,
    working with noisy industrial sensor data, simulations, and large-scale time series.
  </p>
  <div class="home-actions">
    <a class="btn btn--primary" href="/projects/">View Projects</a>
    <a class="btn" href="/resume/">Resume</a>
    <a class="btn" href="https://github.com/Gonza055" target="_blank" rel="noopener">GitHub</a>
  </div>
</div>

---

## About

I'm a Computer Science student at Brigham Young University (BYU) with a focus on Machine Learning and data-driven engineering.  
Most of my work sits at the intersection of **time-series analysis**, **predictive maintenance**, and **software engineering** for industrial operations.

I enjoy turning noisy, complex datasets into clean, reliable pipelines that support real-world decisions.

---

## Technical Focus

<div class="home-grid home-grid--three">

<div class="home-card">
<h3>Machine Learning &amp; Data</h3>
<ul>
  <li>Time-series modeling &amp; anomaly detection</li>
  <li>Feature engineering for reliability &amp; maintenance</li>
  <li>Model evaluation, validation and monitoring</li>
</ul>
</div>

<div class="home-card">
<h3>Software &amp; Tools</h3>
<ul>
  <li>Python, C++, SQL, JavaScript</li>
  <li>NumPy, Pandas, scikit-learn</li>
  <li>Jupyter, Git, Linux</li>
</ul>
</div>

<div class="home-card">
<h3>Domain Experience</h3>
<ul>
  <li>Industrial sensor data (vibration, load, pressure)</li>
  <li>Simulation outputs &amp; operations logs</li>
  <li>Predictive maintenance &amp; reliability analytics</li>
</ul>
</div>

</div>

---

## Selected Projects

<div class="home-grid home-grid--three">

<div class="home-card">
<h3>Predictive Maintenance – Sensor Data Conditioning (2025)</h3>
<p>
Built preprocessing workflows for 50k+ high-noise industrial sensor time-series
(noise reduction, outlier capping, reconstruction) and engineered reliability-focused
features for downstream ML failure prediction.
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
to validate operating scenarios.
</p>
<p class="home-card-meta">
<a href="/projects/">See more details →</a>
</p>
</div>

<div class="home-card">
<h3>ML Failure-Mode Prototyping (2024–25)</h3>
<p>
Exploratory data analysis, feature engineering and baseline ML models
(RF, SVM, gradient boosting) for early detection of abnormal equipment behavior
in industrial maintenance settings.
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

- **Email:** (add your preferred address here)
- **GitHub:** <a href="https://github.com/Gonza055" target="_blank" rel="noopener">Gonza055</a>
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
  border-radius: 0.75rem;
  background: linear-gradient(135deg, #f5f7fb 0%, #e7f0ff 100%);
  margin-bottom: 2.5rem;
}

.home-kicker {
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-size: 0.8rem;
  font-weight: 600;
  color: #6c7a89;
  margin-bottom: 0.25rem;
}

.home-name {
  font-size: 2.7rem;
  margin: 0.1rem 0;
  font-weight: 700;
}

.home-tagline {
  font-size: 1.1rem;
  color: #555;
  margin-bottom: 0.75rem;
}

.home-summary {
  max-width: 720px;
  margin: 0 auto 1.5rem auto;
  color: #444;
  font-size: 1rem;
}

.home-actions .btn {
  display: inline-block;
  margin: 0.25rem 0.4rem;
}

/* Buttons – reuse Minimal Mistakes look but a bit bolder */
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

.home-card {
  border-radius: 0.75rem;
  border: 1px solid #e2e6f0;
  padding: 1.25rem 1.3rem;
  background: #fff;
  box-shadow: 0 4px 12px rgba(15, 23, 42, 0.04);
}

.home-card h3 {
  margin-top: 0;
  margin-bottom: 0.5rem;
  font-size: 1.05rem;
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
