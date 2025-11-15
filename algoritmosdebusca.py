import networkx as nx
import math


def Dijkstra(G, origem, destino):
    menor_caminho = nx.dijkstra_path(G,source=origem,target=destino,weight="weight")

    distancia_total = nx.dijkstra_path_length(G,source=origem,target=destino,weight="weight")
    
    return menor_caminho, distancia_total

    

def heuristica(cidade1, cidade2, coordenadas):
    lat1, lon1 = coordenadas[cidade1]
    lat2, lon2 = coordenadas[cidade2]

    return math.sqrt((lat1 - lat2)**2 + (lon1 - lon2)**2)

def A_estrela(G, origem, destino, coordenadas):
    menor_caminho = nx.astar_path(G,source=origem,target=destino,heuristic=lambda a, b: heuristica(a, b, coordenadas),weight="weight")

    distancia_total = nx.astar_path_length(G,source=origem,target=destino,heuristic=lambda a, b: heuristica(a, b, coordenadas),weight="weight")

    return menor_caminho, distancia_total

