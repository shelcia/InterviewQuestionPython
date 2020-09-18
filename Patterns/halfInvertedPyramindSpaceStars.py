#   ****
#  ****
# ****
# ****


N = int(input(''))
if(N % 2 == 0):
    for index in range(0, N):
        for secondIndex in range(0, N+(N-1-index)):
            if(secondIndex <= N//2-index):
                print(' ', end='')
            else:
                print('*', end='')
        print('')
else:
    for index in range(0, N):
        for secondIndex in range(0, N+(N//2+1)+1 - index):
            if(secondIndex <= N//2-index+1):
                print(' ', end='')
            else:
                print('*', end='')
        print('')
