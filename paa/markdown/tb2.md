# Problema das Partições Inteiras

**Equipe:**

* Mauricio Benjamin
* Pedro Vital

---

## Introdução

O presente trabalho tem como objetivo comparar o desempenho entre duas abordagens clássicas para a solução do **problema das partições inteiras**, utilizando **implementações recursivas** e **de Programação Dinâmica (PD)**. O problema das partições consiste em determinar de quantas formas um número inteiro positivo ( n ) pode ser escrito como soma de inteiros positivos, desconsiderando a ordem dos termos. Por exemplo, para ( n = 4 ), existem 5 partições possíveis:
4, 3+1, 2+2, 2+1+1, e 1+1+1+1.

A escolha desse problema se justifica por seu caráter didático e pela clara demonstração da diferença entre uma abordagem **recursiva pura**, de complexidade exponencial, e uma abordagem **dinâmica**, que explora a **reutilização de sub resultados** para otimizar o desempenho. O objetivo é analisar comparativamente o **tempo de execução** e o **uso de memória** de ambas as implementações, avaliando empiricamente os ganhos obtidos com a Programação Dinâmica.

---

## Metodologia

A metodologia deste trabalho consistiu buscar material refente ao problema proposta, visando entendimento da problemática e ideação para a resolver. Posteriormente foram implementados os algoritmos, tanto recursivo quando dinâmico, além de algoritmos para analisar em diferentes casos, como tempo e consumo de memória, para avaliar em quais cenários cada abordagem se  destaca.

A  Figura 1 apresenta a metodologia adotada

![Metodologia](../projects/examples/flow.png)

Figura 1. Metodologia adotada para este trabalho

### Implementações

Foram avaliadas duas funções principais:

#### Recursiva direta (sem memorização)

```python
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

```

Baseia-se na relação:

P(n,k) = P(n,k-1) + P(n-k,k)

Exemplo de teste de mesa (n = 4) mostrando todos os passos da recursão da função partition_recursive(n,k).

Notação: P(n,k) = partition_recursive(n,k).

Em cada nó há duas opções — "excluir k" => P(n,k-1) ou "incluir k" => P(n-k,k). Quando n==0 retorna 1 (uma partição encontrada); quando n<0 ou k==0 retorna 0.

Árvore de chamadas (expansão e retornos):

```bash
P(4,4)
excluir 4 -> P(4,3)
excluir 3 -> P(4,2)
excluir 2 -> P(4,1)
excluir 1 -> P(4,0) => k==0 -> 0
incluir 1 -> P(3,1)
excluir 1 -> P(3,0) => 0
incluir 1 -> P(2,1)
excluir 1 -> P(2,0) => 0
incluir 1 -> P(1,1)
excluir 1 -> P(1,0) => 0
incluir 1 -> P(0,1) => n==0 -> 1 (leads to partition [1,1,1,1])
=> P(1,1) = 1
=> P(2,1) = 1
=> P(3,1) = 1
=> P(4,1) = 1
incluir 2 -> P(2,2)
excluir 2 -> P(2,1) [já acima] => 1
incluir 2 -> P(0,2) => 1 (leads to partition [2,2])
=> P(2,2) = 1 + 1 = 2
=> P(4,2) = P(4,1) + P(2,2) = 1 + 2 = 3
=> P(4,2) = 3
incluir 3 -> P(1,3)
excluir 3 -> P(1,2)
excluir 2 -> P(1,1) => 1 (veja acima)
incluir 2 -> P(-1,2) => n<0 -> 0
=> P(1,2) = 1
incluir 3 -> P(-2,3) => n<0 -> 0
=> P(1,3) = 1 + 0 = 1 (leads to partition [3,1])
=> P(4,3) = P(4,2) + P(1,3) = 3 + 1 = 4
incluir 4 -> P(0,4) => n==0 -> 1 (leads to partition [4])
=> P(4,4) = P(4,3) + P(0,4) = 4 + 1 = 5
Partições correspondentes encontradas:

[4]
[3,1]
[2,2]
[2,1,1]
[1,1,1,1]
```

