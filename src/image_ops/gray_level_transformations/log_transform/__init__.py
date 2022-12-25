import numpy as np


def log_transform_function(r, c):
    return c * (np.log(r + 1))


