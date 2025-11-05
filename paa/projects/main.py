
from src.recursive import partition_recursive
from src.dynamic import partition_dynamic
from src.eval import benchmark

import os
import csv
from typing import List

import matplotlib.pyplot as plt


def run_benchmarks(test_values: List[int]) -> str:
    """Roda os benchmarks, grava CSV com resultados e gera gráficos.

    Retorna o caminho para a pasta `results` contendo os artefatos.
    """
    os.makedirs("results", exist_ok=True)
    csv_path = os.path.join("results", "results.csv")

    headers = [
        "n",
        "rec_result",
        "dp_result",
        "rec_time_s",
        "dp_time_s",
        "rec_mem_kb",
        "dp_mem_kb",
    ]

    ns = []
    rec_times = []
    dp_times = []
    rec_mems = []
    dp_mems = []

    with open(csv_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(headers)

        for n in test_values:
            print(f"n = {n}")

            rec_result, rec_time, rec_mem = benchmark(
                partition_recursive, n, n
            )
            dp_result, dp_time, dp_mem = benchmark(partition_dynamic, n)

            writer.writerow([
                n,
                rec_result,
                dp_result,
                f"{rec_time:.9f}",
                f"{dp_time:.9f}",
                f"{rec_mem:.6f}",
                f"{dp_mem:.6f}",
            ])

            ns.append(n)
            rec_times.append(rec_time)
            dp_times.append(dp_time)
            rec_mems.append(rec_mem)
            dp_mems.append(dp_mem)

    # Tempo vs n
    plt.figure(figsize=(8, 5))
    plt.plot(ns, rec_times, marker="o", label="Recursivo (memo)")
    plt.plot(ns, dp_times, marker="o", label="Dinâmico")
    plt.xlabel("N Valores de Entrada")
    plt.ylabel("Tempo (s)")
    plt.title("Tempo de execução vs tamanho da entrada")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    time_plot_path = os.path.join("results", "time_vs_n.png")
    plt.savefig(time_plot_path)
    plt.close()

    # Memória vs n
    plt.figure(figsize=(8, 5))
    plt.plot(ns, rec_mems, marker="o", label="Recursivo (peak KB)")
    plt.plot(ns, dp_mems, marker="o", label="Dinâmico (peak KB)")
    plt.xlabel("n")
    plt.ylabel("Memória (KB)")
    plt.title("Uso de memória (pico) vs tamanho da entrada")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    mem_plot_path = os.path.join("results", "memory_vs_n.png")
    plt.savefig(mem_plot_path)
    plt.close()

    print(f"Artefatos gravados em: {os.path.abspath('results')}")
    return os.path.abspath("results")


if __name__ == "__main__":
    test_values = [4, 10, 20, 30, 40, 50, 100]
    print("\n=== Comparativo: Partições Inteiras ===\n")
    run_benchmarks(test_values)
