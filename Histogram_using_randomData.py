# import Numpy and matplotlib
from matplotlib import pyplot as plt
import numpy as np


# Creating random dataset
data_set = np.random.randint(100, size=(50))

# Creation of plot
fig = plt.figure(figsize=(10, 6))

# plotting the Histogram with certain intervals
plt.hist(data_set, bins=[0, 10, 20, 30, 40, 50,
						60, 70, 80, 90, 100])

# Giving title to Histogram
plt.title("Random Histogram")

# Displaying Histogram
plt.show()
