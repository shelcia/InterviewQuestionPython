# you are given with array of numbers.you have to find whether array is beautiful or not.
# A beautiful array is an array whose sum of all numbers is divisible by 2, 3 and 5
N = int(input(""))
array = list(map(int, input().split(" ")[:N]))

sum = 0
for i in range(0, len(array)):
    sum = sum+array[i]

if((sum % 2 == 0) and (sum % 3 == 0) and (sum % 5 == 0)):
    print(1)
else:
    print(0)
