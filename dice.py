import random

name1= raw_input("what is your name")

name2= raw_input("what is your name")

round = 0


def dicesum():

	return random.randint(1,6) + random.randint(1,6)

rollresult1 = dicesum()

rollresult2 = dicesum()

print (rollresult1, rollresult2)


if rollresult1 > rollresult2:
	print("name1 win")
elif rollresult2 > rollresult1:
	print("name2 win")
else:
	print("tie")
