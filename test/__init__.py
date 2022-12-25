from src.hand_detector import detect_hand_in_image
from src.image_ops import read_img
from src.image_ops.scale_img import scale_img


def test_detection_on_image():
    img_path = r'data/palmar left/extra/p/Hand_0000748.jpg'
    img = scale_img(read_img(img_path), 0.4)
    detect_hand_in_image(img)