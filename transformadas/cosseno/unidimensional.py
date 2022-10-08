import numpy as np
import math

tamanhoMatriz = 8

matriz = np.zeros((tamanhoMatriz, tamanhoMatriz), dtype="float")

print(matriz)

for u in range(matriz.shape[0]):
  for n in range(matriz.shape[1]):
    if n != 0:
      matriz[u, n] = 1 * math.sqrt(2/matriz.shape[0]) * math.cos((math.pi * n * (u + 0.5) / matriz.shape[0]))
    elif n == 0:
      matriz[u, n] = (1/ math.sqrt(2)) * math.sqrt(2/matriz.shape[0]) * math.cos((math.pi * n * (u + 0.5) /matriz.shape[0]))
    else:
      raise NameError('Matriz inválida')

print(matriz)