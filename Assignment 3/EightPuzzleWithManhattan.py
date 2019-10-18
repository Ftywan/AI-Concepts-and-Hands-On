'''EightPuzzleWithManhattan.py
This file augments EightPuzzles.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is Manhattan Distance

'''

from EightPuzzle import *
import math

def h(s):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = s.b[i][j]
            if value != 0:
                y = math.floor(value / 3)
                x = value % 3
                distance  += abs(x - j) + abs(y - i)
    return distance