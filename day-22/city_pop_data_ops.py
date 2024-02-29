# excercise 

# objective : 
# Get the total count of males in all the cities
# Get the total count of females in all the cities
# total child count

# Which city has more male pop 
# which city has more female pop

from csv import DictReader 

# step 1 - open the file

city_pop_data_file = open("./day-22/files/city_population_data.csv",'r')
if city_pop_data_file.readable():
    print ("We can perform operations")

    # step 2 - create a csv dictionary reader object
    city_pop_data_csv_reader_obj = DictReader(city_pop_data_file)
    # headers / fieldnames of the file
    print( city_pop_data_csv_reader_obj.fieldnames)


    # step 3 - business logic

    total_population = 0
    total_male_population = 0
    total_female_population = 0
    total_child_population = 0

    highest_male_population_city = None
    highest_male_population_count = 0

    for row in city_pop_data_csv_reader_obj:
        print ("---- Row Data ----")
        print (row["total_population"])
        print (row["male_population"])
        print (row["female_population"])
        print (row["child_population"])
        total_child_population += int(row["child_population"])
        total_female_population += int(row["female_population"])
        total_male_population += int(row["male_population"])
        total_population += int(row["total_population"])

        # 2 business logic
        if int(row["male_population"]) > highest_male_population_count:
            highest_male_population_city = row["city"]
            highest_male_population_count = int(row["male_population"])


    print ("----- RESULT ----")
    print (total_population)
    print (total_male_population)
    print (total_female_population)
    print (total_child_population)

    print ("---- RESULT ----")
    print ("Highest male population city")
    print (highest_male_population_city)

    