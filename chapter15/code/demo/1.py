import time

# t1 = [1, 2, 5, 10, 12]  # i, j index


def get_pair_array(integer_array):
    length = len(integer_array)
    pair_array = []
    for i, v in enumerate(integer_array):
        j = i + 1
        while j <= length - 1:
            v2 = integer_array[j] - v
            pair_array.append(v2)
            j += 1
    return pair_array


# print(l2)  # [1, 4, 9, 11, 3, 8, 10, 5, 7, 2]

from concurrent.futures import thread

tasks = [1, 2, 3]

for task in tasks:
    pass

thread.ThreadPoolExecutor()
