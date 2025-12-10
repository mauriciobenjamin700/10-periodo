def interval_scheduling_greedy(
    intervals: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """
    Seleciona o maior número de intervalos não sobrepostos usando um
    algoritmo guloso.

    Args:
        intervals (list[tuple[int, int]]): Lista de tuplas representando
            os intervalos (início, fim).

    Returns:
        list[tuple[int, int]]: Lista de intervalos selecionados.
    """
    # Ordena pelo tempo de término
    intervals = sorted(intervals, key=lambda x: x[1])

    selected = []
    last_end = float('-inf')

    for start, end in intervals:
        # Se não sobrepõe com o último selecionado
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


__all__ = [
    "interval_scheduling_greedy",
]

if __name__ == "__main__":

    intervals = [
        (1, 4),
        (3, 5),
        (0, 6),
        (5, 7),
        (3, 9),
        (5, 9),
        (6, 10),
        (8, 11)
    ]
    print("Guloso:", interval_scheduling_greedy(intervals))
