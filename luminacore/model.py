from __future__ import annotations
from dataclasses import dataclass
import numpy as np
from .device import OpticalDeviceConfig, NonlinearityConfig, ThermalConfig, effective_phase_error, optical_path_penalty

@dataclass(frozen=True)
class HardwareModel:
    optical: OpticalDeviceConfig = OpticalDeviceConfig()
    nonlinear: NonlinearityConfig = NonlinearityConfig()
    thermal: ThermalConfig = ThermalConfig()
    path_cm: float = 0.2
    optical_power_mw: float = 2.0

    def linear_transform(self, x: np.ndarray, weights: np.ndarray, rng: np.random.Generator) -> np.ndarray:
        path_gain = optical_path_penalty(self.optical, self.path_cm)
        phase_sigma = effective_phase_error(self.optical, self.thermal, self.optical_power_mw)
        perturbation = rng.normal(0.0, phase_sigma, size=weights.shape)
        effective_weights = weights * path_gain + perturbation
        if x.shape[1] != effective_weights.shape[1]:
            raise ValueError(f'Input dimension {x.shape[1]} does not match layer dimension {effective_weights.shape[1]}')
        return x @ effective_weights.T

    def activation(self, x: np.ndarray) -> np.ndarray:
        # Smooth saturating surrogate for a device-level nonlinear transfer curve.
        # This is an abstract model, not a claim of measured VO2 behavior.
        gain = 1.0 / (1.0 + self.nonlinear.insertion_loss_db / 20.0)
        return gain * np.tanh(x)
