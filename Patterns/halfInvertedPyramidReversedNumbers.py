# Write a code to generate a half pyramid pattern using numbers.
# Sample Input :
# 5
# Sample Output :
# 54321
# 4321
# 321
# 21
# 1

N = int(input(''))

for index in range(0, N):
    for secondIndex in range(N-index, 0, -1):
        print(secondIndex, end='')
    print('')
