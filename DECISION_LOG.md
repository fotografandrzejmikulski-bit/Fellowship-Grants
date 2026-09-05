# Architecture Decision Log

## ADR-001 — Edge-first workload

**Decision:** Start with a narrow real-time edge workload rather than generic AI acceleration.

**Reason:** This creates a measurable product criterion around latency, energy, footprint and determinism.

**Status:** Accepted.

## ADR-002 — End-to-end metrics

**Decision:** Report complete-system energy and latency in addition to optical-core metrics.

**Reason:** Interface overhead can dominate system performance.

**Status:** Accepted.

## ADR-003 — VO₂ is a candidate, not a commitment

**Decision:** Treat VO₂ as one nonlinear-device candidate.

**Reason:** Published numerical work is promising but reports microsecond-scale temporal dynamics, which may or may not satisfy the selected workload.

**Status:** Accepted.

## ADR-004 — Evidence levels

**Decision:** Separate hypotheses, simulations, physical measurements and independent validation.

**Reason:** Prevents grant narrative inflation and makes technical review easier.

**Status:** Accepted.

## ADR-005 — Pivot is part of the plan

**Decision:** Permit changes to nonlinear device, optical topology, workload or hybridization when evidence invalidates an assumption.

**Reason:** Preserving a weak architecture solely to protect the original narrative is poor engineering.

**Status:** Accepted.
