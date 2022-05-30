import matplotlib.pyplot as plt # import dependencies
import numpy as np

domain = np.arange(0, 2 * np.pi, 0.01) # define the domain from 0 to 2pi (0.01 step for precision)

x = np.sin(domain) # calculate x values for each point in the domain, sin(Θ)
y = np.cos(domain) # calculate y values for each point in the domain, cos(Θ)

fig, ax = plt.subplots() # create a figure and an axis

ax.plot(x,y) # plot the x and y values

ax.set(title="Sine-Cosine Circle", xlabel="x", ylabel="y") # set the title, axis labels, aspect ratio, and window title
ax.set_aspect("equal", adjustable="box")
fig.canvas.manager.set_window_title("Challenge 1.1: Sine-Cosine Circle")

plt.show() # show the plot