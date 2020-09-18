# Write a code to generate a pyramid pattern using stars from the given input size N.

# Sample Input :
# 5
# Sample Output :
# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

N = int(input(''))

for index in range(1, N+1):
    for secondIndex in range(1, index+1):
        print('*', end='')
    print('')

for index in range(1, N):
    for secondIndex in range(1, N-index+1):
        print('*', end='')
    print('')
