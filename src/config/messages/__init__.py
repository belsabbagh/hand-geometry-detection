from timeit import default_timer


def dataset_load_msg(count, dir_path, start_time, precision=2):
    return f'{count} records were loaded from {dir_path} in {round(default_timer() - start_time, precision)} seconds.'


def dataset_split_msg(tr_count, ts_count):
    return f'Divided dataset into {tr_count} training records and {ts_count} testing records.'
