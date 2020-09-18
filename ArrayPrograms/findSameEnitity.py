# Ramesh is a student and wants to find out if there is any other student
# in his class who has got the same marks as his, in maths.
# Help him to find out.
N = list(map(int, input().split(' ')[:2]))
# N[0] IS THE NUMBER OF STUDENT
array = list(map(int, input().split(' ')[:N[0]]))
count = 0

for index in range(0, len(array)):
    if(array[index] == N[1]):  # N1 IS THE MARK OF RAMESH
        count = count+1
        print(index)
if(count == 0):
    print(-1)
