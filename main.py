import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def generate_random_number(count=100):
    return [random.randint(0, 9) for r in range(count)]


def get_statistics(arr=None):
    _mean = np.mean(arr, axis=1)
    _std = np.std(arr, axis=1)

    return np.array([_mean, _std])


def get_unique_counts(arr=None):
    return np.unique(arr, return_counts=True)[-1]


def create_array(cols=6, rows=1):
    return np.zeros(shape=(rows, cols))


def get_numbers(arr=None):
    for i in range(arr.shape[1]):
        arr[:, i] = generate_random_number(count=arr.shape[0])

    return arr


def get_counts(arr=None, _counts=None):
    for i in range(arr.shape[1]):
        _counts[i, :] = get_unique_counts(arr=arr[:, i])

    return _counts


def plot_counts(arr=None):
    sns.heatmap(arr, cmap=sns.color_palette("Spectral", as_cmap=True))
    plt.show()


if __name__ == "__main__":
    row_count = 10000000  # 1 million
    numbers = create_array(rows=row_count)
    counts = create_array(rows=6, cols=10)

    numbers = get_numbers(arr=numbers)
    counts = get_counts(arr=numbers, _counts=counts)
    stats = get_statistics(arr=numbers)

    plot_counts(arr=counts)
