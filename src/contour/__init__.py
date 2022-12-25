import cv2


def find_contours(img):
    return cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)


def get_hand_shape(contours):
    res = None
    if len(contours) > 0:
        res = get_res(contours)
        hull = cv2.convexHull(res)
    return res, hull


def get_res(contours):
    res=None
    max_area = -1
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > max_area:
            max_area = area
            res = contours[i]
    return res
