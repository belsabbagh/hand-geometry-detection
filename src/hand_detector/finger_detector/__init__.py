import math

import cv2


def calculate_fingers(res):
    #  convexity defect
    hull = cv2.convexHull(res, returnPoints=False)
    if len(hull) <= 3:
        return False, 0
    defects = cv2.convexityDefects(res, hull)
    if defects is None:
        return False, 0
    points = []
    for i in range(defects.shape[0]):  # calculate the angle
        angle, far = calculate_angle_from_defect(defects[i][0], res)
        if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
            points.append(far)
    return (True, points) if len(points) > 0 else (True, 0)


def calculate_angle(s, e, f, res):
    start = tuple(res[s][0])
    end = tuple(res[e][0])
    far = tuple(res[f][0])
    a = math.dist(start, end)
    b = math.dist(start, far)
    c = math.dist(end, far)
    angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
    return angle, far


def calculate_angle_from_defect(defect, res):
    s, e, f, _ = defect
    angle, far = calculate_angle(s, e, f, res)
    return angle, far