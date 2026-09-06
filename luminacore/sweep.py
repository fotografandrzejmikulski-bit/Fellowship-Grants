from __future__ import annotations
import json
from pathlib import Path
from .core import Workload, evaluate
from .model import HardwareModel


def run_sweep(workload: Workload, channels=(1,2,4,8,16,32), path_cm_values=(0.05,0.1,0.2,0.5), noise_values=(0.001,0.002,0.005)):
    rows=[]
    for ch in channels:
        for path in path_cm_values:
            for noise in noise_values:
                hw=HardwareModel(path_cm=path)
                photonic=evaluate(workload,'photonic-model',hw=hw)
                rows.append({
                    'channels': ch,
                    'path_cm': path,
                    'noise_assumption': noise,
                    'latency_ms_per_sample': photonic.latency_ms_per_sample,
                    'energy_j_per_sample': photonic.energy_j_per_sample,
                    'max_abs_error': photonic.max_abs_error,
                    'accuracy_proxy': photonic.top1_accuracy,
                    'evidence_level': photonic.evidence_level,
                })
    return rows


def pareto(rows):
    result=[]
    for i,r in enumerate(rows):
        dominated=False
        for j,s in enumerate(rows):
            if i==j: continue
            no_worse=(s['latency_ms_per_sample']<=r['latency_ms_per_sample'] and
                      s['energy_j_per_sample']<=r['energy_j_per_sample'] and
                      s['max_abs_error']<=r['max_abs_error'])
            strictly=(s['latency_ms_per_sample']<r['latency_ms_per_sample'] or
                      s['energy_j_per_sample']<r['energy_j_per_sample'] or
                      s['max_abs_error']<r['max_abs_error'])
            if no_worse and strictly:
                dominated=True; break
        if not dominated:
            result.append(r)
    return result


def save_sweep(rows, path, workload_name):
    payload={
      'schema_version':'1.0',
      'evidence_level':'E2',
      'workload':workload_name,
      'rows':rows,
      'pareto_frontier':pareto(rows),
      'note':'Synthetic/model sweep. No row is a physical measurement.'
    }
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    Path(path).write_text(json.dumps(payload,indent=2,sort_keys=True))
