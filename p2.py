l=[1,2,3,4,5]
left=0
right=len(l)-1

while(left<right):
    temp=l[left]
    l[left]=l[right]
    l[right]=temp
    left=left+1
    right=right-1

print(l)    
