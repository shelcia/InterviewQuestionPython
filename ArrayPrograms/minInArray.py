# Pk finds it difficult to judge the minimum element in the list of elements given to him.
# Your task is to develop the algorithm in order to find the minimum element.
# Note:Don’t use sorting

N = int(input(""))
array = list(map(int, input().split(" ")[:N]))
min = array[0]

for i in range(1, len(array)):
    if(array[i] < min):
        min = array[i]

print(min)
