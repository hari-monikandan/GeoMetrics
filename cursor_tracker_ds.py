# Need to write a code that can track (x,y) coordinates and find circumference in pixels.
# There should also be an option to set a scale to get answer in physical units
 
# The package pyautogui seems to be a nice method to retreive mouse positions.
import pyautogui
import matplotlib.pyplot as plt

print('Press Ctrl-C to quit.')

list_coordinates = []
try:
    while True:
        x, y = pyautogui.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
        list_coordinates.append(tuple((x,y)))
except KeyboardInterrupt:
    plt.plot([x[0] for x in list_coordinates], [y[1] for y in list_coordinates])
    plt.show()
    print('\n')