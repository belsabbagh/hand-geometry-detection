import cv2
import numpy as np

from src.contour import find_contours, get_hand_shape
from src.hand_detector.finger_detector import calculate_fingers
from src.image_preprocessor import preprocess
from src.painter import draw_hand_geometry


def detect_hand_in_image(img):
    processed_img = preprocess(img)
    contours, _ = find_contours(processed_img)
    res, hull = get_hand_shape(contours)
    status, points = calculate_fingers(res)
    drawing = np.zeros(img.shape, np.uint8)
    draw_hand_geometry(drawing, hull, points, res)
    print("Fingers", len(points) + 1)
    cv2.imshow('output', drawing)
    cv2.waitKey(0)
