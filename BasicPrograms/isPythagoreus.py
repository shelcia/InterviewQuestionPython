# CHECKING PYTHAGOREUS CONDITION
N = list(map(int, input().split(' ')[:3]))

if(N[2]**2 == (N[1]**2+N[0]**2)):
    print("yes")
elif(N[1]**2 == (N[2]**2+N[0]**2)):
    print("yes")
elif(N[0]**2 == (N[1]**2+N[0]**2)):
    print("yes")
else:
    print("no")
