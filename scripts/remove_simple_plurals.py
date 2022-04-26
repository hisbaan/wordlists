#!/usr/bin/python3

import sys
import re

dictionary = dict()

with open(sys.argv[1], "r") as file:
    for line in file:
        if (line != '\n'):
            dictionary[line] = 1
file.close()

r = re.compile(r's$')

remove_list = set()

for i in dictionary.keys():
    if r.search(i):
        if re.sub(r, r'', i) in dictionary:
            remove_list.add(i)

for i in remove_list:
    print(i[0:-1])
    dictionary.pop(i)

list = dictionary.keys()

outfile = open(sys.argv[2], "w")
for item in list:
    outfile.write(item)
outfile.close()
