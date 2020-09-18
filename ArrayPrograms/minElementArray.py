# Prateek finds it difficult to judge the minimum element in the list of elements given to him.
# Your task is to develop the algorithm in order to find the minimum element.

N = int(input(''))
array = list(map(int, input().split(' ')))

min = array[0]

for index in range(1, len(array)):
    if(min > array[index]):
        min = array[index]
print(min)
