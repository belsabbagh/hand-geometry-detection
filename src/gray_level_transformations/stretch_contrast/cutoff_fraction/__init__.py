import numpy as np

from src.image_histogram import generate_image_histogram


def cutoff_fraction(img, c):
    hist = generate_image_histogram(img)
    peak = np.max(hist)
    passed_levels = []
    level = 0
    for i in hist:
        if i > c * peak:
            passed_levels.append(level)
        level += 1
    return min(passed_levels), max(passed_levels)
