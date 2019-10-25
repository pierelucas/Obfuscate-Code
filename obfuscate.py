# Author: PiereLucas(Julian Huch)
# MIT LICENSE

"""
Python obfuscate to to mask code.
Afer masking you have to write a short de-mask and 'eval' script to run.
For some higher grade you can compile your masked code to python bytecode with:
'python -OO -m py_compile <your_script.py>' after that just rename the '.pyc' to '.py'
"""


import os
import string
import random


def rnd_str():
    letters = string.ascii_lowercase+ string.digits
    return "".join(random.choice(letters) for i in range(6))

def read_file():
    while True:
        filepath = str(input("Filepath: "))
        if os.path.exists(filepath):
            with open(filepath, 'rt') as f:
                r_string = f.read()
            return filepath, r_string
        else: continue

def write_file(filepath, c_string):
    newpath = rnd_str() + filepath
    with open(newpath, 'wt') as f:
        f.write(c_string)
    return newpath

def rot13(r_string):
    d = {}
    for c in (65, 97):
        for i in range(26):
            d[chr(i+c)] = chr((i+13) % 26 + c)
    return "".join([d.get(c, c) for c in r_string])


if __name__ == "__main__":
    filepath, r_string = read_file()
    c_string = rot13(r_string)
    newpath = write_file(filepath, c_string)
    print("Sucesfully de/obfuscated → de/obfuscated File:", newpath)
