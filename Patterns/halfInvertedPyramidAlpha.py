# Write a code to generate a aplhabet half pyramid pattern.


# Program to find # Program to find the ASCII value of the given character

# c = 'p'
# print("The ASCII value of '" + c + "' is", ord(c))
# print(chr(65))

N = int(input(''))
for row in range(0, N):
    for count in range(0, N-row):
        print(chr(65+N-count-1), end='')
    print('')
