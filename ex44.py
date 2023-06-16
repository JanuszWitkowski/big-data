#!/usr/bin/python3

import random
import math
import matplotlib.pyplot as plt

class Point:
    def __init__(self, n):
        self.n = n
        self.coords = []

        for i in range(self.n):
            self.coords.append(random.uniform(0.0, 1.0))

    def get_distance(self, other):
        dist = 0
        if self.n == other.n:
            for i in range(self.n):
                dist += (self.coords[i] - other.coords[i]) ** 2
            dist = math.sqrt(dist)
        return dist

def set_of_points(k, n):
    points = []

    for _ in range(k):
        points.append(Point(n))

    return points

def get_all_distances(points):
    distance_dict = {}

    sqrt_n = math.sqrt(points[0].n)
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            dist = points[i].get_distance(points[j]) / sqrt_n
            if dist in distance_dict:
                distance_dict[dist] += 1
            else:
                distance_dict[dist] = 1

    return distance_dict

def plot_histogram(distance_dict, n):
    distance_list = [key for key, val in distance_dict.items() for _ in range(val)]
    plt.hist(distance_list, bins = 200)
    plt.savefig(f"res/points_{n}.png")
    plt.show()

if __name__ == "__main__":
    k = 100
    ns = [1, 10, 100, 1000, 10000]

    for n in ns:
        X = set_of_points(k, n)
        dist_dict = get_all_distances(X)
        plot_histogram(dist_dict, n)

