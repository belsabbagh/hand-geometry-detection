"""Main Module"""
import cv2
import numpy as np

from src.finger_detector import calculate_fingers
from src.image_ops import read_img, draw_contours
from src.image_ops.scale_img import scale_img


def test_3():
    img_path = r'data\hand.png'
    img = scale_img(read_img(img_path), 0.4)
    processed_img = preprocess(img)
    contours, _ = cv2.findContours(processed_img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    res, hull = draw_hand_shape(contours)
    status, points = calculate_fingers(res)
    drawing = np.zeros(img.shape, np.uint8)
    draw_contours(drawing, [res], (0, 255, 0), 2)
    draw_contours(drawing, [hull], (0, 0, 255), 3)
    for pt in points:
        cv2.circle(drawing, pt, 8, [211, 84, 0], -1)
    print("Fingers", len(points) + 1)
    cv2.imshow('output', drawing)
    cv2.waitKey(0)


def draw_hand_shape(contours):
    res = None
    if len(contours) > 0:
        res = get_res(contours)
        hull = cv2.convexHull(res)
    return res, hull


def preprocess(frame):
    frame = cv2.bilateralFilter(frame, 5, 50, 100)
    bgModel = cv2.createBackgroundSubtractorMOG2(0, 50)
    fgmask = bgModel.apply(frame)
    fgmask = cv2.erode(fgmask, np.ones((3, 3), np.uint8), iterations=1)
    img = cv2.bitwise_and(frame, frame, mask=fgmask)
    cv2.imshow('Morph', img)
    skin_mask = mask_color(img, [0, 48, 80], [20, 255, 255])
    cv2.imshow('Threshold Hands', skin_mask)
    return skin_mask


def get_res(contours):
    res=None
    max_area = -1
    for i in range(len(contours)):
        area = cv2.contourArea(contours[i])
        if area > max_area:
            max_area = area
            res = contours[i]
    return res


def mask_color(img, lower, upper):
    return cv2.inRange(cv2.cvtColor(img, cv2.COLOR_BGR2HSV), np.array(lower, dtype=np.uint8), np.array(upper, dtype=np.uint8))


if __name__ == '__main__':
    test_3()
