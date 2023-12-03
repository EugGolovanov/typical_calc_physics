import numpy as np
g = np.float64(9.80665)
a = np.float64(2)
m = np.float64(0.2)
alpha = np.arctan(g/a)
d_alpha = alpha * (0.00001/g)
F = m*np.sqrt(np.power(a, 2) + np.power(g, 2))
print('alpha =', round(alpha, 6), '+-', round(d_alpha,6))
print('F = ', round(F, 6), '+- 1e-06')
