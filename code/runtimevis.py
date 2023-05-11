# Cameron Kerr: May 11 2023 #
# Runtime testing for bowyerwatson.py #

import matplotlib.pyplot as plt
import numpy as np
import timeit
import math
import random
import bowyerwatson as bw

def full_function(n):
    min_coord = 0  # Minimum coordinate value
    max_coord = 1000  # Maximum coordinate value
    
    points = []
    x_list = []
    y_list = []
    for _ in range(n):
        x = random.uniform(min_coord, max_coord)
        y = random.uniform(min_coord, max_coord)
        point = bw.Point(x, y)
        points.append(point) 
    bw.bowyer_watson(points, testing = True)

# Sets up figure
plt.rcParams['figure.figsize'] = [10, 6]

# Generates 50 evenly spaced integers from 10 to 1000
ns = np.linspace(10, 500, 20, dtype=int)

# Runs runtime analysis for each n in ns
ts = [timeit.timeit('full_function({})'.format(n), 'from runtimevis import full_function', number=5)
      for n in ns]

# Plot runtime relative to n
plt.plot(ns, ts, 'ob')
plt.xlabel('n')
plt.ylabel('Time')
plt.title('Runtime of Bowyer Watson Algorithm')
plt.show()