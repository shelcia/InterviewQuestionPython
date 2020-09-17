# TO CHECK IF IT IS A COMPOSITE NUMBER
N = int(input(""))
count = 0
# SRTICT DIVISION
for i in range(2, N//2):
    if(N % i == 0):
        count = count+1
if(count == 0):
    print("no")
else:
    print("yes")
