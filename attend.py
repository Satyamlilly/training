from lib2to3.pgen2.token import SLASHEQUAL


sal=[1,2,3,4,5,6,7]
a=int(input("number of emp"))
for x in range(a):
    sal[x]=int(input("enter"))
for x in range(a):
    if sal[x]>=10000:
        sal[x]+=(0.1*sal[x])
        print(sal[x])
    else:
        print(sal[x])