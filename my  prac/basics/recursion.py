#funtion calling itself is called recursion
def sum_of_n(n):
    #base case
    if (n==1):
        return 1

    #recursive case
    print(n)
    return n+sum_of_n(n-1)
print(sum_of_n(1))
