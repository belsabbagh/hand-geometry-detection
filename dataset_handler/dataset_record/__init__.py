"""
This module contains the structure and methods of a single dataset record
"""


class DatasetRecord:
    """
    The data structure that stores a record of the dataset.
    """
    __img = None
    __metadata = None

    def __init__(self, _img, _img_metadata):
        self.__img = _img
        self.__metadata = _img_metadata

    def __repr__(self):
        return f"{self.get_metadata()}"

    def get_image(self):
        return self.__img

    def get_metadata(self):
        return self.__metadata


class Metadata:
    def __init__(self, _metadata_dict):
        self.__id = _metadata_dict['id'].get(0)
        self.__age = _metadata_dict['age'].get(0)
        self.__gender = _metadata_dict['gender'].get(0)
        self.__skin_color = _metadata_dict['skinColor'].get(0)
        self.__accessories = bool(_metadata_dict['accessories'].get(0))
        self.__nail_polish = bool(_metadata_dict['nailPolish'].get(0))
        self.__hand_aspect = _metadata_dict['aspectOfHand'].get(0)
        self.__img_name = _metadata_dict['imageName'].get(0)
        self.__irregularities = _metadata_dict['irregularities'].get(0)

    def __repr__(self):
        data = {
            'id': self.__id,
            'age': self.__age,
            'gender': self.__gender,
            'skinColor': self.__skin_color,
            'accessories': self.__accessories,
            'nailPolish': self.__nail_polish,
            'handAspect': self.__hand_aspect,
            'imageName': self.__img_name,
            'irregularities': self.__irregularities,
        }
        return f"{data}"

    def get_image_name(self):
        return self.__img_name
