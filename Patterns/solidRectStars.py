# Generate a solid rectangle using stars.

N = list(map(int, input().split(' ')))

for index in range(0, N[0]):
    for secondIndex in range(0, N[1]):
        if(secondIndex == N[1]-1):
            print('*', end='')
        else:
            print('*', end=" ")
    print('')
