'''EightPuzzleWithManhattan.py
This file augments EightPuzzles.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is Manhattan Distance

'''

from EightPuzzle import *

def h(s):
    for i in range(3):
        for j in range(3):
            value = s.b[i][j]
            y = value / 3
            x = value % 3
            distance  = abs(x - j) + abs(y - i)
    return distance