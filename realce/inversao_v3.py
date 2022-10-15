import cv2

# ler imagem e ja converter para escala de cinza
image_gray = cv2.imread("./lenaPoderosa.png", cv2.IMREAD_GRAYSCALE)
cv2.imshow('image', 1 - image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()