import argparse
from .core import load_workload
from .sweep import run_sweep, save_sweep, pareto

def main():
    p=argparse.ArgumentParser(description='LuminaCore architecture sweep and Pareto analysis')
    p.add_argument('--scenario',default='scenarios/edge_proprioception_small.json')
    p.add_argument('--out',default='results/sweep.json')
    args=p.parse_args()
    w=load_workload(args.scenario)
    rows=run_sweep(w)
    save_sweep(rows,args.out,w.name)
    print(f'Generated {len(rows)} modeled configurations; Pareto points={len(pareto(rows))}')
    return 0
if __name__=='__main__': raise SystemExit(main())
