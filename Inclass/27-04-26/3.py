import matplotlib.pyplot as plt
import numpy as np


x = np.array([1, 3, 5, 7, 9])
y = np.array([2, 5, 6, 9, 1])

fig, ax = plt.subplots(figsize=(10, 5), layout='constrained')
ax.scatter(x, y, s=(5), label='point Values')
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.set_title("GRIDS BRO!")
ax.grid()
ax.legend()
ax.set_facecolor("Cyan")
plt.show()
