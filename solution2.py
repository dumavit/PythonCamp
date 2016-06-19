import numpy as np

#  prepare matrix
N = 10  # size
low = 0
high = 9
matrix = np.random.randint(low, high + 1, (N, N, N))


def find_columns(m):
    """ Find 3 perpendicular columns with maximum sum of its elements in NxNxN matrix"""
    N = len(m)
    indexes = []
    for i in range(3):
        sums = np.sum(m, axis=i)  # get sums of columns values in different axis
        indexes.append(np.argmax(sums))  # save index of column with maximum sum
    col1 = m[:, indexes[0] // N, indexes[0] % N]
    col2 = m[indexes[1] // N, :, indexes[1] % N]
    col3 = m[indexes[2] // N, indexes[2] % N, :]
    return col1, col2, col3


if __name__ == "__main__":
    print('\n'.join(str(i) for i in find_columns(matrix)))
