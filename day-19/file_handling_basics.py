# What is file handling?
# File handling is the process of creating, reading, updating and deleting files.

# How to open a file?
# Python has a built-in open() function to open a file.


# chmod 777 file_name    (7)you(7)guest(7)group
# chmod 755 file_name

# 4 - read only             
# 2 - write only
# 1 - execute only
# 0 - no permission

# 7 - read, write and execute
# 6 - read and write
# 5 - read and execute
# 4 - read only
# 3 - write and execute
# 2 - write only
# 1 - execute only
# 0 - no permission


# Syntax:
# file_object = open(file_name, access_mode)
# #Example: 
# file_object = open("certificate.txt", "r+")

# Here are the different modes of opening a file:
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist.
# "a" - Append - Opens a file for appending, creates the file if it does not exist.
# "w" - Write - Opens a file for writing, creates the file if it does not exist.
# "x" - Create - Creates the specified file, returns an error if the file exists.

# rb - read in binary format
# r+ read and write
# rb+ read and write in binary format
# w - write only
# w+ - write and read
# wb - write in binary
# wb+ - writing and reading in binary
# a+ append
# ab+ append and read in binary
# x - create a file
# x+ - create and write to a file

