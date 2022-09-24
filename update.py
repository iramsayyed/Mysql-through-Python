import mysql.connector as c
con=c.connect(host="localhost",
user="root",
password="Ir@m2604",
database= "employee")
cursor=con.cursor()
code=int(input("Enter the code "))
salary=int(input("Enter new salary "))
query="update employee set salary={} where code={}".format(salary,code)
cursor.execute(query)
con.commit()
print("updated")


    
