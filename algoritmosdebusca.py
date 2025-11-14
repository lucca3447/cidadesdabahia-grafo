import networkx as nx
from grafocidadesbahia import G
from grafocidadesbahia import coordenadas
import matplotlib.pyplot as plt


def Dijkstra(G, origem, destino):
    menor_caminho = nx.shortest_path(G, source=origem, target=destino, weight="weight")
    distancia_total = nx.shortest_path_length(G, source=origem, target=destino, weight="weight")
    return menor_caminho, distancia_total


def bfs(G, origem):
    visitados = []
    fila = [origem]

    while fila:
        atual = fila.pop(0)
        if atual not in visitados:
            visitados.append(atual)
            fila.extend(list(G.neighbors(atual)))  
    return visitados


def dfs(G, origem):
    visitados = []

    def cavar(no):
        if no not in visitados:        
            visitados.append(no)
            for viz in G.neighbors(no): 
                cavar(viz)

    cavar(origem)
    return visitados
    

    
