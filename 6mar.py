list1=[1,2,3,4,5]
list2=[4,5,6,7,8]

res=[x for x in list1 if x in list2]
print(res)


words=["hello","world","python"]

res1=[ x[::-1] for x in words]
res1.reverse()
print(res1)

numbers=[1,2,3,4,5,6,7,8,9,10]
res2=list(filter(lambda x: x%2==0,numbers))
print(res2)

res3=[i for i in range(1,51) if i%3==0 and i%5==0]
print(res3)

words1=["hello","world","python","list"]
res4=[x.upper() for x in words1]
print(res4)