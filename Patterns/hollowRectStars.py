# Write a code to generate a hollow rectangle using stars

N = list(map(int, input().split(' ')))

for index in range(0, N[0]):
    for secondIndex in range(0, N[1]):
        if(secondIndex == N[1]-1):
            print('*', end='')
        elif(index == 0 or secondIndex == 0 or index == N[0]-1):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print('')
