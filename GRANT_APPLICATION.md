# Thiel Fellowship Application — LuminaCore

**Applicant:** Andrzej Mikulski  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337  
**Project:** LuminaCore  
**Focus:** Photonic neuromorphic computing for real-time edge AI

> **Application principle:** Every statement below is classified implicitly as either a current fact, a hypothesis, a planned experiment, or a target. The application deliberately avoids presenting unmeasured performance as established fact.

---

## 1. What are you working on?

I am building LuminaCore, a research-stage photonic computing architecture designed for a narrow but demanding problem: real-time neural inference on power- and latency-constrained edge machines.

The central idea is to move selected neural-network operations into the optical domain, where wavelength, phase, interference and propagation can provide physical parallelism. The architecture combines programmable photonic linear operators with compact nonlinear optical elements and a software mapping layer.

My initial target is not to replace GPUs in general. I want to prove a smaller and more important claim: **for specific edge workloads where milliseconds, watts, memory movement, and deterministic on-device operation matter simultaneously, a purpose-built photonic accelerator can provide a measurable system-level advantage over an electronic baseline.**

That claim is falsifiable. LuminaCore is therefore organized around benchmark definitions, explicit power accounting, reproducible simulation, and hardware validation rather than around a single optimistic headline number.

## 2. What is the important problem?

AI hardware is increasingly constrained not only by arithmetic throughput but by moving, storing, converting, and cooling information. Photonic neural networks are attractive because optical systems can exploit large bandwidth and parallelism, and several integrated photonic approaches have demonstrated neural-network computation. The open engineering challenge is turning component-level advantages into a useful, programmable, complete system. citeturn712681search5turn712681search8turn712681search9

This matters most at the edge. A battery-powered autonomous platform cannot assume unlimited electrical power, cooling capacity, memory bandwidth, or communication latency. It must sense, compute, and act locally.

I am therefore treating the problem as a system-design problem rather than as an argument that photons are universally superior to electrons.

## 3. Why now?

Integrated photonics has progressed from isolated laboratory demonstrations toward increasingly capable photonic integrated circuits, while photonic neural-network research has matured sufficiently to expose both the real opportunities and the remaining bottlenecks. Recent reviews describe strong potential in throughput and energy efficiency while identifying nonlinear functions, fan-in/fan-out, integration, calibration, and multi-layer operation as continuing challenges. citeturn712681search5turn712681search6

That combination is exactly the point at which an independent builder can be useful: the field is mature enough for concrete engineering but incomplete enough that architecture and system choices still matter.

## 4. What is the technical thesis?

LuminaCore investigates a heterogeneous architecture built from:

- MZI meshes and/or MRR banks for programmable linear transforms;
- WDM channels for parallel optical dataflow;
- compact nonlinear optical elements for activation-like functions;
- electronic control only where it is necessary for programmability, sensing, calibration, and system integration;
- a software stack that maps trained models to the physical optical parameters.

The core hypothesis is that the useful metric is not optical-core TOPS or propagation latency by itself. It is:

**joules per correct inference + end-to-end latency + accuracy + footprint + calibration burden.**

The architecture wins only if it wins on that complete objective for a defined workload.

## 5. Why VO₂?

VO₂ is one candidate nonlinear material because its insulator-to-metal transition can produce a strongly nonlinear optical response. A published study proposed a VO₂ patch on a SiN/BTO waveguide and reported numerically modeled sub-milliwatt activation threshold behavior, a 5 µm footprint, and an ELU-like response. Critically, that work used numerical simulations and reported temporal dynamics in the microsecond regime; it therefore cannot be treated as evidence for a sub-picosecond nonlinear neuron. citeturn712681search1turn712681academia29

This limitation changes the engineering plan rather than invalidating it. LuminaCore will characterize the actual bandwidth and switching behavior of the nonlinear element and will compare VO₂ against alternative nonlinear mechanisms whenever its dynamics are incompatible with the target workload.

## 6. What is differentiated?

The differentiation is not a claim that no one else has built photonic neural-network hardware. That would be inaccurate.

The intended differentiation is the combination of:

1. **Edge-first optimization** — define the workload before defining the accelerator.
2. **End-to-end accounting** — include laser, modulator, optical loss, control, photodetection, conversion, memory and calibration costs.
3. **Nonlinearity as a first-class system component** — evaluate nonlinear devices by measured bandwidth, hysteresis, insertion loss and energy rather than by transfer-curve shape alone.
4. **Evidence-gated execution** — fabrication decisions are made only after simulation and tolerance-analysis gates pass.
5. **Programmability** — create a model-to-hardware mapping layer instead of a one-off optical demonstration.

## 7. What have you built so far?

The current repository is a research and execution framework rather than evidence of a completed silicon prototype. It contains the architecture hypothesis, benchmark definitions, risk controls, evidence ledger, roadmap, and experiment design needed to turn the hypothesis into an auditable engineering program.

I will only claim a physical demonstrator after physical measurements exist. I will only claim a validated performance improvement after the complete measurement and comparison have been performed.

This distinction is deliberate: the objective is to build something real, not to make the application sound more complete than the underlying evidence.

## 8. What will the Fellowship fund?

The Fellowship would provide the freedom to work full-time on the project and to purchase the specific resources that move it from simulation into measurement:

- optical and optoelectronic laboratory equipment;
- prototyping and packaging work;
- foundry / MPW access where justified;
- characterization and measurement services;
- compute and EDA resources;
- specialist components;
- legal and technical review for intellectual property;
- travel and collaboration required to obtain expert feedback.

