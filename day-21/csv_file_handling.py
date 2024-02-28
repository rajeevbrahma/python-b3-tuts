# comma seperated values

# s.no,name,email,qualification
# 1,X,x@gmail.com,+2
# 2,Y,y@gmail.com,Bachelors

csv_file = open("./day-21/files/basic_csv_file.csv","w+")

if (csv_file.writable()):
    csv_file.writelines([
        "s.no,name,email,qualification\n",
        "1,X,x@gmail.com,+2\n",
        "2,Y,y@gmail.com,Bachelors\n"
        "3,Z,z@gmail.com,+2\n",
        "4,U,u@gmail.com,Bachelors\n"
    ])

csv_file.seek(0)
print (csv_file.readlines())

# csv_data = csv_file.readline()

# print (csv_data)

# ['s.no,name,email,qualification\n',
#   '1,X,x@gmail.com,+2\n',
#     '1,Y,y@gmail.com,Bachelors\n'
# ]
    
csv_file.close() 


