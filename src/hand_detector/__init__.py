import cv2

from src.image_ops import write_image
from src.image_ops.contour import find_contours
from src.hand_detector.shape_detector import get_hand_shape
from src.hand_detector.finger_detector import calculate_fingers
from src.hand_detector.image_preprocessor import preprocess
from src.hand_detector.hand_painter import draw_hand_geometry


def detect_hand_in_image(img):
    processed_img = preprocess(img)
    contours, _ = find_contours(processed_img)
    hand_contour, hull = get_hand_shape(contours)
    status, points = calculate_fingers(hand_contour)
    drawing = draw_hand_geometry(img, hull, points, hand_contour)
    print("Fingers", len(points) + 1)
    write_image(r'out\detected_hand.png', drawing)
    cv2.imshow('output', drawing)
    cv2.waitKey(0)
