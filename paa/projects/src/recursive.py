# def partition_recursive_memo(
#     n: int,
#     k: int,
#     memo: dict[tuple[int, int], int] | None = None
# ) -> int:
#     """
#     Calcula o número de partições inteiras de 'n' usando números até 'k'
#     (inclusive), de forma recursiva com memoization.

#     Uma partição de 'n' é uma forma de escrevê-lo como soma de inteiros
#     positivos, desconsiderando a ordem dos termos
#     (ex: 4 = 3+1 = 2+2 = 2+1+1 = 1+1+1+1).

#     Fórmula recursiva:
#         P(n, k) = P(n, k-1) + P(n-k, k)

#     Parâmetros:
#         n (int): O número inteiro a ser particionado.
#         k (int): O maior número permitido nas somas. Ex: para k=3, só
#                  podem ser usados 1, 2 e 3.
#                  Logo P(4, 3) = 4 (3+1, 2+2, 2+1+1, 1+1+1+1)
#         memo (dict): Cache opcional para armazenar resultados de subproblemas

#     Retorna:
#         int: Quantidade de partições possíveis.
#     """
#     if memo is None:
#         memo = {}

#     if (n, k) in memo:
#         return memo[(n, k)]

#     if n == 0:
#         return 1
#     if n < 0 or k == 0:
#         return 0

#     result = (
#         partition_recursive(n, k - 1, memo)
#         +
#         partition_recursive(n - k, k, memo)
#     )
#     memo[(n, k)] = result
#     return result


def partition_recursive(n: int, k: int) -> int:
    """
    Calcula o número de partições inteiras de 'n' usando números até 'k'
    (inclusive), de forma recursiva sem memoization.

    Atenção: complexidade exponencial; para n/k maiores o tempo cresce muito.
    """
    if n == 0:
        return 1
    if n < 0 or k == 0:
        return 0
    return (
        partition_recursive(n, k - 1)
        + partition_recursive(n - k, k)
    )
