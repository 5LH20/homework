import pymysql

db = pymysql.connect(host='192.168.0.178',user='root',password='kangkangbaobei1',database="5565")

cursor = db.cursor()

cursor.execute("select version()")

data = cursor.fetchone()

print(data)

cursor.execute("select * from sss")
results = cursor.fetchall()

for row in results:
    id = row[0]
    name = row[1]
    sex = row[2]
    department = row[3]
    position = row[4]
    salary = row[5]
    print("id = %s, name = %s, sex = %s, department = %s, position = %s, salary = %s" % (id, name, sex, department, position, salary))

sql = "insert into sss values (null, '%s', %s)" % ("五", 21)
try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

