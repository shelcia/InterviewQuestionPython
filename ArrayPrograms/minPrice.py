# Your old mobile phone gets broken and so you want to purchase a new smartphone and decide to go through all the online websites to find out which dealer has the best offer for a particular model. You document the prices of N dealers. Dealer ids start from 0 and go up to N.  Find out which dealer has the best price for you.

N = int(input(''))
array = list(map(int, input().split(' ')[:N]))

min = array[0]
result = 0
for index in range(1, N):
    if(min > array[index]):
        min = array[index]
        result = index

print('Dealer'+str(result))
