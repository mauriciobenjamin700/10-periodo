def is_compatible(
    selected: list[tuple[int, int]],
    interval: tuple[int, int]
) -> bool:
    """
    Verifica se um intervalo pode ser adicionado sem sobreposição.

    Args:
        selected (list[tuple[int, int]]): Lista de intervalos já selecionados.
        interval (tuple[int, int]): Intervalo a ser verificado.

    Returns:
        bool: True se o intervalo for compatível, False caso contrário.
    """
    start, end = interval
    for start_selected, end_selected in selected:
        # Se sobrepõe
        if not (end <= start_selected or start >= end_selected):
            return False
    return True


def backtrack(
    i: int,
    current_solution: list[tuple[int, int]],
    intervals: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """
    Função auxiliar externa de backtracking que retorna a melhor solução
    encontrada a partir do índice `i` dado o estado `current_solution`.

    Args:
        i (int): índice atual na lista de intervalos
        current_solution (list[tuple[int, int]]): solução parcial
            (mutada durante a recursão)
        intervals (list[tuple[int, int]]): lista de intervalos ordenada

    Returns:
        A melhor solução (lista de intervalos) encontrada neste ramo.
    """
    # Caso base: percorremos todos os intervalos
    if i == len(intervals):
        return current_solution.copy()

    best: list[tuple[int, int]] = []

    # Tentativa 1: incluir o intervalo i, se for compatível
    if is_compatible(current_solution, intervals[i]):
        current_solution.append(intervals[i])
        best_incl = backtrack(i + 1, current_solution, intervals)
        if len(best_incl) > len(best):
            best = best_incl
        current_solution.pop()

    # Tentativa 2: não incluir o intervalo i
    best_excl = backtrack(i + 1, current_solution, intervals)
    if len(best_excl) > len(best):
        best = best_excl

    return best


def interval_scheduling_backtracking(
    intervals: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    """
    Seleciona o maior número de intervalos não sobrepostos usando
    um algoritmo de backtracking.

    Args:
        intervals (list[tuple[int, int]]): Lista de tuplas representando
            os intervalos (início, fim).

    Returns:
        list[tuple[int, int]]: Lista de intervalos selecionados.
    """

    # Ordenar intervalos pode ajudar o backtracking a encontrar boas
    # soluções cedo (heurística).

    intervals = sorted(intervals, key=lambda x: x[1])
    return backtrack(0, [], intervals)


if __name__ == "__main__":
    intervals = [
        (1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11)
    ]
    print("Backtracking:", interval_scheduling_backtracking(intervals))
