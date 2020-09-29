import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

#program is not completed


def diagonalDifference(arr):
    # Write your code here
    print('ho')
    differnce = 0
    leftDiagonalSum = 0
    rightDiagonalSum = 0

    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if(i == j):
                leftDiagonalSum = leftDiagonalSum + arr[i][j]
            elif(i+j == (len(arr) - 1)):
                rightDiagonalSum = rightDiagonalSum + arr[i][j]

    differnce = abs(leftDiagonalSum - rightDiagonalSum)

    return differnce


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input("Enter the number of rows:"))

    # Initialize matrix
    matrix = []
    print("Enter the entries rowwise:")

    # For user input
    for i in range(n):          # A for loop for row entries
        a = []
        for j in range(n):      # A for loop for column entries
            a.append(int(input()))
        matrix.append(a)

    print(diagonalDifference(matrix))

    # fptr.write(str(result) + '\n')

    # fptr.close()
