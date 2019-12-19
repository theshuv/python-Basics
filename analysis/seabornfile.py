# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:37:30 2019

@author: dbda24
"""

# Import the necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import ListedColormap

# Define a variable N
N = 500

#Construct the colormap
#There are six variations of the default theme,
#called deep, muted, pastel, bright, dark, and colorblind.
current_palette = sns.color_palette("muted", n_colors=5)
cmap = ListedColormap(sns.color_palette(current_palette).as_hex())
print(type(cmap))
# Initialize the data
data1 = np.random.randn(N)
data2 = np.random.randn(N)
# Assume that there are 5 possible labels
colors = np.random.randint(0,5,N)

# Create a scatter plot
#cmap is optional but if given it will be used only if list assign to c is float numbers
plt.scatter(data1, data2, c=colors, cmap=cmap)

# Add a color bar
plt.colorbar()

# Show the plot
plt.show()
