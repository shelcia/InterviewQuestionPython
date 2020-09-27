# Find the contiguous subarray within an array, A of length N which has the largest sum.
# Asked in Facebook, Goldman sachs, Google, Paypal, Yahoo, Microsoft, Amazon, LinkedIn

# Input Format:

# The first and the only argument contains an integer array, A.

# Return an integer representing the maximum possible sum of the contiguous subarray.

# Input 1:
#     A = [1, 2, 3, 4, -10]

# Output 1:
#     10

# Explanation 1:
#     The subarray [1, 2, 3, 4] has the maximum possible sum of 10.

# Input 2:
#     A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

# Output 2:
#     6

# Explanation 2:
#     The subarray [4,-1,2,1] has the maximum possible sum of 6.

# Kadane’s Algorithm:

def maxSubContagiousArray(array):
    max_so_far = 0
    max_ending_here = 0

    for index in range(0, len(array)):
        max_ending_here = max_ending_here + array[index]
        if(max_so_far < max_ending_here):
            max_so_far = max_ending_here
        if(max_ending_here < 0):
            max_ending_here = 0
    return max_so_far
    print('')


a = [-2, -3, 4, -1, -2, 1, 5, -3]
print("Maximum contiguous sum is", maxSubContagiousArray(a))
