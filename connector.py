import mysql.connector as sqltor
mycon = sqltor.connect(host='localhost', user='root', password='$S@tiRyz115$', database='aayush')
if mycon.is_connected():
    print("Connection established successfully")
cursor = mycon.cursor()
cursor.execute("SELECT * FROM skibidi")
data = cursor.fetchall()
count = cursor.rowcount
print(f"Total number of rows in skibidi table: {count}")
for row in data:
    print(row)
cursor.close()
mycon.close()
