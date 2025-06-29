import random
import math
import statistics

def inicializar_poblacion(tamaño, dimension, rango):
    return [[random.uniform(*rango) for _ in range(dimension)] for _ in range(tamaño)]

def seleccionar(poblacion, fitnesses):
    return random.choices(poblacion, weights=fitnesses, k=2)

def cruzar(p1, p2):
    return [(x + y) / 2 for x, y in zip(p1, p2)]

def mutar(individuo, variabilidad, rango):
    return [
        max(min(x + random.uniform(-variabilidad, variabilidad), rango[1]), rango[0])
        for x in individuo
    ]

def algoritmo_genetico(fitness_func, dimension, rango, tamaño_poblacion, umbral, max_iteraciones, variabilidad, log_callback=None):
    poblacion = inicializar_poblacion(tamaño_poblacion, dimension, rango)

    for iteracion in range(1, max_iteraciones + 1):
        fitnesses = [fitness_func(ind) for ind in poblacion]
        max_fit = max(fitnesses)
        med_fit = statistics.median(fitnesses)
        min_fit = min(fitnesses)

        if log_callback:
            log_callback(iteracion, max_fit, med_fit, min_fit)

        if max_fit - min_fit < umbral:
            break

        nueva_poblacion = []
        while len(nueva_poblacion) < tamaño_poblacion:
            p1, p2 = seleccionar(poblacion, fitnesses)
            hijo = cruzar(p1, p2)
            hijo_mutado = mutar(hijo, variabilidad, rango)
            nueva_poblacion.append(hijo_mutado)

        poblacion = nueva_poblacion

    mejor = max(poblacion, key=fitness_func)
    return mejor, fitness_func(mejor)
