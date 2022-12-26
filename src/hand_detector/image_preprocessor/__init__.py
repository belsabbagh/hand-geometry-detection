"""
This module is responsible for preprocessing the image before the detection starts.
"""
import cv2
import numpy as np

from src.image_ops import mask_color


def preprocess(_img):
    _img = cv2.bilateralFilter(_img, 5, 50, 100)
    bgModel = cv2.createBackgroundSubtractorMOG2(0, 50)
    fgmask = bgModel.apply(_img)
    fgmask = cv2.erode(fgmask, np.ones((3, 3), np.uint8), iterations=1)
    img = cv2.bitwise_and(_img, _img, mask=fgmask)
    cv2.imshow('Morph', img)
    skin_mask = mask_color(img, [0, 48, 80], [20, 255, 255])
    cv2.imshow('Threshold Hands', skin_mask)
    return skin_mask
