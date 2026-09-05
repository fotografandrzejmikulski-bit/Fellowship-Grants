# LuminaCore Experimental Plan

## Objective

Determine whether the proposed photonic architecture can deliver an end-to-end advantage on a fixed edge-AI workload.

## Experiment E1 — Linear optical transform

**Question:** Can the selected photonic core implement the required matrix transform within application error tolerance?

**Measurements:** transfer matrix, phase settings, insertion loss, output error, temperature sensitivity.

**Pass condition:** predeclared numerical tolerance for the workload is satisfied across repeated runs.

## Experiment E2 — Nonlinear device

**Question:** Can the candidate nonlinear device provide the required transfer function at acceptable loss, power, and bandwidth?

**Measurements:** input-output curve, threshold, response time, hysteresis, thermal recovery, repeatability.

**Pass condition:** bandwidth and stability satisfy the frozen workload specification.

## Experiment E3 — Hardware-aware inference

Inject measured device parameters into the inference model.

Compare ideal and hardware-aware accuracy, quantify error contribution, and identify the dominant physical limitations.

## Experiment E4 — System energy

Measure all active components required for inference. Report optical-core and system totals separately.

## Experiment E5 — System latency

Measure input-to-decision latency under realistic continuous operation. Do not use propagation delay as a proxy for total latency.

## Experiment E6 — Baseline comparison

Run the identical workload on frozen electronic baselines under equivalent accuracy and real-time requirements.

## Experiment E7 — Stress testing

Sweep temperature, input power, calibration state, repeated operation, and controlled device variation.

## Reproducibility package

For every experiment retain:

- configuration;
- raw data;
- processed data;
- scripts;
- environment/dependency manifest;
- calibration information;
- measurement metadata;
- plots generated from raw data.

## Stop / pivot rules

Stop fabrication escalation when simulation or prototype evidence shows that:

- the nonlinear device is fundamentally too slow;
- optical loss eliminates projected advantage;
- control/readout overhead dominates total energy;
- required calibration is incompatible with the workload;
- manufacturing tolerance cannot meet the application requirement.

A pivot may change the workload, nonlinear mechanism, or architecture while preserving the evidence-first methodology.
