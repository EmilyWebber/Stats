from math import sqrt

def get_z_value(percent):
	if percent == int(95):
		return 1.96
	return None

def get_standard_error(samplevariance=False, standard_deviation=False, samplesize=False):
	'''
	If you have the sample variance, return it's square root.
	Otherwise return the standard deviation divided by the square root of the sample size.
	Inputs:
		samplevariance: integer or a float
		standard_deviation: integer or float
		samplesize: integer or float
	'''
	if samplevariance:
		assert(type(samplevariance) == float or type(samplevariance) == int), "Sample variance must be a number"
		return sqrt(samplevariance)
	assert(type(standard_deviation) == float or type(standard_deviation) == int) and (type(samplesize) == float or type(samplesize) == int), "Standard deviation and sample size must be numbers"
	return standard_deviation/sqrt(samplesize)

def get_design_effect(intra_cluster, num_clusters, format=False):
	'''
	Given parameters of a survey design, return the design effect
 	Inputs:
 		intra_cluster: float, also known as "row", or p
 		num_clusters: float or integer, the number of clusters
 	Returns a float of the design effect
 	'''
 	assert type(intra_cluster) == float
 	assert (type(num_clusters) == float) or (type(num_clusters) == int)
 	deff = 1 + intra_cluster * (num_clusters - 1)
 	if format:
 		print ("Design effect is {}".format(deff))
 	return deff

def get_sample_size(n, deff, format=False):
	'''
	Given a sample size and a design effect, return the adjusted sample size
	'''
	assert type(n) == float or type(n) == int
	assert type(deff) == float
	neff = int(round(n / deff))
	if format:
		print ("Adjusted sample size is {}".format(neff))
	return neff

def get_per_person_cost(n, cost):
	'''
	Given a sample size and cost of the survey, return the per person cost
	'''
	assert type(n) == float or int
	assert type(cost) == float or int
	return cost / n

def confidence_interval(percent, mean, samplesize, samplevariance, format=False):
	'''
	Takes parameters, returns a confidence interval to determine range of accuate prediction

	Inputs:
		percent: an integer from 1 to 100 that represents the degree of the confidence interval
		mean: a float that represents the sample mean, used as the center of the confidene interval, must be greater than zero
		samplesize: an integer of the given sample size
		samplevariance: an integer of the given sample variance
		format: a boolean value that, when True, will print the meaning of the confidence interval

	Returns a tuple of the lower and upper bound
	'''
	assert 0 < percent < 100, "Percent must be an integer greater than 0 and less than 100"
	assert samplesize > 30, "Sample size must be larger than 30. Central Limit Theorem does not apply otherwise."
	int(percent)
	float(mean)
	int(samplesize)
	int(samplevariance)
	z_value = get_z_value(percent)
	n = sqrt(samplesize)
	std_error = get_standard_error(samplevariance)
	lb = round(mean - z_value * (std_error/n), 2)
	ub = round(mean + z_value * (std_error/n), 2)
	interval = (lb, ub)
	if format:
		print("For {}% of the samples, the mean will fall within this range {} ".format(percent, interval))
	return interval

def reject_null_hypothesis(p_value, alpha, format=False):
	'''
	Given a p_value and an alpha, determine whether or not to reject the null hypothesis

	Inputs:
		p_value: float
		alpha: float
		format: a boolean value that, when True, will print whether or not to reject the null hypothesis

	Returns True if reject null, False if fail to reject
	'''
	assert 0 < float(p_value) < 1, "p value must be a float less 1 and greater than zero"
	assert 0 < float(alpha) < 1, "alpha must be a float less than 1 and greater than zero"
	reject = p_value < alpha
	if format and not reject:
		print ("Too much evidence of association to pass up this hypothesis. Fail to reject.")
	if format and reject:
		print ("Not enough evidence to support this hypothesis. Rejected.")
	return reject

def one_or_two_sided_p_value(sided, total):
	'''
	Return appropriate p-value given the parameters of the test: either one- or two- sided
	Inputs:
		sided: either 1 or 2, integer or float is fine
		total: must be a float greater than zero and less than one that represents the total p-value for the test
	'''
	assert type(sided) == float or type(sided) == int
	assert 0 < float(total) < 1, "p-value must be a float greater than zero and less than one"
	if sided == 2:
		return total
	elif sided == 1:
		return total/ 2.0