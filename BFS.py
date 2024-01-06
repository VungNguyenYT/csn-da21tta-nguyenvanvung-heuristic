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