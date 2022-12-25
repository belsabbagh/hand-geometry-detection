from src.image_ops.get_img_min_max_levels import get_image_min_max_levels


class ImageShape:
    def __init__(self, img):
        shape = img.shape
        h, w = shape[0], shape[1]
        self.height, self.width = h, w
        self.channel_count = 1 if len(shape) == 2 else shape[2]
        self.pixel_count = h * w
        self.min_level, self.max_level = get_image_min_max_levels(img)

    def __repr__(self):
        return f"Image: {self.width} x {self.height}, {self.channel_count} channels."


def get_shape(img):
    """
    Gets a dictionary of the image's shape
    """
    return ImageShape(img)
