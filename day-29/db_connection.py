import mysql.connector as mysql
 
db = mysql.connect(host='localhost',   
                             user='root',
                             password='admin123',
                             database='db_p_3',
                             port=3306
                )

print (db)
print (db.is_connected())

# db.autocommit = True
# # # prepare a cursor object using cursor() method
# cursor = db.cursor(buffered=True)
# print(cursor)

# print (db.is_connected())
