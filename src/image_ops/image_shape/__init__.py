import numpy as np


class ImageShape:
    def __init__(self, img):
        shape = img.shape
        h, w = shape[0], shape[1]
        self.height, self.width = h, w
        self.channel_count = 1 if len(shape) == 2 else shape[2]
        self.pixel_count = h * w
        self.min_level, self.max_level = np.min(img), np.max(img)

    def __repr__(self):
        return f"Image: {self.width} x {self.height}, {self.channel_count} channels."
