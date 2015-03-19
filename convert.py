#!/usr/bin/env python

import sys
from PIL import Image

if (len(sys.argv) != 3):
    print "Usage: ./convert.py source.asc dest.png"
    exit()

def scale(input):
    input += 40
    return input / 1024.0 * 2**16 * 4

source_path = sys.argv[1]
dest_path = sys.argv[2]

file = open(source_path)
content = [x.strip('\n') for x in file.readlines()]
heights = content[6:]

map = Image.new('I', (3000,3000))

heights_ints = [[scale(int(float(x))) for x in row.strip().split(" ")] for row in heights]

offset = 0
for row in heights_ints:
    for pixel in row:
        map.putpixel((offset % 3000, offset / 3000), pixel)
        offset += 1

map.save(dest_path)

