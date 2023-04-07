#!/usr/bin/python3
import mmh3
from bitarray import bitarray

class BloomFilter:
    def __init__(self, number_of_hashes, bitarray_length):
        self.k = number_of_hashes
        self.n = bitarray_length
        self.hashes = [(lambda x: mmh3.hash(x, i ** 2, signed=False)) for i in range(number_of_hashes)]
        self.array = bitarray(bitarray_length)
        for i in range(bitarray_length):
            self.array[i] = 0
    
    def add(self, x):
        for i in range(self.k):
            self.array[self.hashes[i](x) % self.n] = 1
    
    def check(self, x):
        for i in range(self.k):
            if self.array[self.hashes[i](x) % self.n] == 0:
                return False
        return True
    
    def clear(self):
        for i in range(self.n):
            self.array[i] = 0


# def bloom_hamlet():
#     #