The budget will be released against technical gates, not spent simply because a calendar says it should be spent.

## 9. Two-year execution plan

### Months 1–3: Formalization
Deliver a reproducible reference model, freeze the benchmark, define the electronic baselines, and complete the optical/thermal/error budget.

**Gate:** every headline metric has a defined measurement method.

### Months 4–6: Nonlinear-device validation
Model and characterize candidate nonlinear mechanisms; quantify threshold, response time, loss, hysteresis, temperature sensitivity and stability.

**Gate:** at least one candidate satisfies the workload-level bandwidth requirement in simulation or measurement.

### Months 7–10: Photonic linear core
Implement and validate the programmable linear transform model; perform tolerance analysis and calibration studies.

**Gate:** matrix-operation error remains inside the predeclared application tolerance.

### Months 11–14: System co-design
Integrate optical compute, nonlinear activation, readout and control models; optimize the model-to-hardware mapping.

**Gate:** end-to-end system model demonstrates a credible path to advantage after overheads.

### Months 15–19: Physical prototype
Fabricate or assemble the most promising architecture, then measure optical loss, transfer functions, thermal behavior, timing, repeatability and power.

**Gate:** measured behavior is consistent enough with the model to justify end-to-end demonstration.

### Months 20–24: End-to-end demonstration
Run the predeclared edge workload and compare against strong electronic baselines at matched accuracy constraints.

**Final gate:** publish measured latency, energy, accuracy, limitations and reproducibility artifacts.

## 10. Budget framework — $250,000

| Category | Allocation | Purpose |
|---|---:|---|
| Fabrication / MPW / packaging | $75,000 | Access to fabrication and prototype assembly |
| Optical & electrical laboratory equipment | $55,000 | Lasers, detectors, instrumentation, control and characterization |
| EDA, simulation & compute | $30,000 | Photonic simulation, optimization and model mapping |
| Specialist components / materials / consumables | $25,000 | Prototype construction and iteration |
| Testing & external characterization | $20,000 | Independent or shared-facility measurement |
| Legal / IP / technical review | $15,000 | Prior-art, patent strategy and specialist review |
| Travel / collaboration / founder operating budget | $30,000 | Full-time execution and technical collaboration |
| **Total** | **$250,000** | |

Actual spend will be adjusted to technical progress and vendor/foundry quotations. The budget is a planning framework, not a promise of fixed pricing.

## 11. What could make the project fail?

The most important failure mode is not that an optical component does not work. It is that the complete system loses its advantage once all overheads are counted.

Other major risks include insufficient nonlinear-device bandwidth, optical loss, thermal drift, calibration complexity, fabrication variability, packaging cost, and inability to demonstrate a meaningful workload-level advantage.

My response to these risks is explicit: I will measure them early, maintain credible alternatives, and pivot the target workload or device architecture rather than hide a negative result.

## 12. Why is this a good Thiel Fellowship project?

The Fellowship is specifically designed for young people who want to build instead of remaining entirely within conventional classroom pathways. It provides $250,000 over two years and does not take equity; applicants can be individuals and do not need an incorporated company or full product at the time of application, but they do need meaningful progress toward a concrete vision. citeturn712681search0turn712681search7

LuminaCore fits that structure because the key bottleneck is execution freedom. The project crosses photonics, materials, machine learning, hardware, and software. Its next decisive step is not another generic credential. It is building, measuring, learning, and iterating.

I am not applying for permission to call the idea revolutionary. I am applying for the resources and autonomy required to find out, experimentally, how far it can go.

## 13. What do you care about outside the project?

I am interested in systems that survive extreme constraints, especially biological adaptation. Extremophiles are a useful reminder that constraints can force radically different architectures rather than simply incremental optimization.

That interest shapes how I think about engineering: instead of asking how to make an existing system slightly better, I ask whether the constraint itself suggests a different physical implementation.

## 14. What are you afraid of?

I am more afraid of spending years optimizing a path that should have been abandoned than of discovering that a difficult experiment failed.

A negative result is useful if the experiment is rigorous. The dangerous failure is unmeasured optimism.

## 15. What is something tangible you want?

I want a measured physical prototype that turns the central idea into a falsifiable object: a chip or test assembly, a documented optical path, a reproducible measurement procedure, and an end-to-end benchmark that an independent engineer can inspect.

The artifact I want most is not a slide deck claiming a 1,000× improvement. It is a dataset that makes the real improvement — or the real limitation — impossible to misunderstand.

## 16. What happens after the Fellowship?

If LuminaCore demonstrates a meaningful system-level advantage, the next step is commercialization through a focused edge-compute product and strategic partnerships with photonics fabrication, packaging, and robotics companies.

If the advantage is narrower than expected, the project will identify the workload or device class where the architecture actually matters. Either outcome produces valuable technical knowledge and a more credible basis for the next financing or collaboration step.

## 17. Founder commitment

I am committing to a build-first process in which evidence outranks narrative. I will maintain a public record of major technical decisions, document failures as well as successes, and refuse to convert simulations into “prototype results” or theoretical targets into measured performance claims.

That discipline is the foundation on which I intend to build LuminaCore.

---

## Applicant Contact

**Andrzej Mikulski**  
mojealterego21@gmail.com  
+48 455 575 337

## Verification note

This document was strengthened against current public information from the official Thiel Fellowship FAQ and primary/review literature on integrated photonic neural networks and VO₂ nonlinear activation. Eligibility should be checked again at submission because program terms can change. citeturn712681search0turn712681search5
