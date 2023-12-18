# Práctica 1. Búsqueda informada y no informada.

## Tabla de contenido

1.[Objetivo](#objetivo)
2.[Algoritmos](#algoritmos)
   1.[BFS](#bfs)
   2.[DFS](#dfs)
   3.[BNB](#bnb)
   4.[BNBH](#bnbh)
3.[Resultados](#Resultados)

## Objetivo
El objetivo de este proyecto es implementar algoritmos de búsqueda informada y no informada en un grafo acíclico y 
comparar los resultados según los siguientes criterios:
* Número de nodos generados
* Número de nodos visitados
* Coste del camino

## Algoritmos

### BFS
Breadth First Search usa una FIFO para guardar los nodos vecinos, de esta manera realiza una búsqueda en anchura
encontrando el camino más corto (número de nodos).

### DFS
Depth First Search usa un Stack para guardar los nodos vecinos realizando una búsqueda en profundidad.

### BNB
Branch and Bound es similar a BFS, ya que utiliza una FIFO. La diferencia está en que esta lista se ordena cada vez
que se inserta un nodo según el coste acumulado, priorizando así los caminos de menor coste.

### BNBH
Branch and Bound con heurística similar a BNB, pero en vez de ordenar la lista por el coste acumulado se ordena por
la suma del coste acumulado y la heurística del nodo correspondiente, de esta manera el algoritmo sigue un camino más
guiado hacia la meta (asumiendo que la heurística representa la naturaleza del problema correctamente).

## Resultados
Para comparar los distintos algoritmos se ha representado en un grafo las distintas ciudades de Romania y se ha
ejecutado los algoritmos para 5 rutas distintas.

De Arad a Bucharest  
BFS: generados = 21, visitados = 16, ruta:[B, F, S, A], coste: 450  
DFS - generados = 18, visitados = 10, ruta:[B, P, C, D, M, L, T, A], coste: 733  
BNB - generados = 31, visitados = 24, ruta:[B, P, R, S, A], coste: 418  
BNBH - generados = 16, visitados = 6, ruta:[B, P, R, S, A], coste: 418  

De Oradea a Eforie  
BFS - generados = 45, visitados = 43, ruta:[E, H, U, B, F, S, O], coste: 730  
DFS - generados = 41, visitados = 31, ruta:[E, H, U, B, P, R, S, O], coste: 698  
BNB - generados = 43, visitados = 40, ruta:[E, H, U, B, P, R, S, O], coste: 698  
BNBH - generados = 32, visitados = 15, ruta:[E, H, U, B, P, R, S, O], coste: 698  

De Giurgiu a Zerind  
BFS - generados = 41, visitados = 34, ruta:[Z, A, S, F, B, G], coste: 615  
DFS - generados = 32, visitados = 21, ruta:[Z, A, T, L, M, D, C, P, R, S, F, B, G], coste: 1284  
BNB - generados = 41, visitados = 35, ruta:[Z, A, S, R, P, B, G], coste: 583  
BNBH - generados = 26, visitados = 12, ruta:[Z, A, S, R, P, B, G], coste: 583  

De Neamt a Dobreta  
BFS - generados = 32, visitados = 26, ruta:[D, C, P, B, U, V, I, N], coste: 765  
DFS - generados = 31, visitados = 19, ruta:[D, C, P, R, S, F, B, U, V, I, N], coste: 1151  
BNB - generados = 32, visitados = 26, ruta:[D, C, P, B, U, V, I, N], coste: 765  
BNBH - generados = 23, visitados = 12, ruta:[D, C, P, B, U, V, I, N], coste: 765  

De Mehadia a Fagaras  
BFS - generados = 31, visitados = 23, ruta:[F, S, R, C, D, M], coste: 520  
DFS - generados = 29, visitados = 18, ruta:[F, B, P, R, S, A, T, L, M], coste: 928  
BNB - generados = 36, visitados = 27, ruta:[F, S, R, C, D, M], coste: 520  
BNBH - generados = 25, visitados = 16, ruta:[F, S, R, C, D, M], coste: 520  

BFS: en general encuentra una solución buena.
DFS: encuentra solución visitando menos nodos que BFS, pero la solución suele ser poco óptima.
BNB: encuentra la solución óptima, ya que siempre va por el camino de menor coste incluso si tiene que recorrer más nodo.
BNBH: al tener información extra puede encontrar la solución óptima más rápido que BNB.