from luminacore.core import Workload, compare_outputs, evaluate
import numpy as np


def test_zero_error():
    a = np.array([[1.0, 2.0]])
    maximum, mean = compare_outputs(a, a)
    assert maximum == 0.0
    assert mean == 0.0


def test_both_backends_run():
    workload = Workload("test", 8, 4, 2, 16, 0.90)
    electronic = evaluate(workload, "electronic")
    photonic = evaluate(workload, "photonic-model")
    assert electronic.samples == photonic.samples == 16
    assert electronic.energy_j_per_sample > 0
    assert photonic.energy_j_per_sample > 0


def test_photonic_model_is_deterministic():
    workload = Workload("det", 16, 8, 2, 32, 0.90)
    a = evaluate(workload, "photonic-model")
    b = evaluate(workload, "photonic-model")
    assert a == b
