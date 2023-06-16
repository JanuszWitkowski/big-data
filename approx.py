#!/usr/bin/python3
from numbers import Number

def S(s: Number, k: Number, m: Number) -> Number:
    return 1 - (1 - s**k)**m


if __name__ == "__main__":
    eps = 0.01038
    ks = range(100)
    ms = range(1000)
    ss = [1/3, 1/2]
    rs = [1/10, 9/10]

    for k in ks:
        for m in ms:
            S1 = S(ss[0],k,m)
            S2 = S(ss[1],k,m)
            d1 = abs(S1 - rs[0])
            d2 = abs(S2 - rs[1])
            if d1 < eps and d2 < eps:
                print(f"k = {k}; m = {m}")
                print(f"S1 = {S1} ~= {rs[0]}")
                print(f"S2 = {S2} ~= {rs[1]}")

