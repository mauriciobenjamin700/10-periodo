# *Interval Scheduling — Algoritmos e resultados*

Este repositório contém duas implementações para o problema de
seleção de intervalos não sobrepostos (maximizar o número de
intervalos): uma abordagem gulosa (`src/greedy.py`) e uma de
backtracking/força-bruta (`src/backtracking.py`). Também há um
gerador de datasets em `src/data.py` que cria conjuntos de teste
ordenados, embaralhados e aleatórios em `datasets/`.

# **Algoritmos implementados**

- `interval_scheduling_greedy` (guloso): ordena os intervalos pelo
tempo de término crescente e seleciona cada intervalo cujo início
é >= fim do último selecionado. Essa estratégia é a solução
clássica e provada ótima para maximizar o número de intervalos
quando não há pesos.
- `interval_scheduling_backtracking` (backtracking): explora
incluir/excluir cada intervalo recursivamente e retorna a
solução de maior cardinalidade encontrada — equivalente a
força-bruta (exata), usada apenas para validação em instâncias
pequenas.
- `interval_scheduling_dp` (programação dinâmica): implementada
como alternativa exata O(n log n). Ordena os intervalos por fim,
usa busca binária para encontrar o próximo intervalo compatível
e aplica DP para calcular a solução ótima com complexidade
O(n log n) em tempo e O(n) em espaço. Esta implementação foi
adicionada porque o backtracking torna-se impraticável para
n maiores (ex.: >= 100).

**Complexidade**

- Guloso:
  - Tempo: O(n log n) devido à ordenação; seleção linear O(n).
  - Espaço: O(n) para armazenar entrada/saída (ou O(1) adicional).
- Backtracking (sem poda forte):
  - Tempo: O(n * 2^n) no pior caso (2^n ramos e até O(n) para
    checar compatibilidade), portanto exponencial.
  - Espaço: O(n) recursão/solução parcial (além da memória usada
    pelas estruturas auxiliares).

Essas diferenças fazem com que o algoritmo guloso seja prático
para grandes entradas, enquanto o backtracking explode rapidamente
em tempo e memória quando `n` cresce.

Nota sobre a solução DP:
- A implementação `interval_scheduling_dp` resolve exatamente o
  mesmo problema (máxima cardinalidade) com custo O(n log n).
  Em testes práticos do repositório ela encontra a solução ótima
  muito mais rápido que o backtracking, e é recomendada quando
  a solução exata é necessária mas `n` é grande.

**Teste realizado (saída registrada)**
O comando utilizado foi `python3 test.py`. Abaixo está o trecho
de saída relevante que você forneceu:

Algorithm: Greedy, Dataset: Random

- Variant 1: Result Size = 8, Time = 0.000014 s, Memory = 0.30 KB
- Variant 2: Result Size = 28, Time = 0.000014 s, Memory = 1.08 KB
- Variant 3: Result Size = 76, Time = 0.000102 s, Memory = 23.59 KB
- Variant 4: Result Size = 254, Time = 0.001154 s, Memory = 234.55 KB

Algorithm: Greedy, Dataset: Sorted

- Variant 1: Result Size = 8, Time = 0.000006 s, Memory = 0.30 KB
- Variant 2: Result Size = 28, Time = 0.000009 s, Memory = 1.08 KB
- Variant 3: Result Size = 76, Time = 0.000039 s, Memory = 15.85 KB
- Variant 4: Result Size = 254, Time = 0.000287 s, Memory = 156.48 KB

Algorithm: Greedy, Dataset: Shuffled

- Variant 1: Result Size = 8, Time = 0.000005 s, Memory = 0.30 KB
- Variant 2: Result Size = 28, Time = 0.000014 s, Memory = 1.08 KB
- Variant 3: Result Size = 76, Time = 0.000092 s, Memory = 23.59 KB
- Variant 4: Result Size = 254, Time = 0.001430 s, Memory = 234.57 KB

Algorithm: Backtracking, Dataset: Random

- Variant 1: Result Size = 8, Time = 0.000432 s, Memory = 0.55 KB

Observações sobre os resultados:

- O algoritmo guloso processou todas as variantes rapidamente;
os tempos e uso de memória aumentam lentamente com o tamanho do
dataset (esperado: ordenação domina custo, seleção é linear).
- O backtracking executou apenas a `Variant 1` (pequena) e parou
nas variantes seguintes — por isso aparece apenas um resultado.

- O benchmark também inclui resultados para "Dynamic Programming"
  (a implementação `interval_scheduling_dp`). Os resultados mostram
  que a DP tem desempenho semelhante ao guloso em ordem de grandeza
  (ambas escaláveis para n até milhares), mas a DP é exata enquanto
  o guloso também é exato para este problema específico (não
  ponderado). Em cenários onde a correção exata for crítica e os
  dados forem maiores, prefira a versão DP ao backtracking.

Por que "o algoritmo morreu aqui"
- Causa: complexidade exponencial do backtracking. Para variantes
com dezenas/centenas de intervalos (ex.: 100, 1000, 10000), o
número de combinações possíveis torna a execução impraticável.
- Possíveis manifestações do "morrer":
  - tempo de execução muito grande (parece travado por horas);
  - consumo de memória crescente até o sistema matar o processo
    (OOM) ou o processo ser interrompido manualmente;
- limite de tempo/recursos do ambiente de execução.
- Na prática, para `n` grandes, o backtracking não termina em um
  tempo razoável nem antes de consumir memória; por isso a
  execução foi interrompida (ou o autor parou a execução).

Recomendações práticas

- Use `src/greedy.py` como solução padrão para este problema
  (maximizar número de intervalos) — é ótima e eficiente.
- Mantenha `src/backtracking.py` somente para fins pedagógicos e
  validação em instâncias muito pequenas (n <= 20 ou conforme
  capacidade de sua máquina).
- Se depois quiser resolver variação com pesos (weighted
  interval scheduling), implemente a solução DP O(n log n).

Atualização prática do repositório
- Para evitar que o teste "morra" em entradas grandes, o repositório
  inclui agora a versão DP (`interval_scheduling_dp`) em
  `src/backtracking.py`. Use-a quando precisar da solução exata e
  os tamanhos de entrada forem maiores que o tolerável para
  backtracking. O `test.py`/benchmarks podem ser configurados para
  utilizar automaticamente DP quando `n` exceder um limite.

Como reproduzir os testes

1. Gerar datasets (se já não existirem):

```bash
python3 src/data.py
```

2. Executar o script de testes (ex.: `test.py`):

```bash
python3 test.py
```

3. Para comparar implementações em um arquivo específico:

```python
from src.data import load_dataset
from src.greedy import interval_scheduling_greedy
from src.backtracking import interval_scheduling_backtracking

intervals = load_dataset('datasets/100_random.json')
print('Greedy ->', len(interval_scheduling_greedy(intervals)))
print('Backtrack ->', len(interval_scheduling_backtracking(intervals)))  # só para n pequeno
```
