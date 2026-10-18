---
layout: single
title: "Hatch Digital — Data Engineering & Decision Support"
permalink: /projects/hatch-digital/
description: "Hatch Digital case study: drone measurement concepts, HITM data preparation and validation, and SIC operational decision support."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/hatch-digital-approved.css' | relative_url }}">

<article class="hdcase">
  <header class="hd-hero">
    <div class="hd-hero__copy">
      <a class="hd-back" href="/projects/">← Back to Work</a>
      <div class="hd-brand">
        <span class="hd-brand__hatch">HATCH</span>
        <span class="hd-brand__unit">Hatch Digital</span>
      </div>
      <h1>Data Engineering &amp;<br>Decision Support</h1>
      <p class="hd-hero__meta">Peru · 2026 · Intern</p>
      <p class="hd-hero__lead">
        Supported digital and analytics initiatives for mining operations across three workstreams:
        drones for measurement concepts, Hatch Integrated Tailings Management (HITM) data preparation and validation,
        and SIC decision-support frameworks.
      </p>
      <div class="hd-tags">
        <span>Python</span><span>Data Analysis</span><span>Drones</span><span>HITM</span><span>SIC</span><span>Mining Operations</span>
      </div>
    </div>

    <div class="hd-hero__visual">
      <img src="/assets/images/real/hatch-control-room.webp" alt="Hatch Digital operational environment">
      <div class="hd-hero__visual-shade"></div>
      <div class="hd-hero__caption">Temporary visual · final HD mining/drone image will replace this</div>
    </div>
  </header>

  <nav class="hd-tabs" aria-label="Hatch Digital case study sections">
    <a href="#overview">Overview</a>
    <a href="#problem">Problem</a>
    <a href="#approach">Approach</a>
    <a href="#results">Results</a>
    <a href="#gallery">Gallery</a>
  </nav>

  <div class="hd-sheet">
    <section class="hd-section" id="overview">
      <div class="hd-section__title">
        <span>1.</span>
        <h2>Overview</h2>
      </div>

      <div class="hd-overview">
        <div class="hd-overview__intro">
          <p>
            At Hatch Digital, I worked on data engineering and analytics solutions to support mining operations in Peru.
            The experience combined operational data, geospatial information, digital workflows, and human validation
            to improve how information is prepared and used for decision-making.
          </p>
        </div>
        <aside class="hd-org-card">
          <strong>Hatch Digital</strong>
          <p>Digital engineering for asset-intensive industries, connecting operational context, reliable information, and clearer decisions.</p>
        </aside>
      </div>

      <div class="hd-pillars">
        <div class="hd-pillar"><span class="hd-pillar__icon">▥</span><div><strong>From data to decisions</strong><small>Turning complex data into actionable insights.</small></div></div>
        <div class="hd-pillar"><span class="hd-pillar__icon">◎</span><div><strong>Cross-functional collaboration</strong><small>Worked with engineers, analysts, and domain experts.</small></div></div>
        <div class="hd-pillar"><span class="hd-pillar__icon">⚙</span><div><strong>Real operational context</strong><small>Solutions connected to actual mining operations.</small></div></div>
        <div class="hd-pillar"><span class="hd-pillar__icon">◉</span><div><strong>Impact-oriented mindset</strong><small>Focus on practical tools that create value.</small></div></div>
      </div>
    </section>

    <section class="hd-section" id="problem">
      <div class="hd-section__title">
        <span>2.</span><h2>Problem</h2>
        <p>Three key challenges in mining operations that motivated this work.</p>
      </div>

      <div class="hd-three">
        <article class="hd-workcard">
          <header><span class="hd-workcard__icon">⌁</span><h3>Drones &amp; Measurement</h3></header>
          <div class="hd-problem-visual hd-problem-visual--drone">
            <div class="hd-drone">✣</div>
            <div class="hd-scan"></div>
            <div class="hd-truck">CAEX</div>
          </div>
          <p>Could drone-based capture support a defensible estimate of CAEX load volume and indicate where confidence is insufficient?</p>
        </article>

        <article class="hd-workcard">
          <header><span class="hd-workcard__icon">▤</span><h3>Hatch Integrated Tailings Management (HITM)</h3></header>
          <div class="hd-problem-visual hd-problem-visual--hitm">
            <div class="hd-mini-dashboard">
              <div class="hd-mini-dashboard__head">Data &amp; Facility Monitoring</div>
              <div class="hd-mini-chart"></div>
              <div class="hd-mini-kpis"><span></span><span></span><span></span></div>
            </div>
          </div>
          <p>How can technical spreadsheets become consistent, review-ready inputs without losing engineering logic?</p>
        </article>

        <article class="hd-workcard">
          <header><span class="hd-workcard__icon">◎</span><h3>SIC Decision Support</h3></header>
          <div class="hd-problem-visual hd-problem-visual--sic">
            <div class="hd-sic-side">SIC</div>
            <div class="hd-sic-body">
              <div class="hd-sic-kpis"><span>12</span><span>3</span><span>8</span><span>2</span></div>
              <div class="hd-sic-chart"></div>
            </div>
          </div>
          <p>How can shift deviations be handled through clearer, more traceable, and role-based decision workflows?</p>
        </article>
      </div>
    </section>

    <section class="hd-section" id="approach">
      <div class="hd-section__title">
        <span>3.</span><h2>Approach</h2><p>Three workstreams.</p>
      </div>

      <div class="hd-three">
        <article class="hd-workcard hd-workcard--approach">
          <header><span class="hd-workcard__icon">⌁</span><h3>Drones &amp; Measurement Concepts</h3></header>
          <div class="hd-approach-visual"><img src="/assets/images/diagrams/drone-measurement-architecture.svg" alt="Drone measurement workflow"></div>
          <p>Investigated alternatives, compared capture and reconstruction approaches, and defined structured criteria to assess feasibility, accuracy, and operational value.</p>
          <div class="hd-chiprow"><span>Aerial Capture</span><span>3D Reconstruction</span><span>Evaluation Criteria</span></div>
        </article>

        <article class="hd-workcard hd-workcard--approach">
          <header><span class="hd-workcard__icon">▤</span><h3>Hatch Integrated Tailings Management (HITM)</h3></header>
          <div class="hd-approach-visual"><img src="/assets/images/diagrams/hitm-data-workflow.svg" alt="HITM data preparation and validation workflow"></div>
          <p>Prepared, adjusted, and validated technical data before upload so automated outputs remained reviewable and technically consistent.</p>
          <div class="hd-chiprow"><span>Data Pipelines</span><span>Validation</span><span>Automation</span></div>
        </article>

        <article class="hd-workcard hd-workcard--approach">
          <header><span class="hd-workcard__icon">◎</span><h3>SIC — Operational Decision Support</h3></header>
          <div class="hd-approach-visual"><img src="/assets/images/diagrams/sic-operating-cycle.svg" alt="SIC decision-support cycle"></div>
          <p>Mapped a structured decision cycle for shift deviations and explored how digital support could improve response quality and traceability.</p>
          <div class="hd-chiprow"><span>Decision Support</span><span>Deviation Flow</span><span>Operational Context</span></div>
        </article>
      </div>
    </section>

    <section class="hd-section" id="results">
      <div class="hd-section__title"><span>4.</span><h2>Results</h2></div>

      <div class="hd-results">
        <div class="hd-result"><span>▥</span><div><strong>Clearer evaluation framework</strong><small>Turned a drone concept into a structured assessment problem.</small></div></div>
        <div class="hd-result"><span>▤</span><div><strong>More reliable data workflows</strong><small>Improved the clarity and reviewability of HITM preparation.</small></div></div>
        <div class="hd-result"><span>⚙</span><div><strong>Better decision framing</strong><small>Translated SIC ideas into a practical operational workflow.</small></div></div>
        <div class="hd-result"><span>◎</span><div><strong>Real-world exposure</strong><small>Worked with real mining data, operational context, and multidisciplinary teams.</small></div></div>
      </div>

      <h3 class="hd-subtitle">Selected Evidence</h3>
      <div class="hd-evidence">
        <div class="hd-evidence-slot">
          <div class="hd-evidence-slot__visual hd-evidence-slot__visual--terrain"></div>
          <strong>Drone orthomosaic and volume analysis</strong>
          <small>HD original to insert</small>
        </div>
        <div class="hd-evidence-slot">
          <div class="hd-evidence-slot__visual hd-evidence-slot__visual--hitm"></div>
          <strong>HITM validation dashboard</strong>
          <small>HD original to insert</small>
        </div>
        <div class="hd-evidence-slot">
          <div class="hd-evidence-slot__visual hd-evidence-slot__visual--sic"></div>
          <strong>SIC operational dashboard</strong>
          <small>HD original to insert</small>
        </div>
        <div class="hd-evidence-slot">
          <div class="hd-evidence-slot__visual hd-evidence-slot__visual--field"></div>
          <strong>Field work and operational context</strong>
          <small>HD original to insert</small>
        </div>
      </div>
    </section>

    <section class="hd-section" id="gallery">
      <div class="hd-section__title"><span>5.</span><h2>Gallery</h2><p>Moments from the internship experience.</p></div>

      <div class="hd-gallery">
        <figure>
          <img src="/assets/images/real/hatch-digital-hitm-presentation.webp" alt="Gonzalo presenting HITM work">
          <figcaption>Presenting HITM results</figcaption>
        </figure>
        <figure>
          <img src="/assets/images/real/hatch-digital-practice-team.webp" alt="Hatch Digital team">
          <figcaption>Hatch Digital team</figcaption>
        </figure>
        <figure>
          <img src="/assets/images/social/hatch-digital-social.jpg" alt="Hatch Digital data and decision-support summary">
          <figcaption>Digital workstream summary</figcaption>
        </figure>
        <figure class="hd-gallery__pending">
          <div>Original photo<br><span>workshop / discussion</span></div>
          <figcaption>Workshop and discussion</figcaption>
        </figure>
        <figure class="hd-gallery__pending">
          <div>Original photo<br><span>desk / development</span></div>
          <figcaption>Desk-based development</figcaption>
        </figure>
      </div>
    </section>

    <footer class="hd-footer">
      <p>Built with curiosity, data, and real-world impact.</p>
      <div><a href="https://www.linkedin.com" aria-label="LinkedIn">in</a><a href="https://github.com/gonza055" aria-label="GitHub">GH</a><a href="mailto:gonzalo@example.com" aria-label="Email">✉</a></div>
    </footer>
  </div>
</article>
