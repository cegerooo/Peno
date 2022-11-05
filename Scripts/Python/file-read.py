#!/usr/bin/python3

f = open("file.txt", "r")

for line in f:
    print(line)

myData = "I'm sample data to be written to a file"

f = open("data.txt", "a")
f.write(myData)

f.close()

