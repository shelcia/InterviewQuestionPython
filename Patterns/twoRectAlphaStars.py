# Input Description:
# Given an odd integer R indicates number of rows.R is always an odd number.

# Sample Input :
# 9
# Sample Output :
# bbbb*bbbb
# bbb***bbb
# bb*****bb
# b*******b
# *********
# b*******b
# bb*****bb
# bbb***bbb
# bbbb*bbbb


N = int(input(''))
k = 0
for index in range(0, N):
    if(index <= N//2):
        for secondIndex in range(0, N):
            if (secondIndex >= N//2-index and secondIndex <= N//2+index):
                print('*', end='')
            else:
                print('b', end='')
        print('')
    else:
        for secondIndex in range(0, N):
            if (secondIndex >= index-N//2 and secondIndex <= N-1-(index-N//2)):
                print('*', end='')
            else:
                print('b', end='')
        print('')
