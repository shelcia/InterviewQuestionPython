
def countChar(string):
    array = list(string)
    index = 0
    finalString = ''
    while(index < len(array)-1):
        for j in range(index, len(array)-1):
            if(array[j] == array[j+1]):
                print(array[j], j)
            else:
                index = index + j
                print('index'. index)
                break
    # while(index < len(array)-1):
    #     print('index', index)
    #     count = 1
    #     for j in range(index, len(array)-1):
    #         if(array[j] == array[j+1]):
    #             print(count, array[j])
    #             count = count + 1
    #         else:
    #             finalString = finalString + str(array[j]) + str(count)
    #             index = index + j
    #             break
    print(finalString)


countChar('aaabbbcccaaa')
