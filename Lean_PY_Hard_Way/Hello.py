f = open("Results.txt", "w")

while True:
	Participant = raw_input("Participant Name is > ")

	if Participant == "quit" :
		print("Thank You")
		break

	Score = raw_input("the Score for " + Participant + " is > ")

	f.write(Participant + ", " + Score + "\n")

f.close()
