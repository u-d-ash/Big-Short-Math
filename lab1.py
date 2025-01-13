import math
import matplotlib.pyplot as plt
So, K, T, r, sig = 9, 10, 3, 0.06, 0.3

def get_init_price(M, type):

    delt = T/M
    u = math.exp(sig * math.sqrt(delt) + (r - 0.5 * sig * sig) * delt)
    d = math.exp(-1 * sig * math.sqrt(delt) + (r - 0.5 * sig * sig) * delt)

    R = math.exp(r * delt)

    if(not (d <= R and R <= u)):
        return -1

    p = (R - d)/(u - d)

    C = [[0] * (M + 1)] * (M + 1)

    for i in range(M + 1):

        C[M][i] = max(0, (1 if type == 'call' else -1) * (So * (u ** (M - i)) * (d ** (i)) - K))
    
    for j in range(M):

        j = M - j - 1

        for i in range(j + 1):

            C[j][i] = (p * C[j + 1][i] + (1 - p) * C[j + 1][i + 1])/R
    
    return C[0][0], C

for m in [1, 5, 10, 20, 50, 100, 200]:

    print(f"{m} & {round(get_init_price(m, 'call')[0], 4)} & {round(get_init_price(m, 'put')[0], 4)} \\\\")
    print("\hline")

x1 = [i for i in range(1, 500)]
y1_c = [get_init_price(x, 'call')[0] for x in x1]
y1_p = [get_init_price(x, 'put')[0] for x in x1]

print(f"Call converges at : {y1_c[-1]}")
print(f"Put converges at : {y1_p[-1]}")

x2 = [i for i in range(1, 500, 5)]
y2_c = [get_init_price(x, 'call')[0] for x in x2]
y2_p = [get_init_price(x, 'put')[0] for x in x2]

fig, ax = plt.subplots(2, 2, figsize = (8, 8))

ax[0, 0].plot(x1, y1_c)
ax[0, 0].set_title("Call Price (Step = 1)")

ax[0, 1].plot(x1, y1_p)
ax[0, 1].set_title("Put Price (Step = 1)")

ax[1, 0].plot(x2, y2_c)
ax[1, 0].set_title("Call Price (Step = 5)")

ax[1, 1].plot(x2, y2_p)
ax[1, 1].set_title("Put Price (Step = 5)")

plt.show()

matrix_call = get_init_price(20, 'call')[1]
matrix_put = get_init_price(20, 'put')[1]

t_vals = [0, 0.30, 0.75, 1.50, 2.70]

delt = T/20

print("Call")
print("=" * 25)

for t in t_vals:

    index = int(t/delt)

    print(f"{t} & {str([round(v, 3) for v in matrix_call[index][:index + 1]])} \\\\")
    print("\hline")

print("Put")
print("=" * 25)

for t in t_vals:

    index = int(t/delt)

    print(f"{t} & {str([round(v, 3) for v in matrix_put[index][:index + 1]])} \\\\")
    print("\hline")



