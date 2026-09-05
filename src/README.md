# Source Code

The repository currently separates the research specification from implementation so that no simulated result is mistaken for a measured result.

Planned modules:

```text
src/
├── model/        # neural-network and workload representations
├── photonics/    # optical component and transfer-function models
├── nonlinear/    # candidate activation models
├── mapping/      # model-to-photonic-parameter compilation
├── calibration/  # drift and calibration models
├── benchmarks/   # benchmark runners and baseline interfaces
└── reporting/    # machine-readable result export
```

## Implementation requirements

Any future scientific implementation should:

- expose configuration rather than hard-code assumptions;
- return machine-readable data;
- preserve units explicitly;
- record parameter provenance;
- use deterministic seeds when stochastic algorithms are involved;
- separate model code from visualization code;
- include automated tests for numerical invariants.

No production claim should be inferred merely from the existence of code.
