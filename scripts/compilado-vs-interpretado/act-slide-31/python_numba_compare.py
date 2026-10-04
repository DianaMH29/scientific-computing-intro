import numpy as np
import time
from numba import jit

@jit(nopython=True)
def suma_bucle(n):
    total = 0.0
    for i in range(n):
        total += i
    return total

# Primera llamada: incluye tiempo de compilación JIT
t0 = time.time()
suma_bucle(10_000_000)
print("Primera llamada:", time.time() - t0, "s")

# Segunda llamada: ya compilado, solo ejecución
t0 = time.time()
suma_bucle(10_000_000)
print("Segunda llamada:", time.time() - t0, "s")

