

def binomialCoefficient(n, k):
    # since C(n, k) = C(n, n - k)
    if(k > n - k):
        k = n - k
    # initialize result
    res = 1
    # Calculate value of
    # [n * (n-1) *---* (n-k + 1)] / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return int(res)


def printPascal(n):

    # Iterate through every line
    # and print entries in it
    for line in range(0, n):

        # Every line has number of
        # integers equal to line
        # number
        for i in range(0, line + 1):
            print('[', line, i, ']', binomialCoefficient(line, i),
                  " ", end="")
        print()
    # k = 2
    # res = binomialCoefficient(n, k)
    # print("Value of C(% d, % d) is % d" % (n, k, res))


# Driver program to test above function
if __name__ == "__main__":
    printPascal(8)
