"""Main Module"""
from timeit import default_timer as time

from src.config.messages import dataset_load_msg, dataset_split_msg
from src.dataset_handler import load_dataset, split_dataset

if __name__ == '__main__':
    dir_path, metadata_file = 'data\\train', 'data\\HandInfo.csv'
    test_train_ratio = 0.15
    start = time()
    dataset = load_dataset(dir_path, metadata_file)
    print(dataset_load_msg(len(dataset), dir_path, start, 3))
    train_dataset, test_dataset = split_dataset(dataset, test_train_ratio)
    print(dataset_split_msg(len(train_dataset), len(test_dataset)))
