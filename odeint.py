import numpy as np
from time import sleep
import scipy.integrate as spi
import matplotlib.pyplot as plt


m = 1
k = 1
g = 9.81

#vo = [r, r_dot] = [u, u_dot], u = (x, y)
v0 = np.zeros(4)
v0[2] = 4
v0[3] = 10

def f(v, t0, k):
    u = v[:2]
    u_dot = v[2:]

    udotdot = -k/m * u_dot
    udotdot[1] = -g

    return np.r_[u_dot, udotdot]

fig, ax = plt.subplots(1, 1, figsize=(8, 4))

t = np.linspace(0, 3, 30)

v = spi.odeint(f, v0, t, args = (k,))
ax.plot(v[:, 0], v[:, 1], 'o-', mew = 1, ms = 8,
      mec = 'w', label = f'{k:.1f}')
print(v)

ax.legend()
ax.set_xlim(0,12)
ax.set_ylim(0,6)
plt.show()

