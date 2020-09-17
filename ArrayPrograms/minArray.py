# The Romans have attacked again. This time they are much more than the Persians but Shapur is ready to defeat them. He says: 'A lion is never afraid of a hundred sheep'.

# Nevertheless Shapur has to find weaknesses in the Roman army to defeat them. So he gives the army a weakness number.

# In Shapur's opinion the weakness of an army is equal to the number of triplets i, j, k such that i < j < k and ai > aj > ak where ax is the power of man standing at position x. The Roman army has one special trait — powers of all the people in it are distinct.

# Help Shapur find out how weak the Romans are.

# The first line of input contains a single number n, the number of men in Roman army. Next line contains n different positive integers powers of men in the Roman army.

def minimum(array):
    min = array[0]
    for i in range(1, len(array)):
        if(min > array[i]):
            min = array[i]
    return(min)


N = int(input(""))
array = list(map(int, input().split(" ")[:N]))
if(array[0] > array[1] > array[2]):
    print(minimum(array))
else:
    print(0)
