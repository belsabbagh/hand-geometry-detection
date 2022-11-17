from os.path import isfile, join

from src.img_ops import read_img


def process_img(img):
    """
    Processes the given img before saving it in the dataset.
    Parameters:
        img: The original image
    """
    # TODO pre-processing goes here
    return img


def load_img(file_path):
    img = read_img(file_path)
    return process_img(img)


def load_images(dir_path, img_names_list):
    return [load_img(join(dir_path, f)) for f in img_names_list if isfile(join(dir_path, f))]
