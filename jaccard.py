#!/usr/bin/python3
from minhash import minHash
from kgram import k_grams, k_gram_minHashes
from wordcloud import open_and_clean_file
from utils import get_files, proper_name
from typing import Any, List, Callable
from numbers import Number
from sklearn.cluster import KMeans

def get_docs_k_grams(docs: List[str], k: int) -> List[List[list]]:
    return [k_grams(doc, k) for doc in docs]

def get_docs_minHashes(docs: List[list], hashes: List[Callable[[Any], int]], k: int) -> List[List[int]]:
    return [k_gram_minHashes(doc, hashes, k) for doc in docs]

def jaccard_estimate(minHashesA: List[int], minHashesB: List[int]) -> Number:
    if len(minHashesA) != len(minHashesB):
        return -1
    # print(f"{len([m for i, m in enumerate(minHashesA) if minHashesA[i] == minHashesB[i]])}, {len(minHashesA)}")
    return len([m for i, m in enumerate(minHashesA) if minHashesA[i] == minHashesB[i]]) / len(minHashesA)

def concatenate_strings(strings: List[str]) -> str:
    res = ""
    for string in strings:
        res = res + string + " "
    return res

def jaccard_theory(docA: List[list], docB: List[list]) -> Number:
    # setA = set(docA)
    # setB = set(docB)
    setA = set([str(doc) for doc in docA])
    setB = set([str(doc) for doc in docB])
    return len(setA.intersection(setB)) / len(setA.union(setB))

def kmeans(minHashes: List[List[int]], names: List[str], k: int):
    hash_size = 64
    num_clusters = k
    kmeans = KMeans(n_clusters=num_clusters)
    kmeans.fit(minHashes)
    cluster_labels = kmeans.labels_
    labels_dict = {label: [] for label in cluster_labels}
    for i, label in enumerate(cluster_labels):
        labels_dict[label].append(names[i])
    for key in labels_dict:
        print(labels_dict[key])



DIR_NAME = "chapters" + "/"
# STOP_NAMES = "Szekspir/stop_words_english.txt"
STOP_WORDS = ""


if __name__ == "__main__":
    print("Jaccard")
    import mmh3
    hs = [64, 128, 256]
    k = 7
    hashes = [[hsh for hsh in map(lambda i: lambda x: mmh3.hash(key=x, seed=i), [i**2 for i in range(h)])] for h in hs]
    filenames = get_files(DIR_NAME)
    filenames.sort()

    print("Opening and cleaning files...")
    # docs = [open_and_clean_file(DIR_NAME + filename, STOP_WORDS, False) for filename in filenames]
    docs = [concatenate_strings(open_and_clean_file(DIR_NAME + filename, STOP_WORDS, False)) for filename in filenames]
    names = [proper_name(filename) for filename in filenames]

    print("Getting k-grams...")
    kgrams = get_docs_k_grams(docs, k)
    # print(kgrams)

    print("Getting minHashes...")
    ms = get_docs_minHashes(docs, hashes[2], k)
    n = len(ms)

    infos = [f"{names[i]} vs {names[j]}" for i in range(n) for j in range(i, n)]
    print("Calculating empirical...")
    empirum = [jaccard_estimate(ms[i], ms[j]) for i in range(n) for j in range(i, n)]
    print("Calculating theoretical...")
    theory = [jaccard_theory(kgrams[i], kgrams[j]) for i in range(n) for j in range(i, n)]
    sanity_check = [jaccard_theory(docs[i], docs[j]) for i in range(n) for j in range(i, n)]

    print(names)
    print("Comparison: empirical | theoretical | sanity-check")
    for i, _ in enumerate(empirum):
        # print(f"{infos[i]}: {empirum[i]}")
        print(f"{infos[i]}:\t{empirum[i]} | {theory[i]} | {sanity_check[i]}")
    # print(docs)
    # print(names)
    kmeans(ms, names, k)

