# Print the count of all palindromic numbers till ‘n’(inclusive)

N = int(input(''))


def palindrome(number):
    reversedNumber = list(str(number))
    # print('first  ',reversedNumber)
    reversedNumber.reverse()
    # print('second   ',reversedNumber)
    returnNumber = ''
    return(returnNumber.join(reversedNumber))


count = 0
for number in range(1, N+1):
    # print(number ,'palindrome  ',palindrome(number))
    if(number == int(palindrome(number))):
        count = count+1
print(count)
