# You are given with a list of size ‘n’. The list is imposed with a condition that all
# elements must be of range 0 to n-1.
# Your task is to rearrange the numbers such that arr[i] becomes arr[arr[i]].

N = int(input(''))

array = list(map(int, input().split(' ')[:N]))
newArray = []

for index in range(0, N):
    if(array[index] != array[array[index]]):
        newArray.append(array[array[index]])
    else:
        newArray.append(array[index])

for index in range(0, N):
    if(index == N-1):
        print(newArray[index], end='')
    else:
        print(newArray[index], end=' ')
