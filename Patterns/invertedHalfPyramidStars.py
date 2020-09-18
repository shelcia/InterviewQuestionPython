# Write a code to generate a inverted half pyramid pattern using numbers.
# Sample Input :
# 5
# Sample Output :
# 12345
# 1234
# 123
# 12
# 1

N = int(input(''))

for i in range(1, N+1):
    for j in range(1, N+2-i):
        print(j, end="")
    print('')
