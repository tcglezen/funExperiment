#The format of the email should be 
#command, target, numSwaps, destination




#The spirit of the scramble is to constantly swap letters in the email (e with k, w with g, etc) 

import sys 

#Name of file that we are going to alter 
fileName = sys.argv[1]  

#Number of swaps that we are going to preform 
numSwaps = int(sys.argv[2])

#If last argument of call exists, it is the destination 
if len(sys.argv) >= 4: 
	dest = sys.argv[3] 

else: 
	dest = "newEmailForAshely.txt" 



try: 
	file = open(fileName, "r") 

except: 
	print("invalid input file, program is going to terminate") 
	sys.exit() 


############################################################################

import random as r 

lineList = [line.rstrip('\n') for line in file] 

#Merge email into single list 
emailTxt = ''.join(lineList) 

emailTxt = emailTxt.lower() 

def randomSwap(emailText):
	#Obtain the ascii numbers 
	num1 = r.randint(97, 122) 
	num2 = r.randint(97, 122)

	#Convert them into letters
	letter1 = chr(num1)
	letter2 = chr(num2)

	for i in range(len(emailText)): 
		if emailText[i] == letter1: 
			emailText[i] = letter2
			#print("letter 2 got swapped!")  
		elif emailText[i] == letter2: 
			emailText[i] = letter1 
			#print("letter 1 got swapped!") 

	return emailText 

emailText = list(emailTxt) 
for i in range(numSwaps): 
	emailText = randomSwap(emailText)

result = "".join(emailText) 


newFile = open(dest, 'w') 
newFile.write(result) 

newFile.close()	
