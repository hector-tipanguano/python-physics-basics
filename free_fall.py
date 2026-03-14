import numpy as np
import matplotlib.pyplot as plt

g = 9.81
h0 = 100 # Altura inicial en metros
t_final = np.sqrt(2 * h0 / g) # Tiempo exacto hasta tocar el suelo
t = np.linspace(0, t_final, 100)

# Ecuación: h = h0 - 0.5 * g * t^2
y = h0 - 0.5 * g * t**2

plt.plot(t, y)
plt.xlabel("Tiempo [s]")
plt.ylabel("Altura [m]")
plt.title("Caída Libre desde {}m".format(h0))
plt.grid(True)
plt.show()
