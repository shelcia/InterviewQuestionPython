# TO CHECK IF IT IS A SQUARE GIVEN FOUR POINTS
point1 = list(map(int, input().split(' ')[:2]))
point2 = list(map(int, input().split(' ')[:2]))
point3 = list(map(int, input().split(' ')[:2]))
point4 = list(map(int, input().split(' ')[:2]))
distance1 = (point1[0]-point2[0])**2 + (point1[1]-point2[1])**2
distance2 = (point3[0]-point4[0])**2 + (point3[1]-point4[1])**2
# print("(",point1, ")","(",point2, ")","(",point3, ")","(",point4, ")")
if(distance1 == distance2):
    print("yes")
else:
    print("no")
