# Write a code to generate a full pyramid pattern using stars.


# Sample Input :
# 5
# Sample Output :
#    *
#   * *
#  * * *
# * * * *
# * * * * *

N = int(input(''))

for index in range(0, N+1):
    for secondIndex in range(0, index+1):
        if((index+secondIndex) > N//2+1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')
