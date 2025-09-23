num_input=int(input("Enter the number "))
num=num_input
rslt=0
temp=0
length=len(str(num_input))
for i in range(length):
    rslt=(num%10)**length
    num=num//10
    temp+=rslt
print(temp)
if (temp==num_input):
    print("The number is an armstrong")
else:
    print("The number is not an armstrong")
