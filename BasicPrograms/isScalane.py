# Given 3 numbers A,B,C print 'yes' if they can form the sides of a scalene triangle else print 'no'.

sides = list(map(int, input().split(" ")[:3]))
count = 0
for i in range(1, len(sides)):
    if(sides[0] == sides[i]):
        count = count+1
if(count == 0):
    print("yes")
else:
    print("no")
