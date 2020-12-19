# You are an intern at GUVI and the company wants to organise its data and
# delete unnecessary extra storage elements used.
# You are given k arrays of unequal dimensions. Sort the k arrays individually and concatenate them.
def selectionSort(array):
    for index in range(0, len(array)):
        min = array[index]
        for secondIndex in range(index+1, len(array)):
            if(min > array[secondIndex]):
                array[index], array[secondIndex] = array[secondIndex], array[index]
    return(array)


arrayNumber = int(input(""))
finalSortedArray = []
array = []

for noOfArray in range(0, arrayNumber):
    N = int(input(""))
    array.append(list(map(int, input().split(" ")[:N])))
#     array[noOfArray]=list(map(int,input().split(" ")[:N]))


for noOfFinalArray in range(0, arrayNumber):
    #     print(selectionSort(array[noOfFinalArray]))
    finalSortedArray = finalSortedArray+selectionSort(array[noOfFinalArray])

for indexFinalSortedArray in range(0, len(finalSortedArray)):
    if(indexFinalSortedArray == len(finalSortedArray)-1):
        print(finalSortedArray[indexFinalSortedArray], end="")
    else:
        print(finalSortedArray[indexFinalSortedArray], end=" ")


# SELECTION SORT

# FIND THE MINIMUM IN [0,...N] THEN [1,...N] AND SO ON AND SWAP

def selectionSort(array):
    for index in range(0, len(array)):
        minIndex = index
        for secondIndex in range(index + 1, len(array)):
            if(array[minIndex] > array[secondIndex]):
                minIndex = secondIndex
        array[index], array[minIndex] = array[minIndex], array[index]
    return array


if __name__ == "__main__":

    print(selectionSort([45, 78, 3, 67, 90, 0, 12]))
