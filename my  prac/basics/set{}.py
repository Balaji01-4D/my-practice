s={1,2,3,5,6,'a'}
print(s,type(s))
#set is unordered and non repeative and hetrogenous

#adding an element
s.add(9)
print(s)



#removing an element
s.remove(2)


#hetrogenous data type adding a string
s.add('3')
print(s)


#true=1 & false=0
set1={2,3,4,1,0}
set1.add(True)
print(set1)

#set2 without o and 1 to print true and false
set2={2,3,4}
set2.add(False)
set2.add(True)
print(set2)

#conversion of list into set
a=[1,2,3,'hi']
sr=set(a)
print(type(sr))

#maths set function
seta={1,2,3,'a','b','c'}
setb={4,5,6,'a','d','e'}
print(seta.union(setb))#or print(seta|setb) #union function
print(seta.intersection(setb))#seta & setb
print(seta.difference(setb))  #seta-setb



#membership operator
print(1 in seta)

#loop functions
for i in seta:
    print(i)
    
