import csv
import random
import numpy as np
from wordcloud import open_and_clean_file, frequency_dictionary, sort_words

def random_vectors(n):
    vectors = []
    for _ in range(1024):
        vectors.append([random.choice([-1,1]) for _ in range(n)])
    return vectors

def cos_distance(v1, v2):
    return np.dot(v1,v2)/(np.linalg.norm(v1) * np.linalg.norm(v2))



if __name__ == "__main__":
    dramas = ["hamlet", "KingLear", "Othello", "RomeoJuliet"]
    words = {drama: [] for drama in dramas}
    omega = []
    words_dict = {drama: dict() for drama in dramas}
    for drama in dramas:
        cleaned_words = open_and_clean_file("Szekspir/{}.txt".format(drama), "Szekspir/stop_words_english.txt", True)
        freq_dict = frequency_dictionary(cleaned_words)
        words_dict[drama] = freq_dict
        omega += cleaned_words

    omega = set(omega)
    n = len(omega)
    print(f"n={n}")
    vectors = random_vectors(n)
    scalar_products = {drama: [] for drama in dramas}

    for drama in dramas:
        drama_words = set(words_dict[drama].keys())
        diff = omega.difference(drama_words)
        for word in diff:
            words_dict[drama][word] = 0
        words[drama] = sort_words(words_dict[drama])
        drama_counts = [pair[1] for pair in words[drama][:]]
        for vector in vectors:
            scalar_products[drama].append(np.sign(np.dot(vector,drama_counts)))
        
    for drama_1 in dramas:
        for drama_2 in dramas:
            if drama_1 < drama_2:
                print("{} vs {}:\t{}".format(drama_1,drama_2,cos_distance(scalar_products[drama_1],scalar_products[drama_2])))

