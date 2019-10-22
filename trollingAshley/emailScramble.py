import random 

import sys


fileName = sys.argv[1]

try: 
    file = open(fileName, "r") 
 
except:
    print("invalid input file, program is going to terminate") 
    sys.exit()
 
lineList = [line.rstrip('\n') for line in file] 

#The entire email would ideally be a single string at this point
emailTxt = ''.join(lineList)

#Maybe we should worry about punctuation?
emailWords = emailTxt.split(' ')


def scrambleWord(word): 
    word = list(word)
    random.shuffle(word)
    return ''.join(word)

def middleScramble(word):
    if len(word) <= 2: 
        return word 

    mess = scrambleWord(word[1:-1])
    return word[0] + mess + word[-1] 


newWordList = [scrambleWord(word) for word in emailWords]

newEmail = ' '.join(newWordList)

newFile = open("newEmailForAshley.txt", "w")

newFile.write(newEmail)
