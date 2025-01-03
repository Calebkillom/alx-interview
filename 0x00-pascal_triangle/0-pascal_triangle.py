#!/usr/bin/python3
"""
returns a list of lists of integers representing the Pascal’s triangle of n
"""


def pascal_triangle(n):
    """
    Returns Pascal's Triangle as a list of lists of integers for a given n
    """
    if n <= 0:
        return []
    result = []

    for row_index in range(n):
        current_row = []

        for col_index in range(row_index + 1):
            if col_index == 0 or col_index == row_index:
                current_row.append(1)
            else:
                current_row.append(
                    result[row_index - 1][col_index - 1] + result[row_index - 1][col_index]
                )

        result.append(current_row)

    return result
