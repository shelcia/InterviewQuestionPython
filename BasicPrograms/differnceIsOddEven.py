# Given 2 numbers N,M. Find their difference and check whether it is even or odd.

N = list(map(int, input('').split(' ')[:2]))

if((N[0]-N[1]) % 2 == 0):
    print('even')
else:
    print('odd')
