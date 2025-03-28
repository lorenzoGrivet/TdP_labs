import mysql.connector

cnx = mysql.connector.connect(user='root', host='127.0.0.1', password='password',database='test')

cursor = cnx.cursor()
query= """SELECT * 
FROM voti
WHERE id=2
"""
cursor.execute(query)
rows = cursor.fetchall()

for row in rows:
    print(row["nome"])

print(rows)
cursor.close()
cnx.close()