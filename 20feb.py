#write a python program to check whether a given number is prime number or not 
n=int(input("enter the number:"))
if n>1:
    for i in range (2,(n//2)+1):
        if(n%i==0):
            print("not prime number")
        else:
            print("prime number")
else:
    print("not prime number")