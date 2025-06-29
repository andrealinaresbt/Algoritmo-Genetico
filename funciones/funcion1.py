import math

def fitness(individuo):
    x = individuo[0]
    if x == 0:
        return 0  # evitar división entre cero
    return (math.sin(x) ** 2) / x
