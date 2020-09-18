# You are a passport issuer, but due to some problems in the system,
# there are redundant  passport numbers.
# Your task is to delete all the duplicate passport numbers.
# You are given a list of passport numbers.
N = int(input(""))
array = list(map(str, input().split(" ")[:N]))
newArray = []
ignoredIndexes = []
length = len(array)
for i in range(0, length):
    for j in range(i+1, length):
        if(array[i] == array[j]):
            ignoredIndexes.append(j)
    if(not(i in ignoredIndexes)):
        newArray.append(array[i])

# DISPLAY NEW ARRAY
for k in range(0, len(newArray)):
    # FOR LAST INDEX
    if(k == len(newArray)-1):
        print(newArray[k], end="")
    else:
        print(newArray[k], end=" ")
