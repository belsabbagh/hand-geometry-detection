import cv2

from src.image_ops import write_image
from src.image_ops.contour import find_contours
from src.hand_detector.shape_detector import get_hand_shapes_from_contours, get_largest_shape
from src.hand_detector.finger_detector import find_fingers
from src.hand_detector.image_preprocessor import preprocess
from src.hand_detector.hand_painter import draw_hand_geometry


def detect_hand_in_image(img):
    processed_img = preprocess(img)
    contours, _ = find_contours(processed_img)
    shapes = get_hand_shapes_from_contours(contours)
    for hand_contour, hull in shapes:
        status, points = find_fingers(hand_contour)
        img = draw_hand_geometry(img, hull, points, hand_contour)
    print("Fingers", len(points) + 1)
    write_image(r'out\detected_hand.png', img)
    cv2.imshow('output', img)
    cv2.waitKey(0)
