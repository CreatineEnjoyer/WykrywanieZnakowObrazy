import cv2

img = cv2.imread("ostrzegawcze.jpg")
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

cv2.namedWindow("Find Color", cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar("Red Min", "Find Color", 0, 255, (lambda a: None))
cv2.createTrackbar("Red Max", "Find Color", 0, 255, (lambda a: None))
cv2.createTrackbar("Green Min", "Find Color", 0, 255, (lambda a: None))
cv2.createTrackbar("Green Max", "Find Color", 255, 255, (lambda a: None))
cv2.createTrackbar("Blue Min", "Find Color", 0, 255, (lambda a: None))
cv2.createTrackbar("Blue Max", "Find Color", 255, 255, (lambda a: None))

while 1:
    rmin = cv2.getTrackbarPos("Red Min", "Find Color")
    rmax = cv2.getTrackbarPos("Red Max", "Find Color")
    gmin = cv2.getTrackbarPos("Green Min", "Find Color")
    gmax = cv2.getTrackbarPos("Green Max", "Find Color")
    bmin = cv2.getTrackbarPos("Blue Min", "Find Color")
    bmax = cv2.getTrackbarPos("Blue Max", "Find Color")
    mask = cv2.inRange(rgb, (rmin, gmin, bmin), (rmax, gmax, bmax))
    cv2.imshow("finding colors", mask)
    color = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow("color", color)

    mask_rgb_red = cv2.inRange(rgb, (130, 0, 0), (255, 100, 95))
    #mask_rgb_orange = cv2.inRange(rgb, (198, 137, 0), (255, 206, 91))
    #mask_red_orange = cv2.bitwise_or(mask_rgb_red, mask_rgb_orange)

    mask_rgb_blue = cv2.inRange(rgb, (0, 50, 111), (73, 142, 255))

    mask = cv2.bitwise_or(mask_rgb_red, mask_rgb_blue)
    target = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("target", target)
    cv2.waitKey(1)
