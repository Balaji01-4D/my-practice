n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-3:
            print("*",end=" ")


        else:
            print(" ",end=" ")
    print()