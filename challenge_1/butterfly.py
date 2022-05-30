import matplotlib.pyplot as plt # import dependencies
from matplotlib import cm
from matplotlib.collections import LineCollection
import numpy as np

domain = np.arange(0, 12 * np.pi, 0.01) # define the domain from 0 to 12pi (0.01 step for precision)

x = np.sin(domain) * ((np.e ** np.cos(domain)) - 2 * np.cos(4 * domain) - (np.sin(domain / 12)) ** 5) # calculate x values for each point in the domain, sin(Θ) * (e^cos(Θ) - 2cos(4Θ) - (sin(Θ/12))^5)
y = np.cos(domain) * ((np.e ** np.cos(domain)) - 2 * np.cos(4 * domain) - (np.sin(domain / 12)) ** 5) # calculate y values for each point in the domain, cos(Θ) * (e^cos(Θ) - 2cos(4Θ) - (sin(Θ/12))^5)

fig, ax = plt.subplots() # create a figure and an axis

ax.plot(x,y) # plot the x and y values

line_segs = [] # create an empty list to store the line segments
r = np.sqrt(x**2 + y**2) # calculate the radius at each point


for i in range(len(x) - 1): # iterate points in the domain to create an array of line segments (samples of the line between a point and the next point along)
    line_segs.append([(x[i], y[i]), (x[i+1], y[i+1])])

color = LineCollection(line_segs, cmap=cm.rainbow) # define and assign a LineCollection with the line segments to use the colour map, using the radius as the colour value
color.set_array(r)
ax.add_collection(color)


ax.set(title="Butterfly", xlabel="x", ylabel="y") # set the title, axis labels, aspect ratio, and window title
ax.set_aspect("equal", adjustable="box")
fig.canvas.manager.set_window_title("Challenge 1.3: Butterfly")

plt.show() # show the plot