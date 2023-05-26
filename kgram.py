#!/usr/bin/python3
from minhash import minHash
from typing import Any, List, Callable

def k_grams(li: list, k: int) -> List[list]:
    return [li[i:(i+k)] for i in range(len(li) - k + 1)]

def min_k_gram_hash(li: list, hash: Callable[[Any], int], k: int) -> List[int]:
    # return min([hash(bytes(x)) for x in k_grams(li, k)])
    return min([hash(str(x)) for x in k_grams(li, k)])

def k_gram_minHashes(li: list, hs: List[Callable[[Any], int]], k: int) -> List[int]:
    return minHash(k_grams(li, k), hs)


if __name__ == "__main__":
    print("KGRAM TEST")
    import mmh3
    li = [i+1 for i in range(20)]
    k = 6
    hs = [h for h in map(lambda i: lambda x: mmh3.hash(key=x, seed=i), [i**2 for i in range(64)])]
    print(li)
    print(len(li))
    print(k_grams(li, k))
    print(len(k_grams(li, k)))
    print(min_k_gram_hash(li, mmh3.hash, k))
    print(k_gram_min_hashes(li, hs, k))
    print("Hello World!")
