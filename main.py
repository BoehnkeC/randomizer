import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import dask.array as da


class Array:
    def __init__(self, rows=1, digits=6, numbers=10, chunk_rows=1000):
        self.rows = rows
        self.digits = digits
        self.chunk_rows = chunk_rows
        self.numbers = numbers
        self.arr = None  # array holding the random numbers
        self.knight = None  # array holding statistical numbers, like frequency, called knight because flexible

    def create_random_array(self):
        self.arr = da.from_array(
            np.random.randint(self.numbers, size=(self.rows, self.digits), dtype=np.int8),
            chunks=(self.chunk_rows, self.digits)
        )

    def create_array(self, rows=10, cols=6, dtype=np.float64):
        self.knight = np.zeros(shape=(rows, cols), dtype=dtype)


class Statistics:
    def __init__(self, random_arr=None):
        self.rarr = random_arr
        self.counts = None
        self.mean = None
        self.std = None

    def get_first_level_statistics(self):
        self.mean = self.rarr.mean(axis=1)
        self.std = self.rarr.std(axis=1)

    def get_counts(self, arr=None):
        self.counts = arr

        for n in range(6):
            uniques, counts = da.unique(self.rarr[:, n], return_counts=True)
            self.counts[uniques.compute(), n] += counts.compute()


def plot_counts(arr=None):
    sns.heatmap(arr, cmap=sns.color_palette("Spectral", as_cmap=True))
    plt.show()


if __name__ == "__main__":
    arrays = Array(rows=10000000)
    arrays.create_random_array()
    arrays.create_array(rows=10, cols=6, dtype=np.int64)

    stats = Statistics(random_arr=arrays.arr)
    # stats.get_first_level_statistics()
    stats.get_counts(arr=arrays.knight)

    plot_counts(arr=stats.counts)
