import math
import matplotlib.pyplot as plt

def save_plot(x, y, x_lab, y_lab, file_name):

	plt.plot(x, y)
	plt.xlabel(x_lab)
	plt.ylabel(y_lab)
	plt.savefig(file_name)
	plt.close()


def get_init_price(option_type, model_set, S = 100, K = 100, T = 1, M = 100, r = 0.08, sig = 0.2):

	delt = T/M
	
	if(model_set == 1):
	
		u, d = math.exp(sig * math.sqrt(delt)), math.exp(-1 * sig * math.sqrt(delt))
	
	else:
	
		u, d = math.exp(sig * math.sqrt(delt) + (r - 0.5 * sig ** 2) * delt), math.exp(-1 * sig * math.sqrt(delt) + (r - 0.5 * sig ** 2) * delt)
	
	R = math.exp(r * delt)
	
	if(not (d <= R and R <= u)):
	
		return -1
	
	p = (R - d)/(u - d)
	
	C = [[0] * (M + 1)] * (M + 1)
	
	for i in range(M + 1):
	
		C[M][i] = max(0, (1 if option_type == "call" else -1) * (S * (u ** (M - i)) * (d ** i) - K))
	
	for j in range(M):
	
		j = M - j - 1
		
		for i in range(j + 1):
		
			C[j][i] = (p * C[j + 1][i] + (1 - p) * C[j + 1][i + 1])/R
	
	return C[0][0]

def get_all_plots(ot, ms):

	
	x = [10 * (i + 1) for i in range(50)]

	y = [get_init_price(option_type = ot, model_set = ms, S = v) for v in x]

	save_plot(x, y, "stock price", f"{ot} price", f"{ot}_{ms}_stock.png")

	y = [get_init_price(option_type = ot, model_set = ms, K = v) for v in x]

	save_plot(x, y, "strike price", f"{ot} price", f"{ot}_{ms}_strike.png")

	x = [0.01 * (i + 1) for i in range(50)]

	y = [get_init_price(option_type = ot, model_set = ms, r = v) for v in x]

	save_plot(x, y, "interest rate", f"{ot} price", f"{ot}_{ms}_rate.png")

	x = [0.05 * (i + 1) for i in range(50)]

	y = [get_init_price(option_type = ot, model_set = ms, sig = v) for v in x]

	save_plot(x, y, "sigma", f"{ot} price", f"{ot}_{ms}_sig.png")

	fig, ax = plt.subplots(1, 3, figsize=(18, 3))

	x = [2 * (i + 1) for i in range(100)]

	K_vals = [95, 100, 105]

	for i in range(3):

		ax[i].set_title(f"K = {K_vals[i]}")
		yi = [get_init_price(option_type = ot, model_set = ms, K = K_vals[i], M = v) for v in x]
		ax[i].plot(x, yi)

	plt.savefig(f"{ot}_{ms}_m.png")
	plt.close()

Options = ["call", "put"]

Models = [1, 2]

for o in Options:

	for m in Models:
	
		get_all_plots(o, m)
	





