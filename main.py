"""Main Module"""
import cv2
import pandas as pd

from src.img_ops.get_shape import get_shape
from src.img_ops.read_img import read_img_grayscale, read_img
from src.img_ops.scale_img import scale_img
from src.img_ops.convert_to_float32 import convert_to_float32


TRAINING_DATASET_PATH = 'data/training'
HANDS_METADATA = pd.read_csv('data/HandInfo.csv')

if __name__ == '__main__':
    test_img = read_img_grayscale(f"{TRAINING_DATASET_PATH}/Hand_0000002.jpg")
    print(get_shape(test_img))
    operatedImage = convert_to_float32(test_img)
    dest = cv2.cornerHarris(operatedImage, 2, 7, 0.07)
    dest = cv2.dilate(dest, None)
    test_img[dest > 0.01 * dest.max()] = 255
    test_img = scale_img(test_img, 0.6)
    cv2.imshow("test img", test_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