Conclusão: a função percorre a árvore de decisões “incluir/excluir” e soma 1 para cada folha que atinge n==0; para n=4 o resultado final é 5, enumerando as cinco partições acima.

#### Programação Dinâmica (iterativa)

```python
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
```

Exemplo de teste de mesa (n = 4) mostrando todos os passos da função partition_dynamic(n,k).

```bash
n = 4
dp (inicial) = [1, 0, 0, 0, 0]
# dp[x] = número de partições de x considerando os números já processados
```

`Iteração num = 1 (processando peças de valor 1)`
F
Antes: dp = [1, 0, 0, 0, 0]

Atualizações internas:

```bash
i = 1: dp[1] += dp[0] -> 0 + 1 = 1    => dp = [1, 1, 0, 0, 0]
i = 2: dp[2] += dp[1] -> 0 + 1 = 1    => dp = [1, 1, 1, 0, 0]
i = 3: dp[3] += dp[2] -> 0 + 1 = 1    => dp = [1, 1, 1, 1, 0]
i = 4: dp[4] += dp[3] -> 0 + 1 = 1    => dp = [1, 1, 1, 1, 1]
```

dp depois de num=1 representa partições que usam só 1.

`Iteração num = 2 (processando peças de valor 2)`

Antes: dp = [1, 1, 1, 1, 1]

Atualizações internas:

```bash
i = 2: dp[2] += dp[0] -> 1 + 1 = 2    => dp = [1, 1, 2, 1, 1]
i = 3: dp[3] += dp[1] -> 1 + 1 = 2    => dp = [1, 1, 2, 2, 1]
i = 4: dp[4] += dp[2] -> 1 + 2 = 3    => dp = [1, 1, 2, 2, 3]
```

Em i=2, adicionamos a partição [2] às existentes → dp[2]=2 ([1+1], [2]).

Em i=3, adicionamos combinações que terminam com 2 → [2+1] → dp[3]=2.

Em i=4, usamos dp[2] (já atualizado com num=2) para contar combinações com múltiplos 2s (por ex. 2+2) → dp[4]=3.

Observação: usar i crescente permite reutilizar o mesmo num várias vezes (2+2).

`Iteração num = 3 (processando peças de valor 3)`

Antes: dp = [1, 1, 2, 2, 3]

Atualizações internas:

```bash
i = 3: dp[3] += dp[0] -> 2 + 1 = 3    => dp = [1, 1, 2, 3, 3]
i = 4: dp[4] += dp[1] -> 3 + 1 = 4    => dp = [1, 1, 2, 3, 4]
```

dp[3] incorpora [3]; dp[4] incorpora partições que usam 3 (ex.: 3+1).

`Iteração num = 4 (processando peças de valor 4)`

Antes: dp = [1, 1, 2, 3, 4]

Atualizações internas:

```bash
i = 4: dp[4] += dp[0] -> 4 + 1 = 5    => dp = [1, 1, 2, 3, 5]
```

Interpretação final: dp[4] = 5

`Estado final e correspondência com partições`

```bash
dp final = [1, 1, 2, 3, 5]
dp[4] = 5
Partições de 4 (ordem irrelevante):
1) 1+1+1+1
2) 2+1+1
3) 2+2
4) 3+1
5) 4
```

Observações sobre as iterações

* A dupla iteração (num de 1..n e i de num..n, com i em ordem crescente) assegura:
  * num pode ser usado repetidamente (ex.: 2+2).
  * Não são contadas permutações distintas da mesma combinação (ex.: 1+3 e 3+1 são a mesma partição e só aparecem uma vez), porque a construção acrescenta formas na ordem dos 
* Se iterássemos i em ordem decrescente dentro do loop, o efeito mudaria (cada num só poderia ser usado no máximo uma vez) — útil para problemas 0/1, não para partições ilimitadas.

### Procedimento experimental

Os testes foram feitos, usando como base a função `benchmark` para calcular o  custo de memoria e tempo de execução de  cada função, estratégia (recursiva ou dinâmica). Dado  que  ambas as funções receberam os seguintes valores de entrada para N:

```bash
items = [1, 5, 10, 20, 30, 40, 50]
```

