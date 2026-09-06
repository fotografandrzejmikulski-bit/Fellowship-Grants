from __future__ import annotations
from dataclasses import dataclass, asdict
import json, math, pathlib
from typing import List
import numpy as np

@dataclass
class Workload:
    name: str
    input_dim: int
    output_dim: int
    layers: int
    samples: int
    accuracy_target: float

@dataclass
class RunResult:
    backend: str
    workload: str
    samples: int
    latency_ms_total: float
    latency_ms_per_sample: float
    energy_j_total: float
    energy_j_per_sample: float
    top1_accuracy: float
    max_abs_error: float
    mean_abs_error: float
    passed_accuracy: bool
    passed_error: bool


def make_weights(rng: np.random.Generator, in_dim: int, out_dim: int) -> np.ndarray:
    return rng.normal(0, 1 / math.sqrt(in_dim), size=(out_dim, in_dim))


def _inputs_and_weights(w: Workload, seed: int):
    rng = np.random.default_rng(seed)
    x = rng.normal(size=(w.samples, w.input_dim))
    W = make_weights(rng, w.input_dim, w.output_dim)
    return x, W


def run_electronic(w: Workload, seed: int = 7):
    x, W = _inputs_and_weights(w, seed)
    y_ref = x @ W.T
    y = y_ref.copy()
    latency = (w.input_dim * w.output_dim * w.layers) * 2.2e-9 * w.samples
    energy = (w.input_dim * w.output_dim * w.layers) * 18e-12 * w.samples
    return y_ref, y, latency, energy


def run_photonic(w: Workload, seed: int = 7, noise_std: float = 0.002,
                 core_latency_s: float = 2e-12, core_energy_j: float = 5e-15):
    x, W = _inputs_and_weights(w, seed)
    y_ref = x @ W.T
    rng = np.random.default_rng(seed + 1000)
    y = y_ref + rng.normal(0, noise_std, size=y_ref.shape)
    # Full-system model intentionally includes conversion and control overhead.
    per_sample_latency = core_latency_s * w.layers + 90e-9 + 35e-9 + 60e-9
    per_sample_energy = (
        core_energy_j * (w.input_dim * w.output_dim) * w.layers
        + 0.42e-6 + 0.18e-6 + 0.06e-6
    )
    return y_ref, y, per_sample_latency * w.samples, per_sample_energy * w.samples


def compare_outputs(ref: np.ndarray, pred: np.ndarray):
    err = np.abs(ref - pred)
    return float(err.max()), float(err.mean())


def evaluate(w: Workload, backend: str, seed: int = 7) -> RunResult:
    if backend == "electronic":
        ref, pred, latency, energy = run_electronic(w, seed)
    elif backend == "photonic-model":
        ref, pred, latency, energy = run_photonic(w, seed)
    else:
        raise ValueError(f"Unknown backend: {backend}")

    max_err, mean_err = compare_outputs(ref, pred)
    tol = 0.01
    accuracy_proxy = float(np.mean(np.abs(ref - pred) <= tol))
    return RunResult(
        backend=backend,
        workload=w.name,
        samples=w.samples,
        latency_ms_total=latency * 1e3,
        latency_ms_per_sample=(latency / w.samples) * 1e3,
        energy_j_total=energy,
        energy_j_per_sample=energy / w.samples,
        top1_accuracy=accuracy_proxy,
        max_abs_error=max_err,
        mean_abs_error=mean_err,
        passed_accuracy=accuracy_proxy >= w.accuracy_target,
        passed_error=max_err <= 0.05,
    )


def load_workload(path: str) -> Workload:
    return Workload(**json.loads(pathlib.Path(path).read_text()))


def save_results(results: List[RunResult], path: str) -> None:
    target = pathlib.Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps([asdict(r) for r in results], indent=2))
