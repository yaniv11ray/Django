import mysql.connector
from mysql.connector import  errorcode

config = {
  'user': 'root',
  'password': 'Vinay2022!',
  'host': '127.0.0.1',
  'database': 'yaniv',
  'raise_on_warnings': True
}
cnx=mysql.connector.connect(**config)

#cnx=mysql.connector.connect(user='root',password='Vinay2022!',host='localhost',database='yaniv')
cursor = cnx.cursor()
sql=("SELECT e.employeename as employeename ,d.departmentname as departmentname FROM yaniv.employee as e ,yaniv.department as d where e.departmentid=d.departmentid;")
query=sql
#query = ("SELECT EMPNO, FIRSTNME, MIDINIT, LASTNAME FROM EMPLOYEE LIMIT 5 ")


cursor.execute(query)

print(' ----------------------------------------------|')
#print(d=cursor.execute(query))
print("\U0001F600")

for (employee_name, department_name) in cursor:
    if len(employee_name) > 10:
        raise ValueError ('\U0001F600  \N{smiling face with sunglasses}, value is more than 4')
    print(f"{employee_name}, {department_name}")
print('----------------------------------------------|')

cursor.close()
cnx.close()
