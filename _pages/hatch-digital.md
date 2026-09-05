---
layout: single
title: "Data Engineering & Decision Support"
permalink: /projects/hatch-digital/
description: "Hatch Digital internship case study: data automation, mining data workflows, measurement concepts, and decision-support applications."
---

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{{ '/assets/css/portfolio.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/work.css' | relative_url }}">
<link rel="stylesheet" href="{{ '/assets/css/visual-pass-2.css' | relative_url }}">

<article class="portfolio-page case-page">

  <a class="case-back" href="/projects/">← Selected work</a>

  <header class="case-hero">
    <p class="pf-eyebrow">Hatch Digital · 2026</p>
    <h1>From mining data to clearer operational decisions.</h1>
    <p class="case-hero__lead">
      During my internship with Hatch Digital, I worked across data automation, measurement concepts,
      and decision-support problems for mining and engineering applications. The common lesson was simple:
      technology only becomes useful when the data is trustworthy and the operational decision is clear.
    </p>
    <div class="case-tags">
      <span class="pf-tag">Data Engineering</span>
      <span class="pf-tag">Automation</span>
      <span class="pf-tag">Digital Mining</span>
      <span class="pf-tag">Decision Support</span>
    </div>
  </header>

  <figure class="case-media case-media--wide case-media--photo">
    <img src="/assets/images/real/hatch-presentation-hitm.webp" alt="Gonzalo presenting a Hatch Digital HITM data-validation workflow to colleagues">
    <figcaption>Presenting <em>Digital en práctica</em> to colleagues at Hatch — a retrospective on the internship through three applied workstreams: measurement, data automation, and decision support.</figcaption>
  </figure>

  <section class="case-grid">
    <div class="case-main">
      <section class="case-section">
        <p class="pf-section__label">The challenge</p>
        <h2>Digital work starts before the model.</h2>
        <p>
          Mining and engineering environments generate large amounts of information, but raw data is not
          automatically useful. Before analytics can support a decision, the physical problem has to be understood,
          the information has to be structured and validated, and the intended operational use has to be explicit.
        </p>
      </section>

      <section class="case-section">
        <p class="pf-section__label">01 · Measurement</p>
        <h2>Drones: the problem was not flying — it was measuring with confidence.</h2>
        <p>
          I explored drone-enabled measurement concepts for mining applications. A representative use case was the
          quality of a truck load at the end of a loading cycle: combine continuous capture with an independent aerial
          reference, process the information close to the operation, and turn it into a traceable per-cycle decision.
          The key question was not whether imagery could be collected, but whether the measurement was reliable enough
          to support an operational action.
        </p>
      </section>

      <figure class="case-media case-media--wide case-media--technical">
        <img src="/assets/images/real/hatch-digital-drones.webp" alt="Drone measurement concept showing capture, reference, reconstruction, and comparison steps">
        <figcaption>Measurement concept from <em>Digital en práctica</em>: capture → reference → reconstruct → contrast. A useful measurement must also explain when not to trust it.</figcaption>
      </figure>

      <section class="case-architecture" aria-label="Generalized drone-enabled measurement architecture">
        <div class="case-architecture__head">
          <p class="pf-section__label">Project logic</p>
          <h3>From capture to a decision per cycle.</h3>
          <p>Generalized from the underlying project architecture; client-specific implementation details are intentionally omitted.</p>
        </div>
        <div class="case-architecture__grid">
          <div><span>01</span><strong>Continuous capture</strong><small>Observe each cycle consistently.</small></div>
          <i>→</i>
          <div><span>02</span><strong>Independent reference</strong><small>Add geometry and a second point of view.</small></div>
          <i>→</i>
          <div><span>03</span><strong>Edge processing</strong><small>Convert images and cycle data into usable metrics.</small></div>
          <i>→</i>
          <div><span>04</span><strong>Decision per cycle</strong><small>Release, correct, or add load with traceability.</small></div>
        </div>
      </section>

      <section class="case-section">
        <p class="pf-section__label">02 · Data automation</p>
        <h2>HITM: automation only helps if technical logic survives the pipeline.</h2>
        <p>
          I supported data-processing and validation work for Hatch Integrated Tailings Management (HITM),
          focusing on turning technical source files into more consistent, reviewable information. The work reinforced
          that automation does not remove engineering validation; it makes the rules, exceptions, and handoffs more explicit.
        </p>
      </section>

      <section class="case-media-grid case-media-grid--equal" aria-label="HITM project evidence">
        <figure class="case-media case-media--technical">
          <img src="/assets/images/real/hatch-digital-hitm.webp" alt="HITM workflow showing receive, prepare, validate, and generate-output steps">
          <figcaption>HITM workflow presented during the internship: receive → prepare → validate → generate output.</figcaption>
        </figure>
        <figure class="case-media case-media--photo">
          <img src="/assets/images/real/hatch-presentation-hitm.webp" alt="Gonzalo presenting the HITM workflow">
          <figcaption>The same workstream presented to the Hatch Young Professionals community.</figcaption>
        </figure>
      </section>

      <section class="case-section">
        <p class="pf-section__label">03 · Decision support</p>
        <h2>SIC: turn a shift deviation into a consistent response while there is still time to act.</h2>
        <p>
          My decision-support work explored how shift-level deviations can move from detection to action with clearer
          ownership and traceability. The operating-model work made the sequence more explicit: plan, execute, detect the
          deviation, assess its impact, identify the right decision owner, coordinate the response, execute, verify, and learn.
          Digital tools — including future LLM-based support — sit on top of that structure rather than replacing operational accountability.
        </p>
      </section>

      <section class="case-flow-strip" aria-label="Generalized SIC shift decision cycle">
        <div><span>01</span><strong>Plan</strong><small>Baseline &amp; sequence</small></div>
        <div><span>02</span><strong>Execute</strong><small>Real-time conditions</small></div>
        <div><span>03</span><strong>Detect</strong><small>Deviation from plan</small></div>
        <div><span>04</span><strong>Assess</strong><small>Impact, risk, context</small></div>
        <div><span>05</span><strong>Decide</strong><small>Owner &amp; response</small></div>
        <div><span>06</span><strong>Learn</strong><small>Verify &amp; feed back</small></div>
      </section>

      <section class="case-media-grid case-media-grid--equal" aria-label="SIC and operational decision-support context">
        <figure class="case-media case-media--photo">
          <img src="/assets/images/real/hatch-control-room.webp" alt="Gonzalo in an operations control room with live industrial dashboards">
          <figcaption>Operational context matters: decision support has to fit the environment where people actually monitor and act.</figcaption>
        </figure>
        <figure class="case-media case-media--technical">
          <img src="/assets/images/real/hatch-digital-sic.webp" alt="SIC decision cycle showing detect, evaluate, decide, and close">
          <figcaption>SIC concept from the presentation: detect → evaluate → decide → close, with a clear owner and reason for the action.</figcaption>
        </figure>
      </section>

      <div class="case-evidence-note"><strong>What connected all three workstreams:</strong> define the decision first, determine what information it needs, make validation explicit, and only then decide what automation or modeling is worth adding.</div>

      <section class="case-section">
        <p class="pf-section__label">What I learned</p>
        <h2>The code is only one part of the work.</h2>
        <p>
          The internship changed how I frame technical problems. A useful digital solution sits between the operation,
          the data, and the software. That means understanding what decision should improve, structuring the data around
          that decision, and working with specialists to validate whether the result is credible enough to use.
        </p>
      </section>
    </div>

    <aside class="case-sidebar">
      <div class="case-fact"><span>Role</span><strong>Data Analytics Intern</strong></div>
      <div class="case-fact"><span>Organization</span><strong>Hatch Digital</strong></div>
      <div class="case-fact"><span>Location</span><strong>Peru</strong></div>
      <div class="case-fact"><span>Period</span><strong>Jun – Aug 2026</strong></div>
      <div class="case-fact"><span>Workstreams</span><strong>Drones · HITM · SIC</strong></div>
      <div class="case-fact"><span>Focus</span><strong>Mining &amp; industrial operations</strong></div>
      <div class="case-note">
        <strong>Public case-study scope</strong>
        <p>Authentic internship photos and Gonzalo's own presentation visuals are shown. Underlying client project material is used only to ground the narrative; client names, economics, vendor evaluations, and implementation-specific values are not reproduced.</p>
      </div>
    </aside>
  </section>

  <nav class="case-next">
    <span>Next case study</span>
    <a href="/projects/predictive-maintenance/">Predictive Maintenance &amp; Reliability Analytics →</a>
  </nav>

</article>
