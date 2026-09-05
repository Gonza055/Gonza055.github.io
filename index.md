---
layout: single
title: "Home"
permalink: /
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/visual-v2.css' | relative_url }}">

<div class="portfolio-page">

  <section class="pf-hero">
    <div>
      <p class="pf-eyebrow">Gonzalo Loayza · Computer Science @ BYU</p>
      <h1>Building data and ML systems for real-world industrial problems.</h1>
      <p class="pf-hero__lead">
        I work with time-series, simulation, and operational data to build reliable analytics,
        automation, and decision-support workflows for complex engineering environments.
      </p>
      <div class="pf-hero__meta">
        <span>Machine Learning</span>
        <span>Data Engineering</span>
        <span>Industrial Analytics</span>
        <span>Graduating Dec 2026</span>
      </div>
      <div class="pf-actions">
        <a class="pf-btn pf-btn--primary" href="/projects/">View selected work</a>
        <a class="pf-btn" href="/resume/">Resume</a>
        <a class="pf-btn" href="https://github.com/Gonza055" target="_blank" rel="noopener">GitHub</a>
      </div>
    </div>

    <div class="pf-hero__media" aria-label="Selected visual evidence from industrial and simulation work">
      <img class="pf-hero__media-main" src="/assets/images/projects/EDA4.png" alt="Industrial processing plant context from reliability analytics internship">
      <div class="pf-hero__media-card pf-hero__media-card--a">
        <img src="/assets/images/projects/trainops-caps-004.webp" alt="Rail operations context from Hatch TrainOps work">
      </div>
      <div class="pf-hero__media-card pf-hero__media-card--b">
        <img src="/assets/images/social/hatch-digital-social.jpg" alt="Hatch Digital data engineering and decision support portfolio card">
      </div>
      <span class="pf-hero__media-label">real systems · real data</span>
    </div>
  </section>

  <section class="pf-metrics" aria-label="Selected experience metrics">
    <div class="pf-metric">
      <span class="pf-metric__value">50k+</span>
      <span class="pf-metric__label">industrial sensor time-series processed</span>
    </div>
    <div class="pf-metric">
      <span class="pf-metric__value">200k+</span>
      <span class="pf-metric__label">simulation records analyzed and automated</span>
    </div>
    <div class="pf-metric">
      <span class="pf-metric__value">~70%</span>
      <span class="pf-metric__label">reduction in simulation-output processing time</span>
    </div>
    <div class="pf-metric">
      <span class="pf-metric__value">100+</span>
      <span class="pf-metric__label">industrial assets structured for reliability analysis</span>
    </div>
  </section>

  <section class="pf-section">
    <div class="pf-section__head">
      <div>
        <p class="pf-section__label">Selected work</p>
        <h2>Applied work across data, ML, and engineering systems.</h2>
      </div>
      <p class="pf-section__intro">
        The common thread is practical: understand the physical system, make the data trustworthy,
        and turn analysis into information people can use.
      </p>
    </div>

    <div class="pf-work-grid">
      <a class="pf-work-card pf-work-card--wide" href="/projects/hatch-digital/">
        <div class="pf-work-card__visual pf-work-card__visual--image">
          <img src="/assets/images/social/hatch-digital-social.jpg" alt="Hatch Digital case study cover">
        </div>
        <div>
          <p class="pf-work-card__kicker">Hatch Digital · 2026</p>
          <h3>Data Engineering &amp; Decision Support</h3>
          <p class="pf-work-card__desc">
            Contributed to tailings-data automation, drone-based measurement concepts, and digital
            decision-support work for mining and engineering applications.
          </p>
        </div>
        <div class="pf-work-card__footer">
          <span class="pf-tag">Data Engineering</span>
          <span class="pf-tag">Automation</span>
          <span class="pf-tag">Digital Mining</span>
          <span class="pf-tag">Decision Support</span>
          <span class="pf-card-link">View case study →</span>
        </div>
      </a>

      <a class="pf-work-card" href="/projects/predictive-maintenance/">
        <div class="pf-work-card__visual pf-work-card__visual--image">
          <img src="/assets/images/projects/EDA4.png" alt="Industrial plant context from Buenaventura reliability analytics work">
        </div>
        <div>
          <p class="pf-work-card__kicker">Buenaventura · 2025</p>
          <h3>Predictive Maintenance &amp; Reliability Analytics</h3>
          <p class="pf-work-card__desc">
            Conditioned noisy industrial time-series, engineered reliability features, and analyzed
            equipment behavior to support condition-monitoring and predictive-maintenance exploration.
          </p>
        </div>
        <div class="pf-work-card__footer">
          <span class="pf-tag">50k+ time-series</span>
          <span class="pf-tag">15+ features</span>
          <span class="pf-card-link">View case study →</span>
        </div>
      </a>

      <a class="pf-work-card" href="/projects/operational-mode-discovery/">
        <div class="pf-work-card__visual pf-work-card__visual--image">
          <img src="/assets/images/social/operational-mode-social.jpg" alt="Operational mode discovery and industrial time-series analysis case study cover">
        </div>
        <div>
          <p class="pf-work-card__kicker">BYU Honors · 2025–2026</p>
          <h3>Operational Mode Discovery &amp; Business Value Analysis</h3>
          <p class="pf-work-card__desc">
            Applying PCA, clustering, and time-series analysis to identify recurrent operating modes
            and connect process behavior with performance and business value.
          </p>
        </div>
        <div class="pf-work-card__footer">
          <span class="pf-tag">PCA</span>
          <span class="pf-tag">Clustering</span>
          <span class="pf-tag">Time-Series</span>
          <span class="pf-card-link">View case study →</span>
        </div>
      </a>
    </div>
  </section>

  <section class="pf-section">
    <div class="pf-section__head">
      <div>
        <p class="pf-section__label">Experience</p>
        <h2>Real systems, real data, real constraints.</h2>
      </div>
    </div>

    <div class="pf-experience">
      <div class="pf-exp-year">2026</div>
      <div class="pf-exp-item">
        <h3>Data Analytics Intern · Hatch Digital</h3>
        <p class="pf-exp-meta">Peru · Jun 2026 – Aug 2026</p>
        <p>
          Supported digital and analytics initiatives focused on mining and industrial operations,
          contributing to data automation, measurement concepts, problem framing, and decision-support workflows.
        </p>
      </div>

      <div class="pf-exp-year">2025</div>
      <div class="pf-exp-item">
        <h3>Maintenance Data Analyst Intern · Compañía de Minas Buenaventura</h3>
        <p class="pf-exp-meta">Peru · Jun 2025 – Aug 2025</p>
        <p>
          Processed 50k+ noisy sensor time-series, engineered 15+ reliability features, and structured
          100+ assets under ISO 14224/17359 to improve analytical usability and support condition-monitoring work.
        </p>
      </div>

      <div class="pf-exp-year">2024</div>
      <div class="pf-exp-item">
        <h3>Data Analytics Intern · Hatch Urban Solutions</h3>
        <p class="pf-exp-meta">Vermont, USA · May 2024 – Aug 2024</p>
        <p>
          Built Python and C++ automation workflows for 200k+ rail-simulation records, reducing processing time
          by about 70% and improving repeatability for scenario evaluation and planning analysis.
        </p>
      </div>
    </div>
  </section>

  <section class="pf-section">
    <div class="pf-section__head">
      <div>
        <p class="pf-section__label">Technical toolkit</p>
        <h2>Built around solving the problem, not listing the tools.</h2>
      </div>
    </div>

    <div class="pf-toolkit">
      <div class="pf-tool">
        <h3>Machine Learning &amp; Analytics</h3>
        <p>Time-series analysis, feature engineering, classification, clustering, PCA, model evaluation, SHAP, exploratory data analysis.</p>
      </div>
      <div class="pf-tool">
        <h3>Engineering &amp; Data</h3>
        <p>Python, SQL, C++, Pandas, NumPy, scikit-learn, Jupyter, data preparation, automation, reproducible workflows.</p>
      </div>
      <div class="pf-tool">
        <h3>Decision Support</h3>
        <p>Problem framing, KPI analysis, bottleneck analysis, operational-mode discovery, value-driver identification, Power BI.</p>
      </div>
    </div>
  </section>

  <section class="pf-contact">
    <div>
      <h2>Interested in data, ML, and real operational systems.</h2>
      <p>
        I am a senior Computer Science student at BYU graduating in December 2026. I am especially interested
        in work where software, analytics, and machine learning connect to complex physical or industrial systems.
      </p>
    </div>
    <div class="pf-actions">
      <a class="pf-btn pf-btn--primary" href="mailto:gloayza5@byu.edu">Email me</a>
      <a class="pf-btn" href="https://www.linkedin.com/in/gonzaloayza" target="_blank" rel="noopener">LinkedIn</a>
    </div>
  </section>

</div>
