# You are given a number with duplicate digits your task is to remove the immediate duplicate digits
# and print the result

string = str(input(""))
array = list(string)
newArray = []
# CHECK FOR FIRST ELEMENT IN ARRAY
if(array[0] != array[1]):
    newArray.append(array[0])
# CHECK FOR ELEMENTS BETWEEN FIR AND LAST IN ARRAY
for i in range(1, len(array)-1):
    if(not((array[i] == array[i+1]) or (array[i] == array[i-1]))):
        newArray.append(array[i])
# CHECK FOR LAST ELEMENT IN ARRAY
if(array[len(array)-1] != array[len(array)-2]):
    newArray.append(array[len(array)-1])

# DISPLAY NEW ARRAY
for k in range(0, len(newArray)):
    print(newArray[k], end="")
