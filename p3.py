l=[]
n=int(input('Enter the range: '))
for i in range(n):
    l.append(int(input("enter the element: ")))

'''for i in range(0,4):
    for j in range(0,5-1-i):
        if(l[j]<l[j+1]):
          temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp'''

#approach 1

'''l.sort(reverse=True)

print(l[1])'''


#approach 2

first=second= l[0]

for num in l:
    if(num>first):
        second=first
        first=num


    elif(first>num>second):
        second= num


print(second)        





