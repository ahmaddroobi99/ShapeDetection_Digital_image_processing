import numpy as np
import cv2

img = cv2.imread('Shape.bmp')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thrash = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.imshow("img", img)
i = 1
for contour in contours:
    if i == 1:
        i+=1
        continue
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
    #cv2.drawContours(img, [approx], 0, (0, 0, 0), 5)
    x = approx.ravel()[0]
    y = approx.ravel()[1] - 5
    print("\n")
    if len(approx) == 3:
        cv2.fillPoly(img, pts=[approx], color=(0, 255, 0))
    elif len(approx) == 4:
        cv2.fillPoly(img, pts=[approx], color=(255, 0, 0))

    elif len(approx) >= 5 and len(approx) <= 10:
        cv2.fillPoly(img, pts=[approx], color=(0, 0, 0))
    else:
        cv2.fillPoly(img, pts=[approx], color=(0, 0, 255))

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
