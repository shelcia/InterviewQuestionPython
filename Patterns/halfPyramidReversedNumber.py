# Write a code to generate a half pyramid pattern using numbers.
# Sample Input :
# 5
# Sample Output :
# 5
# 45
# 345
# 2345
# 12345

N = int(input(''))

for index in range(0, N):
    for secondIndex in range(N-index, N+1):
        print(secondIndex, end='')
    print('')
