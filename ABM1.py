# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Initialise variable x0
# Initialise variable y0
# Change x0 and y0 randomly
# Initialise variable x1
# Initialise variable y1
# Change x1 and y1 randomly
# Calculate the Euclidean distance between (x0, y0) and (x1, y1)

import random
import math

x0=0
y0=0
x1=3
y1=4
print("x0", x0)
print("y0", y0)
rn = random.randint(0,99)
if rn < 50:
    x0 = x0 + 1
    y0 = y0 + 3
    x1 = x1 + 18
    y1 = y1 + 8
else:
    x0 = x0 - 1
    y0 = y0 -3
    x1 = x1 - 18
    y1 = y1 - 8
print("x0", x0)
print("rn", rn)
print("y0", y0)
print("x1", x1)
print("y1", y1)

distance= ((x1 - x0)**2+(y1 - y0)**2)**0.5
print("distance", distance)

