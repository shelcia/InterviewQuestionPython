# Given a string, find the length of the longest substring without repeating characters.

# Example 1:
# Input: "abcabcbbdd"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

def subString(str):

    n = len(str)

    # Start pos of final string , length of final string
    start = 0
    max_length = 0

    visited_pos = {}

    current_start = 0
    current_length = 0

    for i in range(0, n):
        if(str[i] not in visited_pos):
            visited_pos[str[i]] = i

        else:
            if(visited_pos[str[i]] >= current_start):
                current_length = i - current_start

                if(max_length < current_length):
                    max_length = current_length
                    start = current_start

                current_start = visited_pos[str[i]] + 1

            visited_pos[str[i]] = i

    if(max_length < i - current_start):
        max_length = i - current_start
        start = current_start

    return max_length


print(subString("pwpancawckw"))
