# Write a code to generate a half pyramid pattern using numbers.
# Sample Input :
# 5

# Sample Output :
# 13579
# 3579
# 579
# 79
# 9

N = int(input(''))

for index in range(0, N):
    for secondIndex in range(0, N-index):
        print(2*secondIndex+1 + 2*index, end='')
    print('')
