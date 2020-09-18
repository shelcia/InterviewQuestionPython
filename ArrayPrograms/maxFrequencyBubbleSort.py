# You are given an array of digits. Your task is to print the digit with maximum frequency.

N = int(input(''))
array = list(map(int, input().split(' ')[:N]))

maxArray = array[0]


def bubbleSort(array):
    for index in range(0, len(array)):
        for secondIndex in range(0, len(array)-index-1):
            if(array[secondIndex] > array[secondIndex+1]):
                array[secondIndex], array[secondIndex +
                                          1] = array[secondIndex+1], array[secondIndex]
    return(array)


def frequency(array):
    #     array.sort()
    max_count = 1
    current_count = 1
    sortedArray = bubbleSort(array)
    maxArray = sortedArray[0]
#     print(sortedArray)
    for index in range(1, len(sortedArray)):
        #         print(index)
        if(sortedArray[index] == sortedArray[index-1]):
            current_count = current_count+1
        else:
            if(max_count < current_count):
                max_count = current_count
                maxArray = sortedArray[index-1]
            current_count = 1
    # FOR LAST ELEMENT
    if(current_count > max_count):
        max_count = current_count
        maxArray = sortedArray[index-1]

    return (maxArray)

#     return(maxArray,max_count)


print(frequency(array))
