number=int(input('enter number'))
binary=[]
x=""
while number:
    y=number%2
    binary.append(y)
    number=number //2
binary.reverse()
for i in binary:
    x=x+str(i)
print(x)
