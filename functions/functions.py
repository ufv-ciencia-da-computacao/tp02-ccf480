from curses import pair_content
import math
import os
import pathlib
import numpy as np
import pandas as pd


def function_1(X):
    numerator = np.power(np.sin(X[0] * np.pi * 2), 3) * np.sin(X[1] * np.pi * 2)  
    denominator = np.power(X[0], 3) * (X[0] + X[1])

    return np.divide(numerator, denominator)


def g1(X):
    df = pd.read_csv(os.path.join(pathlib.Path(__file__).parent.resolve(), 
                                "unidades_geradoras.csv"))
    cost = 0
    for i in range(40):
        constants = df.iloc[i]
        Pi_min, Pi_max = constants["Pi_min"], constants["Pi_max"]
        cost += Pi_min - X[i]
    return cost

def g2(X):
    df = pd.read_csv(os.path.join(pathlib.Path(__file__).parent.resolve(), 
                                "unidades_geradoras.csv"))
    cost = 0
    for i in range(40):
        constants = df.iloc[i]
        Pi_min, Pi_max = constants["Pi_min"], constants["Pi_max"]
        cost += X[i] - Pi_max
    return cost

def g3(X):
    PD = 10500
    for i in range(len(X)):
        X[i] = round(X[i], 2)
    return np.sum(X) - PD

def penalty_func2(X):
    pen = (g3(X))**2 + max(0, g2(X))**2 + max(0, g1(X))**2
    return pen

def f(X, constants):
    part_1 = constants["a"] * np.power(X, 2)
    part_2 = constants["b"] * X
    part_3 = constants["e"] * np.sin(constants["f"] * (constants["Pi_min"] - X))

    res = part_1 + part_2 + np.absolute(part_3) + constants["c"]

    return res


def function_2(X):
    df = pd.read_csv(os.path.join(pathlib.Path(__file__).parent.resolve(), 
                                "unidades_geradoras.csv"))
    cost = 0    

    for i in range(40):
        constants = df.iloc[i]
        cost += f(X[i], constants)

    # print(cost)
    return cost

