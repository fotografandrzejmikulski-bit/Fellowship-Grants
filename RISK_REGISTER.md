# Risk Register

| ID | Risk | Severity | Trigger | Mitigation | Pivot |
|---|---|---:|---|---|---|
| R1 | Nonlinear response too slow | Critical | Measured bandwidth below workload requirement | Characterize early; evaluate alternatives | Change device/workload |
| R2 | Optical loss erases benefit | Critical | System loss budget exceeds threshold | Optimize routing, coupling and WDM jointly | Simplify topology |
| R3 | Readout dominates energy | Critical | ADC/driver/detector power dominates | Move more work into optical domain; lower interface rate | Hybrid architecture |
| R4 | Thermal drift | High | Parameter drift exceeds calibration budget | Thermal modeling + feedback | Reduce depth / change material |
| R5 | Fabrication variability | High | Yield/tolerance simulation fails | Monte Carlo design + calibration margin | Larger/less sensitive devices |
| R6 | Model mapping error | High | Accuracy loss exceeds target | Hardware-aware training/calibration | Narrow workload |
| R7 | Packaging complexity | High | Assembly cost/size blocks edge use | Define package early | Chiplet/alternative package |
| R8 | Weak customer pain | High | Interviews fail to confirm urgent need | Validate use case before scale | Select new edge workload |
| R9 | Unsupported quantitative claims | Critical | Claim lacks primary evidence | Evidence ledger + review gate | Remove claim |
| R10 | IP conflict | High | Prior-art/FTO review identifies conflict | Specialist counsel before filing | Design-around |

## Governance rule

No critical risk may be silently removed from the register. Risks are closed only with measured evidence or an explicit architectural decision.
