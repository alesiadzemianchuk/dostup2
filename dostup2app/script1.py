
import sqlite3
from sqlite3 import Error

path = 'D:\Python\pythonProject\pythonProject9\dostup2\db.sqlite3'

try:
    conn = sqlite3.connect(path)
    print("connect to DB ")
except Error as e:
    print("Could not connect to DB using given credentials")

id = 16
cur = conn.cursor()
sql1 = """SELECT 'ФИО', e.name_ru FROM orders as o 
join employee as e on o.employee_id=e.id
WHERE o.id='%(id)s'
union all
select 'Отдел', d.name from orders as o 
join department as d on o.employee_id=d.id
WHERE o.id='%(id)s'
union ALL
select 'Телефонная связь', case WHEN o.Телефонная_связь='1' then 'V' else 'X' end
FROM orders as o
WHERE o.id='%(id)s' 
 """ % {'id': id}
result = cur.execute(sql1)

rows = cur.fetchall()


with open("1.xls", 'w') as file:
    for x in rows:
        print(x)
        file.write(str(x) + '\n')


conn.close()
