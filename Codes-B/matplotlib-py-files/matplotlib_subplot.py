import matplotlib.pyplot as p
import numpy as np

# # 2 plots side by side
# #plot 1:
# x = np.array([0, 1, 2, 3])
# y = np.array([3, 8, 1, 10])

# p.subplot(1, 2, 1)           # 1st parameter:no. of row, 2nd parameter:no. of column, 3rd parameter: first plot
# p.plot(x,y)

# #plot 2:
# x = np.array([0, 1, 2, 3])
# y = np.array([10, 20, 30, 40])

# p.subplot(1, 2, 2)     # 1st parameter:no. of row, 2nd parameter:no. of column, 3rd parameter: second plot
# p.plot(x,y)

# p.show()
#----------------------------------------------------------------------------------------------------------------

# 2 plots one after other
#plot 1:
x = np.array([0, 1, 2, 3])
y = np.array([3, 8, 1, 10])

p.subplot(2, 1, 1)
p.plot(x,y)

#plot 2:
x = np.array([0, 1, 2, 3])
y = np.array([10, 20, 30, 40])

p.subplot(2, 1, 2)
p.plot(x,y)

p.show()