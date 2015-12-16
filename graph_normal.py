from math import pi, e, sqrt
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import quad
from numpy import trapz
from matplotlib.patches import Rectangle

mean = 0
variance = 1
sigma = sqrt(variance)
Z = 1.28
alternate_mean = 3

# formula for Gaussian distribution, proof of God
def get_y(x, mean, variance, sigma):
	return (e**((-(x-mean)**2)/2*variance))/(sigma * sqrt(2*pi))

# suggestion from stack overflow, returns the index of the nearest matching value
def get_x_index(xs, Z):
	return min(range(len(xs)), key=lambda i: abs(xs[i]-Z))

def graph_normal(mean, variance):
	fig = plt.figure()
	xs = list(np.linspace(-4, 4, 1000))
	ys = [get_y(x, mean, variance, sigma) for x in xs]
	plt.plot(xs, ys)
	plt.vlines(0, ymin=0, ymax=max(ys))
	plt.xlabel("Z Values")
	plt.title("Normal Distribution")
	return fig, xs, ys

def fill_graph(fig, xs, ys, Z, outside=False, inside=False):
	idx = get_x_index(xs, Z)
	y_max =  ys[idx]
	outside_range = 0 < ys < y_max
	inside_range = 0 < ys > y_max
	if outside:
		plt.fill_between(xs, 0, ys, where=outside_range, facecolor="blue")
		area = trapz(ys[0:-idx], dx=0.0001) + trapz(ys[idx:], dx=0.0001)
	if inside:
		plt.fill_between(xs, 0, ys, where=inside_range, facecolor="blue")
		area = trapz(ys[-idx:idx], dx=0.0001)
	proportion = round(area / trapz(ys, dx=0.0001), 2)
	patch = Rectangle((0,0), 1, 1, facecolor="blue")
	plt.legend([patch], ["Proportion of {}".format(proportion)])
	return fig

def add_gaussian(fig, alternate_mean, variance):
	sigma = sqrt(variance)
	lb = alternate_mean - 4
	ub = alternate_mean + 4
	xs = list(np.linspace(lb, ub, 1000))
	ys = [get_y(i, alternate_mean, variance, sigma) for i in xs]
	plt.vlines(alternate_mean, ymin=0, ymax=max(ys))
	plt.plot(xs, ys)
	return fig

fig, xs, ys = graph_normal(mean, variance)
fig = fill_graph(fig, xs, ys, Z, outside=True)
#fig = add_gaussian(fig, alternate_mean, variance)
fig.savefig("Gaussian.png")