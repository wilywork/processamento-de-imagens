# o núcleo da transformada discreta do cosseno para uma matriz de
# entrada com N = M = U = V = 8 é presentado pela imagem

import numpy as np
import math
import cv2

def criarMatriz(altura, largura, canaisCores):
  cor = list()
  if canaisCores == 1: #Escala de cinza
    cor = (255)
  elif canaisCores == 2: #BG
    cor = (255, 0)
  elif canaisCores == 3: #BGR
    cor = (255, 0, 255)
  else: #BGRA
    cor = (255, 0, 255, 0)
  imagem = np.full((altura, largura, canaisCores), cor, dtype=np.uint8)
  return imagem

def normalizaImagem(img):
  imgCinza = criarMatriz(img.shape[0], img.shape[1], 1)
  min = np.amin(img)
  max = np.max(img)
  for i in range(img.shape[0]):
    for j in range(img.shape[1]):
      cinza = int((((img[i, j] - min)/max)) * 255)
      imgCinza[i, j] = [cinza]
  return imgCinza

def funcK(nm):
  if nm != 0:
    return 1
  else:
    return (1 / math.sqrt(2))

TAM = 16

matriz = np.zeros((TAM, TAM), dtype="float")

matrizNew = np.zeros((TAM * TAM, TAM * TAM), dtype="float")

for n in range(TAM):
  for m in range(TAM):
    for u in range(TAM):
      for v in range(TAM):
        matrizNew[(n * TAM) + u, (m * TAM) + v] = funcK(n) * ( (2 / math.sqrt(TAM)) ** 2) * math.cos((math.pi * n * (u + 0.5) / TAM)) * funcK(m) * ( (2 / math.sqrt(TAM)) ** 2) * math.cos((math.pi * m * (v + 0.5) / TAM))

matrizNewNorm = normalizaImagem(matrizNew)

cv2.imshow('image', matrizNewNorm)
cv2.waitKey(0)
cv2.destroyAllWindows()