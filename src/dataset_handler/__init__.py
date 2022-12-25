"""
This module handles loading the dataset_handler in a dictionary indexed by the file path containing objects of each record.

Required inputs:
    1. A directory with images.
    2. A csv file with metadata indexed by image file name.

Main function:
    load_dataset

Known issues:
    The metadata file cannot be in the same directory as the images.
"""

from os import listdir, path
from sklearn.model_selection import train_test_split

import pandas as pd

from src.dataset_handler.config import IMAGE_NAME
from src.dataset_handler.record import DatasetRecord, Metadata
from src.dataset_handler.img_loader import load_img

metadata: pd.DataFrame = pd.DataFrame()


def get_img_metadata(index: str) -> dict[str:int]:
    """
    Loads dictionary of metadata of an image.
    :param index: file name.
    :type index: str
    :return: metadata of the given image.
    :rtype: Dict[str, int]
    """
    return (metadata.loc[index]).to_dict()


def load_dataset(dir_path: str, categories: list[str], metadata_path: str) -> dict[str:DatasetRecord]:
    """
    Creates a dataset_handler from an image directory and a metadata file path.
    :param categories: categories of classified images
    :type categories: List[str]
    :param dir_path: Image directory path.
    :type dir_path: str
    :param metadata_path: Metadata file path.
    :type metadata_path: str
    :return: A DataFrame of the loaded image dataset_handler.
    :rtype: Dict[str, DatasetRecord]
    """
    global metadata
    metadata = pd.read_csv(metadata_path, index_col=IMAGE_NAME)
    dataset = {}
    for cat in categories:
        cat_path = path.join(dir_path, cat, 'p')
        print(cat_path)
        for f in listdir(cat_path):
            img_path = path.join(cat_path, f)
            dataset[img_path] = create_record(img_path)
    return dataset


def create_record(file_path: str) -> DatasetRecord:
    """
    Creates a dataset_handler record from a given image file in a directory.
    :param file_path: Path of image file.
    :type file_path: str
    :return: A DatasetRecord for this image.
    :rtype: src.dataset_handler.record.DatasetRecord
    """
    img_name = path.basename(file_path)
    return DatasetRecord(load_img(file_path), file_path, Metadata(get_img_metadata(img_name)))


def split_dataset(dataset, split_factor):
    return train_test_split(dataset, test_size=split_factor)
