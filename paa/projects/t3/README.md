# Investigando o Problema *Interval Scheduling* com Algoritmos *Greedy* e *Backtracking*

Equipe:

Mauricio Benjamin da Rocha

Pedro Antônio Vital de Sousa Carvalho

## 1. Objetivo do Trabalho

O presente trabalho tem por objetivo analisar comparativamente duas abordagens algorítmicas aplicadas ao problema clássico de *Interval Scheduling*: o Algoritmo *Greedy* (Guloso) e o *Backtracking*. A investigação busca compreender, de forma sistemática, como cada método se comporta na resolução do problema, considerando suas diferenças estruturais, operacionais e computacionais.

Para tanto, são avaliados os seguintes aspectos:

- **Tempo de execução**, a fim de verificar a eficiência temporal de cada abordagem;
- **Consumo de memória**, permitindo identificar o custo computacional associado ao processamento;
- **Qualidade da solução**, com foco na capacidade dos algoritmos em selecionar o maior número possível de intervalos não sobrepostos;
- **Escalabilidade**, observando o desempenho dos métodos diante do aumento progressivo da quantidade de dados.

A análise é conduzida por meio de experimentação computacional utilizando conjuntos de dados compostos por 10, 100, 1000 e 10.000 intervalos, organizados em diferentes padrões (ordenados, aleatórios e embaralhados). Esses conjuntos possibilitam a avaliação das abordagens em cenários distintos, proporcionando uma comparação ampla e tecnicamente fundamentada.

Espera-se, com este estudo, identificar as potencialidades e limitações de cada algoritmo, bem como fornecer subsídios que orientem a seleção das técnicas mais adequadas à resolução de problemas de agendamento em contextos reais e acadêmicos.

## 2. Descrição do Problema

O problema de *Interval Scheduling* consiste em determinar o maior subconjunto possível de intervalos que não apresentem sobreposição temporal entre si. Cada intervalo representa uma tarefa, atividade ou evento associado a um tempo de início e um tempo de término. A solução exige a seleção de um conjunto de intervalos mutuamente compatíveis, de modo que nenhum deles ocorra simultaneamente.

Trata-se de um problema amplamente estudado na área de algoritmos e estruturas de dados, em razão de sua aplicabilidade em diferentes contextos práticos. Entre as situações mais frequentes destacam-se:

- Agendamento de salas ou recursos compartilhados, nos quais múltiplas solicitações disputam o mesmo espaço;
- Gerenciamento de tarefas em sistemas computacionais, onde processos precisam ser executados sem conflito;
- Otimização de cronogramas, incluindo a organização eficiente de atividades em ambientes educacionais, corporativos ou industriais.

A Figura 1 apresenta uma comparação visual entre dois cenários fundamentais para a compreensão do problema. No primeiro, observa-se um conjunto de intervalos dispostos de forma desordenada, representando a maneira como os dados costumam chegar em aplicações reais. No segundo cenário, esses mesmos intervalos são exibidos após serem ordenados pelo tempo de término e processados pelo algoritmo Greedy. A imagem evidencia que a ordenação prévia exerce papel decisivo na eficiência da seleção, uma vez que possibilita ao algoritmo identificar rapidamente os intervalos mais curtos e menos conflitantes, construindo uma solução não sobreposta de maneira simples e eficaz. Assim, a figura ilustra a importância da estruturação adequada dos dados para o desempenho das estratégias algorítmicas utilizadas na resolução do Interval Scheduling.
