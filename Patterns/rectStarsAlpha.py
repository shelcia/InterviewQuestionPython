# Generate the following pattern.
# *****
# b****
# bb***
# bbb**
# bbbb*

N = int(input(''))

for index in range(0, N):
    for bIndex in range(0, index):
        print('b', end='')
    for starIndex in range(index, N):
        print('*', end='')

    print('')
