

#max- appraoch1
l=[] 
for i in range(3):
    print("Enter no.",i+1,":")
    l.append(int(input()))

print("max= ",max(l))  


a=int(input("Enter no. 1:"))
b=int(input("Enter no. 1:"))
c=int(input("Enter no. 1:"))


#max - approach2
max= a if(a>c and a>b) else b if(b>c and b>a) else c    
print(max)


#factorial - appraoch1
sum=1
d=int(input("enter a no.: "))
for i in range(1,d+1):
    sum=sum*i
print(sum)    

#factorial - approach 2 (RECURSION)



#armstrong no.
n=int(input("Enter a number:"))
r=0
temp=n
sum=0
while(n>0):
    rem=n%10
    sum=sum+rem**len(str(temp))
    n=n//10

if(sum==temp):
    print("its a armstrong no.")
else:
    print("its not a armstrong no.")  







