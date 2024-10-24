import networkx as nx
import matplotlib.pyplot as plt

# Crie um objeto de grafo direcionado
grafo: object = nx.DiGraph()

# Função para adicionar uma aresta com peso
def adicionar_aresta():
    origem = input("Digite a cidade de origem: ")
    destino = input("Digite a cidade de destino: ")
    peso = float(input("Digite a distância em KM: "))
    grafo.add_edge(origem, destino, weight=peso)

# Loop para adicionar arestas
while True:
    adicionar_aresta()
    continuar = input("Deseja adicionar outra Rota? (s/n): ")
    if continuar.lower() != 's':
        break

pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black')
labels = nx.get_edge_attributes(grafo, 'weight')
nx.draw_networkx_edge_labels(grafo, pos, edge_labels=labels)

# Solução do problema de distribuição e logística
origem = input("Digite a cidade de origem para a entrega: ")
destino = input("Digite a cidade de destino para a entrega: ")

try:
    caminho_curto = nx.shortest_path(grafo, origem, destino, weight='weight')
    distancia_total = nx.shortest_path_length(grafo, origem, destino, weight='weight')
    print(f"Caminho mais curto para completar a entrega: {caminho_curto}")
    print(f"Distância total em KM: {distancia_total}")
except nx.NetworkXNoPath:
    print("Não há caminho disponível entre as cidades de origem e destino.")

plt.show()