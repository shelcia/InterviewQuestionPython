# Alex works at a clothing store. There is a large pile of socks that must be paired by color for sale. Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
# For example, there are  socks with colors . There is one pair of color  and one of color . There are three odd socks left, one of each color. The number of pairs is .
# Function Description
# Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.
# sockMerchant has the following parameter(s):
# n: the number of socks in the pile
# ar: the colors of each sock
# Input Format
# The first line contains an integer , the number of socks represented in .
# The second line contains  space-separated integers describing the colors  of the socks in the pile.
# Constraints
#  where
# Output Format
# Return the total number of matching pairs of socks that Alex can sell.
# Sample Input
# 9
# 10 20 20 10 10 30 50 10 20
# Sample Output
# 3


# def sockMerchant(n, ar):
#     ar.sort()
#     print(ar)
#     occurance = 0
#     index = 0
#     count = 0
#     while(index < len(ar)-1):
#         print('index', index)
#         for j in range(index+1, len(ar)-1):
#             if(ar[index] == ar[j]):
#                 count = count+1
#                 if(count % 2 != 0):
#                     print(index, ar[index], j, ar[j])
#                     occurance = occurance + 1
#             else:
#                 index = index + count
#                 print(count)
#                 # count = 0
#                 break

#     return occurance


# # array = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# array = [1, 1, 3, 1, 2, 1, 3, 3, 3, 3]

# print('ans', sockMerchant(10, array))

# 1 1 3 1 2 1 3 3 3 3

def cntgloves(arr, n):

    # To store the required count
    count = 0

    # Sort the original array
    arr.sort()
    i = 0
    while i < (n-1):

        # A valid pair is found
        if (arr[i] == arr[i + 1]):
            count += 1

            # Skip the elements of
            # the current pair
            i = i + 2

        # Current elements doesn't make
        # a valid pair with any other element
        else:
            i += 1

    return count


# Driver code
if __name__ == "__main__":

    arr = [6, 5, 2, 3, 5, 2, 2, 1]
    n = len(arr)

    print(cntgloves(arr, n))
