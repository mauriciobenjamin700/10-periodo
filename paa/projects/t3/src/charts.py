from __future__ import annotations


import matplotlib.pyplot as plt


Results = list[dict[str, str]]


def load_data(
    file: str = "backtrack_benchmark_results.json"
) -> Results:
    """
    Carrega resultados de benchmark de arquivo JSON.

    Args:
        file (str): caminho do arquivo JSON.
    Returns:
        list[dict[str, str]]: lista de resultados carregados.
    """
    import json

    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data


def plot_benchmark_results(
    results: Results,
    algorithm: str,
    dataset: str
) -> None:
    """
    Plota resultados de benchmark para um algoritmo e dataset específicos.

    Args:
        results (Results): lista de resultados de benchmark.
        algorithm (str): nome do algoritmo a ser plotado.
        dataset (str): nome do dataset a ser plotado.
    Returns:
        None
    """
    filtered = [
        r for r in results
        if r["Algorithm"] == algorithm and r["Dataset"] == dataset
    ]
    quantities = [int(r["Quantity"]) for r in filtered]
    times = [float(r["Time (s)"]) for r in filtered]
    memories = [float(r["Memory (KB)"]) for r in filtered]

    plt.figure(figsize=(12, 5))

    plt.subplot(1, 2, 1)
    plt.plot(quantities, times, marker='o')
    # plt.xscale('log')
    # plt.yscale('log')
    plt.xlabel('Número de Intervalos')
    plt.ylabel('Tempo (s)')
    plt.title(f'Tempo Gasto - {algorithm} com {dataset} Intervalos')
    plt.grid(True)

    plt.subplot(1, 2, 2)
    plt.plot(quantities, memories, marker='o', color='orange')
    # plt.xscale('log')
    # plt.yscale('log')
    plt.xlabel('Número de Intervalos')
    plt.ylabel('Memória (KB)')
    plt.title(f'Memória Gasta - {algorithm} com {dataset} Intervalos')
    plt.grid(True)

    out = f"benchmark_{algorithm}_{dataset}.png"
    plt.tight_layout()
    plt.savefig(out)
    print("Saved:", out)
    plt.close()
