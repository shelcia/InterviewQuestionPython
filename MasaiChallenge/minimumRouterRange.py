# Minimum Router Range
# Problem
# Submissions
# Leaderboard
# Discussions
# There are N houses in a straight line i.e, on X-axis and K routers whose signal has to reach the entire road of houses All routers have some strength , which denotes the range of signal that it can cover in both the directions.

# The router's strength should not be wasted unnecessarily ,so we have to keep its range minimum.

# Find the minimum range of strength of all , utilising all the given routers such that all houses can receive it.

# Input Format

# The first line contains two integers, N and K - denoting the number of houses and number of routers. The next line contains N integers denoting the position of the houses in the straight line.

# Constraints

# 1 <= N <= 10^5

# 1 <= K < N

# 1 <= Positioni <= 10^7

# Output Format

# Print the minimum range in a new line.

# Sample Input 0

# 3 2
# 1 5 20
# Sample Output 0

# 2
# Explanation 0

# The optimal answer is 2.

# A router positioned at 3, can serve houses at 1 and 5.

# The other router can be placed at 18, to serve house at 20.
