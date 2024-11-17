# Resolución de Trabajos Prácticos: Algoritmos de Búsqueda en Pacman

## Resolución del Problema

### Descripción
El trabajo consistió en implementar y aplicar diferentes algoritmos de búsqueda para resolver problemas de navegación y recolección en el juego Pacman. Las tareas incluían encontrar el camino más corto para que Pacman llegue al objetivo o recolecte toda la comida en el tablero. Los algoritmos implementados fueron Búsqueda en Profundidad (DFS), Búsqueda en Anchura (BFS), Búsqueda de Costo Uniforme (UCS) y A* con una heurística trivial.

### Algoritmos Implementados

#### 1. **Depth-First Search (DFS)**

**Descripción**: DFS explora lo más profundo posible en cada rama antes de retroceder. Esto se logra utilizando una pila (LIFO) para almacenar los nodos a explorar.

**Implementación**:
- Se utilizó una pila para almacenar tuplas de la forma `(estado, acciones acumuladas)`.
- Se expandió el nodo más profundo, marcándolo como visitado, y añadiendo sus sucesores a la pila si no han sido explorados.
- Al encontrar un estado objetivo, se retorna la secuencia de acciones.

**Complejidad**:
- **Tiempo**: \(O(b^m)\), donde \(b\) es el factor de ramificación (número promedio de sucesores por nodo) y \(m\) es la profundidad máxima del árbol.
- **Espacio**: \(O(b \cdot m)\), ya que solo se almacenan los nodos en el camino actual de la búsqueda.

**Ventajas**:
- Requiere menos memoria en comparación con BFS en escenarios donde la solución está en una profundidad considerable.
- Es fácil de implementar y eficiente si la profundidad de la solución es limitada.

**Desventajas**:
- No garantiza encontrar la solución óptima ni la más corta.
- Puede quedar atrapado explorando ramas infinitas o muy profundas si no se maneja con cuidado.

**Aplicación en el TP**: DFS fue usado para explorar el laberinto en busca de soluciones sin importar la longitud de la ruta. Resultó ser útil en laberintos pequeños pero ineficiente en aquellos con muchas bifurcaciones o rutas largas.

#### 2. **Breadth-First Search (BFS)**

**Descripción**: BFS explora los nodos más cercanos al nodo inicial primero, utilizando una cola (FIFO). Esto garantiza que se encuentre la solución más corta en términos de número de movimientos.

**Implementación**:
- Se utilizó una cola para almacenar tuplas de la forma `(estado, acciones acumuladas)`.
- Los nodos se expandieron por niveles, explorando primero los nodos cercanos al nodo inicial.
- Al encontrar un estado objetivo, se retorna la secuencia de acciones.

**Complejidad**:
- **Tiempo**: \(O(b^d)\), donde \(d\) es la profundidad de la solución.
- **Espacio**: \(O(b^d)\), ya que se almacenan todos los nodos de un nivel antes de pasar al siguiente.

**Ventajas**:
- Garantiza encontrar la solución más corta en términos de cantidad de movimientos.
- Funciona bien en problemas donde la solución está cercana al nodo raíz.

**Desventajas**:
- Requiere mucha memoria, ya que debe almacenar todos los nodos de cada nivel.
- No es eficiente si la solución está en una profundidad muy grande.

**Aplicación en el TP**: BFS fue útil en problemas donde se requería encontrar el camino más corto hacia la meta, como el problema de búsqueda en el laberinto. Sin embargo, se encontró que su uso de memoria se incrementa drásticamente en laberintos más complejos.

#### 3. **Uniform Cost Search (UCS)**

**Descripción**: UCS expande siempre el nodo con el menor costo acumulado, asegurando que la solución encontrada sea la de menor costo total (no necesariamente el camino más corto en términos de movimientos). Utiliza una cola de prioridad para ordenar los nodos por su costo acumulado.

**Implementación**:
- Se utilizó una cola de prioridad que priorizaba los nodos con menor costo acumulado.
- Se expandieron los sucesores y se recalculó el costo acumulado hasta ellos.
- Al encontrar un estado objetivo, se retorna la secuencia de acciones que minimiza el costo.

**Complejidad**:
- **Tiempo**: \(O(b^C)\), donde \(C\) es el costo de la solución óptima (en el peor caso).
- **Espacio**: \(O(b^C)\), debido a que se deben almacenar todos los nodos explorados hasta encontrar la solución óptima.

**Ventajas**:
- Encuentra la solución de menor costo acumulado.
- Es completo y óptimo en problemas donde los costos son diferentes.

