import cv2


img = cv2.imread("lenna.png", 1)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("cannytest", cv2.Canny(gray, 100, 200))
cv2.waitKey()
cv2.destroyAllWindows()
