from system import System
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def force(p1, p2):
	"""spring force"""
	k = 0
	r = p1[:2] - p2[:2] #[:2] are the positions of the particles,
						#[2:] are the speeds
	return k * r

np.random.seed(0)
P1 = 5*np.random.random(4)
P2 = 5*np.random.random(4)

state0 = [P1, P2]
mass = [1, 2]
charge = [1, -1]

width = 1
dt = 1
T = 100
sim = System(state0, force, mass, charge, width, dt, T)

solution = sim.integrate_odeint()

fig, ax = plt.subplots()


#TODO Find a way to plot using FuncAnimation from a 'configurational
#matrix'. We have each position and speed for each time, so given
#that we should be able to plot it fairly 'easily'

plt.show()
