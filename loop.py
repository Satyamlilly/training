name=input("your name\n")
while(len(name)==0 or (name.isdigit())):
    name=input(" enter correct name\n")
sname=input("your surname\n")
while(len(sname)==0 or (sname.isdigit())):
    sname=input(" enter correct surname\n")
age=int(input("enter age\n"))
while(age<20):
        age=int(input("enter correct age\n"))
phone=input("enter phone\n")
while(len(phone)!=10 or (not phone.isdigit())):
    phone=input("enter correct phone\n")
city=input("your city\n")
while(len(city)==0 or (city.isdigit())):
    city=input(" enter correct surname\n")
salary=(input("your salary\n"))
while(not salary.isdigit()):
    salary=input("enter correct salary\n")
print("Details below\n")
print(name)
print(sname)
print(age)
print(phone)
print(salary)