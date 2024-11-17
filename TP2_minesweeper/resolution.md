# Trabajo Práctico: Implementación de un Juego de Buscaminas con Inteligencia Artificial

## Resolución del Problema

### Descripción

El objetivo de este trabajo práctico fue implementar un buscaminas y una inteligencia artificial (IA) que pueda jugarlo de manera eficiente. Se desarrolló un agente que, basado en la lógica y conocimiento adquirido durante el juego, deduce la ubicación de las minas y toma decisiones seguras. El proyecto consistió en dos componentes principales:

1. **El Juego de Buscaminas**: Este componente simula un tablero de buscaminas, donde las minas se colocan aleatoriamente en el tablero. El jugador puede seleccionar celdas para descubrir cuántas minas las rodean.
   
2. **MinesweeperAI**: Este componente es una inteligencia artificial diseñada para jugar al buscaminas de manera lógica. Utiliza una base de conocimiento lógica para deducir la ubicación de las minas y los espacios seguros, y elabora estrategias para realizar movimientos seguros o, en su defecto, aleatorios.

### Estrategias Aplicadas

#### 1. **Representación del Juego (Minesweeper)**

El juego se representa mediante una clase `Minesweeper`, que crea un tablero con minas distribuidas aleatoriamente. Las principales características de esta clase son:

- **Tablero de Juego**: Un tablero de tamaño configurable donde las minas se distribuyen aleatoriamente.
- **Método `is_mine()`**: Verifica si una celda específica contiene una mina.
- **Método `nearby_mines()`**: Calcula el número de minas alrededor de una celda dada. Este valor es esencial para que el jugador (o IA) deduzca qué celdas pueden ser seguras.
- **Método `won()`**: Determina si el jugador ha encontrado correctamente todas las minas del tablero.

#### 2. **Base de Conocimiento (Sentence)**

La base de conocimiento lógica está modelada en la clase `Sentence`. Cada "sentencia" representa una declaración lógica sobre el tablero del buscaminas. Una sentencia es de la forma:

- **Celdas**: Un conjunto de celdas que están relacionadas.
- **Count**: El número de celdas de ese conjunto que contienen minas.

Por ejemplo, si alrededor de una celda segura se sabe que hay exactamente 2 minas en 5 celdas adyacentes, se genera la sentencia `{(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5)} = 2`, indicando que dos de estas cinco celdas son minas.

La clase `Sentence` implementa los siguientes métodos:

- **`known_mines()`**: Devuelve el conjunto de celdas que se sabe con certeza que son minas.
- **`known_safes()`**: Devuelve el conjunto de celdas que se sabe con certeza que son seguras.
- **`mark_mine()` y `mark_safe()`**: Permiten actualizar la sentencia cuando se conoce que una celda específica es una mina o es segura.

#### 3. **Inteligencia Artificial (MinesweeperAI)**

La clase `MinesweeperAI` es el núcleo de la IA que juega al buscaminas. Utiliza lógica y deducción para realizar movimientos seguros y evitar las minas. Sus principales componentes y estrategias incluyen:

- **Marcado de celdas como minas o seguras**: La IA marca celdas como seguras o minas en función del conocimiento adquirido y actualiza la base de conocimiento.
- **Generación de nuevas reglas (Sentencias)**: Cada vez que la IA descubre una celda segura, crea una nueva sentencia lógica que describe cuántas minas se encuentran en las celdas vecinas.
- **Inferencia lógica**: La IA es capaz de inferir nueva información combinando las reglas conocidas. Si una sentencia es subconjunto de otra, se puede deducir información adicional (por ejemplo, si todas las celdas de una sentencia son minas, se pueden deducir las minas restantes en la otra sentencia).

### Algoritmos y Complejidad

#### 1. **Método `add_knowledge()`**

Este método es el corazón del proceso deductivo de la IA. Al descubrir una celda segura, realiza los siguientes pasos:

1. Marca la celda como un movimiento realizado.
2. Marca la celda como segura.
3. Crea una nueva sentencia lógica basada en las celdas vecinas.
4. Actualiza la base de conocimiento e intenta deducir nuevas celdas seguras o minas.
5. Realiza inferencias a partir de las sentencias conocidas.

