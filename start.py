x=int(input())
y=int(input())
z=int(input())
if x<y and y>z:
    print(y)
elif x<y and y<z:
    print(z)
else:
    print(x)