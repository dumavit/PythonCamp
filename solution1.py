from random import randint

# prepare NxMxL matrix with random elements
N = 10
M = 10
L = 10
low = 0
high = 9
matrix = [[[randint(low, high) for i in range(N)] for j in range(M)] for k in range(L)]


def find_columns(m):
    """ Find 3 perpendicular columns with maximum sum of its elements in NxMxL matrix"""
    L, M, N = (len(m), len(m[0]), len(m[0][0]))
    sum1 = [0] * N * M  # list for accumulating column sum of 1'st axis
    sum2 = [0] * N * L  # 2'nd axis
    sum3 = [0] * M * L  # 3'rd axis
    for i in range(L * M * N):
        element = m[i // (N * M)][(i // N) % M][i % N]
        sum1[i % (N * M)] += element
        sum2[i // (N * M) * N + i % N] += element
        sum3[i // N] += element
    ind1, ind2, ind3 = (sum1.index(max(sum1)), sum2.index(max(sum2)), sum3.index(max(sum3)))
    col1 = [i[ind1 // N][ind1 % N] for i in m]  # get column from matrix knowing its index
    col2 = [i[ind2 % N] for i in m[ind2 // N]]
    col3 = m[ind3 // M][ind3 % M]
    return col1, col2, col3


if __name__ == "__main__":
    print('\n'.join(str(i) for i in find_columns(matrix)))
