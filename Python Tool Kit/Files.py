# 1) open
f = open("demofile.txt")
f2 = open("demofile.txt", "rt")  # r for read and t for text - it's the default
f3 = open("demofile.txt", "r")  # r for read, default value, opens a file for reading, error if the file does not exist
f4 = open("demofile.txt", "w")  # w for writing, creates the file if it does not exist
f5 = open("demofile.txt", "x")  # x is create - creates the specified file, returns an error if the file exists
f6 = open("demofile.txt", "a")  # a for appending, opens a file for appending, creates the file if it does not exist

# 2) read
f7 = open("demofile.txt", "r")
print(f7.read())
"""
Hello! Welcome to demofile.txt
This file is for testing purposes.
Good Luck! 
"""
f8 = open("demofile.txt", "r")
print(f8.read(5))  # "Hello"

fr = open("demofile.txt", "r")
print(fr.readline())  # "Hello! Welcome to demofile.txt"

fr2 = open("demofile.txt", "r")
print(fr2.readlines())  # ["Hello! Welcome to demofile.txt", "This file is for testing purposes.", "Good Luck!"]

# 3) Append and write: append will append to the end of the file and write will overwrite any existing content
f9 = open("demofile2.txt", "a")
f9.write("Now the file has more content!")
f9.close()
f10 = open("demofile3.txt", "w")
f10.write("Woops! I have deleted the content!")
f10.close()










