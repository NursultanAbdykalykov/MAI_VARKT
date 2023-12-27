import matplotlib.pyplot as plt
from math import log

exp = 2.718282
ro, g, dt, c, b, s, = 1.29, 9.8, 0.1, 0.45, 0.00129, 20
m0 = 229624 # начальная масса ракеты
mk = 22000 # конечная масса ракеты после выхоа на орбиту Земли
alpha = 1768
f1 = 400000 # сила тяги выбрасываемого модуля
f2 = 4 * 670000 # сила тяги оставшегося модуля
t, h, v = 0, 0, 0

t_coords = []
h_coords = []
v_coords = []

tk = ((m0 - mk) / alpha)

while (t <= 300) and (h <= 120000 or v <= 2000):
    if h < 23000:
        F = f1 + f2
        alpha = 1768
    elif 23000 <= h <= 50000:
        F = f2
        alpha = 556
    elif 50000 < h <= 97000:
        F = 0
        alpha = 0
    else:
        F = f2
        alpha = 556

    t_coords.append(t)
    h_coords.append(h)
    v_coords.append(v)

    m = m0 - alpha * t
    a = (F - m * g - 0.5 * c * ro * (exp ** (-b * h)) * s * v * v) / m
    v = v + a * dt
    h = h + v * dt
    t += dt

fig, axs = plt.subplots(nrows=2, figsize=(8, 8))

axs[0].set_xlabel('t, с')
axs[0].set_ylabel('h, м')
axs[0].plot(t_coords, h_coords)

axs[1].set_xlabel('t, с')
axs[1].set_ylabel('V, м/с')
axs[1].plot(t_coords, v_coords)

plt.show()
