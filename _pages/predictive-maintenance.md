---
layout: single
title: "Sensor Data to Reliability"
permalink: /projects/predictive-maintenance/
description: "Buenaventura San Gabriel case study: industrial sensor conditioning, reliability feature engineering, asset structuring, and condition-monitoring analysis."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/buenaventura-approved.css' | relative_url }}?v=20261018-bvn1">

<article class="bvncase">

  <header class="bvn-hero">
    <div class="bvn-hero__overlay"></div>
    <div class="bvn-hero__content">
      <div class="bvn-brand">
        <span class="bvn-brand__mark">B</span>
        <span class="bvn-brand__name">BUENAVENTURA</span>
        <span class="bvn-brand__divider"></span>
        <span class="bvn-brand__unit">SAN GABRIEL</span>
      </div>

      <h1>Sensor Data to <span>Reliability</span></h1>
      <p class="bvn-hero__lead">Maintenance data analysis to understand equipment behavior and build a stronger analytical foundation for condition monitoring and future predictive maintenance.</p>

      <div class="bvn-hero__tags">
        <span>Sensor Data</span>
        <span>Time-Series Analysis</span>
        <span>Reliability Analytics</span>
        <span>Asset Context</span>
      </div>
    </div>
  </header>

  <main class="bvn-sheet">

    <section class="bvn-context">
      <div class="bvn-section-head">
        <span></span><h2>Context</h2>
      </div>

      <div class="bvn-context__grid">
        <div class="bvn-context__copy">
          <h3>Maintenance data in a real mining operation</h3>
          <p>During my internship at Compañía de Minas Buenaventura, I worked with field sensor data from critical equipment to analyze operating behavior and create a reliable data foundation for condition monitoring and future predictive-maintenance work.</p>
        </div>

        <div class="bvn-facts">
          <div><b>Role</b><span>Maintenance Data Analyst Intern</span></div>
          <div><b>Organization</b><span>Compañía de Minas Buenaventura</span></div>
          <div><b>Location</b><span>San Gabriel · Peru</span></div>
          <div><b>Period</b><span>2025</span></div>
          <div><b>Main focus</b><span>Sensor data · reliability analysis</span></div>
        </div>
      </div>
    </section>

    <section class="bvn-grid-two">
      <div>
        <div class="bvn-section-head"><span></span><h2>The Problem</h2></div>
        <h3 class="bvn-kicker">The data existed, but it was not analysis-ready.</h3>

        <div class="bvn-problem-list">
          <div><i>01</i><p><strong>Missing data</strong><br>Gaps and inconsistencies reduced trust in the raw histories.</p></div>
          <div><i>02</i><p><strong>Noise and outliers</strong><br>Sensor noise and abnormal values could dominate the analysis.</p></div>
          <div><i>03</i><p><strong>Limited context</strong><br>Equipment, maintenance, and process context needed to be connected.</p></div>
          <div><i>04</i><p><strong>Not analysis-ready</strong><br>Signals required conditioning, validation, and structured engineering logic.</p></div>
        </div>
      </div>

      <div>
        <div class="bvn-section-head"><span></span><h2>Evidence at a Glance</h2></div>
        <p class="bvn-subcopy">Scale and characteristics of the data foundation developed during the internship.</p>

        <div class="bvn-metrics">
          <div><strong>50k+</strong><span>industrial sensor time-series processed</span></div>
          <div><strong>15+</strong><span>reliability-focused features engineered</span></div>
          <div><strong>100+</strong><span>assets structured for analytical use</span></div>
          <div><strong>ISO</strong><span>14224 / 17359 reliability context</span></div>
        </div>

        <div class="bvn-chart-card">
          <div class="bvn-chart-card__head">
            <strong>Raw vs. conditioned vibration signal</strong>
            <span><i class="raw"></i>Raw signal <i class="conditioned"></i>Conditioned</span>
          </div>
          <svg viewBox="0 0 760 220" role="img" aria-label="Representative raw and conditioned vibration signal">
            <g stroke="#DCE8EA" stroke-width="1">
              <line x1="45" y1="35" x2="735" y2="35"/><line x1="45" y1="75" x2="735" y2="75"/>
              <line x1="45" y1="115" x2="735" y2="115"/><line x1="45" y1="155" x2="735" y2="155"/>
              <line x1="45" y1="195" x2="735" y2="195"/>
            </g>
            <path d="M45 151 L55 86 L65 167 L75 110 L85 176 L95 101 L105 154 L115 129 L125 180 L135 95 L145 163 L155 118 L165 170 L175 131 L185 104 L195 157 L205 143 L215 82 L225 174 L235 121 L245 151 L255 138 L265 178 L275 109 L285 165 L295 128 L305 181 L315 116 L325 155 L335 139 L345 177 L355 105 L365 161 L375 132 L385 173 L395 117 L405 150 L415 134 L425 178 L435 91 L445 165 L455 120 L465 173 L475 129 L485 107 L495 156 L505 140 L515 72 L525 169 L535 124 L545 154 L555 136 L565 180 L575 112 L585 162 L595 130 L605 176 L615 119 L625 150 L635 137 L645 170 L655 113 L665 159 L675 132 L685 168 L695 126 L705 151 L715 139 L725 158" fill="none" stroke="#6BBEF4" stroke-width="2" opacity=".62"/>
            <path d="M45 143 C70 135 85 146 105 137 S145 149 165 139 S205 146 225 134 S265 149 285 138 S325 147 345 136 S385 148 405 139 S445 145 465 133 S505 147 525 131 S565 146 585 137 S625 145 645 136 S685 144 725 138" fill="none" stroke="#008E7E" stroke-width="4"/>
            <circle cx="520" cy="131" r="5" fill="#F59E0B"/>
            <text x="45" y="215" font-family="Inter,Arial" font-size="11" fill="#6B7F8A">Representative view — not a production monitoring screen</text>
          </svg>
        </div>
      </div>
    </section>

    <section>
      <div class="bvn-section-head">
        <span></span><h2>Approach</h2><p>From raw sensor data to a structured analytical foundation.</p>
      </div>

      <div class="bvn-approach">
        <article><em>01</em><h3>Condition the signals</h3><p>Handle missing values, remove noise, cap outliers, and correct operational artifacts.</p></article>
        <b>→</b>
        <article><em>02</em><h3>Engineer reliability features</h3><p>Extract statistical, frequency-based, and trend indicators with equipment meaning.</p></article>
        <b>→</b>
        <article><em>03</em><h3>Interpret operating patterns</h3><p>Relate signal behavior to equipment operation, deviations, and process context.</p></article>
        <b>→</b>
        <article><em>04</em><h3>Structure the assets</h3><p>Organize equipment, maintenance records, sensor metadata, and analytical context.</p></article>
      </div>
    </section>

    <section class="bvn-grid-workflow">
      <div>
        <div class="bvn-section-head"><span></span><h2>Technical Workflow</h2></div>
        <p class="bvn-subcopy">The analysis was designed as a pipeline rather than a single modeling step.</p>

        <div class="bvn-workflow">
          <article><span>▤</span><strong>Raw sensor data</strong><small>Time-series</small></article>
          <b>→</b>
          <article><span>⌁</span><strong>Signal conditioning</strong><small>Cleaning · filtering</small></article>
          <b>→</b>
          <article><span>⚙</span><strong>Feature engineering</strong><small>Reliability indicators</small></article>
          <b>→</b>
          <article><span>▧</span><strong>Asset context</strong><small>Equipment · process</small></article>
          <b>→</b>
          <article><span>▥</span><strong>Monitoring candidates</strong><small>Condition indicators</small></article>
        </div>
      </div>

      <aside>
        <div class="bvn-section-head"><span></span><h2>What the Analysis Looked For</h2></div>
        <div class="bvn-focus">
          <div><span>⌁</span><p><strong>Signal quality</strong><br>Completeness, noise, outliers, and consistency.</p></div>
          <div><span>⚙</span><p><strong>Equipment behavior</strong><br>Normal operation, deviations, trends, and condition indicators.</p></div>
          <div><span>◎</span><p><strong>Process context</strong><br>How equipment behavior relates to operating conditions and events.</p></div>
        </div>
      </aside>
    </section>

    <section>
      <div class="bvn-section-head"><span></span><h2>Key Visualizations</h2><p>Representative views of the analysis and data-processing logic.</p></div>

      <div class="bvn-viz-grid">
        <article>
          <h3>Signal Conditioning</h3>
          <svg viewBox="0 0 360 180" role="img" aria-label="Representative signal conditioning chart">
            <g stroke="#E1EAEC"><line x1="30" y1="40" x2="340" y2="40"/><line x1="30" y1="90" x2="340" y2="90"/><line x1="30" y1="140" x2="340" y2="140"/></g>
            <path d="M30 107 L36 48 L42 129 L48 74 L54 142 L60 69 L66 118 L72 87 L78 144 L84 61 L90 132 L96 77 L102 136 L108 90 L114 68 L120 122 L126 104 L132 51 L138 139 L144 81 L150 116 L156 92 L162 141 L168 72 L174 130 L180 84 L186 142 L192 75 L198 119 L204 93 L210 136 L216 67 L222 128 L228 87 L234 135 L240 79 L246 116 L252 89 L258 140 L264 57 L270 131 L276 77 L282 137 L288 86 L294 70 L300 118 L306 96 L312 48 L318 133 L324 82 L330 120 L336 92 L340 114" fill="none" stroke="#3BA5F2" stroke-width="2" opacity=".55"/>
            <path d="M30 102 C55 95 70 106 88 99 S126 108 145 100 S180 105 198 96 S235 107 254 99 S292 105 310 96 S330 101 340 98" fill="none" stroke="#009B8B" stroke-width="4"/>
          </svg>
          <p>Raw signal vs. conditioned signal</p>
        </article>

        <article>
          <h3>Frequency Analysis</h3>
          <svg viewBox="0 0 360 180" role="img" aria-label="Representative frequency spectrum">
            <g stroke="#E1EAEC"><line x1="30" y1="40" x2="340" y2="40"/><line x1="30" y1="90" x2="340" y2="90"/><line x1="30" y1="140" x2="340" y2="140"/></g>
            <path d="M30 142 L45 135 L55 128 L62 55 L69 137 L82 132 L95 128 L105 125 L118 132 L129 136 L142 131 L154 128 L168 42 L177 130 L190 136 L205 132 L220 138 L235 134 L250 135 L265 132 L280 136 L295 134 L310 138 L325 136 L340 139" fill="none" stroke="#1267E8" stroke-width="3"/>
            <path d="M30 144 C70 137 95 133 126 137 S180 139 220 140 S290 141 340 141" fill="none" stroke="#009B8B" stroke-width="3"/>
          </svg>
          <p>Raw spectrum vs. processed spectrum</p>
        </article>

        <article>
          <h3>Feature Trends</h3>
          <svg viewBox="0 0 360 180" role="img" aria-label="Representative feature trend chart">
            <g stroke="#E1EAEC"><line x1="30" y1="40" x2="340" y2="40"/><line x1="30" y1="90" x2="340" y2="90"/><line x1="30" y1="140" x2="340" y2="140"/></g>
            <path d="M30 125 L48 118 L66 123 L84 111 L102 118 L120 103 L138 108 L156 98 L174 104 L192 84 L210 91 L228 74 L246 82 L264 68 L282 76 L300 57 L318 64 L340 49" fill="none" stroke="#1267E8" stroke-width="3"/>
            <path d="M30 132 L48 129 L66 133 L84 124 L102 127 L120 119 L138 122 L156 111 L174 116 L192 108 L210 113 L228 99 L246 105 L264 95 L282 101 L300 88 L318 93 L340 83" fill="none" stroke="#F59E0B" stroke-width="3"/>
          </svg>
          <p>Reliability indicators over time</p>
        </article>
      </div>
    </section>

    <section class="bvn-grid-two bvn-outcome-grid">
      <div>
        <div class="bvn-section-head"><span></span><h2>Outcome</h2></div>
        <h3 class="bvn-kicker">A stronger foundation for predictive maintenance.</h3>
        <p class="bvn-bodycopy">The work produced cleaner sensor histories, reusable reliability features, more structured asset information, and a clearer basis for condition monitoring and later predictive-maintenance prototyping.</p>

        <div class="bvn-not-model">
          <strong>This was not a production-ready failure-prediction model.</strong>
          <span>It was the engineering and analytical foundation needed before one could be developed responsibly.</span>
        </div>
      </div>

      <div>
        <div class="bvn-section-head"><span></span><h2>Key Contributions</h2></div>
        <div class="bvn-contrib">
          <div><b>01</b><span>Cleaned and structured sensor histories</span></div>
          <div><b>02</b><span>Engineered reliability-focused indicators</span></div>
          <div><b>03</b><span>Improved interpretation of equipment behavior</span></div>
          <div><b>04</b><span>Organized asset and process context</span></div>
          <div><b>05</b><span>Created a foundation for future predictive maintenance</span></div>
        </div>
      </div>
    </section>

    <section>
      <div class="bvn-section-head"><span></span><h2>Gallery</h2><p>Real field context from the internship.</p></div>

      <div class="bvn-gallery">
        <figure><img src="/assets/images/real/buenaventura-site.webp" alt="San Gabriel mining site context"><figcaption>San Gabriel site context</figcaption></figure>
        <figure><img src="/assets/images/real/buenaventura-field-real.webp" alt="Gonzalo Loayza in field PPE at San Gabriel"><figcaption>Field exposure at San Gabriel</figcaption></figure>
        <figure><img src="/assets/images/real/bnv-san-gabriel-hero.webp" alt="Gonzalo Loayza at the San Gabriel operation"><figcaption>Internship field experience</figcaption></figure>
      </div>
    </section>

    <section class="bvn-bottom">
      <div>
        <div class="bvn-section-head"><span></span><h2>What I Learned</h2></div>
        <h3>Predictive maintenance starts before the prediction.</h3>
        <p>A reliable model depends on good data, engineering understanding, and clear context. Signal conditioning, asset structure, process behavior, and domain interpretation determine whether predictive analysis can eventually become useful.</p>
      </div>

      <div>
        <div class="bvn-section-head"><span></span><h2>Technologies &amp; Methods</h2></div>
        <div class="bvn-tech">
          <span>Python</span><span>Data Processing</span><span>Time-Series Analysis</span><span>Feature Engineering</span><span>Asset Management</span>
        </div>
      </div>
    </section>

  </main>

  <nav class="bvn-next">
    <a href="/projects/hatch-digital/"><small>Previous Project</small><strong>← Hatch Digital</strong><span>Mining Data → Decisions</span></a>
    <a href="/projects/operational-mode-discovery/"><small>Next Project</small><strong>BYU Honors Research →</strong><span>Process Data → Operating Modes</span></a>
  </nav>

</article>
