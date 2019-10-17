'''EightPuzzleWithHamming.py
This file augments EightPuzzles.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is Hamming Distance (count the number 
of tiles out of place, but not the blank, in order to maintain admissibility)

'''

from EightPuzzle import *

def h(s):
    count = 0

    for i in range(3):
        for j in range(3):
            if s.b[i][j] != 0 and s.b[i][j] != 3 * i + j:
                count += 1
    return count