#!/usr/bin/python3
import pandas as pd
from random import random, randrange    # random.uniform

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

