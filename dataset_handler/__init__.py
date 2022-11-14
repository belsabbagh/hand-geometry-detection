from os import listdir
from os.path import isfile, join

from dataset_handler.dataset_record import DatasetRecord, Metadata
from dataset_handler.metadata_handler import get_img_metadata, metadata
from src.img_ops import read_img


def load_dataset(dir_path, metadata_path):
    return [load_record(dir_path, f, metadata_path) for f in listdir(dir_path) if isfile(join(dir_path, f))]


def load_record(dir_path, img_name, metadata_path):
    file_path = join(dir_path, img_name)
    return DatasetRecord(read_img(file_path), Metadata(get_img_metadata(metadata_path, img_name)))
