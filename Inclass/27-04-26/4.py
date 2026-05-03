import matplotlib.pyplot as plt
import numpy as np


x = np.random.uniform(-1, 1, 10)
y = np.random.uniform(-1, 1, 10)
fig, ax = plt.subplots(figsize=(10, 10), layout='constrained')
ax.scatter(x, y)
ax.grid()
ax.set_facecolor("Teal")
plt.show()
