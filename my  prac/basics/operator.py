name,age,dob="balalji",8,"1/10/2005" #assignment operator
 
 
 #arthimetic operator
a=100
b=20

print(a-b,a+b,a*b,a/b,a%b,a//b,a**b,sep=('   ')) 


#comparison operator
print(a==b,a!=b,a<b,a>b,a<=b,a>=b,sep='  &  ')


#arguement operator
a+=b
print(a)
a+=a 
print(a)


a,b=b,a


#membership operator

an=[i for i in range(0,20,3)]
print(an)
print(9 in an)
print(9 not in an)

#logical operator(and,or,not)
a1=10
b1=13
statement1=(a1==b1)
statement2=(b1==13)
print(statement1 or statement2) #if 1 is true ouput is true
print(statement1 and statement2)#if must 2 true ouput is true
print(not(True))


#identity operator
a2=56
print(a2 is 56)


