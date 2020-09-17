# FINDING SMALLEST AND LARGEST INDEXES
N = int(input(""))
Array = list(map(int, input().split(' ')[:N]))
max = Array[0]
min = Array[0]
maxIndex = 0
minIndex = 0
for i in range(1, N):
    if(max < Array[i]):
        max = Array[i]
        maxIndex = i
    elif(min > Array[i]):
        min = Array[i]
        minIndex = i
# print(max)
# print(min)
print(minIndex+1, maxIndex+1)
