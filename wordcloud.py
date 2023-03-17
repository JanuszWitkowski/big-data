#!/usr/bin/python3
import argparse
import re
from typing import Any, List, Tuple
from utils import proper_name, random_color_string

def open_and_split_file (filename: str) -> List[str]:
    with open(filename, 'r') as file:
        words = file.read().lower().split()
    return words

def open_and_clean_file (filename: str, stop_name: str) -> List[str]:
    stop_words = []
    if stop_name != "":
        stop_words = open_and_split_file(stop_name)
    with open(filename, 'r') as file:
        words = [word for word in 
                 re.sub("[^a-z0-9]+", " ", file.read().lower().replace('\n', ' ').replace('\r', ' ')).split()
                 if len(word) > 2 and word not in stop_words]
    return words

def frequency_dictionary (words: List[str]) -> dict:
    d = dict()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def most_used_words (word_dict: dict, n: int) -> List[Tuple[str, int]]:
    return sorted(word_dict.items(), key=lambda item:item[1], reverse=True)[:n]

def tuple_list_to_simple_list (tuple_list: List[Tuple[str, int]]) -> List[str]:
    return [tuple[0] for tuple in tuple_list]

def words_to_csv (words_list: List[Tuple[str, int]], filename: str) -> None:
    with open(filename + ".csv", "w") as file:
        file.write("\"weight\";\"word\";\"color\";\"url\"\n")
        for tuple in words_list:
            file.write(f"{str(tuple[1])};{tuple[0]};{random_color_string()};\n")

if __name__ == "__main__":
    print("WordCloudGenerator!")
    argParser = argparse.ArgumentParser()
    argParser.add_argument("input", type=str, help="txt file to create word cloud from")
    argParser.add_argument("-s", "--stop", type=str, help="file with stop-words")
    argParser.add_argument("-t", "--top", type=int, help="select top n words by frequency")
    argParser.add_argument("-i", "--tfidf", action="store_true", help="use TF-IDF as a frequency counter")
    args = argParser.parse_args()
    if args.input == None:
        print("Error: No input file was specified.")
    else:
        filename = args.input
        stop_name = ""
        if args.stop != None:
            stop_name = args.stop
        top = 100
        if args.top != None:
            top = args.top
        print(f"File: {filename}")
        words = open_and_clean_file(filename, stop_name)
        print(f"{len(words)} words.")
        most_used = most_used_words(frequency_dictionary(words), 100)
        print(f"Top {top} words by frequency:")
        print(tuple_list_to_simple_list(most_used))
        words_to_csv(most_used, proper_name(filename))

