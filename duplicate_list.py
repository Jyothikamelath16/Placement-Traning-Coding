ls=[1,2,3,2,4,3]
s=[]
for i in ls:
    a=ls.count(i)
    if a!=1:
        s.append(i)
print(list(set(s)))
