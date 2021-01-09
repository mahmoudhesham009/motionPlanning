import numpy as np
from queue import Queue
from enum import Enum

grid = np.array([
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 0],
    [0, 0, 0, 1, 0, 0],
])

start = (0, 0)
goal = (4, 4)

q = Queue()
visited = set()
branch = {}

q.put(start)
visited.add(start)


class Action(Enum): 
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP = (-1, 0)
    DOWN = (1, 0)

    def __str__(self):
        if self == self.LEFT:
            return '<'
        elif self == self.RIGHT:
            return '>'
        elif self == self.UP:
            return '^'
        elif self == self.DOWN:
            return 'v'


def validActions(grid,node):
    valid= [Action.UP, Action.LEFT, Action.RIGHT, Action.DOWN]
    n, m = grid.shape[0] - 1, grid.shape[1] - 1
    x, y = node
    
    if x - 1 < 0 or grid[x-1, y] == 1:
        valid.remove(Action.UP)
    if x + 1 > n or grid[x+1, y] == 1:
        valid.remove(Action.DOWN)
    if y - 1 < 0 or grid[x, y-1] == 1:
        valid.remove(Action.LEFT)
    if y + 1 > m or grid[x, y+1] == 1:
        valid.remove(Action.RIGHT)
        
    return valid


def BFS(grid,start,goal):
    found=False
    while True:
        currentNode = q.get()
        
        if currentNode == goal: 
            print('Found a path.')
            found = True
            break
            
        else:
            for act in validActions(grid,currentNode):
                nextNode=(currentNode[0]+act.value[0],currentNode[1]+act.value[1])
                if nextNode not in visited:
                    q.put(nextNode)
                    visited.add(nextNode)
                    branch[nextNode] = (currentNode, act)
                    
    path = []
    if found:
        # retrace steps
        path = []
        n = goal
        while branch[n][0] != start:
            path.append(branch[n][1])
            n = branch[n][0]
        path.append(branch[n][1])
            
    return path[::-1]

