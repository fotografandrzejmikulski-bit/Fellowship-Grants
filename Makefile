test:
	PYTHONPATH=. pytest -q
benchmark:
	PYTHONPATH=. python -m luminacore.cli --scenario scenarios/edge_proprioception_small.json --out results/latest.json
stress:
	PYTHONPATH=. python -m luminacore.cli --scenario scenarios/edge_proprioception_stress.json --out results/stress.json
sweep:
	PYTHONPATH=. python -m luminacore.sweep_cli --scenario scenarios/edge_proprioception_small.json --out results/sweep.json

all: test benchmark stress sweep
