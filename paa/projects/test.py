from src.recursive import partition_recursive
from src.dynamic import partition_dynamic


items = [1, 5, 10, 20, 30, 40, 50]


for item in items:
    result = partition_recursive(item, item)
    print(f"Recursive partition of {item}: {result}")

    result = partition_dynamic(item)
    print(f"Dynamic partition of {item}: {result}")
