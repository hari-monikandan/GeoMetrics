# GeoMetrics

# Hari:
We're trying to implement a program that tracks user's cursor movement as they draw the shape, get (x,y) values, use those values to determine circuference d as a sum of distances calculated from the points

MATLAB
LabVIEW

# Dheepan:
In most cases users are probably not going to draw their own sketch since it doesn't gaurantee consistency and will be wobbly. So they will be looking to either use, construction elements such as arcs, curves, lines, regular polygons inbuilt into the platform.

Or they would just want to input a picture. (ML ?!)

Regardless, I think atleast as a starting point, the cursor-tracking feature must be done first.

# Dheepan:
The part of the code that relies on finding the distance between (x1,y1) and (x2,y2) can be written before hand since its not too complicated. Could be a first mini-task.