import matplotlib.pyplot as plt
import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()

# graph without line
# plt.plot(xpoints, ypoints, 'o')
# plt.show()

# Multiple points
xpoints = np.array([1, 2, 6, 8])
ypoints = np.array([3, 8, 1, 10])

# plt.plot(xpoints, ypoints)
# plt.show()

# # Default X-Points: If we do not specify the points in the x-axis, they will get the default values 0, 1, 2, 3,...
# plt.plot(ypoints)
# plt.show()

# Markers
# plt.plot(ypoints, marker = 'o')
# plt.show()

# plt.plot(ypoints, marker = '*')
# plt.show()

# Marker	Description
# 'o'	    Circle	
# '*'	    Star	
# '.'	    Point	
# ','     Pixel	
# 'x'	    X	
# 'X'	    X (filled)	
# '+'	    Plus	
# 'P'	    Plus (filled)	
# 's'	    Square	
# 'D'	    Diamond	
# 'd'	    Diamond (thin)	
# 'p'	    Pentagon	
# 'H'	    Hexagon	
# 'h'	    Hexagon	
# 'v'	    Triangle Down	
# '^'	    Triangle Up	
# '<'	    Triangle Left	
# '>'	    Triangle Right	
# '1'	    Tri Down	
# '2'	    Tri Up	
# '3'	    Tri Left	
# '4'	    Tri Right	
# '|'	    Vline	
# '_'	    Hline

# Format Strings fmt

# You can use also use the shortcut string notation parameter to specify the marker.

# This parameter is also called fmt, and is written with this syntax:

# marker|line|color

# plt.plot(ypoints, 'o:r')
# plt.show()

# Line Syntax	    Description
# '-'	            Solid line	
# ':'	            Dotted line	
# '--'	        Dashed line	
# '-.'	        Dashed/dotted line

# Color Syntax	Description
# 'r'	            Red	
# 'g'	            Green	
# 'b'	            Blue	
# 'c'	            Cyan	
# 'm'	            Magenta	
# 'y'	            Yellow	
# 'k'	            Black	
# 'w'	            White
# 'hotpink'         Pink

# Marker Size (ms)

# plt.plot(ypoints, marker = 'o', ms = 20)
# plt.show()

# Marker Color 
# markeredgecolor or mec
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r')
# plt.show()

# # markerfacecolor or mfc
# plt.plot(ypoints, marker = 'o', ms = 20, mfc = 'r')
# plt.show()

# Using Hexadecimal Value for color
# plt.plot(ypoints, marker = 'o', ms = 20, mec = 'r', mfc = 'g')
# plt.show()

# LineStyle

# plt.plot(ypoints, linestyle = ':')
# plt.show()

# The line style can be written in a shorter syntax:

# linestyle can be written as ls

# dotted can be written as :

# dashed can be written as --

# Line Color

# plt.plot(ypoints, color = 'r')
# plt.show()

# plt.plot(ypoints, c = '#4CAF50')
# plt.show()

# Line Width
# plt.plot(ypoints, linewidth = '20.5')
# plt.show()

# two lines by specifying a plt.plot() function for each line

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()

# two lines by specifiyng the x- and y-point values for both lines

# x1 = np.array([0, 1, 2, 3])
# y1 = np.array([3, 8, 1, 10])
# x2 = np.array([0, 1, 2, 3])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(x1, y1, x2, y2)
# plt.show()

# # Labels
x = np.array([80, 85, 90, 95, 100, 105, 110, 115, 120, 125])
y = np.array([240, 250, 260, 270, 280, 290, 300, 310, 320, 330])

# plt.plot(x, y)

# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.show()

# # Title

# plt.plot(x, y)

# plt.title("Sports Watch Data", loc = 'left')
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")
# plt.show()

# Font Properties
# font1 = {'family':'serif','color':'blue','size':20}
# font2 = {'family':'serif','color':'darkred','size':15}

# plt.title("Sports Watch Data", fontdict = font1)
# plt.xlabel("Average Pulse", fontdict = font2)
# plt.ylabel("Calorie Burnage", fontdict = font2)

# plt.plot(x, y)
# plt.show()

# Grid
# plt.title("Sports Watch Data")
# plt.xlabel("Average Pulse")
# plt.ylabel("Calorie Burnage")

# plt.plot(x, y)

# # plt.grid()
# # plt.grid(axis = 'x')
# # plt.grid(axis = 'y')
# plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)

# plt.show()