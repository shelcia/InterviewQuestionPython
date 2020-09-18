# You are given given task is to print whether array is ‘majestic’ or not.A ‘majsetic’ array is an array whose sum of first three number is equal to last three number.


N = int(input(''))
array = list(map(int, input().split(' ')[:N]))
firstSum = 0
secondSum = 0
for index in range(0, 3):
    firstSum = firstSum+array[index]
for index in range(N-1, N-4, -1):
    secondSum = secondSum+array[index]


if(firstSum == secondSum):
    print(1)
else:
    print(0)