La complejidad de este algoritmo depende de la cantidad de conocimiento que la IA pueda deducir. En el peor caso, puede requerir múltiples iteraciones para deducir toda la información posible, lo que puede llevar a una complejidad alta si el número de celdas y sentencias crece.

#### 2. **Inferencia Lógica**

La IA compara cada nueva sentencia con las sentencias ya conocidas para buscar patrones y relaciones entre ellas. Este proceso es una implementación de **resolución de conjuntos**, donde las reglas (sentencias) se combinan para inferir nueva información. Por ejemplo, si una sentencia es subconjunto de otra, la diferencia entre ambas puede proporcionar nuevas celdas seguras o minas.

- **Complejidad**: La inferencia lógica puede llegar a ser costosa si el número de sentencias crece significativamente. En el peor de los casos, el proceso de inferencia puede requerir \(O(n^2)\) comparaciones, donde \(n\) es el número de sentencias en la base de conocimiento.

#### 3. **Métodos `make_safe_move()` y `make_random_move()`**

- **`make_safe_move()`**: Busca una celda que la IA sepa que es segura y que no haya sido seleccionada aún. La complejidad de este método es lineal en el número de celdas seguras conocidas, \(O(s)\), donde \(s\) es el número de celdas seguras.
  
- **`make_random_move()`**: Si no se puede hacer un movimiento seguro, la IA selecciona un movimiento al azar entre las celdas no exploradas y que no se conocen como minas. La complejidad de este método es \(O(m)\), donde \(m\) es el número de celdas disponibles para ser seleccionadas.

### Ventajas y Desventajas del Enfoque

#### Ventajas:
- **Uso de lógica deductiva**: La IA utiliza reglas lógicas para inferir con precisión qué celdas son seguras o minas, lo que permite jugar de manera óptima en muchos casos.
- **Eficiencia en la deducción**: En escenarios donde hay suficiente información, la IA puede hacer movimientos seguros sin necesidad de recurrir al azar.
- **Actualización continua del conocimiento**: Cada movimiento de la IA aumenta el conocimiento global del tablero, lo que permite inferencias más precisas en futuras jugadas.

#### Desventajas:
- **Complejidad en escenarios grandes**: En tableros grandes con pocas minas, el número de sentencias y la complejidad de la inferencia lógica pueden crecer significativamente, lo que reduce la eficiencia.
- **Dependencia de la información disponible**: En casos donde la IA no tiene suficiente información, puede verse obligada a hacer movimientos aleatorios, lo que incrementa el riesgo de perder.

### Aplicaciones Similares

El enfoque basado en lógica utilizado en este buscaminas es ampliamente aplicable en otros dominios donde se necesita inferencia lógica y deducción. Algunos ejemplos incluyen:

- **Resolución de problemas de satisfacción de restricciones (CSP)**: Similar a cómo se deducen las minas en el buscaminas, los CSP buscan valores para variables que satisfacen un conjunto de restricciones.
- **Juegos de lógica**: Juegos como el Sudoku o el Nonograma pueden resolverse utilizando enfoques similares, donde el conocimiento parcial se expande mediante deducciones lógicas.
- **Sistemas expertos**: En aplicaciones de IA donde un sistema necesita tomar decisiones basadas en un conjunto de reglas lógicas (por ejemplo, diagnósticos médicos o sistemas de recomendación).

### Resultados

La implementación del agente de buscaminas fue exitosa. La IA demostró ser capaz de resolver tableros pequeños y medianos con alta eficiencia, deduciendo la ubicación de las minas y realizando movimientos seguros. En situaciones donde no tenía suficiente información, la IA recurrió a hacer movimientos aleatorios, pero mantuvo un bajo margen de error gracias a su capacidad para aprender de cada nuevo movimiento.

Se observó que la IA es particularmente efectiva en escenarios donde las celdas vecinas proporcionan suficiente información para deducir nuevas reglas. Sin embargo, en tableros más grandes o con distribuciones más dispersas de minas, la IA enfrenta mayores desafíos para generar deducciones precisas en tiempo razonable.
