import sys 

fileName = sys.argv[1]

oldLetter = sys.argv[2]
newLetter = sys.argv[3]

#Making sure that they are strings
oldLetter = str(oldLetter) 
newLetter = str(newLetter) 

try: 
    file = open(fileName, "r") 

except: 
    print("invalid input file, program is going to terminate") 
    sys.exit() 


lineList = [line.rstrip('\n') for line in file]

#Should make the entire email into a single list 
emailTxt = ''.join(lineList) 

def swapLetter(emailText, oldLetter, newLetter):
    dummyLetter = "9"
    emailText = emailText.replace(oldLetter, dummyLetter) 
    emailText = emailText.replace(newLetter, oldLetter)
    emailText = emailText.replace(dummyLetter, newLetter)
    return emailText

#newEmail = replaceLetter(emailTxt, oldLetter, newLetter)
newEmail = swapLetter(emailTxt, oldLetter, newLetter)

print(newEmail)

newFile = open('newEmailFromAshely.txt', 'w')
newFile.write(newEmail)

#newFile.close()
