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
<link rel="stylesheet" href="{{ '/assets/css/visual-v2.css' | relative_url }}">

<div class="resume2026">

  <header class="resume2026__header">
    <div>
      <p class="pf-eyebrow">Resume</p>
      <h1>Gonzalo Loayza</h1>
      <p class="resume2026__headline">
        Senior Computer Science student at BYU with a Machine Learning emphasis and hands-on experience in data science,
        applied analytics, and ML workflows using real-world operational datasets.
      </p>
      <div class="resume2026__contact">
        <span>Provo, UT</span>
        <span>+1 (801) 735-8034</span>
        <a href="mailto:gloayza5@byu.edu">gloayza5@byu.edu</a>
        <a href="https://www.linkedin.com/in/gonzaloayza" target="_blank" rel="noopener">LinkedIn</a>
        <a href="https://github.com/Gonza055" target="_blank" rel="noopener">GitHub</a>
        <a href="/projects/">Selected Work</a>
      </div>
      <div class="pf-actions resume2026__actions">
        <a class="pf-btn pf-btn--primary" href="/assets/resume/Gonzalo_Loayza_Resume.pdf" target="_blank" rel="noopener">Download full CV</a>
      </div>
    </div>
    <div class="resume2026__status">
      <span>Education status</span>
      <strong>B.S. Computer Science<br>Machine Learning Emphasis<br>Expected Dec 2026</strong>
    </div>
  </header>

  <section class="resume2026__summary">
    <p class="resume2026__label">Summary</p>
    <p>
      Senior Computer Science student at BYU with a Machine Learning emphasis and hands-on experience in data science,
      applied analytics, and ML workflows using real-world operational datasets. Skilled in Python, SQL, time-series analysis,
      feature engineering, model evaluation, and decision-support analytics. Strong ability to frame business and operational
      problems, identify value drivers, and apply machine learning to support practical decisions in industrial, infrastructure,
      and environmental contexts.
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
            <li>Supported digital and analytics initiatives focused on mining and industrial operations, including data analysis, operational KPIs, and decision-support workflows.</li>
            <li>Contributed to early-stage problem framing, data preparation, dashboard-oriented analysis, and identification of opportunities for process improvement and operational value creation.</li>
          </ul>
        </article>

        <article class="resume2026__item">
          <div class="resume2026__item-head">
            <div>
              <h3>Maintenance Data Analyst Intern</h3>
              <p class="resume2026__org">Compañía de Minas Buenaventura · San Gabriel Unit · Peru</p>
            </div>
            <span class="resume2026__date">Jun 2025 – Aug 2025</span>
          </div>
          <ul>
            <li>Identified reliability and maintenance-analysis gaps in crushing and grinding equipment data, then processed and cleaned 50k+ noisy sensor time-series to support predictive-maintenance exploration.</li>
            <li>Analyzed operating signals linked to equipment wear, ore variability, and process behavior to support condition-monitoring and reliability-focused decision-making.</li>
            <li>Engineered 15+ features, including temperature deltas, load ratios, and transient-spike indicators, to improve the analytical basis for equipment monitoring workflows.</li>
            <li>Structured 100+ assets under ISO 14224/17359 standards, improving maintenance-data traceability, consistency, and analytical usability.</li>
          </ul>
        </article>

        <article class="resume2026__item">
          <div class="resume2026__item-head">
            <div>
              <h3>Data Analytics Intern</h3>
              <p class="resume2026__org">Hatch Ltd · Urban Solutions Sector · Vermont, USA</p>
            </div>
            <span class="resume2026__date">May 2024 – Aug 2024</span>
          </div>
          <ul>
            <li>Evaluated operational delay and network-performance challenges across simulation scenarios, then analyzed 200k+ records to identify bottlenecks and support planning decisions.</li>
            <li>Built Python and C++ automation workflows that reduced processing time by about 70%, improving analysis speed, repeatability, and scenario-evaluation capacity.</li>
            <li>Integrated rider-survey information with onboard sensor data to strengthen scenario interpretation and validate service-level assumptions.</li>
            <li>Supported planning teams through statistical and optimization-based analysis, translating simulation outputs into practical insights for operational decision-making.</li>
          </ul>
        </article>
      </section>

      <section class="resume2026__section">
        <h2>Projects</h2>

        <article class="resume2026__item">
          <div class="resume2026__item-head">
            <div>
              <h3><a href="/projects/operational-mode-discovery/">Honors Thesis – Operational Mode Discovery and Business Value Analysis in Industrial Time-Series Data</a></h3>
              <p class="resume2026__org">Python · Time-Series Analytics · PCA · Clustering · Business Value Analysis · BYU Honors Program</p>
            </div>
            <span class="resume2026__date">2025 – 2026</span>
          </div>
          <ul>
            <li>Framed an industrial analytics problem around operating variability, recovery losses, throughput pressure, and equipment bottlenecks in a real concentrator environment.</li>
            <li>Integrated minute-level process data with daily KPI context to evaluate how different operating patterns affect recovery, losses, and production stability.</li>
            <li>Applied preprocessing, feature scaling, PCA, and clustering techniques to identify recurrent operational modes and support interpretable performance profiling.</li>
            <li>Connected data infrastructure, control-loop performance, instrumentation gaps, and ML opportunities to a staged roadmap focused on throughput, recovery stability, energy optimization, and business value.</li>
          </ul>
        </article>

        <article class="resume2026__item">
          <div class="resume2026__item-head">
            <div>
              <h3><a href="/projects/wildfire-prediction/">Wildfire Prediction System</a></h3>
              <p class="resume2026__org">Python · XGBoost · Time-Series · API Integration · BYU</p>
            </div>
            <span class="resume2026__date">2026</span>
          </div>
          <ul>
            <li>Built a wildfire-risk prediction prototype using 7-day weather time-series and reported fire data from Utah to prioritize high-risk locations.</li>
            <li>Trained and compared XGBoost, Random Forest, and Naive Bayes models on imbalanced wildfire-event data.</li>
            <li>Applied SHAP interpretability and designed a workflow combining weather APIs, satellite imagery retrieval, and dashboard-style risk visualization.</li>
          </ul>
        </article>
      </section>
    </main>

    <aside class="resume2026__side">
      <section class="resume2026__side-block">
        <h3>Education</h3>
        <div class="resume2026__education">
          <strong>Brigham Young University (BYU)</strong>
          <span>B.S. in Computer Science<br>Machine Learning Emphasis<br>Expected Graduation: December 2026</span>
        </div>
        <p><strong>Relevant Coursework:</strong> Deep Learning, Data Science Capstone, Machine Learning, Algorithms, Data Structures, Computer Systems, Probability &amp; Statistics.</p>
        <p><strong>Honors Thesis:</strong> Operational Mode Discovery and Business Value Analysis in Industrial Time-Series Data.</p>
      </section>

      <section class="resume2026__side-block">
        <h3>Technical Skills</h3>
        <p><strong>Languages:</strong> Python, SQL, C++, JavaScript.</p>
        <p><strong>Data Science &amp; ML:</strong> time-series analysis, feature engineering, classification, unsupervised learning, model evaluation, exploratory data analysis, dimensionality reduction, predictive analytics.</p>
        <p><strong>Libraries &amp; Tools:</strong> scikit-learn, Pandas, NumPy, Jupyter, Git, Linux, SHAP, Power BI.</p>
        <p><strong>Business &amp; Industrial Analytics:</strong> problem framing, KPI analysis, bottleneck analysis, value-driver identification, operational mode discovery, dashboard-oriented thinking, decision-support analytics.</p>
      </section>

      <section class="resume2026__side-block">
        <h3>Certifications</h3>
        <p><strong>AWS Certification in Progress</strong><br>Expected completion: August 2026.</p>
      </section>

      <section class="resume2026__side-block">
        <h3>Awards</h3>
        <p>Donald Goodyear Doll Sr. Scholarship · Dr. Gerald Hatch Scholarship · BYU Honors Program.</p>
      </section>

      <section class="resume2026__side-block">
        <h3>Leadership</h3>
        <p><strong>Emergency Response &amp; Rescue Program, Peruvian Army</strong><br>Leadership training focused on coordination, rapid decision-making, and execution in high-pressure environments.</p>
      </section>

      <section class="resume2026__side-block">
        <h3>Languages</h3>
        <p>English — Fluent<br>Spanish — Native<br>French — Intermediate</p>
      </section>
    </aside>
  </div>

</div>
