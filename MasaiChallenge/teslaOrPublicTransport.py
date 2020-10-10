# Tesla or Public transport
# Problem
# Submissions
# Leaderboard
# Discussions
# You have just received your new Tesla, the problem with this model of tesla is that it just goes from one tesla station to another only (not between stations). Assume that you are currently on station s. The tesla has only two buttons, marked "UP u" and "DOWN d". UP-button takes the tesla u stations up(ahead) (if there aren't enough stations, pressing the UP-botton does nothing, or at least so you assume), whereas the DOWN-button takes you d stations down/back (or none if there aren't enough).

# Assume that you need to go to station g, and that there are only f stations in the city, you quickly decide to write a program that gives you the amount of button pushes you need to perform.

# If you simply cannot reach the correct station, your program halts with the message "use public transport".

# Given input f, s, g, u and d, find the shortest sequence of button presses you must press in order to get from s to g or output "use public transport" if you cannot get from s to g by the given tesla.

# Input Format

# The input will consist of one line, namely f s g u d, where 1 <= s, g <= f <= 1000000 and 0 <= u, d <= 1000000. The stations are one-indexed, i.e. if there are 10 stations, s and g be in [1; 10].

# Constraints

# 1 <= s, g <= f <= 1000000

# 0 <= u, d <= 1000000

# Output Format

# You must reply with the minimum numbers of pushes you must make in order to get from s to g, or output "use public transport" if it is impossible given the configuration of the tesla.

# Sample Input 0

# 10 1 10 2 1
# Sample Output 0

# 6
