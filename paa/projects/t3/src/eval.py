from typing import Callable
import time
import tracemalloc


def benchmark(
    func: Callable[..., int],
    *args: tuple[int]
) -> tuple[int, float, float]:
    """
    Executa uma função medindo tempo e memória.

    Parâmetros:
        func (callable): Função a ser testada.
        *args: Argumentos a serem passados à função.

    Retorna:
        tuple: (resultado, tempo_em_segundos, memória_em_kb)
    """
    tracemalloc.start()
    start_time = time.perf_counter()

    result = func(*args)

    end_time = time.perf_counter()
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    elapsed = end_time - start_time
    memory_kb = peak / 1024
    return result, elapsed, memory_kb
