import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.collections import LineCollection
import numpy as np

domain = np.arange(0, 16 * np.pi, 0.01)

x = np.sqrt(domain) * np.cos(domain)
y = np.sqrt(domain) * np.sin(domain)

fig, ax = plt.subplots()

ax.plot(x,y)

line_segs = []
r = np.sqrt(x**2 + y**2)


for i in range(len(x) - 1):
    line_segs.append([(x[i], y[i]), (x[i+1], y[i+1])])

color = LineCollection(line_segs, cmap=cm.Blues_r)
color.set_array(r)
ax.add_collection(color)

ax.set(title="Fermat's Spiral", xlabel="x", ylabel="y")
ax.set_aspect("equal", adjustable="box")
fig.canvas.manager.set_window_title("Challenge 1.2: Fermat's Spiral")

plt.show()