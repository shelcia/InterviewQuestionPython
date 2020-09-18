# Move all xeroes to right

N = int(input(''))
array = list(map(int, input().split(' ')[:N]))

flag = 0

# BRING/REPLACE ALL NON-ZEROES TO LEFT
for index in range(0, len(array)):
    if(array[index] != 0):
        array[flag] = array[index]
        flag = flag+1
# NOW ADD ALL ZEROS TOWARDS RIGHT
for index in range(flag, len(array)):
    array[index] = 0

print(array)
