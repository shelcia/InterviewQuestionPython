# Generate a floyd's triangle.

# Sample Input :
# 5
# Sample Output :
# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15


N = int(input(''))
val = 1
for index in range(1, N+1):
    for secondIndex in range(1, index+1):
        if(secondIndex == index):
            print(val, end='')
        else:
            print(val, end=' ')
        val = val+1
    print('')
