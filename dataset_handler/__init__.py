from os import listdir
from os.path import isfile, join

import pandas as pd

from dataset_handler.dataset_record import DatasetRecord, Metadata
from src.img_ops import read_img

metadata: pd.DataFrame = pd.DataFrame()


def get_img_metadata(img_name):
    global metadata
    img_metadata = metadata.loc[metadata['imageName'] == img_name]
    return img_metadata.to_dict()


def load_dataset(dir_path, metadata_path):
    global metadata
    metadata = pd.read_csv(metadata_path)
    return [load_record(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f))]


def load_record(dir_path, img_name):
    file_path = join(dir_path, img_name)
    return DatasetRecord(read_img(file_path), Metadata(get_img_metadata(img_name)))
