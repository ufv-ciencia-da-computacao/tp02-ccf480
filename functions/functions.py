import os
import sys
import numpy as np
import pandas as pd


def function_1(X):
    numerator = np.power(np.sin(X[0] * np.pi * 2), 3) * np.sin(X[1] * np.pi * 2)  
    denominator = np.power(X[0], 3) * (X[0] + X[1])

    return np.divide(numerator, denominator)


def f(X, constants):
    part_1 = constants["a"] * np.power(X, 2)
    part_2 = constants["b"] * X
    part_3 = constants["e"] * np.sin(constants["f"] * (constants["Pi_min"] - X))

    return part_1 + part_2 + np.absolute(part_3) + constants["c"]


def function2(X):
    df = pd.read_csv(os.path.join(sys.path[0], "unidades_geradoras.csv"))
    cost = 0    
    
    for i in range(40):
        constants = df.iloc[i]
        cost += f(X[i], constants)

    return cost