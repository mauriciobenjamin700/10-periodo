from src.charts import load_data, plot_benchmark_results


data = load_data("benchmark_results.json")

algorithms = [
    "Greedy",
    "Dynamic Programming",
]

datasets = [
    "Random",
    "Sorted",
    "Shuffled",
]


for algorithm in algorithms:
    for dataset in datasets:
        plot_benchmark_results(data, algorithm, dataset)
