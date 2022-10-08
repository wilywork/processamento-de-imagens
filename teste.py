import numpy as np
import math
import cmath
import cv2
from matplotlib import pyplot as plt
from PIL import Image


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


image_gray = cv2.imread("./lenaPoderosa.png", cv2.COLOR_BGR2GRAY)
#image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)





cv2.imshow('image', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()