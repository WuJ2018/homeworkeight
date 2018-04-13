import random

def roll(beginning,end):
	return random.randint(1,6)

def determineWinnerRound(rollresult1,rollresult2):
	if(rollresult1>rollresult2):
		return "player1"
	elif(rollresult1<rollresult2):
		return "player2"
	else:
		return "Draw, Roll again"

def determineWinnerScore(ScoreA,ScoreB):
	if(ScoreA>1):
		return "player1"
	elif(ScoreB>1):
		return "player2"
	else:
		return "nobody won"


beginning = 1
end = 6
rollrange1 =(beginning,end)
rollrange2 =(beginning,end)
ScoreA = 0
ScoreB = 0
rollresult1 = rollrange1
rollresult2 = rollrange2

GameRunning = 2


while(GameRunning>=0):
	rollresult1 = roll(beginning,end)
	rollresult2 = roll(beginning,end)
	roundWinner = determineWinnerRound(rollresult1,rollresult2)
	if(roundWinner == "player1"):
		ScoreA +=1
	elif(roundWinner == "player2"):
		ScoreB +=1
	else:
		roundWinner == "Draw,roll again"
	GameRunning-=1
	print(rollresult1, rollresult2,roundWinner)


gameWinner = determineWinnerScore(ScoreA, ScoreB)

if(gameWinner != "nobody won"):
	GameRunning = False
print(gameWinner)
