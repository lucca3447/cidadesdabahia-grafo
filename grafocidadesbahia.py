import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

coordenadas = {
    "Salvador": (-12.9714, -38.5014),
    "Feira de Santana": (-12.2664, -38.9663),
    "Vitória da Conquista": (-14.8619, -40.8440),
    "Ilhéus": (-14.7935, -39.0460),
    "Itabuna": (-14.7876, -39.2784),
    "Juazeiro": (-9.4167, -40.5000),
    "Barreiras": (-12.1525, -44.9964),
    "Porto Seguro": (-16.4435, -39.0643),
    "Teixeira de Freitas": (-17.5399, -39.7416),
    "Jequié": (-13.8500, -40.0833),
    "Alagoinhas": (-12.1336, -38.4192),
    "Simões Filho": (-12.7836, -38.4033),
    "Eunápolis": (-16.3715, -39.5821),
    "Paulo Afonso": (-9.3983, -38.2217),
    "Lauro de Freitas": (-12.8978, -38.3222),
    "Camaçari": (-12.6975, -38.3261),
    "Santo Antônio de Jesus": (-12.9694, -39.2619),
    "Valença": (-13.3700, -39.0739),
    "Senhor do Bonfim": (-10.4611, -40.1864),
    "Jacobina": (-11.1811, -40.5111),
    "Irecê": (-11.3033, -41.8550),
    "Brumado": (-14.2036, -41.6669),
    "Guanambi": (-14.2233, -42.7819),
    "Caetité": (-14.0700, -42.4828),
    "Serrinha": (-11.6642, -39.0106),
    "Conceição do Coité": (-11.5600, -39.2800),
    "Cruz das Almas": (-12.6678, -39.1000),
    "Cachoeira": (-12.6000, -38.9667),
    "Ipirá": (-12.1583, -39.7372),
    "Seabra": (-12.4167, -41.7667)
}

arestas = [
    ("Salvador", "Lauro de Freitas", 28),
    ("Lauro de Freitas", "Camaçari", 25),
    ("Camaçari", "Simões Filho", 30),
    ("Simões Filho", "Alagoinhas", 98),
    ("Alagoinhas", "Feira de Santana", 108),
    ("Feira de Santana", "Serrinha", 80),
    ("Serrinha", "Conceição do Coité", 36),
    ("Conceição do Coité", "Ipirá", 110),
    ("Ipirá", "Cruz das Almas", 120),
    ("Cruz das Almas", "Cachoeira", 20),
    ("Cachoeira", "Santo Antônio de Jesus", 40),
    ("Santo Antônio de Jesus", "Valença", 70),
    ("Valença", "Ilhéus", 220),
    ("Ilhéus", "Itabuna", 30),
    ("Itabuna", "Eunápolis", 200),
    ("Eunápolis", "Porto Seguro", 63),
    ("Porto Seguro", "Teixeira de Freitas", 225),
    ("Teixeira de Freitas", "Vitória da Conquista", 330),
    ("Vitória da Conquista", "Brumado", 120),
    ("Brumado", "Caetité", 100),
    ("Caetité", "Guanambi", 45),
    ("Guanambi", "Seabra", 360),
    ("Seabra", "Irecê", 150),
    ("Irecê", "Jacobina", 200),
    ("Jacobina", "Senhor do Bonfim", 120),
    ("Senhor do Bonfim", "Juazeiro", 120),
    ("Juazeiro", "Barreiras", 315),
    ("Barreiras", "Vitória da Conquista", 530),
    ("Vitória da Conquista", "Jequié", 150),
    ("Jequié", "Salvador", 310),

    
    ("Salvador", "Feira de Santana", 112),
    ("Feira de Santana", "Jequié", 254),
    ("Jequié", "Itabuna", 180),
    ("Itabuna", "Vitória da Conquista", 180),
    ("Feira de Santana", "Ipirá", 110),
    ("Feira de Santana", "Cruz das Almas", 80),
    ("Santo Antônio de Jesus", "Feira de Santana", 190),
    ("Ilhéus", "Porto Seguro", 360),
    ("Eunápolis", "Teixeira de Freitas", 160),
    ("Brumado", "Guanambi", 170),
    ("Caetité", "Vitória da Conquista", 160),
    ("Irecê", "Juazeiro", 305),
    ("Jacobina", "Feira de Santana", 210),
    ("Senhor do Bonfim", "Juazeiro", 120),
    ("Barreiras", "Juazeiro", 480),
    ("Seabra", "Vitória da Conquista", 330),
    ("Valença", "Salvador", 120),
    ("Camaçari", "Feira de Santana", 70),
    ("Simões Filho", "Salvador", 25)
]


arestas_arredondadas = [(a, b, round(w, 1)) for a, b, w in arestas]
G.add_weighted_edges_from(arestas_arredondadas)


pos = {cidade: (lon, lat) for cidade, (lat, lon) in coordenadas.items()}

def exibir_grafo():
    plt.figure(figsize=(10, 10))
    nx.draw(
        G, pos, with_labels=True,
        node_color="lightblue", node_size=1800,
        font_size=10, font_weight="bold",
        edge_color="gray", width=2
    )

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

    plt.title("Cidades da Bahia (Posições e distâncias por estrada)", fontsize=14)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.axis("equal")   
    plt.grid(True)
    plt.show(block=False)