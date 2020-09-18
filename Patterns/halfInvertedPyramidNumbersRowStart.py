# Sample Input :
# 3
# Sample Output :
# 12345
# 2345
# 345
# 45
# 5

N = int(input(''))
for index in range(0, N):
    for secondIndex in range(1, N-index+1):
        print(index+secondIndex, end='')
    print('')
