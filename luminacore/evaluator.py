from __future__ import annotations
from dataclasses import dataclass
from .core import RunResult

@dataclass(frozen=True)
class Evaluation:
    accuracy_gate: bool
    error_gate: bool
    comparable: bool
    advantage_claim_allowed: bool
    reason: str

def evaluate_pair(electronic: RunResult, photonic: RunResult) -> Evaluation:
    comparable = electronic.workload == photonic.workload and electronic.samples == photonic.samples
    accuracy = electronic.passed_accuracy and photonic.passed_accuracy
    error = photonic.passed_error
    energy_advantage = photonic.energy_j_per_sample < electronic.energy_j_per_sample
    latency_advantage = photonic.latency_ms_per_sample < electronic.latency_ms_per_sample
    allowed = comparable and accuracy and error and energy_advantage and latency_advantage
    reason = 'pass' if allowed else 'model does not yet establish end-to-end advantage'
    return Evaluation(accuracy, error, comparable, allowed, reason)
