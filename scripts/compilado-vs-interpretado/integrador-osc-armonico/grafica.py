import numpy as np
import matplotlib.pyplot as plt

# Cargar los datos generados por Fortran
datos = np.loadtxt("salida.dat")
t = datos[:, 0]
x = datos[:, 1]

# Graficar
plt.plot(t, x)
plt.xlabel("Tiempo (s)")
plt.ylabel("Posición x(t)")
plt.title("Oscilador armónico simple (datos de Fortran)")
plt.savefig("oscilador.png")
plt.show()

