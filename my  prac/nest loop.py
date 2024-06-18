'''
1
1 2 
1 2 3 
1 2 3 4

'''
n=4
for i in range(1,n+1):#column
    for j in range(1,i+1):#row
        print(j,end=" ")
    print()

    
m=int(input("enter"))
for i in range(m):
    for j in range(m):
        print("*",end=" ")
    print()
