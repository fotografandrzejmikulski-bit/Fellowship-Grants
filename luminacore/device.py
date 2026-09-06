from __future__ import annotations
from dataclasses import dataclass, asdict
import math

@dataclass(frozen=True)
class OpticalDeviceConfig:
    wavelength_nm: float = 1550.0
    waveguide_loss_db_cm: float = 1.0
    modulator_energy_j: float = 120e-15
    detector_energy_j: float = 80e-15
    adc_energy_j: float = 0.18e-6
    dac_energy_j: float = 0.12e-6
    control_energy_j: float = 0.06e-6
    laser_energy_j_per_sample: float = 0.42e-6
    phase_error_rms: float = 0.005
    detector_noise_std: float = 0.001

@dataclass(frozen=True)
class NonlinearityConfig:
    name: str = "VO2-candidate"
    threshold_w: float = 0.5e-3
    temporal_response_s: float = 1e-6
    hysteresis_fraction: float = 0.02
    insertion_loss_db: float = 1.5
    nonlinear_energy_j: float = 0.08e-6

@dataclass(frozen=True)
class ThermalConfig:
    ambient_c: float = 25.0
    delta_c_per_mw: float = 0.35
    phase_drift_per_c: float = 0.001

def db_to_linear(db: float) -> float:
    return 10 ** (-db / 10)

def config_to_dict(cfg) -> dict:
    return asdict(cfg)

def optical_path_penalty(config: OpticalDeviceConfig, path_cm: float) -> float:
    return db_to_linear(config.waveguide_loss_db_cm * path_cm)

def effective_phase_error(config: OpticalDeviceConfig, thermal: ThermalConfig, optical_power_mw: float) -> float:
    thermal_shift = thermal.phase_drift_per_c * thermal.delta_c_per_mw * optical_power_mw
    return math.sqrt(config.phase_error_rms**2 + thermal_shift**2)
