from os.path import isfile, join

from src.image_ops.gray_level_transformations import slice_gray_level
from src.image_ops import read_img, blur_img, convert_to_grayscale
from src.image_ops.scale_img import scale_img


def process_img(_img):
    """
    Processes the given img before saving it in the dataset_handler.
    Parameters:
        _img: The original image
    """
    # TODO pre-processing goes here
    img = blur_img(convert_to_grayscale(_img), 5)
    img = scale_img(img, 0.4)
    res = slice_gray_level(img, 75, 230)
    return res


def load_img(file_path):
    img = read_img(file_path)
    return process_img(img)


def load_images(dir_path, img_names_list):
    return [load_img(join(dir_path, f)) for f in img_names_list if isfile(join(dir_path, f))]
