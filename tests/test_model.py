import numpy as np
from luminacore.core import Workload, evaluate
from luminacore.device import db_to_linear

def test_db_conversion():
    assert np.isclose(db_to_linear(0), 1.0)
    assert db_to_linear(3) < 1

def test_reproducibility():
    w=Workload('t',8,4,2,16,0.8)
    a=evaluate(w,'photonic-model'); b=evaluate(w,'photonic-model')
    assert a.energy_j_total == b.energy_j_total
    assert a.max_abs_error == b.max_abs_error

def test_evidence_is_model_not_measurement():
    w=Workload('t',8,4,1,8,0.8)
    for backend in ('electronic','photonic-model'):
        assert evaluate(w,backend).evidence_level == 'E2'
