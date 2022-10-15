import cv2

# ler imagem e ja converter para cinza
image_gray = cv2.imread("./lenaPoderosa.png", cv2.COLOR_BGR2GRAY)

height, width, _ = image_gray.shape

for i in range(0, height - 1):
    for j in range(0, width - 1):
        pixel = image_gray[i, j]
        pixel[0] = 255 - pixel[0]
        pixel[1] = 255 - pixel[1]
        pixel[2] = 255 - pixel[2]

        image_gray[i, j] = pixel

# exibe a imagem na tela
cv2.imshow('image', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()