import numpy as np

# a = np.arange(5, 10, 2)
# print(a)

# print(np.linspace(0, 10, 5))

# x = np.ones(2, dtype=np.int64)
# print(x)


a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.array([[7, 8, 9], [10, 11, 12]])

c = np.concatenate((a, b), axis=1)
d = np.concatenate((a, b), axis=0)
print(c)
print("\n")
print(d)
