#!/usr/bin/env python

import sys
from PIL import Image

if (len(sys.argv) not in [3, 4]):
    print "Usage: ./convert.py source.asc dest.png [height scaling]"
    exit()

def scale(input, scale_factor):
    input += 40
    return input / 1024.0 * 2**16 * scale_factor

source_path = sys.argv[1]
dest_path = sys.argv[2]

scale_factor = 1.0
if len(sys.argv) == 4:
    scale_factor_str = sys.argv[3]
    try:
        scale_factor = float(scale_factor_str)
    except:
        print "Could not parse double value from %s. Defaulting to %d" % (scale_factor_str, scale_factor)

file = open(source_path)
content = [x.strip('\n') for x in file.readlines()]
heights = content[6:]

map = Image.new('I', (3000,3000))

heights_ints = [[scale(int(float(x)), scale_factor) for x in row.strip().split(" ")] for row in heights]

offset = 0
for row in heights_ints:
    for pixel in row:
        map.putpixel((offset % 3000, offset / 3000), pixel)
        offset += 1

map.save(dest_path)

