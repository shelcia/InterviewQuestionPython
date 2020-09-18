# Generate a hollow inverted half pyramid pattern using numbers.

# Sample Input :
# 5
# Sample Output :
# 12345
# 1  4
# 1 3
# 12
# 1

N = int(input(''))

for index in range(0, N):
    for numberIndex in range(1, N-index+1):
        if(index == 0):
            print(numberIndex, end='')
        else:
            if(numberIndex == 1 or numberIndex == N-index):
                print(numberIndex, end='')
            else:
                print(' ', end='')
    print('')
