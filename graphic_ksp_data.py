import krpc
import matplotlib.pyplot as plt

conn = krpc.connect(name="000")
# Получение объекта космического корабля
vessel = conn.space_center.active_vessel

# Массивы, в которых мы будем хранить полученные во время полёта данные
t_coords = []
v_coords = []
h_coords = []

# # Получение скорости корабля на протяжении полета
while True:

    time = conn.space_center.ut
    altitude = vessel.flight().surface_altitude
    speed = vessel.flight(vessel.orbit.body.reference_frame).speed

    t_coords.append(time)
    h_coords.append(altitude)
    v_coords.append(speed)

    # Проверка условия завершения сбора данных
    if altitude > 120_000:
        break

fig, axs = plt.subplots(nrows=3, figsize=(8, 8))

# график высоты
axs[0].set_xlabel('t, с')
axs[0].set_ylabel('h, м')
axs[0].plot(t_coords, h_coords)

axs[1].set_xlabel('t, с')
axs[1].set_ylabel('V, м/с')
axs[1].plot(t_coords, v_coords)

plt.show()
