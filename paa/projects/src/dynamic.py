def partition_dynamic(n: int) -> int:
    """
    Calcula o número de partições inteiras de 'n' usando programação dinâmica
    iterativa.

    Ideia:
        dp[i] representa o número de formas de escrever o número i
        usando inteiros positivos (ordem não importa).

    Transição:
        dp[i] += dp[i - num] para cada num <= i.

    Parâmetros:
        n (int): O número inteiro a ser particionado.

    Retorna:
        int: Quantidade de partições possíveis.
    """
    dp = [0] * (n + 1)
    dp[0] = 1

    for num in range(1, n + 1):
        for i in range(num, n + 1):
            dp[i] += dp[i - num]

    return dp[n]
