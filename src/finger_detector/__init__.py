import math

import cv2


def calculate_fingers(res, drawing):
    #  convexity defect
    hull = cv2.convexHull(res, returnPoints=False)
    if len(hull) <= 3:
        return False, 0
    defects = cv2.convexityDefects(res, hull)
    if defects is None:
        return False, 0
    count = 0
    for i in range(defects.shape[0]):  # calculate the angle
        s, e, f, d = defects[i][0]
        angle, far = calculate_angle(e, f, res, s)
        if angle <= math.pi / 2:  # angle less than 90 degree, treat as fingers
            count += 1
            cv2.circle(drawing, far, 8, [211, 84, 0], -1)
    return (True, count + 1) if count > 0 else (True, 0)


def calculate_angle(e, f, res, s):
    start = tuple(res[s][0])
    end = tuple(res[e][0])
    far = tuple(res[f][0])
    a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
    b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
    c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
    angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c))  # cosine theorem
    return angle, far
