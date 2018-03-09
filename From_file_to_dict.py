f = open("Results.txt", "r")

participants = {}

for i in f:
	entry = i.strip().split(",")
	Name = entry[0]
	score = entry[1]
	participants[Name] = score

f.close()

print(participants)