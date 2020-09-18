# Given 3 numbers A,B,C print 'yes' if they can form the sides of a right angled triangle,otherwise 'no'.

N = list(map(int, input().split(' ')[:3]))

if(N[2]**2 == (N[1]**2+N[0]**2)):
    print("yes")
elif(N[1]**2 == (N[2]**2+N[0]**2)):
    print("yes")
elif(N[0]**2 == (N[1]**2+N[0]**2)):
    print("yes")
else:
    print("no")
