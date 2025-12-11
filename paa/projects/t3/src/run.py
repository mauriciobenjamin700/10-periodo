import json

from src.backtracking import interval_scheduling_dp
from src.data import random, sorted, shuffled
from src.eval import benchmark
from src.greedy import interval_scheduling_greedy


def main() -> None:
    """
    Executa benchmarks para diferentes algoritmos e datasets,
    salvando os resultados em um arquivo JSON.
    """
    algorithms = {
        "Greedy": interval_scheduling_greedy,
        "Dynamic Programming": interval_scheduling_dp,
    }

    datasets = {
        "Random": random,
        "Sorted": sorted,
        "Shuffled": shuffled,
    }

    results: list[dict[str, str]] = []

    for algo_name, algo_func in algorithms.items():
        for data_name, data_variants in datasets.items():
            print(f"Algorithm: {algo_name}, Dataset: {data_name}")
            for i, dataset in enumerate(data_variants[:2]):
                result, elapsed, memory = benchmark(algo_func, dataset)
                print(
                    f"  Variant {i + 1}: "
                    f"Result Size = {len(result)}, "
                    f"Time = {elapsed:.6f} s, "
                    f"Memory = {memory:.2f} KB"
                )
                results.append({
                    "Algorithm": algo_name,
                    "Dataset": data_name,
                    "Quantity": str(len(dataset)),
                    "Variant": str(i + 1),
                    "Result Size": str(len(result)),
                    "Time (s)": f"{elapsed:.6f}",
                    "Memory (KB)": f"{memory:.2f}",
                })
            print()
    with open("benchmark_results.json", "w") as f:
        json.dump(results, f, indent=4)
