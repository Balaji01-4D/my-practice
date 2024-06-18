arr=[1,2,3,4,5,6,7,8]
odd=[]
for i in arr:
    if i%2==1:
        odd.append(i)
        
print(odd)

even=[i for i in arr if i%2==0]
#arr=[item to added{space}where is i{space}condition]
print(even)


hundred=[i for i in range(1,101)]
print(hundred)

seta={1,2,3,4,5,6,7,8,9,'q'}#converting set into list
lista=[i for i in seta]
print(lista)

threediv=[i for i in hundred if i%3==0]
print(threediv)