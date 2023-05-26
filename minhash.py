#!/usr/bin/python3
from typing import Any, List, Callable
import mmh3

def minHash(L: List[Any], hs: List[Callable[[Any], int]]) -> List[int]:
    # return [min([h(x) for x in L]) for h in hs]
    return [min([h(str(x)) for x in L]) for h in hs]


if __name__ == "__main__":
    n = 10
    m = 50
    s = "test"
    hs = [h for h in map(lambda i: lambda x: mmh3.hash(key=x, seed=i), [i**2 for i in range(n)])]
    L = [bin(j**3) for j in range(m)]
    min_hash = minHash(L, hs)
    print(min_hash)
