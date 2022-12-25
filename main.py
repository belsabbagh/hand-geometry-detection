"""Main Module"""
import copy
import math
from timeit import default_timer as time

import cv2
import numpy as np

from src.classifier import get_detection_data
from src.config.messages import dataset_load_msg
from src.contour import find_contours
from src.dataset import load_dataset
from src.gray_level_transformations import slice_gray_level
from src.image_ops import load_cascade_classifier, read_img_grayscale, show_img, convert_img_to_color, read_img
from src.image_ops.scale_img import scale_img


def test_1():
    """
    Dataset loading
    """
    dir_path, metadata_file = 'data', 'data\\HandInfo.csv'
    test_train_ratio = 0.15
    categories = ['dorsal left', 'dorsal right', 'palmar left', 'palmar right']
    start = time()
    dataset = load_dataset(dir_path, categories, metadata_file)
    elapsed = round(time() - start, 5)
    print(dataset_load_msg(len(dataset), dir_path, elapsed))
    # train_dataset, test_dataset = split_dataset(dataset, test_train_ratio)
    # print(dataset_split_msg(len(train_dataset), len(test_dataset)))
    """
        Training
        """
    """
        Testing
        """
    cc = load_cascade_classifier('data/dorsal left/classifier/cascade.xml')
    correct = []
    incorrect = []
    # results = get_detection_data(read_img('data/dorsal-left-test.jpg'), cc, (120, 120))
    # if results is None:
    #     incorrect.append(1)
    # else:
    #     correct.append(1)
    for file_path, record in dataset.items():
        results = get_detection_data(record.get_image(), cc, (120, 120))
        if results is not None and record.get_metadata().get_hand_aspect() == 'dorsal left':
            correct.append(record)
            continue
        incorrect.append(record)
    print(correct)
    print(incorrect)


def pre_test():
    img_path = r'data\hand.png'
    img = scale_img(read_img_grayscale(img_path), 0.4)
    res = slice_gray_level(img, 75, 230)
    edged = cv2.Canny(res, 75, 230)
    contours, _ = find_contours(edged)
    res = convert_img_to_color(res)
    polygon_approximations = [approx_contour(contour) for contour in contours]
    for approx in polygon_approximations:
        draw_contours(res, approx)
        print(len(approx))
        i, j = approx[0][0]
        if len(approx) == 10:
            put_text_on_image(res, 'hand', i - 20, j - 20)
    show_img('res', res)


def put_text_on_image(res, text, x, y):
    return cv2.putText(res, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, 0, 2)


def draw_contours(img, contour):
    return cv2.drawContours(img, [contour], -1, (0, 255, 0), 3)


def approx_contour(contour):
    return cv2.approxPolyDP(contour, epsilon(contour), True)


def epsilon(contour, coefficient=0.01):
    return coefficient * cv2.arcLength(contour, True)


def calculate_fingers(res, drawing):
    #  convexity defect
    hull = cv2.convexHull(res, returnPoints=False)
    if len(hull) > 3:
        defects = cv2.convexityDefects(res, hull)
        if defects is not None:
            cnt = 0
            for i in range(defects.shape[0]):  # calculate the angle
                s, e, f, d = defects[i][0]
                start = tuple(res[s][0])
                end = tuple(res[e][0])
                far = tuple(res[f][0])
                a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
                b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
                c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
                angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
                if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
                    cnt += 1
                    cv2.circle(drawing, far, 8, [211, 84, 0], -1)
            if cnt > 0:
                return True, cnt + 1
            else:
                return True, 0
    return False, 0


def test_3():
    img_path = r'data\hand.jpg'
    frame = scale_img(read_img(img_path), 0.4)
    frame = cv2.bilateralFilter(frame, 5, 50, 100)
    bgModel = cv2.createBackgroundSubtractorMOG2(0, 50)
    fgmask = bgModel.apply(frame)
    kernel = np.ones((3, 3), np.uint8)
    fgmask = cv2.erode(fgmask, kernel, iterations=1)
    img = cv2.bitwise_and(frame, frame, mask=fgmask)

    # Skin detect and thresholding
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 48, 80], dtype="uint8")
    upper = np.array([20, 255, 255], dtype="uint8")
    skinMask = cv2.inRange(hsv, lower, upper)
    cv2.imshow('Threshold Hands', skinMask)
    skinMask1 = copy.deepcopy(skinMask)
    contours, hierarchy = cv2.findContours(skinMask1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    length = len(contours)
    maxArea = -1
    if length > 0:
        for i in range(length):
            temp = contours[i]
            area = cv2.contourArea(temp)
            if area > maxArea:
                maxArea = area
                ci = i
                res = contours[ci]
        hull = cv2.convexHull(res)
        drawing = np.zeros(img.shape, np.uint8)
        cv2.drawContours(drawing, [res], 0, (0, 255, 0), 2)
        cv2.drawContours(drawing, [hull], 0, (0, 0, 255), 3)

    isFinishCal, cnt = calculate_fingers(res, drawing)
    print("Fingers", cnt)
    cv2.imshow('output', drawing)
    cv2.waitKey(0)

if __name__ == '__main__':
    test_3()
