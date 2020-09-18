# Assume that you are ticket verifier at a club.
# Your club has decided to give a special discount to the person(s) who are satisfying
# the following condition
# Condition:-If ticket number is divisible by date of month. You are eligible for a discount

validity = []


def verifyTicket(array, date):
    for index in range(0, len(array)):
        if(array[index] % date == 0):
            validity.append(1)
        else:
            validity.append(0)
    return validity


N = int(input(""))
array = list(map(int, input().split(' ')[:N]))
date = int(input(""))

# print(verifyTicket(array,date))
valditedArray = verifyTicket(array, date)

for index in range(0, len(valditedArray)):
    if(index == len(valditedArray)-1):
        print(valditedArray[index], end="")
    else:
        print(valditedArray[index], end=" ")
