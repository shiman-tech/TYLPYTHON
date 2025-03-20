'''a=int(input("a:"))
b=int(input("b:"))

a=a+b
b=a-b
a=a-b

print("a=",a," b=",b)'''


d={'Shiman':1,'Lingesh':2,'Akshay':2,'Babuboi':3}
sorteditem=sorted(d.items(),key=lambda x: (-x[1],x[0]))
print(sorteditem)

key,value=sorteditem[0]
print(key,value,sep=',')


