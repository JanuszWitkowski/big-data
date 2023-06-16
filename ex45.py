#!/usr/bin/python3

import numpy as np
import math
import matplotlib.pyplot as plt
from sympy.solvers import solve
from sympy import Symbol

def S(s: float, k: float, m: float):
    return 1 - (1 - s ** k) ** m

def find_solution(s: float, target: float):
    func = lambda m : S(s, 0.910239226626837 * math.log(10.0 ** (1/m) / (10.0 ** (1/m) - 3.0 ** (2.0/m))), m)
    # func = lambda m: S(s, 1.44269504088896 * math.log(10.0 ** (1/m) / (10.0 ** (1/m) - 1.0)), m)
    
    K = Symbol('k')
    M = Symbol('m')

    print(solve(S(s, K, M) - target, K, M))
    
    ms = np.linspace(0, 1000)    
    plt.plot(ms, [func(m) for m in ms])

    plt.xlabel("m")
    plt.ylabel("S(s, k, m)")

    plt.savefig(f"res/skm_{round(s, 1)}_{round(target, 1)}.png")
    plt.show()

if __name__ == "__main__":
    find_solution(1/3, 1/10)
    # find_solution(1/2, 9/10)
