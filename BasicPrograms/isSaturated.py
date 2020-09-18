# You are provided with a number ’n’. Your task is to tell whether that number is saturated. A saturated number is a number which is made by exactly two digits.

number = int(input(''))
array = list(str(number))
flag = 0

firstNumber = array[0]
for index in range(1, len(array)):
    if(firstNumber != array[index]):
        secondNumber = array[index]
        # print(secondNumber)
        break
for index in range(1, len(array)):
    if(array[index] != firstNumber and array[index] != secondNumber):
        # print(firstNumber,array[index],secondNumber)
        flag = flag+1
        break

if(flag == 0):
    print('Saturated')
else:
    print('Unsaturated')
