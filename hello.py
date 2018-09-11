import random 

print("1 is rock, 2 is paper, 3 is scissors")
userMove = int(input())

rand = random.randint(1,3)
print("You:", userMove)
print("Computer:", rand)

def comp_rock():
	if userMove==1:
		print("It's a tie")
	elif userMove==3:
		print("You win")
	elif userMove==2:
		print("You lose")
	else:
		print("INVALID INPUT")
		# maybe needed comp_rock()

def comp_paper():
	if userMove==2:
		print("It's a tie")
	elif userMove==1:
		print("You win")
	elif userMove==3:
		print("You lose")
	else:
		print("INVALID INPUT")
		# maybe needed comp_paper()

def comp_scissors():
	if userMove==3:
		print("It's a tie")
	elif userMove==2:
		print("You win")
	elif userMove==1:
		print("You lose")
	else:
		print("INVALID INPUT")
		# maybe needed comp_scissors()

if rand==1:
	comp_rock()
elif rand==2:
	comp_paper()
else:
	comp_scissors()




