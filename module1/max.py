def maximum(numbers):
    maxi=numbers[0]
    for i in numbers:
        if maxi < i:
            maxi=i
    print(maxi)