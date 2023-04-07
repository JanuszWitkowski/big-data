#!/usr/bin/python3
import pandas as pd
from random import random, randrange    # random.uniform(a, b)

class RVitter :
    def __init__(self, size_of_sample: int):
        self.k = 0
        self.n = size_of_sample
        self.data = [None for _ in range(size_of_sample)]
    
    def step(self, elem):
        self.k += 1
        if self.k <= self.n:
            self.data[self.k - 1] = elem
        else:
            if random() < self.n/self.k:
                self.data[randrange(self.n)] = elem
    
    def get(self):
        return self.data
    
    def clear(self):
        self.k = 0
        for i in range(self.n):
            self.data[i] = None


if __name__ == "__main__":
    rv = RVitter(40)
    for i in range(10**3):
        rv.step(i)
    print(rv.get())

