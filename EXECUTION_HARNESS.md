# LuminaCore Execution Harness

This repository contains a deterministic execution harness for comparing a reference electronic workload with a **modelled photonic path**.

The photonic path is explicitly a model. It is not a fabricated-device measurement and must not be cited as hardware evidence.

## Local execution

```bash
PYTHONPATH=. pytest -q
PYTHONPATH=. python -m luminacore.cli \
  --scenario scenarios/edge_proprioception_small.json \
  --out results/latest.json
```

## Contract

Each run is driven by a machine-readable scenario. Outputs contain latency, energy, numerical error, an accuracy proxy, and pass/fail flags.

The photonic model deliberately includes conversion and control overheads rather than reporting optical-core latency or energy alone.

## Evidence promotion

- E0: hypothesis
- E1: analytical estimate
- E2: simulation/model
- E3: physical measurement
- E4: independent validation

The current software benchmark is E2 only. A hardware backend must provide raw measurements and metadata before any result can be promoted to E3.
