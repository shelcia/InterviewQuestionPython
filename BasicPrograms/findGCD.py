# FINDING GREATEST COMMON DIVISOR
def gcd(a, b):
    if(b == 0):
        return a
    else:
        return gcd(b, a % b)


N = list(map(int, input().split(' ')[:2]))

if(N[0] == 0 or N[1] == 0):
    print(-1)
else:
    print(abs(gcd(N[0], N[1])))
