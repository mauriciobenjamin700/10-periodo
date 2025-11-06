# Problema das Partições Inteiras

**Equipe:**

* Mauricio Benjamin
* Pedro Vital

---

## Introdução

O presente trabalho tem como objetivo comparar o desempenho entre duas abordagens clássicas para a solução do **problema das partições inteiras**, utilizando **implementações recursivas** e **de Programação Dinâmica (PD)**.

O problema das partições consiste em determinar de quantas formas um número inteiro positivo ( n ) pode ser escrito como soma de inteiros positivos, desconsiderando a ordem dos termos. Por exemplo, para ( n = 4 ), existem 5 partições possíveis:
4, 3+1, 2+2, 2+1+1, e 1+1+1+1.

A escolha desse problema se justifica por seu caráter didático e pela clara demonstração da diferença entre uma abordagem **recursiva pura**, de complexidade exponencial, e uma abordagem **dinâmica**, que explora a **reutilização de subresultados** para otimizar o desempenho.

O objetivo é analisar comparativamente o **tempo de execução** e o **uso de memória** de ambas as implementações, avaliando empiricamente os ganhos obtidos com a Programação Dinâmica.

---

## Metodologia

### Implementações

Foram avaliadas duas funções principais presentes no repositório:

1. **Recursiva direta (sem memorização):**
   Função `partition_recursive(n, k)` localizada em `src/recursive.py`.
   Baseia-se na relação:
   [
   P(n,k) = P(n,k-1) + P(n-k,k)
   ]
   Essa versão possui complexidade exponencial no pior caso, devido à recomputação de subproblemas.

2. **Programação Dinâmica (iterativa):**
   Função `partition_dynamic(n)` localizada em `src/dynamic.py`.
   Utiliza um vetor `dp[0..n]` e aplica a transição clássica `dp[i] += dp[i-num]` para cada `num` em `1..n`, reduzindo o número de operações ao armazenar resultados intermediários.

### Procedimento experimental

Os testes foram realizados através do script `projects/main.py`, que atua como driver de experimentação. Para cada valor de ( n ) definido na lista `test_values`, o script executa ambas as funções e registra em um arquivo CSV:

* o número de partições obtido (para verificação da corretude dos resultados);
* o tempo de execução (em segundos), medido com `time.perf_counter`;
* o pico de memória (em kilobytes), obtido via `tracemalloc`.

Cada função foi executada uma única vez por valor de ( n ). Para medições mais estáveis, recomenda-se adaptar o código para realizar várias repetições e calcular médias, alterando o parâmetro `repeat` na função `benchmark` presente em `src/eval.py`.

### Artefatos gerados

Após a execução dos testes, os seguintes arquivos são produzidos automaticamente:

* `projects/results/results.csv`: contém os resultados numéricos (tempo e memória);
* `projects/results/time_vs_n.png`: gráfico de tempo em função de ( n );
* `projects/results/memory_vs_n.png`: gráfico de pico de memória em função de ( n ).

### Execução dos testes

No diretório `projects/`, o experimento é executado com o comando:

```bash
python3 main.py
```

Os resultados e gráficos são salvos em `projects/results/`.

---

## Resultados

Os dados a seguir devem ser extraídos do arquivo `results.csv` gerado automaticamente após a execução do script.

### Tabela de tempos de execução (exemplo)

|  n | Recursivo (s) | Dinâmico (s) |
| -: | ------------: | -----------: |
|  4 |   0.000000123 |  0.000000010 |
| 10 |           ... |          ... |

### Tabela de uso de memória (pico, KB)

|  n | Recursivo (KB) | Dinâmico (KB) |
| -: | -------------: | ------------: |
|  4 |          1.234 |         0.987 |
| 10 |            ... |           ... |

### Gráficos

Os gráficos de desempenho podem ser inseridos diretamente no relatório, por exemplo:

* ![Tempo Gasto](../projects/results/time_vs_n.png)
* ![Memória Gasta](../projects/results/memory_vs_n.png)

### Análise dos resultados

De forma geral, espera-se que a **Programação Dinâmica** apresente desempenho significativamente superior, especialmente para valores maiores de ( n ), devido à eliminação das recomputações redundantes da versão recursiva.

A versão recursiva direta, por sua natureza exponencial, deve apresentar rápido crescimento do tempo de execução e do uso de memória. Já a versão dinâmica mantém crescimento aproximadamente polinomial, sendo mais estável e previsível.

Caso os resultados não confirmem essa expectativa, recomenda-se verificar:

1. a equivalência dos resultados numéricos entre as funções;
2. o número de repetições das medições (para evitar ruído estatístico);
3. a interferência de outros processos durante a execução dos testes.

---

## Referências

[Introdução à teoria das partições de inteiros](https://www.obm.org.br/content/uploads/2020/02/23_SO_George_Lucas_Nivel_3_-Introducao_Teoria_das_particoes_de_inteiros_compressed.pdf)

[Combinação e Partições](https://www.youtube.com/watch?v=I4VIh-umY34)
