import mysql.connector as c
con=c.connect(host="localhost",
user="root",
password="Ir@m2604",
database= "employee")
cursor=con.cursor()
while True:
    # code=int(input("Enter the employee code:"))
    # name=input("Enter the name:")
    # salary=int(input("Enter the salary:"))
    # query="insert into employee values ({},'{}',{})".format(code,name,salary)
    query="select name from employee"

    
    cursor.execute(query)
    con.commit()
    print("data inserted ")
    x=int(input(("1->Enter more\n2->Exit\nEnter chice ")))
    if x == 2:
        break
# choice=int(input)
