import mysql.connector as mysql



# create connection - create cursor - do operations - close the connection

db_config = {
    "table":"user"
}
# creating connection
db = mysql.connect(host='localhost',   
                             user='root',
                             password='admin123',
                             database='db_p_3__2',
                             port=3306
                )

print (db)
print (db.is_connected())
# db.autocommit = True

# creating cursor
# # prepare a cursor object using cursor() method
cursor = db.cursor()
print(cursor)

# CRUD OPERATIONS

# Create document
create_string = f"INSERT INTO {db_config['table']} (account_number,name, password,balance) VALUES (123456791,'user4','pasd1',8293.23);"

cursor.execute(operation=create_string)
db.commit()

# Read documents
read_query = "SELECT * FROM user;"
# execute the query
cursor.execute(read_query)
print (cursor)
# read from the cursor
rows = cursor.fetchall() # will give me all the rows and columns in the table
print (rows)

# Read document
read_query = f"SELECT * FROM user where id={7};"
# execute the query
cursor.execute(read_query)
print (cursor)
# read from the cursor
row = cursor.fetchone() # will give me all the rows and columns in the table
print (row)

# update document
update_query = f"UPDATE {db_config['table']} set name='Mark',password='mark@123' where id=7;"
# execute the query
cursor.execute(update_query)
db.commit()

db.close()

# Delete document



# project - 

# create table with the following schema
# country_name, population, capital, continent, finance_capital
# 1. Insert as many countries as possible for each continent
# 2. Get me all the countries from Africa, Asia, Europe, South America
# 3. Get me all the countries which has population more than 10 crore
# 4. Get me countries with poulation between 5 to 10 cr



# [ mac: os - [Docker : DC1 [LINUX/WINDOWS[mysql(8.2)]],
#              DC2 [LINUX/WINDOWS[mysql(8.3)]] ]   ]

# 8.2

# 8.3

# 8.4




[windows: windows os [mysql server, workbench] ]




