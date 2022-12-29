from src.hand_detector.hand_shape import HandShape


def get_hand_shapes_from_contours(contours):
    return [HandShape(i) for i in contours]
