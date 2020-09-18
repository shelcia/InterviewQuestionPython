# Assume you are a student studying in school.
# You are given a task to find first negative integer for each and every window of size k.
N = int(input(""))
array = list(map(int, input().split(" ")[:N]))
K = int(input(""))  # WINDOW SIZE
newArray = []

for index in range(0, len(array)-K+1):
    for windowIndex in range(index, index+K):
        if(array[windowIndex] < 0):
            newArray.append(array[windowIndex])
            break
        else:
            result = (array[index] > 0)
            # IF EVERY ELEMENT PRESENT IN THE WINDOW IS A POSITIVE NUMBER
            for resultIndex in range(index+1, index+K):
                result = result and (array[resultIndex] > 0)
            if(result):
                newArray.append(0)
                break

# DISPLAY NEW ARRAY
for index in range(0, len(newArray)):
    # FOR LAST INDEX
    if(index == len(newArray)-1):
        print(newArray[index], end="")
    else:
        print(newArray[index], end=" ")
