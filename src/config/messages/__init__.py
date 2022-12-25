def dataset_load_msg(count, dir_path, duration):
    return f'{count} records were loaded from {dir_path} in {duration} seconds.'


def dataset_split_msg(tr_count, ts_count):
    return f'Divided dataset into {tr_count} training records and {ts_count} testing records.'
