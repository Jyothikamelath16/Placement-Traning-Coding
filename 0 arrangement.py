ls=[2,0,4,3,0,7,0,6,7,0,3]
n=len(ls)
for i in range(n):
    if ls[i]==0:
        ls.remove(0)
        ls.append(0)
print(ls)
