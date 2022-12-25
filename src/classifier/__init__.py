import cv2


def find_object_in_image(_img, cc, min_size):
    img = _img
    res = get_detection_data(img, cc, min_size)
    return draw_rectangle_from_detection(img, res)


def get_detection_data(_img, cc, min_size):
    res = cc.detectMultiScale(_img, scaleFactor=1.05, minNeighbors=5, minSize=min_size, flags=cv2.CASCADE_SCALE_IMAGE)
    return res if len(res) > 0 else None


def draw_rectangle_from_detection(_img, res, color=(0, 255, 0), thickness=2):
    img = _img
    if res is None:
        return _img
    for x, y, w, h in res:
        cv2.rectangle(img, (x, y), (x + w, y + h), color, thickness)
    return img
