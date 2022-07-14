import pickle
import sys
import pandas as pd
from functions.functions import function_2, penalty_func2
from math import sin, pi
from pso import PSO

def g1(X):
    return (X[0]*X[0])-X[1]+1

def penalty_func(X):
    return max(0,g1(X))**2 + max(0,g2(X))**2

def g2(X):
    return 1 - X[0] + (X[1]-4)*(X[1]-4)

def f1(X):
    return -(((sin(2*pi*X[0])**3)*sin(2*pi*X[1]))/((X[0]**3)*(X[0]+X[1])))


if __name__  == "__main__":
    # pso = PSO(2, penalty_func, f1, [(0.000000001, 10), (0, 10)], 50, 100)


    d = {}
    m = 30
    arr = []

    df = pd.read_csv(sys.path[0] + "/functions/unidades_geradoras.csv")
    Pi_min = df["Pi_min"].values
    Pi_max = df["Pi_max"].values
    bounds = [(x, y) for x, y in zip(Pi_min, Pi_max)]
    
    try:
        for i in range(0, m):
            print(i)
            arr.append(PSO(40, penalty_func2, function_2, bounds, 5, 200).minimize())

        d["func_2"] = arr
        with open("experimento_func_2_B.pkl", "wb") as f:
            pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)
    except:
        d["func_2"] = arr
        with open("experimento_func_2_B.pkl", "wb") as f:
            pickle.dump(d, f, pickle.HIGHEST_PROTOCOL)
    
