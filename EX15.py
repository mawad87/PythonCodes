# in the below code we are opening and read txt file in 2 different ways

from sys import argv

script, filename = argv 

txt = open(filename)

print "Here's your file %r:" % filename

print txt.read()

print "Type the filename again:"

file_again = raw_input("> ")

txt_again = open(file_again) 

print txt_again.read()

# From the above open(txt file name) to open a txt file in python
# [filename/variable].read to read the txt file
