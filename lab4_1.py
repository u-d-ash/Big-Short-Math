import matplotlib.pyplot as plt
import math
import numpy as np

np.random.seed(42)

mu = np.array([0.1, 0.25, 0.15])
sig = np.array([[0.005, -0.010, 0.004], [-0.010, 0.040, -0.002], [0.004, -0.002, 0.023]])

def generate_weights(n):

	vector = []
	rem = 1
	
	for i in range(n - 1):
	
		x = np.random.uniform(0, rem)
		vector.append(x)
		rem -= x
	
	vector.append(rem)
	
	return np.array(vector)

def generate_bullet_points(n):

	x = []
	y = []

	for i in range(n):
	
		weights = generate_weights(3)
		mu_p = np.dot(weights, mu)
		var_p = np.dot(np.dot(weights, sig), weights.T)
		
		x.append(math.sqrt(var_p))
		y.append(mu_p)
	
	return x, y

a, b = generate_bullet_points(10000)

plt.scatter(a, b)
plt.show()

 

