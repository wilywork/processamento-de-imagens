import cv2

image_gray = cv2.imread("./lenaPoderosa.png", cv2.IMREAD_GRAYSCALE)

for i in range(0, image_gray.shape[0] - 1):
    for j in range(0, image_gray.shape[1] - 1):
        image_gray[i, j] = 1 - image_gray[i, j]

cv2.imshow('image', image_gray)
cv2.waitKey(0)
cv2.destroyAllWindows()