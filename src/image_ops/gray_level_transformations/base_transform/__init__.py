import numpy as np

import src.image_ops
from src.image_ops.quantize_intensity import quantize_intensity


def base_transform(img, transform, *args):
    img_shape = src.image_ops.get_shape(img)
    h, w = img_shape.height, img_shape.width
    return np.array([[quantize_intensity(transform(img[r][p], *args)) for p in range(w)] for r in range(h)], dtype=np.uint8)
