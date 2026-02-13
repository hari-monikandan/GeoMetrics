import numpy as np
import matplotlib.pyplot as plt
import math

a = input('What is the value of semi-major axis?')
b = input('What is the value of semi-minor axis?')

major = int(a)
minor = int(a)

# Creating a list of x-values between (0,0) and (a,0). Total circumference is 4 times the first quadrant

x_values = np.linspace(0,major,10000)

# Formula for an ellipse is y = sqrt(a^2 - x^2)*(b/a). So finding y values for corresponding x points.

y_values = np.sqrt(major**2 - x_values**2)*(minor/major)

# Now need to order pairs (x,y) and find distances between every consecutive point.

ordered_pair = [(x,y) for x,y in zip(x_values, y_values)]

# Finding distance between pairs

def distance_finder(point1, point2):
    return np.sqrt((point1[0]-point2[0])**2 + (point1[1] - point2[1])**2)

# Find all the small line distances between the ordered pairs

small_dists = [distance_finder(ordered_pair[i], ordered_pair[i+1]) for i in range(0, len(ordered_pair)-1)]

# Total circumference of ellipse is 4 times the sum of all the small distances in first quadrant.
print(4*sum(small_dists))