t=(1,2,3)
t1=('a','b')
t=t+(4,)
print(t)


print(t*2)

t2=t+t1
print(t2),                                      

print(t[-40:3])  #-40 doesnt exist so it will start from 


a=(10,20)
b=(10,20)
c=(20,10,30,40)

print(a==b)

print(c<a) #it compares the first element from both the tuples

l,m,n,o=c
print(f"{l},{m}")


l,*m= c
print(l)
print(m)
print(*m)

*l,m,n=c   # there are 3 variables so one for m and one for n and the left out elements will go to l
print(l)

del a
print("hello")
#print(a)  #error occurs here since a doesnt exist anymore

print(max(c))
print(min(c))