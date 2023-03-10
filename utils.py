import random

color_values = '0123456789abcdef'

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

def random_color_string () -> str:
    str = "#"
    for _ in range(6):
        str = str + random.choice(color_values)
    return str
