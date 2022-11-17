from os import listdir
from os.path import isfile, join

import pandas as pd

from src.dataset_handler.config import IMAGE_NAME
from src.dataset_handler.dataset_record import DatasetRecord, Metadata
from src.img_loader import load_img

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


def load_dataset(dir_path: str, metadata_path: str) -> pd.DataFrame:
    """
    Creates a dataset from an image directory and a metadata file path.
    :param dir_path: Image directory path.
    :type dir_path: str
    :param metadata_path: Metadata file path.
    :type metadata_path: str
    :return: A DataFrame of the loaded image dataset.
    :rtype: pd.DataFrame
    """
    global metadata
    metadata = pd.read_csv(metadata_path, index_col=IMAGE_NAME)
    return pd.DataFrame([create_record(dir_path, f) for f in listdir(dir_path) if isfile(join(dir_path, f))])


def create_record(dir_path: str, img_name: str) -> DatasetRecord:
    """
    Creates a dataset record from a given image file in a directory.
    :param dir_path: Path of image directory.
    :type dir_path: str
    :param img_name: Image file name.
    :type img_name: str
    :return: A DatasetRecord for this image.
    :rtype: src.dataset_handler.dataset_record.DatasetRecord
    """
    return DatasetRecord(load_img(join(dir_path, img_name)), img_name, Metadata(get_img_metadata(img_name)))
