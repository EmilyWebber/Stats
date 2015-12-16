from graph_normal import *
from math import sqrt

def graph(Z, mean, variance, sigma):
	fig, xs, ys = graph_normal(mean, variance)
	fig = fill_graph(fig, xs, ys, Z, outside=True)
	return fig

if __name__ == "__main__":
	mean = 0
	variance = 1
	sigma = sqrt(variance)
	fig = graph(1.28, mean, variance, sigma)
	plt.title("Significance Threshold is 10% \n Power is 90%")
	fig.savefig("Graphs/TentoNinety.png")
	fig1 = graph(1.96, mean, variance, sigma)
	plt.title("Significance Threshold is 5% \n Power is 95%")
	fig1.savefig("Graphs/FiveToNinetyFive.png")