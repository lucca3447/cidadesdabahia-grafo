import networkx as nx
import matplotlib.pyplot as plt
import os

from algoritmosdebusca import Dijkstra
from grafocidadesbahia import exibir_grafo 
from grafocidadesbahia import G, coordenadas
from algoritmosdebusca import heuristica
from algoritmosdebusca import A_estrela

while True:
    os.system("cls")
    print("Algoritmos de busca em grafos de cidades da bahia")
    print("O que deseja fazer?")
    print(" 1-Exibir grafo\n 2-Dijkstra \n 3-A* \n 4-BFS(Garante apenas o menor número de arestas porém, não funciona por pesos)\n 5-DFS (Apenas vai percorrer o grafo de forma exploratoria)\n 6-Sair")

    escolha = input("")


    match(escolha):
        case "1":
            exibir_grafo()
        
        case "2":
            input("Você escolheu aplicar Dijkstra, aperte qualquer tecla para continuar")
            print("A quais cidades(vertices) deseja aplicar o algoritmo?")
            origem = input("Insira a origem ->   ")
            destino = input("Insira o destino ->  ")
            
            menor_caminho, distancia_total = Dijkstra(G, origem, destino)
            
            print(f"Distância total aproximada entre {origem} e {destino}--> {distancia_total} km")
            print(f"Menor caminho percorrido segundo o algoritmo de Dijkstra--> {menor_caminho}")
            input("\nAperte  espaço para  voltar ao menu")
        case "3":
            input("Você escolheu aplicar A*, aperte qualquer tecla para continuar")
            print("A quais cidades (vertices) deseja aplicar o algoritmo?")
            origem = input("Insira a origem ->")
            destino = input("Insira o destino ->")

            menor_caminho, distancia_total = A_estrela(G, origem, destino, coordenadas)

            print(f"Distancia total aproximada entre {origem} e {destino} --> {distancia_total}")
            print(f"Menor caminho encontrado segundo o algoritmo A* --> {menor_caminho}")
            input("\nAperte espaço para voltar ao menu")


            

        case "6":
            confirmar = input("Você escolheu sair. Confirmar (s/n)? ")
            if confirmar.lower() == "s":
                print("Encerrando...")
                break  
            else:
                print("Retornando ao menu...")
        case _:
            print("Opção invalida, por favor tente novamente")
            input("Aperte qualquer tecla para continuar")




    