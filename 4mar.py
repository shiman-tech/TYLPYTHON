

def prime(n):
    
    for i in range(2,n):
        if  n%i==0:
            return 0
            
    
        
        return 1
        

lst=[1,2,3,4,5,6,7,8,9]
#l=list(filter(prime,lst))

#l=list(map(lambda x: x*x,lst))
#l=list(filter(lambda x: x%2==0 ,l))

lst=list(map(lambda x: x*x,filter(lambda x: x%2==0,lst)))
print(lst)


l=[x for x in range(1,5)]
print(l)

ll=[[0 for i in range(3)] for j in range(4)]
print(ll)

for i in ll:
    print(i)


for i in range(1,6):
    for j in range(1,7):
        print(i*j)
    print("\n")

ll=[[i*j for j in range(1,7)] for i in range(1,6)]   
print(ll)

word="python"
vowels="aeiou"

result=[char for char in word if char in vowels]
print(result)






