# LuminaCore

## Photonic Neuromorphic Computing for Real-Time Edge AI

**Applicant:** Andrzej Mikulski  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337  
**Status:** Independent founder / research-stage deep-tech project  
**Repository:** Fellowship-Grants

---

## Executive Summary

LuminaCore is a research-stage photonic computing architecture aimed at reducing the latency, data-movement cost, and power burden of neural inference at the edge.

The core hypothesis is intentionally testable rather than assumed: **a heterogeneous photonic neural processor combining programmable linear optical transforms with compact optical nonlinear elements can deliver a useful latency/energy advantage for tightly constrained real-time edge workloads, once system-level overheads are included.**

The project targets a concrete first application: low-latency perception/proprioception pipelines for battery-constrained autonomous machines. The initial goal is not to replace GPUs universally. It is to establish a measurable advantage in a narrow workload where latency, power, footprint, and deterministic on-device operation matter simultaneously.

The architecture investigates MZI/MRR-based photonic linear operators, wavelength-division multiplexing (WDM), and phase-change-material-assisted nonlinear optical functions, with VO₂ as one candidate device technology. Existing literature supports the feasibility of the underlying building blocks, including numerical work on a VO₂/SiN/BTO nonlinear activation device with sub-milliwatt activation threshold and a 5 µm footprint; that work also reports microsecond-scale temporal dynamics, so LuminaCore does **not** treat sub-picosecond nonlinear response as an established fact. citeturn712681search1turn712681academia29

The repository is designed as an evidence-first research package: architecture, hypotheses, simulation plans, benchmark definitions, risk register, milestone gates, grant narrative, and reproducibility standards are separated so that claims can be distinguished from measurements and future targets.

## What is novel

LuminaCore combines four ideas into one edge-oriented system hypothesis:

1. **Programmable optical linear algebra** for matrix-vector operations.
2. **WDM parallelism** to increase throughput without proportionally increasing spatial routing complexity.
3. **On-chip nonlinear optical elements** to reduce repeated optical/electrical conversion where technically justified.
4. **A workload-first evaluation methodology** that measures complete-system latency and energy rather than quoting optical-core numbers alone.

The fourth point is a deliberate design principle: claims will only be promoted to headline results after end-to-end validation.

## Research questions

### RQ1 — Latency
Can the optical compute path reduce end-to-end inference latency for a selected real-time edge workload after accounting for modulation, control, photodetection, ADC/DAC, memory, and packaging overheads?

### RQ2 — Energy
Can the complete accelerator achieve lower joules per inference than a strong electronic baseline under equal accuracy and throughput constraints?

### RQ3 — Nonlinearity
Can a compact phase-change-material-based nonlinear element provide a stable, repeatable activation function with acceptable insertion loss, thermal behavior, hysteresis, and bandwidth?

### RQ4 — Programmability
Can trained neural-network layers be mapped to the photonic architecture without unacceptable accuracy loss or calibration burden?

### RQ5 — Edge utility
Does the architecture remain advantageous after realistic system constraints such as battery budget, thermal budget, optical sources, packaging, and control electronics are included?

## Falsifiable success criteria

The project will not define success as “photonic computing is faster.” Success requires measured thresholds on a predeclared benchmark.

A prototype milestone is considered successful only if it demonstrates:

- a reproducible optical matrix operation;
- measured linear-operator error below a predeclared tolerance;
- a demonstrated nonlinear activation transfer curve;
- stable operation over a defined temperature and power range;
- an end-to-end inference experiment on a representative edge task;
- complete-system latency and energy measurements;
- a documented comparison against an electronic baseline.

Target values are hypotheses, not guaranteed results, until measured.

## Technical architecture

```text
Sensor / Event Stream
        |
        v
  Input Encoding
        |
        v
+-----------------------+
| Photonic Linear Core  |
| MZI mesh / MRR bank   |
| WDM parallel channels |
+-----------+-----------+
            |
            v
+-----------------------+
| Optical Nonlinearity  |
| VO₂ / alternative PCM |
+-----------+-----------+
            |
            v
   Optical Fan-out
            |
            v
+-----------------------+
| Readout / Control     |
| PD + ADC + calibration|
+-----------+-----------+
            |
            v
   Edge Decision / Actuation
```

## Why the edge first

Large data-center accelerators optimize for aggregate throughput. Edge systems impose a different objective function: low latency, low power, small physical footprint, predictable behavior, and minimal data movement. The first LuminaCore benchmark therefore focuses on a narrow, high-value control/perception loop rather than attempting to compete with general-purpose accelerators on every workload.

## Evidence discipline

The project distinguishes four evidence levels:

