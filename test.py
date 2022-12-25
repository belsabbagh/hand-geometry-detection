import os

import pandas as pd

from src.dataset import IMAGE_NAME
from src.dataset.config import ASPECT_OF_HAND


if __name__ == '__main__':
    source = 'data\\train'
    destination = 'data\\train'
    metadata = pd.read_csv('data\\HandInfo.csv', index_col=IMAGE_NAME)
    categories = ['dorsal left', 'dorsal right', 'palmar left', 'palmar right']

    # gather all files
    allfiles = os.listdir(source)

    # iterate on all files to move them to destination folder
    for f in allfiles:
        if f in categories:
            continue
        meta = (metadata.loc[f]).to_dict()
        src_path = os.path.join(source, f)
        dst_path = os.path.join(destination, f'{meta[ASPECT_OF_HAND]}', 'p', f)
        os.rename(src_path, dst_path)
