"""
This module contains the structure and methods of a single dataset_handler record
"""
from src.dataset_handler.config import IRREGULARITIES, ASPECT_OF_HAND, NAIL_POLISH, ACCESSORIES, SKIN_COLOR, GENDER, AGE, ID


class DatasetRecord:
    """
    The data structure that stores a record of the dataset_handler.
    """
    __img = None
    __img_path = None
    __metadata = None

    def __init__(self, _img, __img_path, _img_metadata):
        self.__img = _img
        self.__img_path = __img_path
        self.__metadata = _img_metadata

    def __repr__(self):
        return f"{self.get_metadata()}"

    def get_image(self):
        return self.__img

    def get_image_path(self):
        return self.__img_path

    def get_metadata(self):
        return self.__metadata

    def tolist(self):
        return [self.__img, self.__img_path, self.__metadata]


class Metadata:
    def __init__(self, _metadata_dict):
        self.__id = _metadata_dict[ID]
        self.__age = _metadata_dict[AGE]
        self.__gender = _metadata_dict[GENDER]
        self.__skin_color = _metadata_dict[SKIN_COLOR]
        self.__accessories = bool(_metadata_dict[ACCESSORIES])
        self.__nail_polish = bool(_metadata_dict[NAIL_POLISH])
        self.__hand_aspect = _metadata_dict[ASPECT_OF_HAND]
        self.__irregularities = _metadata_dict[IRREGULARITIES]

    def __repr__(self):
        data = {
            ID: self.__id,
            AGE: self.__age,
            GENDER: self.__gender,
            SKIN_COLOR: self.__skin_color,
            ACCESSORIES: self.__accessories,
            NAIL_POLISH: self.__nail_polish,
            ASPECT_OF_HAND: self.get_hand_aspect(),
            IRREGULARITIES: self.__irregularities,
        }
        return f"{data}"

    def get_hand_aspect(self):
        return self.__hand_aspect

    def tolist(self):
        return [
            self.__id,
            self.__age,
            self.__gender,
            self.__skin_color,
            self.__accessories,
            self.__nail_polish,
            self.get_hand_aspect(),
            self.__irregularities,
        ]
