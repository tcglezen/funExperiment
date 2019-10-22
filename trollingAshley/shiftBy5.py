import sys 

fileName = sys.argv[1] 

try: 
    file = open(fileName, "r") 

except: 
    print("Invalid input file, program is going to terminate") 
    sys.exit() 

lineList = [line.rstrip('\n') for line in file] 

#Merge email into a single string 
emailTxt = ''.join(lineList) 

#Partition it into each word
emailList = emailTxt.split(' ') 

def shift(word, shift = 5): 
    newWord = [chr(ord(letter) - 5) for letter in word]
    return ''.join(newWord) 
    return newWord

emailList = [shift(word) for word in emailList]

newEmail = ' '.join(emailList) 

newFile = open("ghettoEmail.txt", "w") 

newFile.write(newEmail) 


