# Write a code to generate a half pyramid pattern using numbers.
# Sample Input :
# 5
# Sample Output :
# 5
# Sample Output :
# 55555
# 4444
# 333
# 22
# 1
N = int(input(''))

for index in range(0, N):
    for secondIndex in range(0, N-index):
        print(N-index, end='')
    print('')
