from cv2 import Mat
from src.hand_detector.hand_painter import draw_hand_geometry
from src.hand_detector.hand_shape import HandShape, NotAHandException
from src.hand_detector.image_preprocessor import preprocess
from src.image_ops.contour import find_contours


def detect_hand_in_image(img) -> Mat:
    """
    Detects hand shapes in an image. It starts by preprocessing the image and finding contours of the edges.
    For each contour, it attempts to construct a HandShape object and draws the detected shape on the image if exists.
    """
    processed_img = preprocess(img)
    contours, _ = find_contours(processed_img)
    res = img
    for c in contours:
        try:
            hand = HandShape(c)
            res = draw_hand_geometry(img, hand)
        except NotAHandException:
            continue
    return res
