import cv2


def get_hand_shape(contours):
    contour = None
    if len(contours) > 0:
        contour = get_largest_contour(contours)
        hull = cv2.convexHull(contour)
    return contour, hull


def get_largest_contour(contours):
    max_contour=None
    max_area = -1
    for i in contours:
        area = cv2.contourArea(i)
        if area > max_area:
            max_area = area
            max_contour = i
    return max_contour
