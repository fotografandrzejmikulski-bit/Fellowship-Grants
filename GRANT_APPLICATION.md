# Thiel Fellowship Application — LuminaCore

**Applicant:** Andrzej Mikulski  
**Email:** mojealterego21@gmail.com  
**Phone:** +48 455 575 337  
**Project:** LuminaCore  
**Focus:** Photonic neuromorphic computing for real-time edge AI

> **Application principle:** Every statement below is classified as a current fact, a hypothesis, a planned experiment, or a target. The application does not present unmeasured performance as established fact.

## 1. What are you working on?

I am building LuminaCore, a research-stage photonic computing architecture designed for a narrow but demanding problem: real-time neural inference on power- and latency-constrained edge machines.

The central idea is to move selected neural-network operations into the optical domain, where wavelength, phase, interference and propagation can provide physical parallelism. The architecture combines programmable photonic linear operators with compact nonlinear optical elements and a software mapping layer.

My initial target is not to replace GPUs in general. I want to prove a smaller and more important claim: **for specific edge workloads where latency, energy, footprint and deterministic on-device operation matter simultaneously, a purpose-built photonic accelerator can provide a measurable system-level advantage over a strong electronic baseline.**

That claim is falsifiable. LuminaCore is therefore organized around benchmark definitions, explicit power accounting, reproducible simulation, and hardware validation rather than around a single optimistic headline number.

## 2. What problem matters?

AI hardware is increasingly constrained not only by arithmetic throughput but by moving, storing, converting and cooling information. Photonic neural networks are attractive because optical systems can exploit bandwidth and parallelism, and integrated photonic approaches have demonstrated increasingly complete neural computation. The engineering problem is turning component-level advantages into a useful, programmable, complete system.

This matters particularly at the edge. A battery-powered autonomous platform cannot assume unlimited electrical power, cooling capacity, memory bandwidth or communication latency. It must sense, compute and act locally.

I am therefore treating the problem as a system-design problem rather than as a claim that photons are universally superior to electrons.

## 3. Why now?

Integrated photonics and photonic neural-network research have reached a point where concrete architectures can be evaluated against real system constraints. Recent work includes complete nonlinear photonic neurons and integrated photonic networks trained with on-chip backpropagation, while reviews continue to identify practical challenges such as nonlinearity, calibration, integration and system overhead.

That creates an unusually useful engineering window: the field is mature enough to build against, but important architecture and workload choices remain open.

## 4. What is the technical thesis?

LuminaCore investigates a heterogeneous architecture built from:

- MZI meshes and/or MRR banks for programmable linear transforms;
- WDM channels for parallel optical dataflow;
- compact nonlinear optical elements for activation-like functions;
- electronic control and readout where required for programmability and calibration;
- a software layer that maps trained models to physical optical parameters.

The useful metric is not optical-core TOPS or propagation latency by itself. It is the complete trade-off among:

**joules per correct inference + end-to-end latency + accuracy + footprint + calibration burden.**

The architecture wins only if it wins on that complete objective for a defined workload.

## 5. Why VO₂?

VO₂ is one candidate nonlinear material because its insulator-to-metal transition can produce a strongly nonlinear optical response. Published work proposed a VO₂ patch on a SiN/BTO waveguide and reported a numerically modeled sub-milliwatt activation threshold, a 5 µm footprint and an ELU-like response. The same work reported microsecond-scale temporal dynamics. I therefore treat VO₂ as a promising but unproven candidate for the target workload, not as evidence of a sub-picosecond nonlinear neuron.

This limitation changes the engineering plan rather than invalidating it. LuminaCore will characterize the real bandwidth, loss, hysteresis, thermal behavior and switching dynamics, and it will compare VO₂ with alternative nonlinear mechanisms where necessary.

## 6. What is differentiated?

The differentiation is not that no one else has built photonic neural-network hardware. That would be inaccurate.

The differentiation hypothesis is the combination of:

1. **Edge-first optimization** — define the workload before defining the accelerator.
2. **End-to-end accounting** — include optical generation, modulation, loss, control, photodetection, conversion, memory and calibration costs.
3. **Nonlinearity as a system component** — evaluate nonlinear devices by bandwidth, hysteresis, insertion loss, stability and energy, not by transfer-curve shape alone.
4. **Evidence-gated execution** — fabrication decisions follow simulation and tolerance-analysis gates.
5. **Programmability** — build a model-to-hardware mapping layer rather than a one-off optical demonstration.

## 7. What have you built so far?

The current repository is a research and execution framework rather than evidence of a completed silicon prototype. It contains an executable benchmark harness, machine-readable scenarios, numerical tests, evaluator rules, evidence boundaries, experiment design, risk controls and the grant narrative.

The software benchmark currently executes a deterministic electronic reference and a photonic **model**, including conversion and control overheads. These outputs are explicitly classified as model evidence, not physical measurements.

I will only claim a physical demonstrator after physical measurements exist. I will only claim a validated performance improvement after the complete measurement and comparison have been performed.

## 8. What will the Fellowship fund?

The Fellowship would provide the freedom to work full-time on the project and acquire the resources required to move from simulation into measurement:

