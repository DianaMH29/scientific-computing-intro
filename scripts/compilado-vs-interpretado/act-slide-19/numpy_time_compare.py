import time
import numpy as np

n = 10_000_000

# Versión con bucle puro
t0 = time.time()
suma = 0.0
for i in range(n):
    suma += i
t1 = time.time()
print(f"Bucle puro: {t1 - t0:.4f} s")

# Versión vectorizada con NumPy
t0 = time.time()
suma_np = np.sum(np.arange(n, dtype=np.float64))
t1 = time.time()
print(f"NumPy: {t1 - t0:.4f} s")

