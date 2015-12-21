from graph_normal import *
from math import sqrt

def graph(Z, mean, variance, sigma):
	fig, xs, ys = graph_normal(mean, variance)
	fig = fill_graph(fig, xs, ys, Z, inside=True)
	return fig

if __name__ == "__main__":
	mean = 0
	variance = 1
	sigma = sqrt(variance)
	fig = graph(0.68, mean, variance, sigma)
	plt.title("Significance Threshold is 50% \n Power is 50%")
	fig.savefig("Graphs/Fifty_Reverse.png")
	fig1 = graph(0.39, mean, variance, sigma)
	plt.title("Significance Threshold is 30% \n Power is 70%")
	fig1.savefig("Graphs/Thirty_Seventy_Reverse.png")