import matplotlib.pyplot as plt
import numpy as np


# Line styles
# 'solid' (default)	'-'	
# 'dotted'			':'	
# 'dashed'			'--'	
# 'dashdot'			'-.'	
# 'None'				'' or ' '

# Apply Line Styles
ypoints = np.array([3, 8, 1, 10])

# argument linestyle, or shorter ls
plt.plot(ypoints, linestyle = 'dotted')
plt.show()

# Line Color
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, color = 'r')
plt.show()

plt.plot(ypoints, c = '#4CAF50') # parameter c can be any color name as well
plt.show()

# Line Width
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, linewidth = '20.5')
plt.show()

# Multi-Lines: Example 1
y1 = np.array([3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])

plt.plot(y1)
plt.plot(y2)
plt.show()

# Multi-Lines: Example 2
x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()
