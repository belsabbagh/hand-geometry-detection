import cv2

from src.image_ops.get_shape import ImageShape


def get_shape(img):
    """
    Returns an object with data about the given image's shape
    """
    return ImageShape(img)


def read_img(file_path, color_mode=None):
    if color_mode is None:
        color_mode = cv2.IMREAD_UNCHANGED
    return cv2.imread(file_path, color_mode)


def read_img_color(file_path):
    return read_img(file_path, cv2.IMREAD_COLOR)


def read_img_grayscale(file_path):
    return read_img(file_path, cv2.IMREAD_GRAYSCALE)


def show_img(window_name, img):
    cv2.imshow(window_name, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return None


def load_cascade_classifier(xml_path):
    return cv2.CascadeClassifier(xml_path)


def blur_img(img, val):
    return cv2.medianBlur(img, val)


def binarize_img(img):
    return cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]


def convert_img_to_color(img):
    return cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)


def convert_to_grayscale(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
