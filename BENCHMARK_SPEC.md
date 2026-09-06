# LuminaCore Benchmark Specification v0.2

## Purpose

Predefine evaluation before interpreting results. Favorable metrics must not be selected after experiments are observed.

## Primary metric

**Energy per correct inference (J/correct inference).**

Secondary metrics: end-to-end latency, accuracy, throughput, peak and steady-state power, calibration overhead, optical insertion loss, model-to-hardware error and footprint.

## Fair comparison

Every baseline uses the same task, accuracy requirement, input stream, precision assumptions, batch/real-time constraints and auxiliary-hardware cost boundary.

## Energy accounting

The complete-system metric includes all components required to produce the result: optical source, modulation, optical compute, nonlinear stage, thermal control, detectors, ADC/DAC, electronic control, memory movement and calibration.

An optical-core-only metric may be reported separately, but it never substitutes for the complete-system metric.

## Latency accounting

Measure from the declared input boundary to the declared output/actuation boundary. Report both optical-core latency and complete end-to-end latency.

## Accuracy

Report baseline accuracy, ideal mapped-model accuracy, hardware-aware simulated accuracy and measured prototype accuracy whenever each is available.

## Repetitions

Every physical measurement must report repetitions, mean, median, dispersion or confidence interval, environmental conditions and calibration state.

## Negative-result policy

A failed target is a valid result. The benchmark must not be redefined after observing a result solely to create a favorable comparison.

## Baseline classes

At minimum, freeze one efficient CPU/MCU-class baseline and one appropriate accelerator-class baseline for the selected workload before final hardware comparison.

## Acceptance gate

A system-level advantage is claimed only after material overheads are included and the result is reproducible across independent runs.
