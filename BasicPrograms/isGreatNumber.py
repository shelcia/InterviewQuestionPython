# You are given a number ‘n’. You have to tell whether a number is great or not.
# A great number is a number whose sum of digits let (m) and product of digits let(j)
# when summed together gives the number back
# m+j=n

n = list(map(int, input().split()))

n1 = n[0]
a = []
while n1 > 0:
    a.append(n1 % 10)
    n1 = int(n1/10)
add = 0
mul = 1
for i in range(0, len(a)):
    add += a[i]
    mul *= a[i]

res = add+mul

if(res == n[0]):
    print("Great")
else:
    print("no")
