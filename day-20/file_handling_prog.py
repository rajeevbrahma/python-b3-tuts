import io
# # Open a file 

# Syntax:
# file_object = open(file_name, access_mode)
# #Example: 
# file_object = open("certificate.txt", "r+")

# try:
#     create_a_file = open("leave_letter.txt",'x') # create a file
# except FileExistsError:
#     file_name = input("Ooops file name exists give a new name - ")
#     create_a_file = open(file_name,'x') # create a file

# create_a_file = open("/day-20/files/leave_letter2.txt",'x')

# "day-20/files/txt_files/leave_letter.txt" - create a file with this path

try:
    # write operation
    write_to_a_file = open("./day-20/files/leave_letter.txt",'w') # write mode only

    print (write_to_a_file.writable())
    print (write_to_a_file.readable())
    write_to_a_file.seek(5)
    write_to_a_file.write("Leave Letter\n") # write to the file
    write_to_a_file.write("Sub: Requesting one day leave\n") # write to the file
    
    # write_to_a_file.read() # unsupported operation erro - uncomment to see
except FileNotFoundError:
    print ("OOPss File not found")
except io.UnsupportedOperation:
    print ("You have opened the file in write only mode")
finally:
    write_to_a_file.close()

# this content is not yet hard written

try:
    # write operation
    read_from_a_file = open("./day-20/files/leave_letter.txt",'r') # write mode only
    print (read_from_a_file.readable())
    
    if (read_from_a_file.readable()):
        # read_from_a_file.seek(0)
        print (read_from_a_file.read())

except FileNotFoundError:
    print ("OOPss File not found")

finally:
    read_from_a_file.close()

try:
    # write operation
    write_and_read_a_file = open("./day-20/files/leave_letter.txt",'a+') # write mode only
    
    print (write_and_read_a_file.readable())
    print (write_and_read_a_file.writable())
    
    # write_and_read_a_file.seek(0)
    if (write_and_read_a_file.writable()):
        write_and_read_a_file.writelines([
            "\nDear Sir,\n",
            "   I am not feeling well hence requesting a day off.\n\n"
            "Thank you\n\n"
            "regards\n"
            "Mark\n"
        ])

except FileNotFoundError:
    print ("OOPss File not found")
finally:
    write_and_read_a_file.close()


read_and_write_to_a_file = open("./day-20/files/leave_letter.txt",'r+') # write mode only

print (read_and_write_to_a_file.readline())
print (read_and_write_to_a_file.readline())
print (read_and_write_to_a_file.readline())
print (read_and_write_to_a_file.readline())

# print (read_and_write_to_a_file.readlines())



# exercise :
# Generate a certificate in the following format

# """
#                 Python Course Completion certificate
    
#                                     , has succesfully completed
#     online course PYTHON FOR BEGINEERS

#     This professional has demonstrated commitment to enhance their 
#     skills in advacing their career. Well Done..

#     Date : 
#     certificate code : 

# """
