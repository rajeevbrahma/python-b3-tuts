import csv # we have excel specific operations defined in this module 

# Dict - Dictionary format

# csv methods

# seek()        # sets the file's current position to the number specified
# tell()        # returns the file's current position
# close()       # closes the file

# writer()      # returns a writer object which is used to write to the csv file
# reader()      # returns a reader object which is used to read from the csv file

# writeheader() # writes the fieldnames as the first row

# writerow()    # writes a row to the csv file
# writerows()   # writes multiple rows to the csv file

# DictWriter()  # returns a DictWriter object which is used to write to the csv file
# DictReader()  # returns a DictReader object which is used to read from the csv file

# headers - will be your keys
# Row - will be the values

# {
#     "s.no":1,
#     "name":"X",
#     "email":"x@gmail.com",
#     "qualification":"+2"
# }



# line_num      # gives the line number

csv_file = open('./day-21/files/basic_csv_file.csv','r') # opened a csv file in read mode

csv_reader = csv.reader(csv_file) # creating a reader object for the csv file that we have opened
for row in csv_reader:
    print (row)

# we read all the rows in the csv and
# by this time the cursor is at the end of your file
# to read the contents again we have move the cursor to the beginning of the file

csv_file.seek(0)

csv_dict_reader = csv.DictReader(csv_file)
print (csv_dict_reader)

for row in csv_dict_reader:
    print (row)








# [
#     's.no,name,email,qualification\n', # each row is in the format # str

#     '1,X,x@gmail.com,+2\n', 
    
#     '2,Y,y@gmail.com,Bachelors\n', 
    
#     '3,Z,z@gmail.com,+2\n', 
    
#     '4,U,u@gmail.com,Bachelors\n'
# ] 


['s.no', 'name', 'email', 'qualification'] #each row in the format of list and 

['1', 'X', 'x@gmail.com', '+2']

['2', 'Y', 'y@gmail.com', 'Bachelors']

['3', 'Z', 'z@gmail.com', '+2']

['4', 'U', 'u@gmail.com', 'Bachelors']   # list

# each row is represented in the dictionary format
# each dictionary consists of key value pairs
# key - column header, values - row element

{'s.no': '1', 'name': 'X', 'email': 'x@gmail.com', 'qualification': '+2'}
{'s.no': '2', 'name': 'Y', 'email': 'y@gmail.com', 'qualification': 'Bachelors'}
{'s.no': '3', 'name': 'Z', 'email': 'z@gmail.com', 'qualification': '+2'}
{'s.no': '4', 'name': 'U', 'email': 'u@gmail.com', 'qualification': 'Bachelors'}




# city data 

# city_name, population, is_capital, male_pop, female_pop, zipcode, child_population

# 10 values

# now read from the above created csv file 
# 1. using basic file handling read methods
# 2. using csv module reader methods
# 3. using csv module DictReader method

# now give me total population
# now give me the total female population
# give me total male population 

# Tell whose population is more 






