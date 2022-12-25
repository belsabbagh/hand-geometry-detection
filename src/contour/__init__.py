import cv2


def find_contours(img):
    return cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)