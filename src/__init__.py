import cv2

L = 256
PEAK_INTENSITY = L - 1
BLACK = 0


def put_text_on_image(res, text, x, y):
    return cv2.putText(res, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)


def draw_contours(img, contour):
    return cv2.drawContours(img, [contour], -1, (0, 255, 0), 3)


def approx_contour(contour):
    return cv2.approxPolyDP(contour, epsilon(contour), True)


def epsilon(contour, coefficient=0.01):
    return coefficient * cv2.arcLength(contour, True)
