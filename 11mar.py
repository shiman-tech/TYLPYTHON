t1=(4,3)
t2=(1,2)

tres=t1+t2
print(tres)
l=list(tres)
print(l)
l.sort()
l=tuple(l)
print(l)

flag=1
lb=0
ub=len(l)-1
while(lb<ub):
    if(l[lb]!=l[ub]):
        flag=0
    lb=lb+1
    ub=ub-1


if(flag==1):
    print("its a palindrome") 
else:
    print("its not a palindrome")    
    

t3=t1[::-1]    
if(t1==t3):
    print("its a palindrome")
else:
    print("its not a palindrome")    


s=("hello","gaming","is")

max=s[0]
for i in s:
    if(len(i)>len(max)):
        max=i
print(max)  

print(len(max))

t=""
tup=['a','b']
for i in tup:
    t=t+i

print(t)


       



