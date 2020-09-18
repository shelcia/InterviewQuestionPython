# You are given with an array of numbers,
# Your task is to print the difference of indices of largest and smallest number.
# All number are unique.

N = int(input(""))
array = list(map(int, input().split(" ")[:N]))

maxIndex = 0
minIndex = 0
max = array[0]
min = array[0]
for i in range(1, len(array)):
    if(array[i] > max):
        max = array[i]
        maxIndex = i
    if(array[i] < min):
        min = array[i]
        minIndex = i

print(maxIndex-minIndex)
