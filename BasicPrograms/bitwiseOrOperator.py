# Given a number N and an array of N elements, find the Bitwise OR of the array elements.
N = int(input(""))
array = list(map(int, input().split(' ')[:N]))
result = array[0]
for i in range(1, N):
    result = result | array[i]
print(result)
