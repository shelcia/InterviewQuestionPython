# Write a code to generate a half pyramid number pattern.

# Sample Input :
# 5
# Sample Output :
# 12345
# 1234
# 123
# 12
# 1

N = int(input(''))

for index in range(1, N+1):
    for secondIndex in range(1, N-index+2):
        print(secondIndex, end='')
    print('')
