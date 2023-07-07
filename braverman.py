#!/usr/bin/python3
import random
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import chisquare, chi2, chi2_contingency
from collections import Counter

class SlidingWindow:
    def __init__(self, k: int):
        self.k = k
        self.n = 0
        self.c = 0
        self.elem = None
        # self.sample = []
        self.freq = []
        self.treewidth = "Twinwidth"
    
    def read(self, x):
        self.n += 1
        if random.random() < 1.0/float(self.n):
        # if random.random() < 1.0/sqrt(self.n):
            self.elem = x
            self.c = self.n
            # self.sample.append(self.c)
            # self.sample.append(self.elem)
        self.freq.append(self.c)
        # self.freq.append(self.n - self.c + 1)
        self.n %= self.k
    
    def get(self):
        return self.elem, self.c
    
    # def get_sample(self):
    #     return self.sample

    def frequencies(self):
        return self.freq
    
    def clear(self):
        self.n = 0
        self.c = 0
        self.elem = None
        # self.sample = []


def histogram(sample: list, b: int):
    # plt.figure(figsize=(16, 8))
    plt.hist(sample, density=True, bins=b)
    plt.savefig("z25_braverman/histogram.png")


def check_correctness(n: int, k: int, iter: int):
    sw = SlidingWindow(k)
    # data = [i+1 for i in range(n)]
    sample = []
    for _ in range(iter):
        for j in range(1, n+1):
            sw.read(j)
            if j % k == 0:
                # print(f"x={x}; j={j}; sample={sw.get()}")
                single_sample = sw.get()
                sample.append(single_sample[1])
        # sample += sw.get_sample()
        # sw.clear()

    # print(sample)
    histogram(sample, k)

    # chi2, p = chisquare(sample)
    # chi2, p = chisquare(sample, ddof=4)
    # print(chi2)
    # print(p)
    # print(chi2.ppf(sample, 4))
    # freq_dict = dict()
    # for i in range(1, k+1):
    #     freq_dict[i] = 0
    # for j in sw.frequencies():
    #     freq_dict[j] += 1
    # frequencies = list(freq_dict.values())
    # print(frequencies)
    # chi2, p = chisquare(frequencies)
    # # chi2, p = chisquare(frequencies, ddof=4)
    # print(chi2)
    # print(p)

    p_wanted = 0.01
    threshold = 11.345
    counter = Counter(sample)
    frequencies = [counter[i] for i in range(1, k+1)]
    _, p, _, _ = chi2_contingency(frequencies)
    print("p=" + str(p))
    if p <= p_wanted:
        print("H0 rejected 1")
    else:
        print("H0 approved 1")
    chi2result, _ = chisquare(frequencies, ddof=4)
    print(f"chi2result={chi2result}")
    if threshold < chi2result:
        print("H0 rejected 2")
    else:
        print("H0 approved 2")



if __name__ == "__main__":
    n = 10000
    k = 5
    iter = 1
    check_correctness(n, k, iter)

