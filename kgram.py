#!/usr/bin/python3
from typing import Any, List, Callable

def k_grams(li: list, k: int) -> List[list]:
    return [li[i:(i+k)] for i in range(len(li) - k + 1)]

def min_k_gram_hash(li: list, hash: Callable[[Any], int], k: int) -> List[int]:
    # print([hash(bytes(x)) for x in k_grams(li, k)])
    return min([hash(bytes(x)) for x in k_grams(li, k)])


if __name__ == "__main__":
    import mmh3
    li = [i+1 for i in range(20)]
    k = 6
    print(li)
    print(len(li))
    print(k_grams(li, k))
    print(len(k_grams(li, k)))
    print(min_k_gram_hash(li, mmh3.hash, k))
    print("Hello World!")
