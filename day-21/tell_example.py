
# write operation

tell_example_file = open("./day-20/files/example_file.txt",'w+') # write and read
if (tell_example_file.writable()):
    tell_example_file.writelines([
        "This is line 1\n",
        "This is line 2\n",
        "This is line 3\n",
        "This is line 4\n",
        "This is line 5\n",
        "This is line 6\n",
        "This is line 7\n",
    ])

print (tell_example_file.tell())
# tell_example_file.close()
tell_example_file.seek(5)
print (tell_example_file.tell())

