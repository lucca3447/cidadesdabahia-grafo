import os
import time
from algoritmosdebusca import Dijkstra
from grafocidadesbahia import exibir_grafo 
from grafocidadesbahia import G, coordenadas, pos
from algoritmosdebusca import A_estrela
from grafocidadesbahia import mostrar_caminho

while True:
    os.system("cls")
    print("Algoritmos de busca em grafos de cidades da bahia")
    print("\nO que deseja fazer?")
    print(" 1- Exibir grafo\n 2- Dijkstra \n 3-A* \n 4-Sair")

    escolha = input("")

    match(escolha):

        case "1":
            try:
                exibir_grafo()
            except Exception as e:
                print(f"Erro ao exibir grafo: {e}")
                input("Aperte qualquer tecla para continuar")

        case "2":
            input("Você escolheu aplicar Dijkstra, aperte qualquer tecla para continuar")
            print("A quais cidades(vertices) deseja aplicar o algoritmo?")
            origem = input("Insira a origem ->   ").strip()
            destino = input("Insira o destino ->  ").strip()

            try:
                inicio = time.perf_counter()

                menor_caminho, distancia_total = Dijkstra(G, origem, destino)

                mostrar_caminho(G, pos, menor_caminho)

                fim = time.perf_counter()
                tempo = fim - inicio

                print(f"Distância total aproximada entre {origem} e {destino}--> {distancia_total} km")
                print(f"Menor caminho percorrido segundo o algoritmo de Dijkstra--> {menor_caminho}")
                print(f"Tempo -> {tempo:.4f} segundos")

            except KeyError:
                print("\nERRO: Uma das cidades digitadas não existe no grafo.")
                print(f"Cidades disponíveis: {list(G.nodes)}")

            except Exception as e:
                print(f"\nErro ao executar Dijkstra: {e}")

            input("\nAperte espaço para voltar ao menu")

        case "3":
            input("Você escolheu aplicar A*, aperte qualquer tecla para continuar")
            print("A quais cidades (vertices) deseja aplicar o algoritmo?")
            origem = input("Insira a origem ->").strip()
            destino = input("Insira o destino ->").strip()

            try:
                inicio = time.perf_counter()

                menor_caminho, distancia_total = A_estrela(G, origem, destino, coordenadas)

                mostrar_caminho(G, pos, menor_caminho)

                fim = time.perf_counter()
                tempo = fim - inicio

                print(f"Distancia total aproximada entre {origem} e {destino} --> {distancia_total}")
                print(f"Menor caminho encontrado segundo o algoritmo A* --> {menor_caminho}")
                print(f"Tempo -> {tempo:.4f}")

            except KeyError:
                print("\nERRO: Uma das cidades digitadas não existe no grafo.")
                print(f"Cidades disponíveis: {list(G.nodes)}")

            except Exception as e:
                print(f"\nErro ao executar A*: {e}")

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
