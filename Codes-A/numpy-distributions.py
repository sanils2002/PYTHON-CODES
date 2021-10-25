# Use the random.normal() method to get a Normal Data Distribution.
# Its 3 parameters:
# loc - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat the graph distribution should be.
# size - The shape of the returned array.

from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

# Binomial Distribution
# Its parameters:
# n - number of trials.
# p - probability of occurence of each trial
# size - The shape of the returned array.

x = random.binomial(n=10, p=0.5, size=10)
print(x)

# Uniform Distribution
# Its 3 parameters:
# a - lower bound - default 0 .0.
# b - upper bound - default 1.0.
# size - The shape of the returned array.

x = random.uniform(size=(2, 3))
print(x)