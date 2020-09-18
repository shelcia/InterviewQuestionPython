# Generate a half pyramid pattern using numbers.

# Sample Input :
# 5
# Sample Output :
# 1
# 12
# 123
# 1234
# 12345

N = int(input(''))

for index in range(1, N+1):
    for secondIndex in range(1, index+1):
        print(secondIndex, end='')
    print('')
