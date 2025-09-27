st="([])"
flag=True
stack=[]
pair={')':'(','}':'{',']':'['}
for i in st:
    if i in "({[":
        stack.append(i)
    elif i in ")}]":
        if not stack or stack[-1]!=pair[i]:
            flag=False
            break
        else:
            stack.pop()
if flag==True:
    print("Valid")
else:
    print("Invalid")
