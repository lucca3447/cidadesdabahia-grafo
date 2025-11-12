import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()


coordenadas = {
    "Salvador": (-12.9714, -38.5014),
    "Feira de Santana": (-12.2664, -38.9663),
    "Camaçari": (-12.6996, -38.3263),
    "Alagoinhas": (-12.1357, -38.4192),
    "Juazeiro": (-9.4167, -40.5033),
    "Serrinha": (-11.6566, -39.0148)
}


arestas = [
    ("Salvador", "Feira de Santana", 108),
    ("Feira de Santana", "Serrinha", 82),
    ("Feira de Santana", "Alagoinhas", 108),
    ("Salvador", "Camaçari", 50),
    ("Camaçari", "Alagoinhas", 87),
    ("Feira de Santana", "Juazeiro", 390),
    ("Serrinha", "Juazeiro", 380)
]


G.add_weighted_edges_from(arestas)


pos = {cidade: (lon, lat) for cidade, (lat, lon) in coordenadas.items()}


plt.figure(figsize=(8, 8))
nx.draw(
    G, pos, with_labels=True,
    node_color="lightblue", node_size=1800, font_size=10,
    font_weight="bold", edge_color="gray", width=2
)

nx.draw_networkx_edge_labels(G, pos, edge_labels=nx.get_edge_attributes(G, "weight"))

plt.title("Cidades da Bahia (Posições e distâncias reais)", fontsize=14)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.grid(True)
plt.show()

