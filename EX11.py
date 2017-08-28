print "How old are you ?"

## by default the output of raw_input is string

## so with the below I used int() function to convert the input into numbers

age = int(raw_input())

print "How tall are you ?"

height = float(raw_input())

print "How much do you weigh ?"

weight = float(raw_input())

# %d refer to integer
# %f refer to float number

print "So, you're %d years old, %f tall and %f heavy" %(
	   age, height, weight)