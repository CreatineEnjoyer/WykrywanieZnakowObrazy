import cv2


def picture1():
    img = cv2.imread("zakazu_i_ostrzegawczy.png")
    resized = cv2.resize(img, (1360, 768))
    # cv2.imshow("original", resized)

    # color detecting
    rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)
    mask_rgb_red = cv2.inRange(rgb, (201, 0, 0), (255, 101, 67))
    mask_rgb_orange = cv2.inRange(rgb, (231, 139, 0), (255, 201, 67))

    mask = cv2.bitwise_or(mask_rgb_red, mask_rgb_orange)
    target = cv2.bitwise_and(resized, resized, mask=mask)
    # cv2.imshow("colors", target)

    # edge detecting
    gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (2, 2))
    edge = cv2.Canny(blur, 160, 180)
    # cv2.imshow('canny', edge)
    dilate = cv2.dilate(edge, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)))
    # cv2.imshow('dilate', dilate)

    # finding contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 10000:
            cv2.drawContours(resized, cnt, -1, (255, 0, 126), 3)

            epsilon = cv2.arcLength(cnt, True)
            approximation = cv2.approxPolyDP(cnt, 0.02 * epsilon, True)
            x, y, width, height = cv2.boundingRect(approximation)
            cv2.rectangle(resized, (x, y), (x + width, y + height), (0, 255, 0), 4)

            if len(approximation) <= 5:
                sign_type = "Warning sign"
            elif len(approximation) > 5:
                sign_type = "Prohibition sign"
            else:
                sign_type = "Other sign"
            cv2.putText(resized, sign_type, (x + width + 5, y + height), cv2.FONT_HERSHEY_DUPLEX, 0.5, (30, 255, 0), 2)

    return cv2.imshow('picture1', resized)


def picture2():
    img = cv2.imread("zakazu_i_informacyjne.jpg")
    resized = cv2.resize(img, (1000, 800))
    # cv2.imshow("original", resized)

    # color detecting
    hsv = cv2.cvtColor(resized, cv2.COLOR_BGR2HSV)
    mask_hsv_red = cv2.inRange(hsv, (75, 24, 116), (121, 255, 255))
    mask_hsv_blue = cv2.inRange(hsv, (160, 113, 132), (179, 255, 255))

    mask = cv2.bitwise_or(mask_hsv_red, mask_hsv_blue)
    target = cv2.bitwise_and(resized, resized, mask=mask)
    # cv2.imshow("colors", target)

    # edge detecting
    gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (2, 2))
    edge = cv2.Canny(blur, 160, 180)
    # cv2.imshow('canny', edge)
    dilate = cv2.dilate(edge, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1)))
    # cv2.imshow('dilate', dilate)

    # finding contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area == 922.5 or area > 12000:
            cv2.drawContours(resized, cnt, -1, (255, 0, 126), 3)

            epsilon = cv2.arcLength(cnt, True)
            approximation = cv2.approxPolyDP(cnt, 0.02 * epsilon, True)
            x, y, width, height = cv2.boundingRect(approximation)
            cv2.rectangle(resized, (x, y), (x + width, y + height), (0, 255, 0), 4)

            if len(approximation) <= 4:
                sign_type = "Information sign"
            elif len(approximation) > 7:
                sign_type = "Prohibition sign"
            else:
                sign_type = "Other sign"
            cv2.putText(resized, sign_type, (x + 10, y + 30), cv2.FONT_HERSHEY_DUPLEX, 0.66, (30, 255, 0), 2)

    return cv2.imshow('picture2', resized)


def picture3():
    img = cv2.imread("ostrzegawcze.jpg")
    # cv2.imshow("original", img)

    # color detecting
    rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    mask_rgb_red = cv2.inRange(rgb, (130, 0, 0), (255, 100, 95))
    mask_rgb_orange = cv2.inRange(rgb, (198, 137, 0), (255, 206, 91))
    mask = cv2.bitwise_or(mask_rgb_red, mask_rgb_orange)
    target = cv2.bitwise_and(img, img, mask=mask)
    # cv2.imshow("colors", target)

    # edge detecting
    gray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    blur = cv2.blur(gray, (2, 2))
    edge = cv2.Canny(blur, 160, 180)
    # cv2.imshow('canny', edge)
    dilate = cv2.dilate(edge, cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1)))
    # cv2.imshow('dilate', dilate)

    # finding contours
    contours, hierarchy = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 2000:
            cv2.drawContours(img, cnt, -1, (255, 0, 126), 3)

            epsilon = cv2.arcLength(cnt, True)
            approximation = cv2.approxPolyDP(cnt, 0.02 * epsilon, True)
            x, y, width, height = cv2.boundingRect(approximation)
            cv2.rectangle(img, (x, y), (x + width, y + height), (0, 255, 0), 4)

            if len(approximation) >= 3:
                sign_type = "Warning sign"
            else:
                sign_type = "Other sign"
            cv2.putText(img, sign_type, (x + 10, y + 30), cv2.FONT_HERSHEY_DUPLEX, 0.66, (30, 255, 0), 2)

    return cv2.imshow('picture3', img)


def main():
    picture1()
    picture2()
    picture3()
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
