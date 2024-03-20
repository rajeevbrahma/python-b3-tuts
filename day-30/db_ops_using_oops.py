import mysql.connector as mysql
# objective - create db crud ops class

# scope - connect to db, reconnect to db, close the connection
class Database:
    
    def __init__(self,host,user,password,database,port):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.db_connection = None
        self.db_cursor = None

    def connect(self):
        self.db_connection =  mysql.connect(host='localhost',   
            user='root',
            password='admin123',
            database='db_p_3',
            port=3306
        )
        self.db_connection.autocommit = True
        if (self.db_connection.is_connected()):
            print (f"Connected to database - {self.database}")
        self.db_cursor = self.db_connection.cursor() 

    def reconnect(self):
        self.db_connection.reconnect()
        if (self.db_connection.is_connected()):
            print (f"Reconnected to database - {self.database}")
    
    def disconnect(self):
        self.db_connection.close()

        if (not self.db_connection.is_connected()):
            print (f"Disconnected from database - {self.database}")


# scope - create doc, update doc, read doc, read all, delete
class DbOps(Database):
    
    def __init__(self,host,user,password,database,port,table):
        super().__init__(host,user,password,database,port)
        self.table = table

    def create(self,document):
        create_string = f"INSERT INTO {self.table} \
            (account_number,name, password,balance) VALUES \
                {document['account_number'],document['name'],document['password'],document['balance']};"
        print (create_string)
        self.db_cursor.execute(create_string)

    def read(self,doc_id):
        pass 

    def read_all(self):
        read_all_query = f"SELECT * FROM {self.table}"
        self.db_cursor.execute(read_all_query)
        return self.db_cursor.fetchall()

    def delete(self,doc_id):
        pass

    def update_name(self,doc_id,name):
        pass
    
    def update_password(self,doc_id,password):
        pass 

    def update_balance(self,doc_id,balance):
        pass



db = DbOps('localhost','root','admin123','db_p_3',3306,'user')
db.connect()
db.disconnect()
db.reconnect()
# db.create(
#     {
#         "name":"John",
#         "password":"john@123",
#         "account_number":268342734,
#         "balance":2839423.2
#     }
# )
print (db.read_all())
