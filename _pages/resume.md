---
layout: single
title: "Resume"
permalink: /resume/
description: "Resume of Gonzalo Loayza, BYU Computer Science student focused on machine learning, data engineering, industrial analytics, and decision support."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/resume-2026.css' | relative_url }}">

<div class="resume2026">

  <header class="resume2026__header">
    <div>
      <p class="pf-eyebrow">Resume</p>
      <h1>Gonzalo Loayza</h1>
      <p class="resume2026__headline">
        Senior Computer Science student at BYU with a Machine Learning emphasis and applied experience across
        data engineering, industrial analytics, time-series, simulation, and decision-support workflows.
      </p>
      <div class="resume2026__contact">
        <span>Provo, UT</span>
        <a href="mailto:gloayza5@byu.edu">gloayza5@byu.edu</a>
        <a href="https://www.linkedin.com/in/gonzaloayza" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://github.com/Gonza055" target="_blank" rel="noopener">GitHub</a>
        <a href="/projects/">Selected Work</a>
      </div>
      <div class="pf-actions resume2026__actions">
        <a class="pf-btn pf-btn--primary" href="/assets/resume/Gonzalo_Loayza_Resume.pdf" target="_blank" rel="noopener">Download PDF</a>
      </div>
    </div>
    <div class="resume2026__status">
      <span>Education status</span>
      <strong>B.S. Computer Science<br>Expected Dec 2026</strong>
    </div>
  </header>

  <section class="resume2026__summary">
    <p class="resume2026__label">Profile</p>
    <p>
      Experienced with Python, SQL, C++, time-series analysis, feature engineering, model evaluation, and
      operational analytics using real-world datasets. I am particularly interested in technical problems where
      understanding the system, improving the data foundation, and connecting analytics to practical decisions
      matter as much as the model itself.
    </p>
  </section>

  <div class="resume2026__layout">
    <main>
      <section class="resume2026__section">
        <h2>Experience</h2>

        <article class="resume2026__item">
          <div class="resume2026__item-head">
            <div>
              <h3>Data Analytics Intern</h3>
              <p class="resume2026__org">Hatch Digital · Peru</p>
            </div>
            <span class="resume2026__date">Jun 2026 – Aug 2026</span>
          </div>
          <ul>
            <li>Supported digital and analytics initiatives for mining and industrial operations, including tailings-data automation, operational KPIs, measurement concepts, and decision-support workflows.</li>
            <li>Contributed to problem framing, data preparation, dashboard-oriented analysis, and identification of opportunities for process improvement and operational value creation.</li>
          </ul>
        </article>

        <article class="resume2026__item">
          <div class="resume2026__item-head">
            <div>
              <h3>Maintenance Data Analyst Intern</h3>
              <p class="resume2026__org">Compañía de Minas Buenaventura · Peru</p>
            </div>
            <span class="resume2026__date">Jun 2025 – Aug 2025</span>
          </div>
          <ul>
            <li>Processed and cleaned 50k+ noisy sensor time-series from crushing and grinding equipment to support predictive-maintenance exploration.</li>
            <li>Analyzed operating signals linked to equipment wear, ore variability, and process behavior for reliability-focused decision-making.</li>
            <li>Engineered 15+ features, including temperature deltas, load ratios, and transient-spike indicators.</li>
            <li>Structured 100+ assets under ISO 14224/17359 standards to improve maintenance-data traceability and analytical usability.</li>
          </ul>
        </article>

        <article class="resume2026__item">
          <div class="resume2026__item-head">
            <div>
              <h3>Data Analytics Intern</h3>
              <p class="resume2026__org">Hatch Ltd · Urban Solutions · Vermont, USA</p>
            </div>
            <span class="resume2026__date">May 2024 – Aug 2024</span>
          </div>
          <ul>
            <li>Analyzed 200k+ rail-simulation records to evaluate delays, network performance, and operational bottlenecks.</li>
            <li>Built Python and C++ automation workflows that reduced simulation-output processing time by about 70%.</li>
            <li>Integrated rider-survey information with onboard sensor data to strengthen scenario interpretation and service-level assumptions.</li>
            <li>Supported planning decisions through statistical and optimization-based analysis of simulation outputs.</li>
          </ul>
        </article>
      </section>

      <section class="resume2026__section">
        <h2>Selected Projects</h2>

        <article class="resume2026__item">
          <div class="resume2026__item-head">
            <div>
              <h3><a href="/projects/operational-mode-discovery/">Operational Mode Discovery &amp; Business Value Analysis</a></h3>
              <p class="resume2026__org">BYU Honors Program · Python · PCA · Clustering · Industrial Time-Series</p>
            </div>
            <span class="resume2026__date">2025 – 2026</span>
          </div>
          <ul>
            <li>Framed an industrial analytics problem around operating variability, recovery losses, throughput pressure, and equipment bottlenecks.</li>
            <li>Integrated minute-level process data with daily KPI context and applied preprocessing, feature scaling, PCA, and clustering.</li>
            <li>Connected operating modes and data-quality gaps to a staged roadmap focused on performance stability and business value.</li>
          </ul>
        </article>

        <article class="resume2026__item">
          <div class="resume2026__item-head">
            <div>
              <h3><a href="/projects/wildfire-prediction/">Wildfire Prediction System</a></h3>
              <p class="resume2026__org">BYU · Python · XGBoost · SHAP · API Integration</p>
            </div>
            <span class="resume2026__date">2026</span>
          </div>
          <ul>
            <li>Built a wildfire-risk prediction prototype using seven-day weather time-series and reported fire data.</li>
            <li>Compared XGBoost, Random Forest, and Naive Bayes models on imbalanced event data and applied SHAP interpretability.</li>
            <li>Designed a workflow combining weather APIs, satellite-imagery retrieval, and dashboard-style risk visualization.</li>
          </ul>
        </article>
      </section>
    </main>

    <aside class="resume2026__side">
      <section class="resume2026__side-block">
        <h3>Education</h3>
        <div class="resume2026__education">
          <strong>Brigham Young University</strong>
          <span>B.S. Computer Science<br>Machine Learning Emphasis<br>Expected Dec 2026</span>
        </div>
      </section>

      <section class="resume2026__side-block">
        <h3>Technical Skills</h3>
        <div class="resume2026__chips">
          <span class="pf-tag">Python</span>
          <span class="pf-tag">SQL</span>
          <span class="pf-tag">C++</span>
          <span class="pf-tag">JavaScript</span>
          <span class="pf-tag">scikit-learn</span>
          <span class="pf-tag">Pandas</span>
          <span class="pf-tag">NumPy</span>
          <span class="pf-tag">SHAP</span>
          <span class="pf-tag">Power BI</span>
          <span class="pf-tag">Git</span>
          <span class="pf-tag">Linux</span>
        </div>
      </section>

      <section class="resume2026__side-block">
        <h3>Analytics Focus</h3>
        <p>Time-series analysis · Feature engineering · Classification · Unsupervised learning · Model evaluation · Dimensionality reduction · Predictive analytics · KPI and bottleneck analysis.</p>
      </section>

      <section class="resume2026__side-block">
        <h3>Awards</h3>
        <p>Donald Goodyear Doll Sr. Scholarship · Dr. Gerald Hatch Scholarship · BYU Honors Program.</p>
      </section>

      <section class="resume2026__side-block">
        <h3>Leadership</h3>
        <p>Emergency Response &amp; Rescue Program, Peruvian Army — leadership training in coordination, rapid decision-making, and high-pressure execution.</p>
      </section>

      <section class="resume2026__side-block">
        <h3>Languages</h3>
        <p>English — Fluent<br>Spanish — Native<br>French — Intermediate</p>
      </section>
    </aside>
  </div>

</div>
