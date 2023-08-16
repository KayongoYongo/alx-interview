#!/usr/bin/python3
"""A function that rotates a 2D matrix in a 90
degree clockwise manner
"""


def transpose(matrix):
    """
    This function will transpose the matrix

    Args:
        A 2D matrix

    Return:
        A transposed matrix
    """
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    return matrix


def reverse_rows(matrix):
    """
    This function reverses the rows of a matrix

    Args:
        A 2D matrix

    Return:
        A matrix whose rows have been reversed
    """
    for row in matrix:
        row.reverse()

    return matrix


def rotate_2d_matrix(matrix):
    """
    This function rotates a 2D matrix

    Args:
        A 2D matrix

    Return:
        A rotated 2D matrix
    """
    transposed_matrix = transpose(matrix)
    rotated_matrix = reverse_rows(transposed_matrix)
    return rotated_matrix
