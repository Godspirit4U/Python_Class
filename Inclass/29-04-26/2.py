import matplotlib.pyplot as plt
import numpy as np

n = int(input("ENter no of iterations: "))

x = np.random.uniform(1, -1, n)
y = np.random.uniform(1, -1, n)

in_circle = x**2 + y**2 <= 1
cum_sum = np.cumsum(in_circle)
total_noof_point = np.arange(1, n+1)
pi_value = (4 * cum_sum) / total_noof_point
fig, ax = plt.subplots(1,2,figsize = (12,6), layout = "constrained")
ax[0].plot(total_noof_point, label = "PI Value")
ax[0].grid()
ax[0].axhline(np.pi, colour = "red")
ax[0].set_xlabel("Number of Iterations")
ax[0].set_ylabel("PI Values")
ax[0].legend()
ax[1].add