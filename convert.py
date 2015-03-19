#!/usr/bin/env python

import sys
from PIL import Image

if (len(sys.argv) not in [3, 4]):
    print "Usage: ./convert.py source.asc dest.png [height scaling]"
    exit()

def scale(input, scale_factor):
    # Raise lowest value to a minimum of 40m to allow some depth for lakes.
    input += 40

    # Cities supports heights of 0-1024m.
    input /= 1024.0

    # Scale to 16-bit value.
    input *= 2**16

    # Scale with user provided scale factor to increase contrast.
    input *= scale_factor

    return input

source_path = sys.argv[1]
dest_path = sys.argv[2]

scale_factor = 1.0
if len(sys.argv) == 4:
    scale_factor_str = sys.argv[3]
    try:
        scale_factor = float(scale_factor_str)
    except:
        print "Could not parse double value from %s. Defaulting to %d" % (scale_factor_str, scale_factor)


map = Image.new('I', (3000,3000))
pixel_loc = 0

with open(source_path) as file:
    for line in file:
        # Skip non-data rows. Data rows should start with 1-9.
        if line[0] not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            continue

        heights = [scale(int(float(x)), scale_factor) for x in line.strip().split(" ")]
        for height in heights:
            x = pixel_loc % 3000
            y = pixel_loc / 3000
            map.putpixel((x, y), height)
            pixel_loc += 1

map.save(dest_path)

