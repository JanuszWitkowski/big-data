#!/usr/bin/python3
from minhash import minHash
from kgram import min_k_gram_hash, k_gram_minHashes
from wordcloud import open_and_clean_file
from utils import get_files, proper_name
from typing import Any, List, Callable
from numbers import Number

def get_docs_minHashes(docs: List[list], hashes: List[Callable[[Any], int]], k: int) -> List[List[int]]:
    return [k_gram_minHashes(doc, hashes, k) for doc in docs]

def jaccard_estimate(minHashesA: List[int], minHashesB: List[int]) -> Number:
    if len(minHashesA) != len(minHashesB):
        return -1
    # print(f"{len([m for i, m in enumerate(minHashesA) if minHashesA[i] == minHashesB[i]])}, {len(minHashesA)}")
    return len([m for i, m in enumerate(minHashesA) if minHashesA[i] == minHashesB[i]]) / len(minHashesA)



DIR_NAME = "chapters" + "/"
# STOP_NAMES = "Szekspir/stop_words_english.txt"
STOP_NAMES = ""


if __name__ == "__main__":
    print("Jaccard")
    import mmh3
    hs = [64, 128, 256]
    k = 7
    hashes = [[hsh for hsh in map(lambda i: lambda x: mmh3.hash(key=x, seed=i), [i**2 for i in range(h)])] for h in hs]
    filenames = get_files(DIR_NAME)

    print("Opening and cleaning files...")
    docs = [open_and_clean_file(DIR_NAME + filename, STOP_NAMES) for filename in filenames]
    names = [proper_name(filename) for filename in filenames]

    print("Getting minHashes...")
    ms = get_docs_minHashes(docs, hashes[0], k)
    n = len(ms)

    print("Calculating...")
    jaccards = [jaccard_estimate(ms[i], ms[j]) for i in range(n) for j in range(i, n)]
    infos = [f"{names[i]} vs {names[j]}" for i in range(n) for j in range(i, n)]

    print(names)
    for i, _ in enumerate(jaccards):
        print(f"{infos[i]}: {jaccards[i]}")
    # print(docs)

