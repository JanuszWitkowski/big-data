#!/usr/bin/python3
import sys
import re

if __name__ == "__main__":
    args = sys.argv
    print("WordCloudGenerator!")
    if len(args) > 1:
        filename = args[1]
        print(filename)
        with open(filename, 'r') as file:
            data = re.sub("^[a-z0-9]+", " ", file.read().lower().replace('\n', ' ').replace('\r', ' ')).split()
        print(data)
