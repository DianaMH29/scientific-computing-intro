from multiprocessing import Pool
import numpy as np
import time

def suma_parcial(bloque):
    return np.sum(bloque)
t0 = time.time()

if __name__ == "__main__":
    datos = np.ones(1_000_000)
    bloques = np.array_split(datos, 8)  # 4 procesos

    with Pool(processes=8) as pool:
        resultados = pool.map(suma_parcial, bloques)

    print("Suma total:", sum(resultados))
t1= time.time()
print(f"{t1-t0:.4f} s")
