# Input Description:
# Given an odd integer R indicates number of rows.R is always an odd number.

# Sample Input :
# 5
# Sample Output :
# bbbb*bbbb
# bbb***bbb
# bb*****bb
# b*******b
# *********

N = int(input(''))
for index in range(0, N):
    for secondIndex in range(0, 2*N-1):
        if (secondIndex >= (2*N-1)//2-index and secondIndex <= (2*N-1)//2+index):
            print('*', end='')
        else:
            print('b', end='')
    print('')
