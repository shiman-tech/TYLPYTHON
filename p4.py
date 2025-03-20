a=10
result= 'greater than 10' if a>10 else 'lesser than 10' if a<10 else 'equal to 10'
print(result)

l=[1,2,3,4,5,6]
ll=['c','a','b']
res=[x for x in range(10 )]
print(res)

res1=[x if x%2==0 else x*-1 for x in range(10)]
print(res1)

l.append(7)
print(l)

l.insert(0,0)
print(l)

l.extend([8,9])
print(l)

l.remove(9)  #value as a parameter 
print(l)

print(l.pop(8))  #index as a parameter

l.sort(reverse=True)
print(l)

ll.sort()
print(ll)

l.reverse()
print(l)

ll.reverse()
print(ll)

print(ll.index('b'))

lt=l.copy()
print(l)
print(lt)

lst=[1,2,3,4,4,4,2]
print(lt.count(2))  #index as a parameter

print(max(lst))
print(min(lst))





