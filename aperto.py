def contruir_adjacencias(vertices, arestas):
    adjacencias = {
        vertice: []
        for vertice in vertices
    }

    for origem, destino in arestas:
        adjacencias[origem].append(destino)
        adjacencias[destino].append(origem)
    return adjacencias


def calc_graus(vertices, adjacencias):
    graus = {}
    for vertice in vertices:
        graus[vertice] = len(adjacencias[vertice])
    return graus


def verificar_lema_aperto_maos(graus, arestas):
    soma_dos_graus = sum(graus.values())
    dobro_das_arestas = 2 * len(arestas)

    print("\n Verificação do Lema do Aperto de Mãos.")
    print(f"Soma dos graus: {soma_dos_graus}")
    print(f"Quantidade de Arestas: {len(arestas)}")
    print(f"2 x |E| = {dobro_das_arestas}")

    return soma_dos_graus == dobro_das_arestas


vertices = {"A", "B", "C", "D", "E", "F"}
arestas = [
    {"A", "B"},
    {"A", "D"},
    {"B", "C"},
    {"B", "E"},
    {"C", "F"},
    {"D", "E"},
    {"E", "F"}
]

adjacencias = contruir_adjacencias(vertices, arestas)
graus = calc_graus(vertices, adjacencias)

for vertice in sorted(vertices):
    grau = graus[vertice]
    print(f"{vertice}: "
          f"adjacentes = {sorted(adjacencias[vertice])}, "
          f"grau = {grau}"
    )

lema_valido = verificar_lema_aperto_maos(graus, arestas)

if lema_valido:
    print("O Lema do Aperto de Mãos foi satisfeito")
else:
    print("Existe um erro na representação ou no cálculo")
