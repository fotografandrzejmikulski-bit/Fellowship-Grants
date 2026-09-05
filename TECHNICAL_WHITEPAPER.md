# LuminaCore Technical Whitepaper

## 1. Thesis

LuminaCore investigates whether a heterogeneous photonic neural accelerator can improve **system-level** latency and energy for a selected real-time edge inference workload.

The project does not assume that optical propagation speed automatically translates into lower end-to-end latency, nor that an optical core's energy excludes the cost of lasers, modulation, thermal control, readout, conversion, memory and calibration. Those overheads are part of the engineering problem.

## 2. System objective

Let the application metric be:

\[
J_{inf}=J_{source}+J_{encode}+J_{compute}+J_{nonlinear}+J_{readout}+J_{control}+J_{memory}+J_{calibration}
\]

and:

\[
T_{e2e}=T_{capture}+T_{encode}+T_{compute}+T_{nonlinear}+T_{readout}+T_{control}+T_{decision}.
\]

A photonic architecture is useful only if it improves these end-to-end metrics under matched accuracy constraints.

## 3. Optical linear compute

MZI meshes can implement programmable linear transformations through interference and phase control. MRR banks offer a compact alternative for wavelength-domain weighting. WDM provides a mechanism for parallel optical channels sharing physical routing resources.

The project will compare MZI and MRR-based realizations rather than treating either as universally optimal.

## 4. Nonlinear activation

Neural networks require nonlinear transformations between linear operators. Purely linear optical systems do not provide complete deep-network functionality without additional mechanisms.

VO₂ is investigated as one candidate because its phase transition can produce strong nonlinear optical behavior. Published work has numerically studied VO₂ integrated with SiN/BTO for a sub-milliwatt-threshold ELU-like activation. The same work reports microsecond-scale temporal dynamics, demonstrating why activation bandwidth must be treated as a first-order design constraint. citeturn712681search1turn712681academia29

Alternative nonlinear candidates remain in scope if measurements show that VO₂ is incompatible with the target edge workload.

## 5. Calibration and drift

An analog optical accelerator is sensitive to fabrication tolerances, phase errors, temperature, source variation, detector noise and device aging. LuminaCore therefore treats calibration as a hardware function, not merely a post-processing detail.

The prototype model will include:

- parameter drift;
- phase noise;
- optical loss uncertainty;
- nonlinear threshold variation;
- detector noise;
- quantization at interfaces;
- calibration time and energy.

## 6. Mapping neural networks to optics

A trained layer is represented as a numerical matrix and mapped to a photonic parameter set. The compiler layer will expose an explicit error model:

\[
E_{map}=E_{quant}+E_{phase}+E_{loss}+E_{thermal}+E_{device}.
\]

The system will compare ideal inference against hardware-aware inference and report the accuracy delta.

## 7. Benchmark philosophy

The benchmark should be narrow enough to be physically meaningful and difficult enough that latency and power matter operationally.

Candidate workload classes include event-driven perception, low-dimensional sensor fusion, and lightweight control policies. The final benchmark will be frozen before performance results are used in the grant narrative.

## 8. Electronic baselines

No claim of photonic advantage is valid without comparison to strong electronic baselines. Baselines will be chosen according to the same workload, accuracy target, batch size, precision and real-time constraint.

Metrics will include:

- latency per inference;
- throughput;
- joules per inference;
- watts at steady state;
- model accuracy;
- physical footprint;
- calibration overhead;
- total bill-of-materials estimate.

## 9. Architectural alternatives

The project retains several branches:

### A. MZI + VO₂
High programmability with explicit optical nonlinearity.

### B. MZI + alternative nonlinear device
Used if VO₂ bandwidth or stability is inadequate.

### C. MRR/WDM + nonlinear device
Potentially more compact and wavelength-efficient.

### D. Hybrid photonic/electronic accelerator
Used when the best engineering point is not fully optical.

The goal is not ideological purity. The goal is the strongest measured system.

## 10. Expected contribution

The strongest outcome is a reproducible methodology and a physical demonstration that clarifies exactly where photonic neural computation provides an advantage and where interface overheads erase it.

Recent reviews confirm strong research momentum in integrated PNNs while identifying integration, nonlinear computation, fan-in/fan-out, and multi-layer scalability as important remaining challenges. citeturn712681search5turn712681search6

## 11. Engineering principle

**Measure the system you intend to ship, not the component you want to advertise.**

This principle governs every quantitative claim in the repository.
