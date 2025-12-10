from os.path import abspath, dirname, join

from .data_generation import load_dataset, Interval


ROOT = dirname(dirname(abspath(__file__)))


random: list[list[Interval]] = [
    load_dataset(join(ROOT, "datasets/10_random.json"), False),
    load_dataset(join(ROOT, "datasets/100_random.json"), False),
    load_dataset(join(ROOT, "datasets/1000_random.json"), False),
    load_dataset(join(ROOT, "datasets/10000_random.json"), False),
]

sorted: list[list[Interval]] = [
    load_dataset(join(ROOT, "datasets/10_ordered.json"), True),
    load_dataset(join(ROOT, "datasets/100_ordered.json"), True),
    load_dataset(join(ROOT, "datasets/1000_ordered.json"), True),
    load_dataset(join(ROOT, "datasets/10000_ordered.json"), True),
]

shuffled: list[list[Interval]] = [
    load_dataset(join(ROOT, "datasets/10_shuffled.json"), False),
    load_dataset(join(ROOT, "datasets/100_shuffled.json"), False),
    load_dataset(join(ROOT, "datasets/1000_shuffled.json"), False),
    load_dataset(join(ROOT, "datasets/10000_shuffled.json"), False),
]
