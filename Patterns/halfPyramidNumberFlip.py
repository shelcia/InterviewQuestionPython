# Write a code to generate a half pyramid number pattern.

# Sample Input :
# 5
# Sample Output :
# 12345
# 4321
# 123
# 21
# 1

N = int(input(''))

for index in range(1, N+1):
    if(index % 2 != 0):
        for j in range(1, N-index+2):
            print(j, end="")
        print('')
    else:
        for j in range(N-index+1, 0, -1):
            print(j, end="")
        print('')
