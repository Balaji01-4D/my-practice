a=[]
n=int(input("enter number of the element"))
for i in range(1,n+1):
    b=int(input("enter the elements"))
    a.append(b)

print(a)
x=int(input("enter the element you want to search:"))

found =False
for i in range(len(a)):
    if (a[i]==x):
        found=True
        print("%d found at the %dth postion"%(x,i))
        break
if (found==False):
    print("%d is not in list"%x)