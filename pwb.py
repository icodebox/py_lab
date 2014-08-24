import os
import random

def cointoss():
	
	if (random.randint(0,1) == 0):
		return "H"
	else:
		return "T"
	
def main():
	
	answer = 'y'
	result = ''
	Beauty, Player = 0, 0
	
	print("Playing with Beauty v 0.0.1")
	
	while(1):
		flips = input("Please enter count of flips: ")
		if (flips.isdigit() != True):
			continue
		else:
			flips = int(flips)
			break
				
	while(flips > 0):
		for i in range(2):
			result=result+cointoss()
		if(result == "HH"):
			print (result)
			print("Player wins!")
			Player+=1
		elif(result == "TT"):
			print (result)
			print("Player wins!")
			Player+=1
		else:
			print (result)
			print("Beauty wins!")
			Beauty+=1
		result = ''
		flips-=1
	print("Score: Player-"+str(Player)+" vs Beauty-"+str(Beauty))
			
main()
