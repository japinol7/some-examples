""" Calculates n rows of the Floyd's triangle.
The Floyd's triangle is defined by filling the rows of the triangle with consecutive numbers,
starting with a 1 in the top left corner.
Ex:
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
16 17 18 19 20 21
22 23 24 25 26 27 28
"""
__author__ = 'Joan A. Pinol  (japinol)'

from time_it.time_it import time_it

N_ROWS_DEFAULT = 10


def calc_floyd_triangle(n_rows=N_ROWS_DEFAULT):
    rows = []
    num = 1
    for i in range(n_rows):
        columns = []
        for j in range(i + 1):
            columns.append(num)
            num = num + 1
        rows.append(columns)
    return rows


def print_floyd_triangle(rows):
    for column in rows:
        for item in column:
            print(item, end=' ')
        print()


if __name__ == "__main__":
    res = time_it(calc_floyd_triangle)
    print(f"Floyd's triangle of {N_ROWS_DEFAULT} rows:")
    print_floyd_triangle(res)
