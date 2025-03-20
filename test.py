import numpy as np
from collections import defaultdict

s='hello'
s1='lloeh'

if(list(s).sort()==list(s1).sort()):
    print("its a anagram")
s2=''

for i in s:
    s2=s2+i
print(s2)   

res="".join(s)
print(res)

'''arr=np.array([[1,2,3],
             [4,5,6],
             [7,8,9]])
print(arr.T)

rarr=np.flip(arr)
print(rarr)'''

l1=[1,2,3]
l2=['a','b','c']
l3=list(zip(l1,l2))
print(l3)

#transpose of a matrix
matrix=[[1,2,3],
        [4,5,6],
        [7,8,9]]
l=list(map(list,zip(*matrix)))
print(l)

for i in l:
    i.reverse()

print(l)    

for i in range(len(matrix)):           
    for j in range(i+1,len(matrix)):    
        matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

print(matrix)       


#default dictionaries : setting the value of keys as lists

strs = ["eat","tea","tan","ate","nat","bat"]
d=defaultdict(list)
d["hello"].append(3)
d["hello"].append(5)
print(d)
print(dict(d))



#keypad sequence
keypad=['0','.','abc','def','ghi','jkl','mno','pqrs','tvu','wxyz']

digits='777 7266'
sequence=''
for i in range(len(digits)):
    digit=digits[i]
    if((i!=0 and digit==digits[i-1]) or digit==' ' ):
        continue
    
    
    idx=int(digit)-int('0')
    count=0
    for j in range(i+1,len(digits)):
        if( j < len(digits) and digit==digits[j] ):
            count=count+1

    sequence=sequence+keypad[idx][count]      

print(sequence)    

year=1900
r=True if((year %4==0 and year%100!=0) or (year%400==0) ) else False
print(r)


l=[10,20,30,40,50,60]
k=",".join(map(str,l))
print(k)


for i in range(5):
    for j in range(i+1):
        print('*',end="")
    print("")   


def pattern(n):
    if(n==0):
        return
    print('*'*n)
    pattern(n-1)


pattern(5) 

def pattern1(n,i):
    if(n==0):
        return
    
    print(' '*i+'*'*n)
    pattern1(n-1,i+1)


pattern1(5,0)


def pattern2(row,star,space):

    if(star==row):
        return
    
    print(' '*space+"*"*(2*star+1))
    pattern2(row,star+1,space-1)


    
row=5 
pattern2(row,0,row-1)


l=['*'* i for i in range(1,6)]
for i in l:
    print(i)





     








                                










