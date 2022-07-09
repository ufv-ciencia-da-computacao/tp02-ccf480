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
    #pso = PSO(2, penalty_func2, function_2, [(0, 10), (0, 10)], 50, 100)


    df = pd.read_csv(sys.path[0] + "/functions/unidades_geradoras.csv")
    Pi_min = df["Pi_min"].values
    Pi_max = df["Pi_max"].values
    bounds = [(x, y) for x, y in zip(Pi_min, Pi_max)]
    
    pso = PSO(40, penalty_func2, function_2, bounds, 50, 10)
    print(pso.minimize())
