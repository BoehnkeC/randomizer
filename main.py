import random
import numpy as np


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


if __name__ == "__main__":
    row_count = 1000000  # 1 million
    numbers = create_array(rows=row_count)
    counts = create_array(rows=6, cols=10)

    for i in range(numbers.shape[1]):
        numbers[:, i] = generate_random_number(count=numbers.shape[0])

    stats = get_statistics(arr=numbers)

    for i in range(numbers.shape[1]):
        counts[i, :] = get_unique_counts(arr=numbers[:, i])
