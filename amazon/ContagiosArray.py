# Find the contiguous subarray within an array, A of length N which has the largest sum.

def findContagious(arr):
    max_sum = arr[0]
    start_ptr = 0
    final_ptr = 1
    current_sum = arr[0]
    print('arr', arr)
    i = 1
    while (i < len(arr)):
        current_sum = current_sum + arr[i]
        if(current_sum > max_sum):
            print('sums', current_sum, max_sum, start_ptr, final_ptr)
            max_sum = current_sum
            final_ptr = i + 1
        else:
            start_ptr = i
            final_ptr = i
        i = i + 1
    # for i in range(1, len(arr)):
    #     current_sum = current_sum + arr[i]
    #     if(current_sum > max_sum):
    #         max_sum = current_sum
    #         final_ptr = i + 1
    #     else:
    #         start_ptr = i
    #         final_ptr = i

    print('max sum', max_sum)
    print(arr[start_ptr: final_ptr])


if __name__ == '__main__':
    arr = [-2, -3, 4, -1, -2, 1, 5, -3]
    findContagious(arr)
