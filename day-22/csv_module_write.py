import csv # importing csv module which has all the methods specially designed to operate
# on the csv files.


#    h1[r1[     b1[  c1[ (P) f1,f2],f3]  b2[f4] ]]

# colony ,streetname, house number 

# city, colony, streetname, housenumber

# state, city, colony, streetname, housenumber 

# country, state, city, streetname, housenumber 



# objective:  create a file and write some tabular into the file
"""
    file_name - city_population_data.csv

    s.no, city, total_population, male_population,female_population,child_population
     1      x        127398923       27837423        273949             27323

"""


file_path = "./day-22/files/city_population_data.csv"

try:
    city_pop_data_csv_file = open(file=file_path,mode='x').close()
except FileExistsError:
    print ("Thats ok we are learning")

city_pop_data_csv_file = open(file=file_path,mode='w')

# using basic file handling method
if city_pop_data_csv_file.writable():
    print ("We can write something to the file")
    city_pop_data_csv_file.writelines([
        "s.no, city, total_population, male_population,female_population,child_population\n"
        "1,X,1000,400,300,300\n",
        "2,Y,1500,500,300,700\n",
    ])
city_pop_data_csv_file.close()

# using csv writer method
city_pop_data_csv_file = open(file=file_path,mode='w')

city_pop_data_csv_writer_obj = csv.writer(city_pop_data_csv_file)

city_pop_data_csv_writer_obj.writerow([
    "s.no", "city", "total_population", "male_population","female_population","child_population"     
])

city_pop_data_csv_writer_obj.writerows([
    [1,"X",1000,400,300,300],
    [2,"Y",1500,500,300,700]
])

city_pop_data_csv_file.close()

# using csv Dictionary Writer method 
city_pop_data_csv_file = open(file=file_path,mode='w')

city_pop_data_csv_dict_writer_obj = csv.DictWriter(
    city_pop_data_csv_file,
    fieldnames=[
        "s.no", "city", "total_population", "male_population","female_population","child_population"
])


city_pop_data_csv_dict_writer_obj.writeheader()

city_pop_data_csv_dict_writer_obj.writerow(
    {"s.no":1,"city":"X","total_population":1000,
     "male_population":400,"female_population":300,"child_population":300
    }
)

city_pop_data_csv_dict_writer_obj.writerows([
        {
            "s.no":2,"city":"Y","total_population":900,
            "male_population":370,"female_population":270,"child_population":240
        },
        {
            "s.no":3,"city":"Z","total_population":950,
            "male_population":380,"female_population":290,"child_population":260
        }
    ]
)

city_pop_data_csv_file.close()
