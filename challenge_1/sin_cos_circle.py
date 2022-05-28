import matplotlib.pyplot as plt
import numpy as np

domain = np.arange(0, 2 * np.pi, 0.01)

x = np.sin(domain)
y = np.cos(domain)

fig, ax = plt.subplots()

ax.plot(x,y)

ax.set(title="Sine-Cosine Circle", xlabel="x", ylabel="y")
ax.set_aspect("equal", adjustable="box")
fig.canvas.set_window_title("Challenge 1.1: Sine-Cosine Circle")

plt.show()