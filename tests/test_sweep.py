from luminacore.core import Workload
from luminacore.sweep import run_sweep, pareto

def test_sweep_and_pareto():
    w=Workload('t',8,4,1,8,0.8)
    rows=run_sweep(w,channels=(1,2),path_cm_values=(0.1,0.2),noise_values=(0.001,))
    assert len(rows)==4
    frontier=pareto(rows)
    assert len(frontier)>=1
    assert all(r['evidence_level']=='E2' for r in frontier)
