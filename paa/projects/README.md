Explicação curta sobre memoização (em português):

O que é: memoização é uma técnica de otimização que armazena (cache) o resultado de chamadas de função para entradas já calculadas, evitando recomputações caras quando os mesmos subproblemas aparecem novamente.

Como funciona no código:

A função recebe um dicionário memo: dict[tuple[int,int], int].
Antes de calcular, verifica se a chave (n, k) já existe em memo; se sim, retorna o valor armazenado.
Se não existir, calcula recursivamente, guarda o resultado em memo[(n, k)] e retorna.
Isso transforma muitas chamadas repetidas (exponenciais) em acesso O(1) ao dicionário.
Efeito na complexidade:

Sem memo: complexidade exponencial (muitas subárvores repetidas).
Com memo: número de subproblemas distintos limitado por O(n * k); tempo aproximado O(n * k) e espaço O(n * k) para o cache.
Vantagens e trade-offs:

Vantagem: redução dramática do tempo para problemas com sobreposição de subproblemas.
Trade-off: uso de memória adicional para o cache; potencial overhead de manutenção do dicionário.
Cuidado com argumentos mutáveis (não devem ser usados como chaves) e com cache muito grande.
Alternativa prática: functools.lru_cache (menos código, automático). Exemplo de substituição:
