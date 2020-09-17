# Given 2 numbers N and K followed by N elements,print the number of repetition of K otherwise print '-1' if the element not found.

N = list(map(int, input().split(" ")[:2]))
array = list(map(int, input().split(" ")[:N[0]]))
count = 0
for i in range(0, N[0]):
    if(array[i] == N[1]):
        count = count+1
if(count == 0):
    print(-1)
else:
    print(count-1)