```python
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
```

## Resultados

As Tabelas apresentam os resultados obtidos, ilustrado que para uma abordagem voltada para a necessidade de  velocidade no processo, a  Programação Dinâmica se destaca, enquanto que para casos onde o uso de memória alocada é essencial, devemos dar preferência ao uso da Programação Recursiva.

Tabela 1. Tabela de resultados e tempos de execução

|  n | Recursivo (resultado) | Dinâmico (resultado) | Recursivo (s) | Dinâmico (s) |
| -: | --------------------: | -------------------: | ------------: | -----------: |
|  4 |                     5 |                    5 |   0.000004894 |  0.000006787 |
| 10 |                    42 |                   42 |   0.000010087 |  0.000006420 |
| 20 |                   627 |                  627 |   0.000176126 |  0.000020861 |
| 30 |                  5604 |                 5604 |   0.001427475 |  0.000065593 |
| 40 |                 37338 |                37338 |   0.010669526 |  0.000138066 |
| 50 |                204226 |               204226 |   0.066098276 |  0.000460070 |

Tabela 2. Tabela de uso de memória (pico, KB)

|  n | Recursivo (KB) | Dinâmico (KB) |
| -: | -------------: | ------------: |
|  4 |       0.000000 |      0.164062 |
| 10 |       0.031250 |      0.210938 |
| 20 |       0.062500 |      0.414062 |
| 30 |       0.093750 |      0.804688 |
| 40 |       0.156250 |      1.195312 |
| 50 |       0.218750 |      1.585938 |

### Gasto de Memória e Tempo de Execução

As Figuras 2 e 3 apresentam os resultados obtidos da experimentação, de forma visual, onde podemos observar o grau de crescimento de tempo gasto da programação recursiva, quanto maior o valor de N. Vale salientar que quando a questão é o pico de memória alocada para  operações, o uso de programação dinâmica pode não ser a melhor solução para o problema, pois tende a crescer muito, em relação ao da  programação recursiva.

* ![Tempo Gasto](../projects/results/time_vs_n.png)

Figura 2. Comparativo de tempo gasto, dado entradas de valor N variadas

* ![Memória Gasta](../projects/results/memory_vs_n.png)

Figura 2. Comparativo de pico de memória alocada, dado entradas de valor N variadas

### Análise dos resultados

De acordo com os dados coletados, a Programação Dinâmica (PD) apresenta vantagem clara em tempo de execução, enquanto a solução recursiva direta consome menos memória de pico, porém escala muito pior em tempo.

Principais observações:

* Tempo: para N pequenos (p.ex. 4 ou 10) os tempos são comparáveis, mas a partir de N maiores a diferença cresce rapidamente. Ex.: N=30 — recursivo 0.001427s vs dinâmico 0.0000656s; N=40 — recursivo 0.01067s vs dinâmico 0.000138s; N=50 — recursivo 0.06610s vs dinâmico 0.000460s (≈143× mais rápido para PD em N=50).
* Memória (pico): a implementação dinâmica usa mais memória devido ao vetor dp de tamanho O(n). Ex.: N=50 — recursivo ≈0.2188 KB vs dinâmico ≈1.5859 KB (≈7× maior para PD). Para N pequenos a diferença é desprezível.
* Tendência: o tempo da versão recursiva cresce de forma exponencial/praticamente inviável para N maiores; a versão dinâmica cresce de forma muito mais suave (aproximadamente polinomial) e é mais estável e previsível.

Conclusão: para necessidades de desempenho em N moderados/altos, prefira a abordagem de Programação Dinâmica. Use a versão recursiva apenas para N pequenos, propósitos educativos ou quando a minimização absoluta de alocação adicional for imprescindível — mesmo assim, a recursão rapidamente se torna impraticável em tempo para valores maiores de N.

## Referências

[Introdução à teoria das partições de inteiros](https://www.obm.org.br/content/uploads/2020/02/23_SO_George_Lucas_Nivel_3_-Introducao_Teoria_das_particoes_de_inteiros_compressed.pdf)

[Combinação e Partições](https://www.youtube.com/watch?v=I4VIh-umY34)
