import cv2
image = cv2.imread("flower.jpg")

blur = cv2.GaussianBlur(image,(75,75),0)

cv2.imshow("Original", image)
cv2.imshow("Blurred", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()