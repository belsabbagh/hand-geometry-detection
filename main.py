"""Main Module"""
from timeit import default_timer as time

from src.dataset_handler import load_dataset, split_dataset

if __name__ == '__main__':
    dir_path, metadata_file = 'data\\train', 'data\\HandInfo.csv'
    test_train_ratio = 0.15
    start = time()
    dataset = load_dataset(dir_path, metadata_file)
    print(f'{len(dataset)} records were loaded from {dir_path} in {round(time() - start, 2)} seconds.')
    train_dataset, test_dataset = split_dataset(dataset, test_train_ratio)
    print(f'Divided dataset into {len(train_dataset)} training records and {len(test_dataset)} testing records.')
