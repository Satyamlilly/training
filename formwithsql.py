import sys
import mariadb
try: con = mariadb.connect( 

    user="root", 

    password="root", 

    host="localhost", 

    port=3306, 

    database="employees" 

)

except mariadb.Error as ex: 

    print(f"An error occurred while connecting to MariaDB: {ex}") 

    sys.exit(1) 
cur = con.cursor()
try:
    cur.execute("CREATE TABLE Details (Name VARCHAR(30),Surname VARCHAR(30),City VARCHAR(20), Age INT, Phone VARCHAR(20), Salary INT, Department VARCHAR(20))")
except Exception as a:
    print(a)
con.commit()


def nullchecker(x):
    if len(x)==0:
        return True
    else:
        return False

def numericcheck(y):
    if (y.isnumeric()):
        return True
    else:
        return False

def phonecheck(z):
    if (len(z)!=10):
        return True
    else:
        return False

def printandshow(a,b,c,d,e,f,g):
    #display
    deet1=("\nThe entered details are as follow\n")
    deet2=("Name:" +a +"\nSurname:"+b +"\nCity:"+c+"\nAge:"+d+"\nPhone:"+e+"\nSalary:Rs"+f+"\nDepartment:"+g)
    print(deet1+deet2)
    #writing
    file=open('details.txt','w')
    file.write(deet1+deet2)
    file.close()

def bonuscheck(m):
    if int(m)>=20000:
        bon=0.1*int(m)
        print("Hurray!! you earned a bonus on your salary of Rupees "+str(bon))

#for name input
name=input("your name\n")
while(nullchecker(name) or numericcheck(name)):
    name=input("enter correct name\n")

#for surname input
sname=input("your surname\n")
while(nullchecker(sname) or numericcheck(sname)):
    sname=input("enter correct surname\n")

#for city input
city=input("your city\n")
while(nullchecker(city) or numericcheck(city)):
    city=input("enter correct city\n")

#for age input
age=input("your age\n")
while(nullchecker(age) or not numericcheck(age) or int(age)<20):
    age=input("enter correct age\n")

#for phone input
phone=input("your phone\n")
while(nullchecker(phone) or phonecheck(phone) or not numericcheck(phone)):
    phone=input("enter correct phone\n")

#for salary input
salary=input("your salary\n")
while(nullchecker(salary) or not numericcheck(salary)):
    salary=input("enter correct salary\n")

#for department input
dep=input("your department\n")
while(nullchecker(dep) or numericcheck(dep)):
    dep=input("enter correct department\n")

#printing and display
printandshow(name,sname,city,age,phone,salary,dep)

#bonus checker
bonuscheck(salary)

cur.execute("INSERT INTO Details (Name,Surname,City,Age, Phone, Salary, Department) VALUES (?,?,?,?,?,?,?)",(name,sname,city,age,phone,salary,dep))
con.commit()