import pandas as pd
import numpy as np
import math
import matplotlib.pyplot as plt
import random


def generate_dataframe(center1, center2, std_dev, d, n):
    cov_matrix = np.diag([std_dev ** 2] * d)
    ndarray1 = np.random.multivariate_normal(center1, cov_matrix, size = n // 2)
    ndarray2 = np.random.multivariate_normal(center2, cov_matrix, size = math.ceil(n / 2))
    
    ndarray = np.concatenate((ndarray1, ndarray2))
    
    dataframe = pd.DataFrame(data = ndarray)
    
    dataframe['Clase'] = np.append([1] * (n // 2), [0] * (math.ceil(n / 2)))
    return dataframe

def generate_dataframe_ej_a(d, n, c):
    return generate_dataframe([1] * d, [-1] * d, c * math.sqrt(d), d, n)

def generate_dataframe_ej_b(d, n, c):
    return generate_dataframe(np.append([1],[0] * (d-1)), np.append([-1], [0] * (d-1)), c, d, n)

def generate_random_spirals(n):    
    coords_x = []
    coords_y = []
    clase = []
    
    total_cant_0 = n // 2
    total_cant_1 = n - total_cant_0
    
    cant_0 = 0
    cant_1 = 0
    
    while (cant_0 < total_cant_0 or cant_1 < total_cant_1):
        betweenCurves = False
        # random() generates a random float uniformly in the half-open range 0.0 <= X < 1.0 (doc. de Python)
        # Como el area es proporcional al cuadrado del radio, genero uniformemente areas aleatorias y tomo sus 
        # raices cuadradas
        r = math.sqrt(random.random())
        # Genero angulo
        theta = 2 * math.pi * random.random()
        # Intentando graficar las curvas en desmos (una graficadora) para entender
        # porque los thetas anteriores me cortaban la espiral, me di cuenta que tomando el rango de valores
        # de theta anteriores no me alcanza para generar sobre toda la espiral, asi que agregué
        # este for para ir recorriendo la espiral con diferentes thetas (basados en el generado de manera uniforme)
        # e ir limitando por el radio
        for theta0 in [theta + (2 * math.pi * i) for i in range(-1, 5)]:
            if ((theta0 / (4 * math.pi)) < r and r < ((theta0+ math.pi) / (4 * math.pi))):
                coords_x.append(r * math.cos(theta))
                coords_y.append(r * math.sin(theta))
                clase.append(0)
                cant_0+=1
                betweenCurves = True
        # Si no está entre las curvas, lo mando a la clase 1
        if cant_1 < total_cant_1 and not(betweenCurves):
            coords_x.append(r * math.cos(theta))
            coords_y.append(r * math.sin(theta))
            clase.append(1)
            cant_1+=1
            
    spirals = {'x': coords_x, 'y': coords_y, 'Clase' : clase}
    dataframe = pd.DataFrame(spirals)
    return dataframe