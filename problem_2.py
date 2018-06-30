# import numpy as np
Matrix_N = 5
# Angle90 = np.pi/2
#
def main():
    matrix = [[1,  2,  3,  4,  5,],
              [6,  7,  8,  9,  10 ,],
              [11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25]]
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]

    print("==========Original Matrix==========")
    print_matrix(matrix)
    print("==========Rotated Matrix==========")
    print_matrix(rotate(matrix))

def print_matrix(matrix):
    for x_line in range(Matrix_N):
        for y_line in range(Matrix_N):
            print('{}\t'.format(matrix[x_line][y_line]), end=" ")
        print('\n')

# def rotate(matrix):
#     matrix1 = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
#     for y_line in range(Matrix_N):
#         for x_line in range(Matrix_N):
#             x_rotate = x_line*np.uint32(np.cos(Angle90))\
#                        - y_line*np.uint32(np.sin(Angle90))
#             y_rotate = x_line*np.uint32(np.sin(Angle90)) \
#                        + y_line*np.uint32(np.cos(Angle90))
#             print(x_rotate, y_rotate)
#             matrix1[y_line][x_line] = matrix[y_rotate][x_rotate + Matrix_N - 1]
#     return matrix1

def rotate(matrix):
    matrix = transpose(matrix)
    matrix = reverse(matrix)
    return matrix

def transpose(matrix):
    for x in range(Matrix_N):
        for y in range(x):
            temp = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = temp
    return matrix

def reverse(matrix):
    for x in range(round(Matrix_N/2)):
        for y in range(Matrix_N):
            temp = matrix[x][y]
            matrix[x][y] = matrix[Matrix_N-1-x][y]
            matrix[Matrix_N - 1 - x][y] = temp
    return matrix

if __name__ == '__main__':
    main()