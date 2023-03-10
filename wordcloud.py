#!/usr/bin/python3
import sys
import re
from typing import Any, List, Tuple
from numbers import Number

def proper_name (filename):
    # name = filename
    name = filename[:-4]
    l = len(name)
    idx = 0
    while idx < l and name[-idx] != '/':
        idx += 1
    if idx == l:
        return name
    return name[-idx+1:]

def open_and_split_file (filename: str):
    with open(filename, 'r') as file:
        words = file.read().lower().split()
    return words

def open_and_clean_file (filename: str, stop_name: str):
    stop_words = []
    if stop_name != "":
        stop_words = open_and_split_file(stop_name)
    with open(filename, 'r') as file:
        words = [word for word in 
                 re.sub("[^a-z0-9]+", " ", file.read().lower().replace('\n', ' ').replace('\r', ' ')).split()
                 if len(word) > 2 and word not in stop_words]
    return words

def frequency_dictionary (words: List[str]):
    d = dict()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def most_used_words (word_dict: dict, n: Number):
    return sorted(word_dict.items(), key=lambda item:item[1], reverse=True)[:n]

def tuple_list_to_simple_list (tuple_list: List[Tuple[str, Number]]):
    return [tuple[0] for tuple in tuple_list]

def words_to_csv (words_list: List[Tuple[str, Number]], filename: str):
    with open(filename + ".csv", "w") as file:
        file.write("\"weight\";\"word\";\"color\";\"url\"\n")
        for tuple in words_list:
            file.write(f"{str(tuple[1])};{tuple[0]};;\n")

if __name__ == "__main__":
    args = sys.argv
    print("WordCloudGenerator!")
    if len(args) > 1:
        filename = args[1]
        print(filename)
        stop_name = ""
        if len(args) > 2:
            stop_name = args[2]
        words = open_and_clean_file(filename, stop_name)
        print(f"{len(words)} words.")
        most_used = most_used_words(frequency_dictionary(words), 100)
        print(most_used)
        words_to_csv(most_used, proper_name(filename))
