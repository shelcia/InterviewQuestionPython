# Loki wants to steal the tesseract but in order to do so, he has to rearrange the elements
# in an array in a specific manner which is mentioned in a clue.
# The clue says ‘cursed are the odd and sorted are the even’.
# Loki manages to decode the clue which translates to “sort the even positioned elements of an array,
# starting from the element at index 0, in ascending order”.
# Manipulate the array so as to help Loki steal the tesseract.


# EVEN SORTING
def bubbleSort(array):
    for index in range(0, len(array)):
        for secondIndex in range(0, len(array)-index-2):
            if(array[secondIndex] > array[secondIndex+2]):
                array[secondIndex], array[secondIndex +
                                          2] = array[secondIndex+2], array[secondIndex]

    return(array)


N = int(input(''))

array = list(map(int, input().split(' ')[:N]))

newArray = bubbleSort(array)

for index in range(0, len(newArray)):
    if(index == len(newArray)-1):
        print(newArray[index], end='')
    else:
        print(newArray[index], end=' ')
