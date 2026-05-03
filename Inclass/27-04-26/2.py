import matplotlib.pyplot as plt
import numpy as np


x = np.array([x for x in range(0, 11)])
y = x ** 2

print(x)
print(y)


fig, ax = plt.subplots(
    figsize=(10, 8), layout='constrained')
ax.plot(x, y)
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.set_title("GRIDS BRO!")
ax.set_facecolor("Pink")
ax.set_visible("True")
ax.set_frame_on("True")
plt.show()
