# Reporting Contract

Every benchmark export is machine-readable JSON. Human-readable reports must state the evidence level and whether each value is measured, simulated, analytically estimated, or synthetic.

## Evidence labels

- `E0_HYPOTHESIS`
- `E1_ANALYTICAL`
- `E2_SIMULATION_MODEL`
- `E3_PHYSICAL_MEASUREMENT`
- `E4_INDEPENDENT_VALIDATION`

The current harness produces E2-class model results only.

## Required report fields

A report should identify the scenario, evaluator version, software version, random seed, workload dimensions, precision assumptions, latency accounting method, energy accounting method and any excluded overhead.
