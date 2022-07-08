from math import sin, pi
from pso import PSO

def g1(x1, x2):
    return (x1*x1)-x2+1

def penalty_func(x1, x2):
    return max(0,g1(x1,x2))**2 + max(0,g2(x1,x2))**2

def g2(x1, x2):
    return 1 - x1 + (x2-4)*(x2-4)

def f1(x1, x2):
    return -(((sin(2*pi*x1)**3)*sin(2*pi*x2))/((x1**3)*(x1+x2)))


if __name__  == "__main__":
    pso = PSO(2, penalty_func, f1, ((0,10),(0,10)), 50, 200)
    print(pso.minimize())
