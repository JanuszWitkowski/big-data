#!/usr/bin/python3
import argparse
import re
from typing import Any, List, Tuple
from numbers import Number
from math import log2
from utils import proper_name, random_color_string

# Simple function that just splits file into list of lines.
def open_and_split_file (filename: str) -> List[str]:
    with open(filename, 'r') as file:
        words = file.read().lower().split()
    return words

def open_and_clean_file (filename: str, stop_name: str, remove_short: bool) -> List[str]:
    stop_words = []
    if stop_name != "":
        stop_words = open_and_split_file(stop_name)
    with open(filename, 'r') as file:
        words = [word for word in 
                 re.sub("[^a-z0-9]+", " ", file.read().lower().replace('\n', ' ').replace('\r', ' ')).split()
                 if ((not remove_short) or len(word) > 2) and word not in stop_words]
    return words

def frequency_dictionary (words: List[str]) -> dict:
    d = dict()
    for word in words:
        if word in d:
            d[word] += 1
        else:
            d[word] = 1
    return d

def most_used_words (word_dict: dict, n: int) -> List[Tuple[str, Number]]:
    return sorted(word_dict.items(), key=lambda item:item[1], reverse=True)[:n]

def tuple_list_to_simple_list (tuple_list: List[Tuple[str, Number]]) -> List[str]:
    return [tuple[0] for tuple in tuple_list]

def words_to_csv (words_list: List[Tuple[str, Number]], filename: str, with_color: bool) -> None:
    if with_color:
        with open(filename + ".csv", "w") as file:
            file.write("\"weight\";\"word\";\"color\";\"url\"\n")
            for tuple in words_list:
                file.write(f"{str(int(tuple[1]))};{tuple[0]};{random_color_string()};\n")
    else:
        with open(filename + ".csv", "w") as file:
            file.write("\"weight\";\"word\";\"color\";\"url\"\n")
            for tuple in words_list:
                file.write(f"{str(int(tuple[1]))};{tuple[0]};;\n")


def dict_key_int (dict: dict, key: Any) -> int:
    if key in dict:
        return dict[key]
    else:
        return 0

def how_many_in_dictionaries (word: str, dicts: List[dict]) -> int:
    ctr = 0
    for dict in dicts:
        if dict_key_int(dict, word) > 0:
            ctr += 1
    return ctr

def documents_dictionaries (filenames: List[str], stop_name: str):
    return [frequency_dictionary(open_and_clean_file(filename, stop_name, True)) for filename in filenames]

def calculate_tf (word: str, doc_dict: dict) -> Number:
    return dict_key_int(doc_dict, word)

def calculate_idf (word: str, Documents: List[dict]) -> Number:
    return log2(len(Documents) / how_many_in_dictionaries(word, Documents))

def tfidf (word: str, doc_dict: dict, Documents: List[dict]) -> Number:
    return calculate_tf(word, doc_dict) * calculate_idf(word, Documents)

def tfidf_dictionary (doc: dict, Documents: List[dict]) -> dict:
    tfidf_dict = dict()
    for word in doc:
        tfidf_dict[word] = tfidf(word, doc, Documents)
    return tfidf_dict


if __name__ == "__main__":
    print("WordCloudGenerator!")
    argParser = argparse.ArgumentParser()
    argParser.add_argument("input", nargs='+', type=str, help="txt files to create word clouds from")
    argParser.add_argument("-s", "--stop", type=str, help="file with stop-words")
    argParser.add_argument("-t", "--top", type=int, help="select top n words by frequency")
    argParser.add_argument("-i", "--tfidf", action="store_true", help="use TF-IDF as a frequency counter; check for the first given file")
    argParser.add_argument("-c", "--color", action="store_true", help="make csv file with random colors")
    args = argParser.parse_args()

    stop_name = ""
    if args.stop != None:
        stop_name = args.stop
    top = 100
    if args.top != None:
        top = args.top
    
    if args.input == None:
        print("Error: No input file was specified.")
    else:
        if args.tfidf:
            print("tfidf")
            docs_dicts = documents_dictionaries(args.input, stop_name)
            main_doc = docs_dicts[0]
            most_used = most_used_words(tfidf_dictionary(main_doc, docs_dicts), top)
            print(f"Top {top} words by TF-IDF:")
            print(tuple_list_to_simple_list(most_used))
            words_to_csv(most_used, proper_name(args.input[0]) + '_tf-idf', args.color)
        else:
            for filename in args.input:
                print(f"File: {filename}")
                words = open_and_clean_file(filename, stop_name, True)
                print(f"{len(words)} words.")
                most_used = most_used_words(frequency_dictionary(words), top)
                print(f"Top {top} words by frequency:")
                print(tuple_list_to_simple_list(most_used))
                words_to_csv(most_used, proper_name(filename), args.color)

