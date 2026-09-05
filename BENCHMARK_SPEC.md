# LuminaCore Benchmark Specification

## Purpose

Predefine the evaluation before interpreting results. This prevents favorable metrics from being selected after experiments are observed.

## Primary metric

**Energy per correct inference (J/correct inference).**

Secondary metrics:

- end-to-end latency (µs / ms);
- accuracy;
- throughput;
- peak and steady-state power;
- calibration overhead;
- optical insertion loss;
- model-to-hardware error;
- footprint.

## Fair comparison rules

Every baseline must use:

- the same task dataset;
- the same accuracy target;
- the same input stream;
- equivalent precision constraints;
- equivalent batch/real-time constraints;
- the same inclusion rule for auxiliary hardware costs.

## Energy accounting

The reported system energy must include all components required to produce the result:

`laser + modulation + optical compute + thermal control + detectors + ADC/DAC + electronic control + memory movement + calibration`.

A separate optical-core-only metric may be reported, but it must never substitute for the complete-system metric.

## Latency accounting

Measure from the defined input boundary to the defined output/actuation boundary. Report both:

1. optical-core latency;
2. complete end-to-end latency.

## Accuracy

Report baseline accuracy, ideal mapped-model accuracy, simulated hardware-aware accuracy, and measured prototype accuracy whenever each is available.

## Repetitions

Every physical measurement should specify:

- number of repetitions;
- mean;
- median;
- standard deviation or confidence interval;
- environmental conditions;
- calibration state.

## Negative-result policy

A failed target is a valid scientific result. No benchmark will be redefined after a result is observed solely to create a favorable comparison.

## Baseline classes

At minimum, compare against one efficient CPU/MCU-class baseline and one appropriate accelerator-class baseline for the selected workload. Exact devices should be frozen before final comparison.

## Acceptance gate

The project will claim a system-level advantage only after all material overheads are included and the result is reproducible across independent runs.
