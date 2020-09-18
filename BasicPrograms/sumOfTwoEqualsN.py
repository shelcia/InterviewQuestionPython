# You are given with a number ‘n’. You have to count the pair of two numbers a and b such that sum of two numbers are equal to n.


N = int(input(''))

count = 0
for firstNumber in range(0, N):
    for secondNumber in range(0, N):
        if(firstNumber+secondNumber == N):
            # print('(',firstNumber,secondNumber,')')
            count = count+1

print(count)
