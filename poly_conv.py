import numpy as np

p1 = [1, -1, 2, 0]
p2 = [1, -3]

result = np.convolve(p1, p2)
print(result)