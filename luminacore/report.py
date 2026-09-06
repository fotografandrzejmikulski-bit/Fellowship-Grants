import json
from pathlib import Path


def report(path: str) -> None:
    rows = json.loads(Path(path).read_text())
    print("LuminaCore benchmark report")
    print("===========================")
    for row in rows:
        print(
            f"{row['backend']:18} | "
            f"{row['latency_ms_per_sample']:.9f} ms/sample | "
            f"{row['energy_j_per_sample']:.6e} J/sample | "
            f"max err {row['max_abs_error']:.6f} | "
            f"accuracy proxy {row['top1_accuracy']:.4f}"
        )
    if len(rows) >= 2:
        electronic, photonic = rows[0], rows[1]
        print("\nDirectional model comparison:")
        print(
            "latency ratio (electronic / photonic-model): "
            f"{electronic['latency_ms_per_sample'] / photonic['latency_ms_per_sample']:.3f}x"
        )
        print(
            "energy ratio (electronic / photonic-model): "
            f"{electronic['energy_j_per_sample'] / photonic['energy_j_per_sample']:.3f}x"
        )
        print("Evidence level: E2_SIMULATION_MODEL; not a hardware measurement.")
