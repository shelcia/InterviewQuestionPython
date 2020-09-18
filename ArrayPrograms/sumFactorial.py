# You are given a very long integer.Your task is to determine the
# smallest possible number such that sum of factorial of digits results back in ‘n’.
# Print -1 if no number is possible

N = str(input(""))


def factorial(number):
    mul = 1
    for index in range(1, int(number)+1):
        mul = mul*index
    return(mul)


sum = 0
count = 0
result = 0
for index in range(0, int(N)+1):
    arrayOfIndex = list(str(index))
    sum = 0

    for secondIndex in range(0, len(arrayOfIndex)):

        sum = sum+int(factorial(arrayOfIndex[secondIndex]))
#         print("index: " ,index,arrayOfIndex, sum)
        if(sum == int(N)):
            #             print("result: ",arrayOfIndex)
            result = index
            count = 1
            break
    if(count == 1):
        break


if(count != 1):
    print(-1)
else:
    print(result)
