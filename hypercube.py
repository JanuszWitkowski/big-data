from random import random
from math import sqrt
from typing import List
import matplotlib.pyplot as plt

def list_of_points(n: int, k: int) -> List[List[float]]:
    return [[random() for _ in range(n)] for _ in range(k)]

def distance(p1: List[float], p2: List[float]) -> float:
    return sqrt(sum([(p1[i] - p2[i]) ** 2 for i in range(len(p1))]))

def list_of_distances(points: List[List[float]]) -> List[float]:
    return [distance(p1, p2) for p1 in points for p2 in points if p1 != p2]

def distances_sqrtn(distances: List[float], n: int) -> List[float]:
    return list(map(lambda x: x/sqrt(n), distances))


def average_distance(distances: List[float], k: int) -> float:
    return sum(distances) / k


if __name__ == "__main__":
    k = 100
    ns = [1, 10, 100, 1000, 10000]
    for n in ns:
        # print(list_of_distances(list_of_points(n, k)))
        distances_normed = distances_sqrtn(list_of_distances(list_of_points(n, k)), n)
        avg_dist = average_distance(distances_normed, k)
        print(avg_dist)

        plt.figure(figsize=(16,8))
        plt.hist(distances_normed, bins=100)
        plt.savefig("z44_hypercube/" + "k" + str(k) + "_n" + str(n) + ".png", dpi=300)

