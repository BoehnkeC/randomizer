import random
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import dask.array as da
import dask.dataframe as daf


class Array:
    def __init__(self, rows=1, columns=6, chunk_rows=1000):
        self.rows = rows
        self.cols = columns
        self.chunk_rows = chunk_rows
        self.arr = None  # array holding the random numbers
        self.stats = None  # array holding statistical numbers, like frequency

    def create_random_array(self):
        self.arr = da.from_array(
            np.random.randint(10, size=(self.rows, self.cols), dtype=np.int8),
            chunks=(self.chunk_rows, self.cols)
        )

    def create_array(self, cols=10, rows=6):
        self.stats = np.zeros(shape=(cols, rows), dtype=np.float64)


class Statistics:
    def __init__(self, random_arr=None, arr=None):
        self.rarr = random_arr
        self.arr = arr
        self.df = None
        self.mean = None
        self.std = None

    def get_first_level_statistics(self):
        self.mean = self.rarr.mean(axis=1)
        self.std = self.rarr.std(axis=1)

    def get_counts(self):
        def _my_function():
            print("Hello")

        blocks = da.map_blocks(_my_function, self.rarr)
        # self.arr = np.unique(self.rarr.compute(), return_counts=True)[-1]
        print(blocks)

    @staticmethod
    def _my_function():
        print("Hello")


def plot_counts(arr=None):
    sns.heatmap(arr, cmap=sns.color_palette("Spectral", as_cmap=True))
    plt.show()


if __name__ == "__main__":
    array = Array(rows=1000)
    array.create_random_array()

    stats = Statistics(random_arr=array.arr, arr=array.create_array())
    stats.get_first_level_statistics()
    stats.get_counts()
    # array.create_array()

    # plot_counts(arr=counts)
