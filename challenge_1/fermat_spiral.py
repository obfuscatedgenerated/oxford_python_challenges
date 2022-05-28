import matplotlib.pyplot as plt
import numpy as np

domain = np.arange(0, 16 * np.pi, 0.01)

a = 15
x = a * np.sqrt(domain) * np.cos(domain)
y = a * np.sqrt(domain) * np.sin(domain)

fig, ax = plt.subplots()

ax.plot(x,y)

ax.set(title="Fermat's Spiral", xlabel="x", ylabel="y")
ax.set_aspect("equal", adjustable="box")
fig.canvas.manager.set_window_title("Challenge 1.2: Fermat's Spiral")

plt.show()