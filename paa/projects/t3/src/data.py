"""Gerador de datasets para testes de interval scheduling.

Gera arquivos JSON em `datasets/` com intervalos representados
como listas [start, end], garantindo `end > start` para cada
intervalo. Para cada tamanho em [10, 100, 1000, 10000] cria três
variedades:
 - ordered: ordenados por tempo de término (end asc)
 - shuffled: mesma lista ordenada, embaralhada
 - random: pares gerados aleatoriamente (não ordenados)

Uso:
	python3 src/data.py

Os arquivos gerados têm nomes como `datasets/10_ordered.json`.
"""

from __future__ import annotations

import json
import os
import random


Interval = tuple[int, int]


def generate_random_intervals(
    n: int,
    max_coord: int | None = None
) -> list[Interval]:
    """
    Gera `n` intervalos aleatórios garantindo end > start.

    Args:
        n (int): número de intervalos a serem gerados.
        max_coord (int | None): valor máximo para coordenadas
            start e end. Se None, usa `max(10, n * 10)`.
    Returns:
        list[Interval]: lista de intervalos gerados.
    """
    if n <= 0:
        return []

    if max_coord is None:
        max_coord = max(10, n * 10)

    intervals: list[Interval] = []
    for _ in range(n):
        start = random.randint(0, max_coord - 1)
        # comprimento mínimo 1
        length = random.randint(1, max(1, max_coord // 10))
        end = start + length
        intervals.append((start, end))

    return intervals


def write_json(path: str, data: list[Interval]) -> None:
    """
    Salva lista de intervalos em arquivo JSON no caminho dado.

    Args:
        path (str): caminho do arquivo a ser salvo.
        data (list[Interval]): lista de intervalos a serem salvos.
    Returns:
        None
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump([[s, e] for s, e in data], f, ensure_ascii=False)


def generate_and_save_all(
    sizes: tuple[int, ...] = (10, 100, 1000, 10000)
) -> list[str]:
    """
    Gera e salva datasets retornando lista de caminhos criados.

    Args:
        sizes (tuple[int, ...]): tamanhos dos datasets a serem gerados.

    Returns:
        list[str]: caminhos dos arquivos JSON criados.
    """
    created = []
    for n in sizes:
        base_max = max(10, n * 10)
        # Random (não ordenado)
        rand = generate_random_intervals(n, max_coord=base_max)
        path_rand = f"datasets/{n}_random.json"
        write_json(path_rand, rand)
        created.append(path_rand)

        # Ordered: ordenar por tempo de término (end crescente)
        ordered = sorted(rand, key=lambda x: x[1])
        path_ord = f"datasets/{n}_ordered.json"
        write_json(path_ord, ordered)
        created.append(path_ord)

        # Shuffled: mesma lista ordenada, embaralhada
        shuffled = ordered.copy()
        random.shuffle(shuffled)
        path_shuf = f"datasets/{n}_shuffled.json"
        write_json(path_shuf, shuffled)
        created.append(path_shuf)

    return created


if __name__ == "__main__":
    random.seed(42)
    sizes = [10, 100, 1000, 10000]
    print("Gerando datasets (ordenados, desordenados e aleatórios)...")
    paths = generate_and_save_all(sizes)
    print("Arquivos criados:")
    for p in paths:
        print(" -", p)
