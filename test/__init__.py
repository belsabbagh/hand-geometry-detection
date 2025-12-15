import os

import cv2

from src.hand_detector import detect_hand_in_image
from src.image_ops import read_img, write_image


def test_detection_on_image(img_path):
    img = detect_hand_in_image(read_img(img_path))
    write_image(os.path.join("out", "detected_hand.png"), img)
    cv2.imshow("output", img)
    cv2.waitKey(0)


def test_detection_on_directory():
    dir_path = os.path.join("data", "test")
    for f in os.listdir(dir_path):
        test_detection_on_image(os.path.join(dir_path, f))


def test_detection_on_video():
    cam = cv2.VideoCapture(0)
    while True:
        _, frame = cam.read()
        post = detect_hand_in_image(frame)
        cv2.imshow("Camera", post)
        if cv2.waitKey(1) == ord("q"):
            break

    cam.release()
    out.release()
