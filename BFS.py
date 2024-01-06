from operator import truediv
from random import randint

class node:
    def __init__(self, name, par = None):
        self.name = name
        self.par = par
    def display(self):
        print(self.name)

from collections import defaultdict 

data = defaultdict(list)
data['A'] = ['B', 'C', 'D']
data['B'] = ['E', 'F']
data['C'] = ['G', 'H']
data['D'] = ['I', 'J']
data['F'] = ['K', 'L', 'M']
data['H'] = ['N', 'O']

def equal(O, G):
    return O.name == G.name

def checkInArray(tmp, open):
    for x in open:
        if equal(x, tmp):
            return True
    return False
def path (O):
    print(O.name)
    if O.par != None:
        path(O.par)
    else:
        return


#Thuật toán BFS
def BFS(S = node('A'), G = node('M')):
    open = []
    Closed = []
    open.append(S)
    while True:
        if len(open) == 0:
            print('Tìm kiếm thất bại')
            return
        O = open.pop(0)
        Closed.append(O)
        if equal(O, G) == True:
            print('Tìm kiếm thành công')
            path(O)
            return
        for x in data [O.name]:
            tmp = node(x)
            tmp.par = O

            ok1 = checkInArray(tmp, open)
            ok2 = checkInArray(tmp, Closed)
            
            #Nếu tmp không thuộc Open(O) và Close thì đưa vào cuối Open
            if not ok1 and not ok2:
                open.append(tmp)

BFS()
