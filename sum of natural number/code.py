def sum_of_natnum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

n = 10  # Change this value to the desired number of natural numbers
print("The sum is:",sum_of_natnum(n))
