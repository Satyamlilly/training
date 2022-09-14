name=input("your name\n")
age=input("your age\n")
phone=input("your phone\n")

if(len(name)!=0):
    print("correct age")
else:
    print("enter correct name")
if(int(age)>18 and age.isdigit()):
    print("correct age")
else:
    print("enter correct age")
if(len(phone)==10 and phone.isdigit()):
    print("correct phone")
else:
    print("enter correct phone")