**Desventajas**:
- Puede ser lento en problemas con muchas soluciones posibles de alto costo.
- Requiere grandes cantidades de memoria en escenarios complejos con muchos nodos de bajo costo.

**Aplicación en el TP**: UCS fue utilizado en problemas donde se requería minimizar el costo de las acciones, como la búsqueda con penalización por moverse hacia el lado oeste del tablero. Fue eficiente para encontrar rutas óptimas cuando los costos de movimiento no eran uniformes.

#### 4. **A* Search**

**Descripción**: A* combina la búsqueda de costo uniforme con una función heurística que estima el costo restante desde un estado dado hasta el objetivo. Esto permite encontrar soluciones óptimas con una búsqueda más eficiente que UCS, al guiar la exploración hacia los estados más prometedores.

**Implementación**:
- Se utilizó una cola de prioridad que ordenaba los nodos por \(f(n) = g(n) + h(n)\), donde \(g(n)\) es el costo acumulado y \(h(n)\) es la estimación del costo restante.
- Al expandir un nodo, se calculó el nuevo costo acumulado \(g(n)\) y se estimó el costo restante \(h(n)\).
- Al encontrar un estado objetivo, se retornó la secuencia de acciones de menor costo total.

**Complejidad**:
- **Tiempo**: Depende de la calidad de la heurística. En el peor caso, \(O(b^d)\), pero puede ser más rápido con una buena heurística.
- **Espacio**: Similar al tiempo, en el peor caso \(O(b^d)\).

**Ventajas**:
- Es óptimo y completo si la heurística es admisible (no sobreestima el costo).
- Puede ser mucho más eficiente que UCS si la heurística guía la búsqueda correctamente.

**Desventajas**:
- La eficiencia depende de la calidad de la heurística. Si la heurística es pobre, A* puede comportarse como UCS o peor.
- Requiere mucha memoria en problemas complejos.

**Aplicación en el TP**: A* se utilizó en el problema de las cuatro esquinas, donde se requiere visitar todos los vértices del laberinto. Aunque se implementó una heurística trivial, se dejó espacio para probar heurísticas más avanzadas, lo que podría mejorar significativamente el rendimiento en este tipo de problemas.

### Resumen de la Complejidad

| Algoritmo           | Complejidad de Tiempo | Complejidad de Espacio | Optimalidad | Completitud |
|---------------------|-----------------------|------------------------|-------------|-------------|
| Depth-First Search   | \(O(b^m)\)            | \(O(b \cdot m)\)        | No          | Sí          |
| Breadth-First Search | \(O(b^d)\)            | \(O(b^d)\)              | Sí          | Sí          |
| Uniform Cost Search  | \(O(b^C)\)            | \(O(b^C)\)              | Sí          | Sí          |
| A* Search            | \(O(b^d)\) (depende de \(h\)) | \(O(b^d)\)           | Sí (con heurística admisible) | Sí |

### Resultados
Se implementaron y probaron exitosamente todos los algoritmos. DFS y BFS resolvieron problemas pequeños y moderados con eficiencia variable. UCS y A* fueron más efectivos para problemas donde el costo de las acciones era importante, o cuando se requería una solución óptima. En el caso de A*, con una buena heurística se podrían mejorar aún más los resultados en escenarios complejos como el problema de las esquinas.

## Aplicaciones Similares

Los algoritmos implementados tienen múltiples aplicaciones en la vida real, como:

- **DFS**: Exploración de gráficos en búsqueda de dependencias o en juegos donde es importante explorar todo el espacio antes de tomar decisiones.
- **BFS**: Se utiliza en redes sociales para encontrar el camino más corto entre usuarios, en redes de transporte público para encontrar la ruta más corta, o en cualquier otro problema donde se necesite garantizar la solución más corta en términos de movimientos.
- **UCS**: Ideal para encontrar caminos más eficientes en términos de costo, como en redes de carreteras con diferentes costos por tramo, o en problemas de planificación de recursos donde el costo varía.
- **A* Search**: Utilizado en robótica y videojuegos para encontrar caminos eficientes en entornos dinámicos, o en sistemas de navegación que requieren encontrar rutas óptimas en mapas con muchas restricciones.

## Documentación de la Presentación

Para la presentación del trabajo, se seleccionó el problema de búsqueda en el laberinto con cuatro esquinas (`CornersProblem`), donde se implementó A* con una heurística trivial. Se mostró cómo el agente exploraba eficientemente el laberinto hasta encontrar una solución óptima, expandiendo el menor número posible de nodos gracias a la heurística utilizada. Los algoritmos fueron validados mediante pruebas automáticas y visuales, garantizando su correcto funcionamiento.
