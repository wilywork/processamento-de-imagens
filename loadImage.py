import cv2

# ler imagem e ja converter para cinza
image_gray = cv2.imread("./lenaPoderosa.png", cv2.COLOR_BGR2GRAY)

# converte a imagem para o tipo informado
image_rgb = cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB)

# exibe a imagem na tela
cv2.imshow('image', image_rgb)
cv2.waitKey(0)
cv2.destroyAllWindows()