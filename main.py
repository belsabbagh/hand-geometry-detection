"""Main Module"""
from timeit import default_timer as time

import pandas as pd

from src.dataset_handler import load_dataset

if __name__ == '__main__':
    train_path, test_path, metadata_file = 'data\\train', 'data\\test', 'data\\HandInfo.csv'

    start = time()
    train_dataset = load_dataset(train_path, metadata_file)
    print(f'{len(train_dataset)} training records were loaded from {train_path} in {round(time() - start, 2)} seconds.')

    start = time()
    test_dataset = load_dataset(test_path, metadata_file)
    print(f'{len(test_dataset)} testing records were loaded from {test_path} in {round(time() - start, 2)} seconds.')
