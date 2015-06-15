def printMenu():
	print '*' * 56
	print '*'+(" " * 54)+"*"
	print "*****************Welcome to Psyquiz*********************"
	print "******Test your knowledge on Psytrance Music!!!*********"
	print '*'+(" " * 54)+"*"
	print '*' * 56

tunes = {
	"Berg" : "Stranger to Yourself",
	"Block Device" : "The Earth, the Moon, the Sun",
	"Maitika" : "Human Sight",
	"Liquid Soul and Zyce" : "Science Fiction",
	"Zyce and Aquafeel" : "Dark Side"
}

def generateQuestion(tunes):
	ans = ""
	score = 0
	for key in tunes:
		ans = raw_input("Who is the artist of: " + tunes[key] + " ?\n")
		if ans == key:
			score += 1
		else:
			print "Haa Haa. Wrong."
	if score == 5:
		print "Congratulations, You got 5/5!! You definitely know your shit!"
	elif score == 4:
		print "Sweet, you got 4/5."
	elif score == 3:
		print "Okay you got 3/5. Not bad."
	elif score == 2:
		print "2/5. Go listen to some more psytrance."
	else:
		print score + "/5. You probably listen to Justin Bieber"

printMenu();
generateQuestion(tunes);
