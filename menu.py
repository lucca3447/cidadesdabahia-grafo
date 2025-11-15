import os
import time
from algoritmosdebusca import Dijkstra
from grafocidadesbahia import exibir_grafo 
from grafocidadesbahia import G, coordenadas
from algoritmosdebusca import A_estrela


while True:
    os.system("cls")
    print("Algoritmos de busca em grafos de cidades da bahia")
    print("O que deseja fazer?")
    print(" 1-Exibir grafo\n 2-Dijkstra \n 3-A* \n 4-Sair")

    escolha = input("")


    match(escolha):
        case "1":
            exibir_grafo()
        
        case "2":
            input("Você escolheu aplicar Dijkstra, aperte qualquer tecla para continuar")
            print("A quais cidades(vertices) deseja aplicar o algoritmo?")
            origem = input("Insira a origem ->   ")
            destino = input("Insira o destino ->  ")
            
            inicio = time.perf_counter()
            
            menor_caminho, distancia_total = Dijkstra(G, origem, destino)
            
            fim = time.perf_counter()
            
            tempo = fim - inicio

            print(f"Distância total aproximada entre {origem} e {destino}--> {distancia_total} km")
            print(f"Menor caminho percorrido segundo o algoritmo de Dijkstra--> {menor_caminho}")
            print(f"Tempo -> {tempo:.4f} segundos")
            input("\nAperte  espaço para  voltar ao menu")
        
        case "3":
            input("Você escolheu aplicar A*, aperte qualquer tecla para continuar")
            print("A quais cidades (vertices) deseja aplicar o algoritmo?")
            origem = input("Insira a origem ->")
            destino = input("Insira o destino ->")

            inicio = time.perf_counter()

            menor_caminho, distancia_total = A_estrela(G, origem, destino, coordenadas)

            fim = time.perf_counter()

            tempo = inicio - fim

            print(f"Distancia total aproximada entre {origem} e {destino} --> {distancia_total}")
            print(f"Menor caminho encontrado segundo o algoritmo A* --> {menor_caminho}")
            print(f"Tempo -> {tempo:.4f}")
            input("\nAperte espaço para voltar ao menu")
        
        case "4":
            confirmar = input("Você escolheu sair. Confirmar (s/n)? ")
            if confirmar.lower() == "s":
                print("Encerrando...")
                break  
            else:
                print("Retornando ao menu...")
        case _:
            print("Opção invalida, por favor tente novamente")
            input("Aperte qualquer tecla para continuar")




    