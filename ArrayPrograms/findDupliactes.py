# You are given an array of ids of prisoners.
# The jail authority found that there are some prisoners of same id.
M = int(input(""))
array = list(map(int, input().split(' ')[:M]))

for i in range(0, len(array)):
    for j in range(i+1, len(array)):
        if(array[i] == array[j]):
            print(array[i])
