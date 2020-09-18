# ROTATE THE ARRY BY K STEPS

N = list(map(int, input().split(' ')[:2]))
array = list(map(int, input().split(' ')[:N[0]]))

i = 0
while(i < N[1]):
    lastInteger = array[len(array)-1]
    for index in range(len(array)-1, 0, -1):
        array[index], array[index-1] = array[index-1], array[index]
    i = i+1

array[0] = lastInteger

print(array)

# 1 9 8 4 0 0 2 7 0 6
# O(N[0]*N[1])
