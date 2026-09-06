# Evaluator Protocol

## Primary metrics

The evaluator reports:

1. latency per sample;
2. energy per sample;
3. maximum and mean absolute numerical error;
4. a deterministic task-level accuracy proxy.

## Fair-comparison rules

Both backends must use identical workload dimensions, sample counts, random seeds, precision assumptions and accuracy targets.

The photonic system model must account for relevant system overheads: optical source, modulation, optical loss, photodetection, conversion, control, memory movement and calibration where present.

## Anti-gaming rules

- Never report optical-core latency as end-to-end latency.
- Never compare simulated photonic numbers with measured electronic numbers without labeling evidence levels.
- Do not remove unfavorable overheads after seeing results.
- Do not modify the benchmark workload in response to a result without a dated decision-log entry.
- Do not promote synthetic or simulated results to physical evidence.

## Hardware transition

The future hardware backend must implement the same evaluator contract and archive raw traces, calibration state, instrument identifiers, environmental conditions and software versions.
