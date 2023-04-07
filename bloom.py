#!/usr/bin/python3
import mmh3
from bitarray import bitarray
from math import log, exp
from wordcloud import open_and_clean_file

class BloomFilter:
    def __init__(self, number_of_hashes: int, bitarray_length: int):
        self.k = number_of_hashes
        self.n = bitarray_length
        self.hashes = [(lambda x: mmh3.hash(x, i ** 2, signed=False)) for i in range(number_of_hashes)]
        self.array = bitarray(bitarray_length)
        for i in range(bitarray_length):
            self.array[i] = 0
    
    def add(self, x: str):
        for i in range(self.k):
            self.array[self.hashes[i](x) % self.n] = 1
    
    def check(self, x: str) -> bool:
        for i in range(self.k):
            if self.array[self.hashes[i](x) % self.n] == 0:
                return False
        return True
    
    def clear(self):
        for i in range(self.n):
            self.array[i] = 0


def bloom_hamlet(unique_words_as_length: bool):
    file_name = "Szekspir/hamlet.txt"
    stop_name = "Szekspir/stop_words_english.txt"
    words = open_and_clean_file(file_name, stop_name)
    m = len(words)
    k = 8
    n = m
    # Check that we 
    if unique_words_as_length:
        dic = dict()
        for word in words:
            if word not in dic:
                dic[word] = 0
        n = len(dic)
    bf = BloomFilter(k, n)
    dic = dict()
    # Check false-positives
    fp_ctr = 0
    for word in words:
        if not bf.check(word):
            bf.add(word)
            dic[word] = 1
        else:
            if word in dic:
                dic[word] += 1
            else:
                # False-Positive
                fp_ctr += 1
                dic[word] = 1
    print("----------------------------------------")
    print(f"{k} hashes, {n} bits of BloomFilter array")
    print(f"Number of False-Positives: {fp_ctr}")
    print(f"Expected probability: Pr_exp(FP) = {(1 - exp(-(m*k)/n))**k}")
    print(f"Actual empirical probability: Pr_emp(FP) = {fp_ctr/m}")
    print(f"Best theoretical probability: Pr_th(FP) = {1/(2**k)}")
    print(f"Filter size should theoretically be equal: {log(2) * k * m}")
    print("----------------------------------------")



if __name__ == "__main__":
    bloom_hamlet(False)
    # bloom_hamlet(True)

