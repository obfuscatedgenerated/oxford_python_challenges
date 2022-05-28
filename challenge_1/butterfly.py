import matplotlib.pyplot as plt
import numpy as np

domain = np.arange(0, 12 * np.pi, 0.01)

x = np.sin(domain) * ((np.e ** np.cos(domain)) - 2 * np.cos(4 * domain) - (np.sin(domain / 12)) ** 5)
y = np.cos(domain) * ((np.e ** np.cos(domain)) - 2 * np.cos(4 * domain) - (np.sin(domain / 12)) ** 5)

fig, ax = plt.subplots()

ax.plot(x,y)

ax.set(title="Butterfly", xlabel="x", ylabel="y")
ax.set_aspect("equal", adjustable="box")
fig.canvas.manager.set_window_title("Challenge 1.3: Butterfly")

plt.show()