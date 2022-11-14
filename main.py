"""Main Module"""
from timeit import default_timer

from dataset_handler import load_dataset

if __name__ == '__main__':
    training_path, metadata_file = 'data\\train', 'data/HandInfo.csv'
    start = default_timer()
    dataset = load_dataset(training_path, metadata_file)
    time = default_timer() - start
    print(f'{len(dataset)} records were loaded from {training_path} in {time} seconds.')
