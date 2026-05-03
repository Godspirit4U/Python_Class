import matplotlib.pyplot as plt
import numpy as np

n = int(input("ENter no of iterations: "))

x = np.random.uniform(1, -1, n)
y = np.random.uniform(1, -1, n)

in_circle = x**2 + y**2 <= 1
cum_sum = np.cumsum(in_circle)
# print(in_circle)
total_noof_point = np.arange(1, n+1)
pi_value = 4 * (cum_sum[-1] / total_noof_point)
print(pi_value)
