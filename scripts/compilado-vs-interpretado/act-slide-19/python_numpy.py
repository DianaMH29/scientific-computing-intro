import numpy as np

a = np.array([1.0, 2.0, 3.0, 4.0, 5.0])
b = np.array([10.0, 20.0, 30.0, 40.0, 50.0])

c = a + b  # operación vectorizada, sin bucle explícito

print("Resultado:", c)

