largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    try:
        num = int(num)
        if(largest == None):
            largest = num
        else:
            if(largest < int(num)):
                largest = int(num)
        if(smallest == None):
            smallest = num
        else:
            if(smallest > int(num)):
                smallest = int(num)
    except:
        print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)
