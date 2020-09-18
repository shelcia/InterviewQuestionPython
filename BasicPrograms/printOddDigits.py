# Given a number N, print the odd digits in the number(space seperated) or print -1 if there is no odd digit in the given number.

number = int(input(''))
array = list(str(number))
flag = 0

for digit in range(0, len(array)-1):
    if(int(array[digit]) % 2 == 0):
        print(' ', end='')
    else:
        print(array[digit], end='')
        flag = flag+1

if(int(array[len(array)-1]) % 2 == 0):
    print('', end='')
else:
    print(int(array[len(array)-1]), end='')

if(flag == 0):
    print(-1)
