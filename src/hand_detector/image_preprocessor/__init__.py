import cv2
import numpy as np

from src.image_ops import mask_color


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
