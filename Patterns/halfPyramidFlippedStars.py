# *****
# ****
#  ***
#   **
#    *

N = int(input(''))
for index in range(0, N):
    for secondIndex in range(0, N):
        if(secondIndex < index):
            print(' ', end='')
        else:
            print('*', end='')
    print('')
