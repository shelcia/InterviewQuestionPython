# Given a number N and an array of N elements ,find the Bitwise AND of the array elements.
# result=0
def bitwiseand(array, N):
    result = array[0]
    for i in range(1, N):
        result = result & array[i]
#         print(result)
    return result


N = int(input(""))
array = list(map(int, input().split(' ')[:N]))
print(bitwiseand(array, N))
