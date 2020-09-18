# Write a code to generate a aplhabet half pyramid pattern.

# Sample Input :
# 5
# Sample Output :
# EEEEE
# DDDD
#  CCC
#   BB
#    A


N = int(input(''))

for row in range(0, N):
    for column in range(0, N):
        if(column < row):
            print(' ', end='')
        else:
            print(chr(65+N-row-1), end='')
    print('')
