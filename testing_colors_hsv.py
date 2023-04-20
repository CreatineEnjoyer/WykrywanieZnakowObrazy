import cv2

img = cv2.imread("ostrzegawcze.jpg")
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.namedWindow("Find Color", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Hue Min", "Find Color", 0, 179, (lambda a: None))
cv2.createTrackbar("Hue Max", "Find Color", 179, 179, (lambda a: None))
cv2.createTrackbar("Sat Min", "Find Color", 0, 255, (lambda a: None))
cv2.createTrackbar("Sat Max", "Find Color", 255, 255, (lambda a: None))
cv2.createTrackbar("Val Min", "Find Color", 0, 255, (lambda a: None))
cv2.createTrackbar("Val Max", "Find Color", 255, 255, (lambda a: None))

while 1:
    hmin = cv2.getTrackbarPos("Hue Min", "Find Color")
    hmax = cv2.getTrackbarPos("Hue Max", "Find Color")
    smin = cv2.getTrackbarPos("Sat Min", "Find Color")
    smax = cv2.getTrackbarPos("Sat Max", "Find Color")
    vmin = cv2.getTrackbarPos("Val Min", "Find Color")
    vmax = cv2.getTrackbarPos("Val Max", "Find Color")
    mask = cv2.inRange(hsv, (hmin, smin, vmin), (hmax, smax, vmax))
    cv2.imshow("finding colors", mask)

    mask_hsv_red = cv2.inRange(hsv, (75, 24, 116), (121, 255, 255))
    mask_hsv_blue = cv2.inRange(hsv, (160, 113, 132), (179, 255, 255))

    mask = cv2.bitwise_or(mask_hsv_red, mask_hsv_blue)
    target = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("color", target)

    cv2.waitKey(1)
