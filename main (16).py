import random as rn 
a=[]
for i in range (20):
    a.append(rn.randint(1,100))
    print("масив:",a)
    print(min(a))
    print(max(a))