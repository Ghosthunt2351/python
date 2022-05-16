from sys import argv
from random import randint

itterator, start = argv
start = int(start)
print([i for i in range(start, randint(start, start + 100))])
