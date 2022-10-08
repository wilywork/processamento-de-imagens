import numpy as np
import math
import cmath
from matplotlib import pyplot as plt

tamanhoMatriz = 8

matriz = np.zeros((tamanhoMatriz, tamanhoMatriz), dtype="complex")

for k in range(matriz.shape[0]):
  for n in range(matriz.shape[1]):
    matriz[k,n] = (1/8) * cmath.exp((-2 * (math.pi) * 1j * k * n) / 8)


plt.plot(matriz.real, matriz.imag, '.')
plt.ylabel('Imaginary')
plt.xlabel('Real')
plt.show()