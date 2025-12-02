---
layout: page
title: "Projects"
permalink: /projects/
---

# Projects

Below are selected projects that demonstrate my experience with
machine learning, time-series analysis, and data-centric software
development.

---

## Predictive Maintenance – Sensor Data Conditioning & Feature Engineering {#predictive-maintenance}

**Context.** Industrial maintenance setting with 50k+ high-noise sensor
time-series from crushing and grinding equipment.

**What I built**

- A reproducible preprocessing pipeline (smoothing, outlier capping, signal
  reconstruction) for noisy sensor data.
- A reliability-focused feature set including load ratios, temperature deltas,
  and transient-spike metrics designed for condition-based maintenance.
- Structured datasets ready for downstream failure-prediction models.

**Tech stack**

- Python, Pandas, NumPy, Jupyter  
- Time-series preprocessing, feature engineering, EDA

**Impact**

- Enabled future ML experimentation for early-warning indicators and
  reliability analysis on critical assets.

---

## TrainOps Simulation Data Optimization {#trainops}

**Context.** Data-engineering project using simulation outputs from TrainOps
for rail operations planning (~200k records across multiple scenarios).

**What I built**

- Python and C++ parsers to transform raw simulation outputs into structured,
  analysis-ready datasets.
- Automation scripts that eliminated manual parsing and reduced processing time
  by about 70%.
- Workflows to integrate rider-survey data with onboard sensor logs to validate
  demand and service patterns.

**Tech stack**

- C++, Python, Pandas, basic SQL, Git

**Impact**

- Improved clarity and speed of scenario comparison for planning teams and
  supported data-driven decision-making.

---

## Predictive Maintenance Modeling Prototype (Academic) {#pm-modeling}

**Context.** Academic project inspired by industrial predictive-maintenance
settings.

**What I built**

- An ML pipeline including data cleaning, noise reduction, feature engineering,
  and exploratory labeling of time-series patterns.
- Baseline models (Random Forest, SVM, Gradient Boosting) to test early
  detection of abnormal equipment behavior.
- Evaluation and comparison of models using standard metrics and visualization.

**Tech stack**

- Python, scikit-learn, Pandas, NumPy, Matplotlib

**Outcome**

- Served as an experimental foundation for later industrial work on predictive
  maintenance.

---

## Honors Thesis – Unsupervised Mode Discovery in Mineral Processing (In Progress)

**Goal.** Design an unsupervised-learning framework to identify operating modes
in mineral-processing circuits using plant datasets.

**Approach**

- Clustering, dimensionality reduction, and statistical validation of
  discovered modes.
- Focus on supporting performance monitoring and early detection of suboptimal
  operating states.

*(More details coming as the research progresses.)*
