#!/usr/bin/python3
import random
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from scipy.stats import chisquare

class SlidingWindow:
    def __init__(self, k: int):
        self.k = k
        self.n = 0
        self.c = 0
        self.elem = None
        # self.sample = []
        self.treewidth = "Bojko baza"
    
    def read(self, x):
        self.n += 1
        if random.random() < 1.0/self.n:
        # if random.random() < 1.0/sqrt(self.n):
        # if random.random() < 1.0/():
            self.elem = x
            self.c = self.n
            # self.sample.append(self.c)
            # self.sample.append(self.elem)
        self.n %= self.k
    
    def get(self):
        return self.elem, self.c
    
    # def get_sample(self):
    #     return self.sample
    
    def clear(self):
        self.n = 0
        self.c = 0
        self.elem = None
        # self.sample = []


def histogram(sample: list, n: int):
    # plt.figure(figsize=(16, 8))
    plt.hist(sample, density=True, bins=n)
    plt.savefig("braverman/histogram.png")


def check_correctness(n: int, k: int, iter: int):
    sw = SlidingWindow(k)
    data = [i for i in range(n)]
    sample = []
    for _ in range(iter):
        for j, x in enumerate(data):
            sw.read(x)
            if j % (k+1) == 0:
                print(f"x={x}; j={j}; sample={sw.get()}")
                sample.append(sw.get()[1])
        # sample += sw.get_sample()
        sw.clear()
    print(sample)
    histogram(sample, k)



if __name__ == "__main__":
    n = 100
    k = 5
    iter = 100
    check_correctness(n, k, iter)



# import random
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import chisquare

# def generate_histogram(window_size, observations):
#     sample = []
#     positions = []
#     histogram = [0] * window_size
#     p_value = None

#     for i, observation in enumerate(observations):
#         if len(sample) < window_size:
#             sample.append(observation)
#             positions.append(i)
#         else:
#             idx = random.randint(0, i)
#             if idx < window_size:
#                 replaced_observation = sample[idx]
#                 replaced_position = positions[idx]
#                 sample[idx] = observation
#                 positions[idx] = i
#                 histogram[replaced_observation] += 1

#                 if i > window_size:
#                     total = sum(histogram)
#                     expected_counts = [total / window_size] * window_size
#                     chi2, p = chisquare(histogram, f_exp=expected_counts, ddof=window_size - 1)
#                     if p <= 0.01:
#                         p_value = p
#                         break

#     plt.hist(sample, density=True, bins=range(window_size + 1))
#     plt.show()

#     return p_value

# # Przykładowe użycie
# window_size = 5
# observations = np.random.randint(0, window_size, 10000)

# p_value = generate_histogram(window_size, observations)

# if p_value is not None:
#     if p_value <= 11.345:
#         print("Odrzucamy hipotezę zerową. Próbka nie pochodzi z rozkładu jednostajnego.")
#     else:
#         print("Nie ma podstaw do odrzucenia hipotezy zerowej. Próbka pochodzi z rozkładu jednostajnego.")






# import random
# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.stats import chisquare

# def generate_histogram(window_size, observations):
#     sample = []
#     positions = []
#     histogram = [0] * window_size
#     p_value = None

#     for i, observation in enumerate(observations):
#         if len(sample) < window_size:
#             sample.append(observation)
#             positions.append(i)
#         else:
#             idx = random.randint(0, i)
#             if idx < window_size:
#                 replaced_observation = sample[idx]
#                 replaced_position = positions[idx]
#                 sample[idx] = observation
#                 positions[idx] = i
#                 histogram[replaced_observation] += 1

#                 if i > window_size:
#                     expected_counts = [(i - window_size) / window_size] * window_size
#                     chi2, p = chisquare(histogram, f_exp=expected_counts, ddof=window_size - 1)
#                     if p <= 0.01:
#                         p_value = p
#                         break

#     plt.hist(sample, density=True, bins=range(window_size + 1))
#     plt.show()
#     plt.savefig("braverman/histogram.png")

#     return p_value

# # Przykładowe użycie
# if __name__ == "__main__":
#     window_size = 5
#     observations = np.random.randint(0, window_size, 10000)

#     p_value = generate_histogram(window_size, observations)

#     if p_value is not None:
#         if p_value <= 11.345:
#             print("Odrzucamy hipotezę zerową. Próbka nie pochodzi z rozkładu jednostajnego.")
#         else:
#             print("Nie ma podstaw do odrzucenia hipotezy zerowej. Próbka pochodzi z rozkładu jednostajnego.")

