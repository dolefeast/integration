import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


v0 = [0, 10, 1, 0]

def acc(v, t):
    u = v[:2]
    r = np.linalg.norm(u)
    udot = v[2:]
    
    udotdot = - c * r**-3 * u
    return np.r_[udot, udotdot]    

t = np.linspace(0, 200, 500)

G = 1
M = 10
c = G * M

p_path = spi.odeint(acc, v0, t)

fig, ax = plt.subplots(1, 1)

for i in p_path:
    plt.plot((i[0], i[1]))

plt.show()
