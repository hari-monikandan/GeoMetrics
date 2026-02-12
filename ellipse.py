import numpy as np
import matplotlib.pyplot as plt
import math as m

a = input('What is the value of semi-major axis?')
b = input('What is the value of semi-minor axis?')

# Creating a list of x-values between (0,0) and (a,0). Total circumference is 4 times the first quadrant

x = np.linspace(0,a,10000)

# Formula for an ellipse is y = sqrt(a^2 - x^2)*(b/a). So finding y values for corresponding x points.

y = m.sqrt(a**2 - x**2)*(b/a)

# Now need to order pairs (x,y) and find distances between every consecutive point.

ordered_pair = [(i,j) for i in x for j in y]