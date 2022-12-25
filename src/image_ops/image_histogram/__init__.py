from itertools import chain

import matplotlib.pyplot as plt
import numpy as np


def generate_image_histogram(img):
    return np.histogram(img)


def plot_image_histogram(img):
    plt.hist(list(chain.from_iterable(img)))
    plt.show()
