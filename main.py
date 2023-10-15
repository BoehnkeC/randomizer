import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import dask.array as da


class Array:
    def __init__(self, rows=1, digits=6, numbers=10, chunk_rows=2):
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

    def create_array(self, rows=10, cols=6):
        self.knight = np.zeros(shape=(rows, cols), dtype=np.float64)


class Statistics:
    def __init__(self, random_arr=None):
        self.rarr = random_arr
        self.counts = None
        self.df = None
        self.mean = None
        self.std = None

    def get_first_level_statistics(self):
        self.mean = self.rarr.mean(axis=1)
        self.std = self.rarr.std(axis=1)

    def get_counts(self):
        """TODO:
        pap_blocks returns the result as many times as there are chunks.
        Hence, the array (10 x 6) returned twice if there are 2 chunks.
        The array is filled with the unique counts per chunk and must be added chunk-wise.
        Consider creating a target dask array with equal chunk count as the input array, (10 x 6 x chunks).
        Put the results from map_block into the respective chunks and sum the chunks with dask methods.
        """
        tmp = da.map_blocks(self._my_function, self.rarr, dtype=np.int8).compute()
        print(type(tmp))
        # print(tmp.compute())

    def _my_function(self, chunk):
        result = np.zeros(shape=(10, 6), dtype=np.float64)

        # for n in range(1):
        uniques, counts = np.unique(chunk[:, 0], return_counts=True, axis=0)
        result[uniques, 0] += counts
        print(result)

        return result


def plot_counts(arr=None):
    sns.heatmap(arr, cmap=sns.color_palette("Spectral", as_cmap=True))
    plt.show()


if __name__ == "__main__":
    array = Array(rows=4)
    array.create_random_array()
    print(array.arr.compute())

    stats = Statistics(random_arr=array.arr)
    stats.get_first_level_statistics()
    stats.get_counts()
    # print(stats.counts.compute())

    # plot_counts(arr=counts)
