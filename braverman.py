#!/usr/bin/python3
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

