João Lucca Sotero Gomes de Jesus

Algoritmo e Estrutura de Dados

Este projeto implementa algoritmos de busca (Dijkstra e A*) aplicados a um grafo realista contendo cidades do estado da Bahia e as distâncias aproximadas entre elas.
O objetivo é comparar rotas, visualizar caminhos e entender o funcionamento de algoritmos de menor caminho utilizando a biblioteca NetworkX.

1. Exibição do grafo completo

Mostra 30 cidades (nós), as posições das cidades estão de acordo com suas coordenadas reais

Mostra todas as estradas (arestas) com peso (distância). Os pesos estão com as distâncias referentes as estradas, não a localização geografica

Visualização feita com Matplotlib + NetworkX

2. Algoritmo de Dijkstra

Calcula o menor caminho entre duas cidades

Exibe:

rota encontrada

distância total

tempo de execução em milissegundos

grafo com o caminho destacado em vermelho

3. Algoritmo A*

Utiliza heurística baseada na posição geográfica das cidades

Encontra caminhos mais eficientes que o Dijkstra em muitos casos

Também exibe tempo, distância e o caminho no grafo

4. Tratamento de Erros

Inclui proteção contra:

cidade inexistente

grafos desconectados

falta de caminho

inputs vazios

erros inesperados durante execução