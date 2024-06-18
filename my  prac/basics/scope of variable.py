def add():
    global a#modify the global variable inside the function
    a=a+b
    
    print(a+b)


a=10
b=12
print(a,b)
add()
print(a,b)#modified a will be printed here
