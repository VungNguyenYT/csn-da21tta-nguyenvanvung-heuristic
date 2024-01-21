from operator import truediv
from random import randint

from collections import defaultdict
from queue import PriorityQueue

data = defaultdict(list)
data['A'] = ['B', 2, 'C', 1, 'D', 3]
data['B'] = ['E', 5, 'F', 4]
data['C'] = ['G', 6, 'H', 3]
data['D'] = ['I', 2, 'J', 4]
data['F'] = ['K', 2, 'L', 1, 'M', 4]
data['H'] = ['N', 2, 'O', 4]

class Node:
    def __init__(self, name, par = None, g = 0):
        self.name = name
        self.par = par
        self.g = g
    def display(self):
        print(self.name, self.g)
    
    #less than
    def __lt__(self, other):
        if other == None:
            return False
        return self.g < other.g 
    
    #equal
    def __eq__(self, other):
        if other == None:
            return False
        return self.name == other.name

def equal(O, G):
       if O.name == G.name:
           return True
       return False

def checkInPriority(tmp, c):
    if tmp == None:
        return False
    return(tmp in c.queue)

def getPath(O):
    print(O.name)
    if O.par != None:
        getPath(O.par)
    else:
        return
    
def UniformCostSearch(S = Node('A'), G = Node('N')):
    open = PriorityQueue()
    Closed = PriorityQueue()
    open.put(S)

    while True:
        if open.empty() == True:
            print('tìm kiếm thất bại')
            return
        
        O = open.get()
        Closed.put(O)

        print('duyệt: ', O.name, O.g)

        if equal(O,G) == True:
            print('Tìm kiếm thành công')
            getPath(O)
            print('distance: ', O.g)
            return
        
        i = 0
        while i < len(data[O.name]):
            name = data[O.name] [i]
            g = O.g + data[O.name] [i+1]
            tmp = Node(name = name, g = g)
            tmp.par = O

            ok1 = checkInPriority(tmp, open)
            ok2 = checkInPriority(tmp, Closed)

            if not ok1 and not ok2:
                open.put(tmp)
            i += 2

UniformCostSearch(Node('A'), Node('N'))