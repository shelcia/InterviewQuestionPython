# Find the smallest positive number missing from an unsorted array

N = int(input(''))
array = list(map(int, input().split(' ')[:N]))
array.sort()

for index in range(0, len(array)):
    if(array[index] > 0):
        positiveInteger = array[index]
        positiveIndex = index
        break

if(1 < positiveInteger):
    print(1)
else:
    for index in range(positiveIndex, len(array)):
        # print("index",index+1-positiveIndex)
        if((index+1-positiveIndex) != array[index]):
            # print("array",array[index])
            print(index+1-positiveIndex)
            break