| Level | Meaning |
|---|---|
| E0 | Idea or hypothesis |
| E1 | Analytical/model-based result |
| E2 | Simulation result |
| E3 | Physical measurement / prototype result |
| E4 | Independent replication or external validation |

Only E2–E4 evidence may be used to support quantitative performance claims, and each claim must identify its measurement or simulation methodology.

## Current research basis

Recent reviews identify photonic neural networks as a serious research direction for high-throughput and energy-efficient neural computation, while also emphasizing the remaining challenges around integration, nonlinear operators, fan-in/fan-out, and multi-layer systems. citeturn712681search5turn712681search8turn712681search9

Published work specifically relevant to this project reports a simulated SiN/BTO waveguide with a VO₂ patch for all-optical nonlinear activation, with sub-milliwatt threshold behavior and a 5 µm footprint. Importantly, its reported temporal dynamics are on the microsecond scale, which is a critical constraint for LuminaCore's engineering roadmap. citeturn712681search1turn712681academia29

## Milestones

### Phase 1 — Architecture and simulation
- Formalize optical dataflow.
- Implement reference numerical model.
- Define benchmark workload and electronic baselines.
- Establish power and latency accounting rules.

### Phase 2 — Device-level validation
- Model candidate nonlinear optical element.
- Sweep geometry, optical power, thermal conditions, and hysteresis.
- Quantify loss, extinction ratio, response time, and repeatability.

### Phase 3 — System co-design
- Integrate linear core + nonlinear element + readout model.
- Quantify calibration overhead and error propagation.
- Optimize workload-to-hardware mapping.

### Phase 4 — Prototype planning
- Freeze fabrication specifications only after simulation gates pass.
- Select fabrication path and packaging assumptions.
- Build optical test methodology before hardware arrival.

### Phase 5 — Hardware proof of concept
- Characterize fabricated devices.
- Compare measured behavior against pre-registered simulations.
- Demonstrate an end-to-end benchmark.

### Phase 6 — External validation
- Release reproducible datasets, scripts, measurement methodology, and limitations.
- Seek independent technical review and manufacturing feedback.

## Risk register

| Risk | Impact | Mitigation |
|---|---|---|
| VO₂ dynamics too slow for target workload | High | Evaluate alternative nonlinear mechanisms and application bandwidth requirements |
| Optical loss erodes system advantage | High | Include loss budget from the beginning; optimize architecture jointly |
| ADC/DAC and control electronics dominate energy | High | Optimize end-to-end path, not optical core alone |
| Thermal drift / hysteresis | High | Closed-loop calibration and thermal characterization |
| Fabrication variability | High | Tolerance analysis and redundant calibration strategies |
| Insufficient benchmark advantage | High | Pivot to narrower workloads where the architecture has structural advantage |
| Packaging complexity | Medium/High | Define packaging constraints before tape-out |
| Overclaiming immature results | Critical | Evidence-level labeling and predeclared success criteria |

## Intellectual property strategy

The preferred strategy is evidence-first: publish non-sensitive scientific methodology while reserving potentially patentable implementation details until an appropriate prior-art and freedom-to-operate review has been completed. No patentability claim in this repository should be interpreted as legal advice or as proof that an invention is novel.

## Reproducibility

All simulation code should:

- pin dependency versions;
- expose configuration files;
- save machine-readable outputs;
- generate plots from source data;
- record random seeds where applicable;
- document hardware assumptions;
- separate measured data from synthetic data;
- include a provenance note for every externally sourced parameter.

## Repository map

- `GRANT_APPLICATION.md` — full English grant application.
- `TECHNICAL_WHITEPAPER.md` — architecture and research thesis.
- `EXPERIMENT_PLAN.md` — pre-registered experimental design.
- `BENCHMARK_SPEC.md` — benchmark and baseline definitions.
- `RISK_REGISTER.md` — technical and commercialization risks.
- `ROADMAP.md` — milestone gates and resource allocation.
- `EVIDENCE_LEDGER.md` — claim-to-source/evidence mapping.
- `CITATIONS.md` — external references.
- `CITATION_POLICY.md` — rules for source quality and quantitative claims.
- `RESEARCH_LOG.md` — dated research and implementation log.
- `DECISION_LOG.md` — architecture decisions and reversals.
- `data/README.md` — data provenance policy.
- `src/README.md` — software architecture and future implementation boundary.

## Applicant

**Andrzej Mikulski**  
mojealterego21@gmail.com  
+48 455 575 337

## Status

This repository is a research and grant-preparation package. It intentionally distinguishes demonstrated results from proposed work. Quantitative targets remain targets until experimentally validated.