- optical and optoelectronic laboratory equipment;
- prototyping, fabrication and packaging;
- foundry / MPW access where technically justified;
- characterization and measurement services;
- EDA, simulation and compute resources;
- specialist components and consumables;
- legal and technical review for intellectual property;
- travel and collaboration needed for expert feedback.

The budget will be managed against technical gates rather than spent automatically against a calendar.

## 9. Two-year execution plan

### Months 1–3: Formalization
Deliver a reproducible reference model, freeze the benchmark, define electronic baselines, and complete the optical/thermal/error budget.

**Gate:** every headline metric has a defined measurement method.

### Months 4–6: Nonlinear-device validation
Model candidate nonlinear mechanisms and quantify threshold, response time, loss, hysteresis, temperature sensitivity and stability.

**Gate:** at least one candidate satisfies the workload-level bandwidth requirement in simulation or measurement.

### Months 7–10: Photonic linear core
Implement and validate programmable linear transforms, then run tolerance and calibration studies.

**Gate:** matrix-operation error remains inside the predeclared application tolerance.

### Months 11–14: System co-design
Integrate optical compute, nonlinear activation, readout and control models and optimize model-to-hardware mapping.

**Gate:** the complete system model shows a credible path to advantage after overheads.

### Months 15–19: Physical prototype
Fabricate or assemble the most promising architecture. Measure loss, transfer functions, thermal behavior, timing, repeatability and power.

**Gate:** measured behavior is sufficiently consistent with the model to justify end-to-end demonstration.

### Months 20–24: End-to-end demonstration
Run the predeclared edge workload and compare against strong electronic baselines at matched accuracy constraints.

**Final gate:** release measured latency, energy, accuracy, limitations and reproducibility artifacts.

## 10. Budget framework — $250,000

| Category | Allocation | Purpose |
|---|---:|---|
| Fabrication / MPW / packaging | $75,000 | Fabrication access and prototype assembly |
| Optical & electrical laboratory equipment | $55,000 | Lasers, detectors, instrumentation, control and characterization |
| EDA, simulation & compute | $30,000 | Photonic modeling, optimization and mapping |
| Specialist components / materials / consumables | $25,000 | Prototype construction and iteration |
| Testing & external characterization | $20,000 | Independent or shared-facility measurement |
| Legal / IP / technical review | $15,000 | Prior-art, patent and specialist review |
| Travel / collaboration / founder operating budget | $30,000 | Full-time execution and technical collaboration |
| **Total** | **$250,000** | |

Actual expenditure will be adjusted to technical progress and supplier/foundry quotations. The budget is a planning framework, not a fixed-price commitment.

## 11. What could make it fail?

The most important failure mode is not that an optical component does not work. It is that the complete system loses its advantage once all overheads are counted.

Other major risks include insufficient nonlinear-device bandwidth, optical loss, thermal drift, calibration complexity, fabrication variability, packaging cost and inability to demonstrate a meaningful workload-level advantage.

My response is explicit: measure these risks early, maintain credible alternatives, and pivot the target workload or device architecture rather than hide a negative result.

## 12. Why is this a Thiel Fellowship project?

The Thiel Fellowship is a two-year, $250,000 program for young people who want to build new things outside the conventional classroom path. Applicants do not need an incorporated company or a full product, but they do need meaningful progress toward a concrete vision; a selected fellow who is in university must leave in order to accept the Fellowship.

LuminaCore fits this structure because the next decisive step is execution: building, measuring, iterating and discovering whether a difficult systems hypothesis survives contact with hardware.

I am not applying for permission to call the idea revolutionary. I am applying for the resources and autonomy required to find out, experimentally, how far it can go.

## 13. What do you care about outside the project?

I am interested in systems that survive extreme constraints, especially biological adaptation. Extremophiles demonstrate that constraints can force radically different architectures instead of incremental optimization.

That interest shapes my engineering approach: instead of asking how to make an existing system slightly better, I ask whether the constraint itself suggests a different physical implementation.

## 14. What are you afraid of?

I am more afraid of spending years optimizing a path that should have been abandoned than of discovering that a difficult experiment failed.

A negative result is useful if the experiment is rigorous. The dangerous failure is unmeasured optimism.

## 15. What is something tangible you want?

I want a measured physical prototype that turns the central idea into a falsifiable object: a chip or test assembly, a documented optical path, a reproducible measurement procedure and an end-to-end benchmark that an independent engineer can inspect.

The artifact I want most is not a slide deck claiming a spectacular improvement. It is a dataset that makes the real improvement — or the real limitation — impossible to misunderstand.

## 16. What happens after the Fellowship?

If LuminaCore demonstrates a meaningful system-level advantage, the next step is commercialization through a focused edge-compute product and partnerships with photonics fabrication, packaging and robotics companies.

If the advantage is narrower than expected, the project will identify the workload or device class where the architecture actually matters. Either outcome produces technical knowledge and a credible basis for further financing or collaboration.

## 17. Founder commitment

I am committing to a build-first process in which evidence outranks narrative. I will maintain a public record of major technical decisions, document failures as well as successes, and refuse to convert simulations into prototype results or targets into measurements.

That discipline is the foundation on which I intend to build LuminaCore.

---

## Applicant Contact

**Andrzej Mikulski**  
mojealterego21@gmail.com  
+48 455 575 337
