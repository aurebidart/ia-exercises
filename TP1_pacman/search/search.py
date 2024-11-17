# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.
    """
    # Pila para mantener los estados a explorar: cada elemento es una tupla (estado, acciones)
    stack = util.Stack()
    # Añadimos el estado inicial a la pila, con una lista vacía de acciones
    start_state = problem.getStartState()
    stack.push((start_state, []))
    
    # Conjunto para mantener los estados ya explorados
    visited = set()

    # Mientras la pila no esté vacía, seguimos explorando
    while not stack.isEmpty():
        # Extraemos el estado y las acciones acumuladas hasta ese estado
        state, actions = stack.pop()

        # Si hemos llegado al estado objetivo, devolvemos las acciones
        if problem.isGoalState(state):
            return actions

        # Si el estado no ha sido explorado aún
        if state not in visited:
            # Marcamos este estado como visitado
            visited.add(state)

            # Obtenemos los sucesores de este estado
            for successor, action, step_cost in problem.getSuccessors(state):
                # Si el sucesor no ha sido explorado, lo añadimos a la pila
                if successor not in visited:
                    # Añadimos el sucesor con la acción correspondiente a las acciones acumuladas
                    stack.push((successor, actions + [action]))

    # Si no se encuentra solución, devolvemos una lista vacía
    return []


def breadthFirstSearch(problem: SearchProblem):
    """
    Search the shallowest nodes in the search tree first.
    """
    # Cola para mantener los estados a explorar: cada elemento es una tupla (estado, acciones)
    queue = util.Queue()
    # Añadimos el estado inicial a la cola, con una lista vacía de acciones
    start_state = problem.getStartState()
    queue.push((start_state, []))
    
    # Conjunto para mantener los estados ya explorados
    visited = set()

    # Mientras la cola no esté vacía, seguimos explorando
    while not queue.isEmpty():
        # Extraemos el estado y las acciones acumuladas hasta ese estado
        state, actions = queue.pop()

        # Si hemos llegado al estado objetivo, devolvemos las acciones
        if problem.isGoalState(state):
            return actions

        # Si el estado no ha sido explorado aún
        if state not in visited:
            # Marcamos este estado como visitado
            visited.add(state)

            # Obtenemos los sucesores de este estado
            for successor, action, step_cost in problem.getSuccessors(state):
                # Si el sucesor no ha sido explorado, lo añadimos a la cola
                if successor not in visited:
                    # Añadimos el sucesor con la acción correspondiente a las acciones acumuladas
                    queue.push((successor, actions + [action]))

    # Si no se encuentra solución, devolvemos una lista vacía
    return []

def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """
    # Cola de prioridad que mantiene los nodos a explorar con su coste f(n) = g(n) + h(n)
    priority_queue = util.PriorityQueue()

    # Estado inicial y coste inicial (g(n) = 0, h(n) = heurística inicial)
    start_state = problem.getStartState()
    priority_queue.push((start_state, []), 0)

    # Diccionario que almacena el coste mínimo g(n) encontrado hasta el momento
    cost_so_far = {start_state: 0}

    # Mientras haya nodos por explorar
    while not priority_queue.isEmpty():
        # Extraemos el nodo con menor f(n)
        state, actions = priority_queue.pop()

        # Si hemos llegado al estado objetivo, devolvemos las acciones
        if problem.isGoalState(state):
            return actions

        # Obtenemos los sucesores del estado actual
        for successor, action, step_cost in problem.getSuccessors(state):
            # Coste acumulado hasta el sucesor (g(n) actual + coste del paso actual)
            new_cost = cost_so_far[state] + step_cost

            # Si es la primera vez que encontramos este sucesor o si encontramos un camino más barato
            if successor not in cost_so_far or new_cost < cost_so_far[successor]:
                cost_so_far[successor] = new_cost
                # Calculamos el coste total f(n) = g(n) + h(n)
                priority = new_cost + heuristic(successor, problem)
                # Añadimos el sucesor a la cola de prioridad con su coste f(n)
                priority_queue.push((successor, actions + [action]), priority)

    # Si no se encuentra solución, devolvemos una lista vacía
    return []



# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
