def DFS(file_name):
    with open(file_name, 'r') as file:
        lines = file.readlines()

        # Extrair informações do grafo do arquivo
        num_vertices = int(lines[0])
        edges = [line.strip().split() for line in lines[1:]]
        G = {str(i): [] for i in range(num_vertices)}

        for edge in edges:
            u, v = edge
            G[u].append(v)

    # Restante do código DFS
    cor = {}
    d = {}
    f = {}
    edge_type = {}
    mark = [0]  # Usando uma lista para passar a variável mark por referência

    for u in G.keys():
        cor[u] = 'BRANCO'

    for u in G.keys():
        if cor[u] == 'BRANCO':
            DFS_VISIT(u, G, cor, d, f, edge_type, mark)

    return cor, d, f, edge_type


def DFS_VISIT(u, G, cor, d, f, edge_type, mark):
    cor[u] = 'CINZA'
    mark[0] += 1
    d[u] = mark[0]

    for v in G[u]:
        if cor[v] == 'BRANCO':
            edge_type[(u, v)] = 'Árvore'
            DFS_VISIT(v, G, cor, d, f, edge_type, mark)
        elif cor[v] == 'CINZA':
            edge_type[(u, v)] = 'Retorno'
        elif d[u] < d[v]:
            edge_type[(u, v)] = 'Avanço'
        else:
            edge_type[(u, v)] = 'Cruzamento'

    cor[u] = 'PRETO'
    mark[0] += 1
    f[u] = mark[0]


cor, d, f, edge_type = DFS('grafo.txt')

# Exemplo de uso das informações sobre as arestas
for u in cor.keys():
    print(f"Vértice {u}: Tempo cinza -> {d[u]}, Tempo preto -> {f[u]}")

printed_edges = set()  # Conjunto para armazenar as arestas já impressas

for (u, v), etype in edge_type.items():
    if (u, v) not in printed_edges:
        print(f"Aresta ({u}, {v}): {etype}")
        printed_edges.add((u, v))