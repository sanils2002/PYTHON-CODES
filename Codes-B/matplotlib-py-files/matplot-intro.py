# check version

import matplotlib

print(matplotlib.__version__)

# pyplot submodule of matplotlib: Most of the Matplotlib utilities lies under the pyplot submodule

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([0, 6])
ypoints = np.array([0, 250])

plt.plot(xpoints, ypoints)
plt.show()