# Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

# Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

# For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

# Function Description

# Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

# repeatedString has the following parameter(s):

# s: a string to repeat
# n: the number of characters to consider
# Input Format

# The first line contains a single string, .
# The second line contains an integer, .

# Constraints

# For  of the test cases, .
# Output Format

# Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

# Sample Input 0

# aba
# 10
# Sample Output 0

# 7
# Explanation 0
# The first  letters of the infinite string are abaabaabaa. Because there are  a's, we print  on a new line.

# Sample Input 1

# a
# 1000000000000
# Sample Output 1

# 1000000000000
# Explanation 1
# Because all of the first  letters of the infinite string are a, we print  on a new line.


def countRepeatLeatters(s):
    count = 0
    array = list(str(s))
    # print('string:', s)

    for elm in array:
        if(elm == 'a'):
            count = count + 1

    return count


def repeatedString(s, n):

    if(n % len(s) == 0):
        for index in range(1, n//len(s)):
            s = s + s

        print(s)
    else:
        reminder = n % len(s)
        # print('reminder:', reminder)
        additionalString = s
        additionalString = additionalString[0:reminder]
        # print('additonalstring: ', additionalString)
        finalString = ''
        for index in range(0, n//len(s)):
            finalString = finalString + s
            # print(index, finalString)
        finalString = finalString + additionalString
        # print(finalString)

        print('count:', countRepeatLeatters(finalString))


# repeatedString('aba', 10)

# def repeatedString(s, n):
#     s, n = input().strip(), int(input().strip())
#     print(s.count("a") * (n // len(s)) + s[:n % len(s)].count("a"))


# repeatedString('a', 1000000000000)
repeatedString('a', 20)
