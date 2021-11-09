import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D"])
y = np.array([3, 8, 1, 10])

# plt.bar(x,y)
# plt.show()

# Horizontal bars
# plt.barh(x, y)
# plt.show()

# Add Colour
# plt.bar(x, y, color = "red")
# plt.show()


# changing widht 
# plt.bar(x, y, width = 0.1)
# plt.show()

# changing height of horizontal bars
plt.barh(x, y, height = 0.1)
plt.show()