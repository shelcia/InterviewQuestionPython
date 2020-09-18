# Write a code to generate an inverted half pyramid pattern using stars.

# Sample Input :
# 5
# Sample Output :
# *  *  *  *  *
# *  *  *  *
# *  *  *
# *  *
# *

N = int(input(''))

for index in range(0, N+1):
    for secondIndex in range(0, N-index):
        if(secondIndex == N-index-1):
            print('*', end='')
        else:
            print('*', end='  ')
    print('')
