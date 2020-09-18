# Generate a number pyramid pattern.

# Sample Input :
# 4
# Sample Output :
# 1234567
# 12345
# 123
# 1

N = int(input(''))

for index in range(0, N):
    for numberIndex in range(1, 2*(N-index)):
        print(numberIndex, end='')
    print('')
