from sys import exit

def tiger_room():
	print "There's a tiger in here!"
	print "It's lying in front of the next door."
	print "Will you yell at it or rub its belly?"
	
	# how to incorporate "or sing it a song?"
	
	next = raw_input("> ")
	if "yell" in next or "Yell" in next:
		die("You scared the tiger and it bit you. You lose.")
	
	elif "rub" in next or "Rub" in next:
		print "Tigers love a good belly rub."
		print "You become friends."
		gold_room()
	
	else:
		die("You took too long and the tiger ate you")
		
	
# figure out third branch and put it here. Where else could the story go?	
	#else :
		#print "

def gold_room():
	print "How will you choose to enter the last door?"
	print "Will you hop on the back of your new tiger friend and ride in style?"
	print "Or, will you walk through the door side by side?"
	
	while True:
	
		next = raw_input ("> ")
		if "ride" in next or "Ride" in next:
			print "Oh no! Why would you try to ride a tiger??!"
			print "You've made a fatal mistake in your new friendship."
			die("The tiger bites you and keeps the treasure for himself. You lose")
	
		elif "walk" in next or "Walk" in next:
			print "You did it! The room is filled with long lost pirate treasure and"
			print "Tiger Snax. You and your new friend split the treasure and live"  
			print "happily ever after."
			next == False
			exit(0)
	
		else:
			print "I wasn't sure what you selected. Will you ride or walk?"
		

def wizard_room():
	print "There's a wizard in the room blocking your access to the next door."
	print "To pass, you must answer three questions:"
	print "What is your name?"
	
	next = raw_input("> ")
	print "You're a natural, %s" % next
	
	print "What is your favorite color?"
	
	next2 = raw_input("> ")
	
	print "What is the airspeed velocity of an unladen swallow?"
	
	next3 = raw_input("> ")
	if "African" in next3 or "European" in next3 or "42" in next3:
		print "You did it, %s! You may pass" % next
		portal_room()
		# how to make the answer not case sensitive?
		# You can just convert the string into lower or uppercase for comparison. Like this example:
		#string1 = 'Hello'
		#string2 = 'hello'
		#
		#if string1.lower() == string2.lower():
		#    print "The strings are the same (case insensitive)"
		#else:
		#    print "The strings are not the same (case insensitive)"
		
	else:
		die("You answered incorrectly and are turned into a newt.")

def portal_room():
	print "You open the door to find a portal giving you access to all space and time."
	print "What will you do??"
	print ["A. 'Whole lot of nope. I'm going back to the left door.'", 
	"B. Stare into the void.", "C. Step through."]
	
	# list isn't printing right, also not being used as a list
	
	next = raw_input("> ")
	
	if "A" in next or "a" in next: # how to make "a" also work?
		tiger_room()
	
	elif "B" in next or "b" in next:
		print "You stare into the void so long, you either go crazy or achieve a state \
		 of zen, whichever comes first."
		die("You lose the game, but win at life. Namaste.")
	
	else:
		time_travel()

def time_travel():
	print "Would you like to travel into the near past, far past or teleport out of \
	 this crazy room?"
	
	next = raw_input("> ")
	
	if "near" in next:
		die("Phew! You went back in time 5 minutes before you ever started this silly \
		 game. It's like it never happened.")
	
	elif "far" in next:
		die("You went back too far! An oblivious dinosaur accidentally steps on you. \
		 You're squashed.")
	
	else: 
		print "You won! You teleported right to the treasure room. All the gold \
		 is yours!"
		exit(0)
	
	# needs a do not understand option in case one of the three choices isn't selected


#This is how the game exits
def die(why):
	print why
	exit(0)

#This is where the game actually starts

def start():
	print "You wake up in a room with two doors."
	print "Will you go through the door on the left or right?"
	
	#try making a one letter input as an acceptable command. You could ask like this:  
	#
	#print "Will you go through the door on the [l]eft or [r]ight?"
	#
	#next = raw_input("> ")
	#if "l" in next or "left" in next:
	#	tiger_room()
	#elif "r" in next ot "right" in next:
	
	next = raw_input("> ")
	if next == "left":
		tiger_room()
	elif next == "right":
		wizard_room()
	else:
		print "You must choose one of the doors. There's no other way out"
		print "and you forgot to bring snacks."
		
start()	


#Need to figure out where to incorporate a list



