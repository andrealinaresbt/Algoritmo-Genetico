import math

def fitness(individuo):
    x, y = individuo
    return 20 + x - 10 * math.cos(2 * math.pi * x) + y - 10 * math.cos(2 * math.pi * y)
