# Desarrollo de una IA para el Juego de Nim mediante Q-learning

## Introducción

El juego de Nim es un juego de estrategia en el que dos jugadores se turnan para quitar objetos de varias pilas, y el objetivo es evitar ser quien retire el último objeto. Este proyecto implementa una inteligencia artificial (IA) capaz de aprender a jugar al Nim a través de **aprendizaje por refuerzo**, específicamente usando la técnica de **Q-learning**.

Q-learning es un método de aprendizaje basado en recompensas que permite a un agente aprender a tomar decisiones óptimas en un ambiente dado. Este enfoque es ideal para juegos de estrategia como el Nim, en los que cada decisión influye directamente en el resultado final.

## Teoría de Q-learning

Q-learning es un algoritmo de **aprendizaje por refuerzo** sin modelo (model-free) que permite a un agente aprender el valor de realizar acciones en diferentes estados, con el objetivo de maximizar su recompensa acumulada a lo largo del tiempo. Este valor se representa mediante la función \( Q(s, a) \), donde \( s \) es el **estado** actual del agente y \( a \) es la **acción** tomada en ese estado.

La fórmula básica de Q-learning se aplica cada vez que el agente realiza una acción y se define como:

\[
Q(s, a) \leftarrow Q(s, a) + \alpha \times \left(\text{recompensa} + \gamma \times \text{mejor recompensa futura} - Q(s, a)\right)
\]

donde:
- \( \alpha \) es la **tasa de aprendizaje**, que determina cuánto se ajusta el valor de Q en función de la nueva información.
- \( \gamma \) es el **factor de descuento**, que pondera la importancia de recompensas futuras.
- **Recompensa** es el valor inmediato recibido por la acción en el estado actual.
- **Mejor recompensa futura** es el valor máximo de \( Q \) que el agente podría recibir al tomar cualquier acción desde el nuevo estado alcanzado.

### Estados y Acciones en Q-learning

En Q-learning, un **estado** representa una situación completa del juego (en este caso, la configuración de las pilas en el Nim), mientras que una **acción** corresponde a una decisión del jugador (por ejemplo, quitar 1 o 2 objetos de una pila específica).

Cada par \( (s, a) \) se asocia con un valor de recompensa esperado que la IA ajusta a medida que juega, permitiéndole aprender qué decisiones maximizarán su probabilidad de ganar.

### Estrategia Epsilon-Greedy

El agente necesita explorar diferentes acciones para descubrir las mejores estrategias. Para esto, Q-learning usa una estrategia **epsilon-greedy**, en la cual:
- Con probabilidad \( \epsilon \), el agente elige una acción aleatoria (exploración).
- Con probabilidad \( 1 - \epsilon \), elige la acción con el valor \( Q(s, a) \) más alto conocido (explotación).

La exploración ayuda al agente a evitar quedar atrapado en estrategias locales poco óptimas y le permite encontrar la mejor acción para cada estado.

## Aplicación de Q-learning en el Juego de Nim

Para aplicar Q-learning al juego de Nim, desarrollamos una IA que aprende a jugar entrenándose a sí misma en partidas repetidas. A continuación se describe cómo la teoría de Q-learning se traduce en nuestro desarrollo:

1. **Representación de Estados y Acciones**:
   - **Estado**: El estado del juego es la configuración actual de las pilas de Nim, que indica cuántos objetos quedan en cada pila. Cada estado se almacena como una tupla de enteros.
   - **Acción**: La acción es un par `(i, j)` que indica la pila `i` de la cual quitar `j` objetos. En este caso, ajustamos el juego para que solo se puedan quitar 1 o 2 objetos en cada turno.

2. **Inicialización de Valores Q**:
   - La IA utiliza un diccionario `self.q` para almacenar los valores \( Q(s, a) \). Cada vez que el agente encuentra un nuevo par de estado y acción, el valor Q inicial se considera como `0`.
   
3. **Actualización de Valores Q**:
   - Cada vez que la IA realiza una acción y observa el nuevo estado resultante, ajusta el valor Q de acuerdo con la fórmula de Q-learning.
   - Cuando la acción resulta en una victoria (el oponente se queda sin opciones de juego), se asigna una **recompensa de +1**. Si la acción resulta en una derrota (el jugador queda sin opciones), la **recompensa es -1**. En caso contrario, la **recompensa es 0**, ya que el juego continúa.
   - La IA actualiza el valor Q del estado anterior, considerando tanto la recompensa inmediata como la mejor recompensa futura disponible desde el nuevo estado.

4. **Elección de Acciones con Epsilon-Greedy**:
   - Durante el entrenamiento, la IA utiliza una estrategia epsilon-greedy para equilibrar la exploración y explotación. Esto le permite explorar acciones nuevas, especialmente al principio del entrenamiento, y optar por las mejores decisiones aprendidas a medida que avanza el juego.

5. **Entrenamiento de la IA**:
   - La IA juega miles de partidas contra sí misma, aplicando Q-learning en cada turno. Esto le permite ajustar continuamente los valores Q para aprender qué acciones son más ventajosas en cada estado.
   - Al finalizar el entrenamiento, la IA ha aprendido una estrategia que maximiza su probabilidad de ganar, habiendo ajustado sus valores Q en función de experiencias pasadas.

## Resultados y Conclusión

Tras el entrenamiento, la IA desarrollada es capaz de tomar decisiones óptimas en cada estado del juego, anticipando jugadas y aplicando estrategias basadas en Q-learning. La capacidad de aprender de sus experiencias y ajustarse a las recompensas futuras permite a la IA desempeñarse bien en el juego de Nim y adaptarse a las configuraciones de las pilas en cada partida.

Este proyecto demuestra el potencial del aprendizaje por refuerzo para desarrollar agentes que optimizan sus decisiones basadas en experiencias previas, aplicando Q-learning para ajustar las decisiones en función del entorno y obtener resultados óptimos.
