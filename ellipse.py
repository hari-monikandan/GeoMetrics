import numpy as np
import matplotlib.pyplot as plt
import math

a = input('What is the value of semi-major axis?')
b = input('What is the value of semi-minor axis?')

major = int(a)
minor = int(a)

# Creating a list of x-values between (0,0) and (a,0). Total circumference is 4 times the first quadrant

x_values = np.linspace(0,major,10)

# Formula for an ellipse is y = sqrt(a^2 - x^2)*(b/a). So finding y values for corresponding x points.

y_values = np.sqrt(major**2 - x_values**2)*(minor/major)

# Now need to order pairs (x,y) and find distances between every consecutive point.

ordered_pair = [(x,y) for x,y in zip(x_values, y_values)]

print(ordered_pair)