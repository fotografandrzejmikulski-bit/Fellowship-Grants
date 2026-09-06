import argparse
from .core import load_workload, evaluate, save_results


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the LuminaCore evidence-first benchmark harness")
    parser.add_argument("--scenario", default="scenarios/edge_proprioception_small.json")
    parser.add_argument("--out", default="results/latest.json")
    args = parser.parse_args()
    workload = load_workload(args.scenario)
    results = [evaluate(workload, "electronic"), evaluate(workload, "photonic-model")]
    save_results(results, args.out)
    for result in results:
        print(
            f"{result.backend}: latency={result.latency_ms_per_sample:.9f} ms/sample, "
            f"energy={result.energy_j_per_sample:.6e} J/sample, "
            f"max_error={result.max_abs_error:.6f}, accuracy_proxy={result.top1_accuracy:.4f}"
        )
    print("Evidence level: E2_SIMULATION_MODEL (not a hardware measurement).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
