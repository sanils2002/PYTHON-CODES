import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o')
plt.show()

plt.plot(ypoints, marker = '*')
plt.show()

# Mark each point with a circle and in color
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, 'o:r')
plt.show()

# Marker size

ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20)
plt.show()

# mec and mfc arguments to color the entire marker:
ypoints = np.array([3, 8, 1, 10])

plt.plot(ypoints, marker = 'o', ms = 20, mec = 'b', mfc = 'r')
plt.show()

# Note: We can use Hexadecimal color values or even supported color names