# Given an integer R indicates number of rows.

# Sample Input :
# 5
# Sample Output :
# 1
# 22
# 333
# 4444
# 55555

N = int(input(''))

for index in range(1, N+1):
    for secondIndex in range(1, index+1):
        print(index, end='')
    print('')
