import random
import time
import tracemalloc

from merge_sort import merge_sort
from quick_sort import quick_sort


def test_performance(size):

    data_random = [random.randint(1, 10000) for _ in range(size)]
    data_sorted = sorted(data_random)
    data_reverse = sorted(data_random, reverse=True)

    datasets = [
        ("Random Data", data_random),
        ("Sorted Data", data_sorted),
        ("Reverse Sorted Data", data_reverse)
    ]

    print("\nDataset size:", size)

    for name, data in datasets:

        tracemalloc.start()
        start = time.time()
        merge_sort(data.copy())
        merge_time = time.time() - start
        _, merge_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        tracemalloc.start()
        start = time.time()
        quick_sort(data.copy())
        quick_time = time.time() - start
        _, quick_peak = tracemalloc.get_traced_memory()
        tracemalloc.stop()

        print("\n", name)
        print("Merge Sort -> Time:", round(merge_time, 6),
              "seconds | Memory:", round(merge_peak/1024, 2), "KB")

        print("Quick Sort -> Time:", round(quick_time, 6),
              "seconds | Memory:", round(quick_peak/1024, 2), "KB")


if __name__ == "__main__":

    sizes = [1000, 5000, 10000]

    for s in sizes:
        test_performance(s)
