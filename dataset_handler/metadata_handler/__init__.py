import pandas as pd


metadata = None


def get_img_metadata(metadata_path, img_name):
    global metadata
    metadata = pd.read_csv(metadata_path)
    img_metadata = metadata.loc[metadata['imageName'] == img_name]
    return img_metadata.to_dict()
