# Lema do Aperto de Mãos em Python

Implementação em Python de um grafo simples não direcionado usando **lista de adjacência**, com cálculo do **grau de cada vértice** e verificação automática do **Lema do Aperto de Mãos**.

Projeto desenvolvido na disciplina de **Grafos** do curso de **Engenharia da Computação**, ministrada pelo **Professor William Cesar Augustonelli** na **Unisal – São José, Campinas**.

---

## O que o projeto faz

1. Recebe um conjunto de vértices e uma lista de arestas.
2. Constrói a lista de adjacência do grafo.
3. Calcula o grau de cada vértice.
4. Exibe, para cada vértice, seus adjacentes e seu grau.
5. Verifica se o Lema do Aperto de Mãos é satisfeito e informa o resultado.

## O conceito

O **Lema do Aperto de Mãos** afirma que, em qualquer grafo não direcionado, a soma dos graus de todos os vértices é igual ao dobro do número de arestas:

```
Σ grau(v) = 2 × |E|
```

Isso acontece porque cada aresta contribui com 1 para o grau de cada uma de suas duas extremidades. Uma consequência direta é que todo grafo tem uma quantidade **par** de vértices de grau ímpar.

## Grafo de exemplo

```
A ─── B ─── C
│     │     │
D ─── E ─── F
```

- Vértices: `A, B, C, D, E, F`
- Arestas: `A-B, A-D, B-C, B-E, C-F, D-E, E-F`

## Saída esperada

```
A: adjacentes = ['B', 'D'], grau = 2
B: adjacentes = ['A', 'C', 'E'], grau = 3
C: adjacentes = ['B', 'F'], grau = 2
D: adjacentes = ['A', 'E'], grau = 2
E: adjacentes = ['B', 'D', 'F'], grau = 3
F: adjacentes = ['C', 'E'], grau = 2

 Verificação do Lema do Aperto de Mãos.
Soma dos graus: 14
Quantidade de Arestas: 7
2 x |E| = 14
O Lema do Aperto de Mãos foi satisfeito
```

## Como executar

Requisito: **Python 3.6 ou superior** (o código usa f-strings). Não há dependências externas.

```bash
python grafos_lema_aperto_maos.py
```

## Estrutura do código

| Função | Responsabilidade |
|---|---|
| `contruir_adjacencias(vertices, arestas)` | Monta o dicionário de listas de adjacência a partir dos vértices e das arestas |
| `calc_graus(vertices, adjacencias)` | Calcula o grau de cada vértice (tamanho da sua lista de adjacência) |
| `verificar_lema_aperto_maos(graus, arestas)` | Compara a soma dos graus com `2 × \|E\|`, exibe o cálculo e retorna `True` ou `False` |

## Tecnologias e ferramentas

- **Linguagem:** Python 3
- **Bibliotecas:** apenas a biblioteca padrão do Python, sem imports e sem dependências externas
- **Recursos da linguagem:** dicionários, conjuntos (`set`), listas, *dict comprehension*, f-strings e as funções nativas `sum`, `len` e `sorted`
- **Estrutura de dados de grafo:** lista de adjacência

## Complexidade

Sendo `V` o número de vértices e `E` o de arestas:

- Construção da lista de adjacência: **O(V + E)**
- Cálculo dos graus: **O(V)**
- Verificação do lema: **O(V)**

## Limitações conhecidas

- Cada aresta é representada por um `set` de dois vértices, portanto **laços** (aresta de um vértice nele mesmo) e **arestas paralelas** não são suportados. Para multigrafos, uma representação por tuplas seria mais adequada.
- O grafo é fixo no código. Ler os dados de arquivo ou da entrada padrão seria uma extensão natural.

## Contexto acadêmico

- **Instituição:** Unisal – São José, Campinas
- **Curso:** Engenharia da Computação
- **Disciplina:** Grafos
- **Professor:** William Cesar Augustonelli

## Autor

**Vic Novo**, estudante de Engenharia da Computação em 2026.