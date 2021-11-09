import matplotlib.pyplot as plt
import numpy as np

# A histogram is a graph showing frequency distributions.
# It is a graph showing the number of observations within each given interval.

# hist() function will use an array of numbers to create a histogram
x = np.random.normal(170, 10, 250)
plt.hist(x)
plt.show() 