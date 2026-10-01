---
layout: single
title: "Home"
permalink: /
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/portfolio-v3.css' | relative_url }}">

<div class="home3">
  <section class="home3-hero">
    <div class="home3-hero__copy">
      <p class="home3-kicker">Gonzalo Loayza · Computer Science @ BYU</p>
      <h1>Applied Machine Learning for Real-World Industrial Systems.</h1>
      <p class="home3-hero__lead">I work at the intersection of software, data, and physical systems — turning imperfect operational data into reliable analytics, automation, and decision-support tools.</p>
      <div class="home3-hero__meta">
        <span>Data</span>
        <span>Machine Learning</span>
        <span>Engineering</span>
        <span>Decision Support</span>
      </div>
      <div class="home3-actions">
        <a class="home3-btn home3-btn--primary" href="/projects/">Explore Selected Work →</a>
        <a class="home3-btn" href="/resume/">View Resume</a>
      </div>
    </div>

    <div class="home3-hero__visual" aria-label="Gonzalo working across industrial analytics environments">
      <figure><img src="/assets/images/real/hatch-control-room.webp" alt="Gonzalo in an industrial operations environment"></figure>
      <figure><img src="/assets/images/real/hatch-presentation-hitm.webp" alt="Gonzalo presenting applied digital work"></figure>
      <figure><img src="/assets/images/real/buenaventura-site.webp" alt="Gonzalo at a mining site"></figure>
    </div>
  </section>

  <section class="home3-proof" aria-label="Selected evidence">
    <div class="home3-proof__item"><strong>50k+</strong><span>industrial sensor time-series processed</span></div>
    <div class="home3-proof__item"><strong>200k+</strong><span>simulation records analyzed and automated</span></div>
    <div class="home3-proof__item"><strong>100+</strong><span>industrial assets structured for reliability analysis</span></div>
    <div class="home3-proof__item"><strong>~70%</strong><span>reduction in simulation-output processing time</span></div>
  </section>

  <section class="home3-section">
    <div class="home3-section__head">
      <div>
        <p class="home3-label">Selected Work</p>
        <h2>Four environments. One consistent approach.</h2>
      </div>
      <p class="home3-section__intro">Understand the physical system, make the data trustworthy, and turn analysis into information people can actually use.</p>
    </div>

    <div class="home3-work">
      <a class="home3-card" href="/projects/hatch-digital/">
        <div class="home3-card__media"><img src="/assets/images/real/hatch-presentation-hitm.webp" alt="Gonzalo presenting Hatch Digital work"></div>
        <div class="home3-card__body">
          <p class="home3-card__meta">Hatch Digital · 2026</p>
          <h3>Mining Data → Decisions</h3>
          <p class="home3-card__flow">Data engineering &amp; decision support</p>
          <p class="home3-card__desc">Applied work across measurement, data validation, automation, and shift-level decision support for mining and industrial operations.</p>
          <div class="home3-card__footer"><span class="home3-pill">Drones</span><span class="home3-pill">HITM</span><span class="home3-pill">SIC</span></div>
        </div>
      </a>

      <a class="home3-card" href="/projects/predictive-maintenance/">
        <div class="home3-card__media"><img src="/assets/images/real/buenaventura-site.webp" alt="Gonzalo at Buenaventura"></div>
        <div class="home3-card__body">
          <p class="home3-card__meta">Buenaventura San Gabriel · 2025</p>
          <h3>Sensor Data → Reliability</h3>
          <p class="home3-card__flow">Predictive maintenance &amp; reliability analytics</p>
          <p class="home3-card__desc">Processed noisy equipment time-series, engineered reliability features, and structured asset data for condition-monitoring analysis.</p>
          <div class="home3-card__footer"><span class="home3-pill">50k+ time-series</span><span class="home3-pill">15+ features</span><span class="home3-pill">100+ assets</span></div>
        </div>
      </a>

      <a class="home3-card home3-card--honors" href="/projects/operational-mode-discovery/">
        <div class="home3-card__media"><img src="/assets/images/diagrams/honors-regimes.svg" alt="Operating-mode clusters from BYU Honors research"></div>
        <div class="home3-card__body">
          <p class="home3-card__meta">BYU Honors · 2025–2026</p>
          <h3>Process Data → Operating Modes</h3>
          <p class="home3-card__flow">Industrial time-series research</p>
          <p class="home3-card__desc">Used PCA, DBSCAN, and KPI context to identify recurrent operating regimes and connect them with throughput, recovery, and process behavior.</p>
          <div class="home3-card__footer"><span class="home3-pill">PCA</span><span class="home3-pill">DBSCAN</span><span class="home3-pill">Time-Series</span></div>
        </div>
      </a>

      <a class="home3-card" href="/projects/trainops/">
        <div class="home3-card__media"><img src="/assets/images/projects/trainops-caps-009-2.webp" alt="TrainOps simulation output"></div>
        <div class="home3-card__body">
          <p class="home3-card__meta">Hatch Urban Solutions · 2024</p>
          <h3>Simulation Data → Operational Insights</h3>
          <p class="home3-card__flow">Automation &amp; simulation analytics</p>
          <p class="home3-card__desc">Built Python and C++ workflows for large-scale rail-simulation outputs, improving repeatability and reducing processing time by about 70%.</p>
          <div class="home3-card__footer"><span class="home3-pill">200k+ records</span><span class="home3-pill">Python</span><span class="home3-pill">C++</span></div>
        </div>
      </a>
    </div>
  </section>

  <section class="home3-section">
    <div class="home3-section__head">
      <div>
        <p class="home3-label">How I Work</p>
        <h2>Build from the decision backward.</h2>
      </div>
    </div>

    <div class="home3-principles">
      <article class="home3-principle">
        <span class="home3-principle__num">01</span>
        <h3>Understand the system</h3>
        <p>Start with the physical process, operating context, constraints, and the decision that actually needs to improve.</p>
      </article>
      <article class="home3-principle">
        <span class="home3-principle__num">02</span>
        <h3>Make the data trustworthy</h3>
        <p>Structure, clean, validate, and contextualize the data before adding modeling or automation.</p>
      </article>
      <article class="home3-principle">
        <span class="home3-principle__num">03</span>
        <h3>Build for the decision</h3>
        <p>Use the simplest analysis, model, or software workflow that turns reliable information into useful action.</p>
      </article>
    </div>
  </section>

  <section class="home3-section">
    <div class="home3-section__head">
      <div>
        <p class="home3-label">Additional Technical Work</p>
        <h2>Beyond industrial analytics.</h2>
      </div>
    </div>

    <div class="home3-more">
      <a class="home3-more__feature" href="/projects/wildfire-prediction/">
        <img src="/assets/images/real/wildfire-team.webp" alt="Wildfire Prediction project team">
        <div class="home3-more__copy">
          <h3>Wildfire Prediction System</h3>
          <p>A machine-learning prototype using weather histories, model comparison, maps, and satellite-image retrieval to prioritize higher-risk locations.</p>
          <span class="home3-link">View project →</span>
        </div>
      </a>

      <aside class="home3-more__about">
        <p class="home3-label">About</p>
        <h3>Software meets physical systems.</h3>
        <p>I am a BYU Computer Science student graduating in December 2026, interested in applied ML, data engineering, and industrial AI for complex real-world systems.</p>
        <a class="home3-link" href="/resume/">Experience &amp; education →</a>
      </aside>
    </div>
  </section>

  <section class="home3-final">
    <h2>Interested in data, ML, and real operational systems.</h2>
    <p>I am especially interested in opportunities where software and analytics connect to mining, infrastructure, energy, transportation, or other complex physical systems.</p>
    <div class="home3-actions">
      <a class="home3-btn home3-btn--primary" href="mailto:gloayza5@byu.edu">Email me</a>
      <a class="home3-btn" href="https://www.linkedin.com/in/gonzaloayza" target="_blank" rel="noopener">LinkedIn</a>
      <a class="home3-btn" href="https://github.com/Gonza055" target="_blank" rel="noopener">GitHub</a>
    </div>
  </section>
</div>
