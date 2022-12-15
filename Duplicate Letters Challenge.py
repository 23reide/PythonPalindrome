#Write a function in Python to check duplicate letters. 
#It must accept a string, i.e., a sentence. 
#The function should return True if the sentence has any word with duplicate (double) letters, else return False.

#Get the sentence input
sentence = input("Enter a sentence:")

def checkLetters (sentence):
    #Assume the sentenceence has no duplicate letters
    duplicates = False

    sentence = [*sentence]
    j = 0
    for i in sentence:
        j+=1
        if(j == len(sentence)):
            #return True or False
            print(duplicates)
            #Restart
            sentence = input("Enter a sentence:")
            checkLetters(sentence)
        print(i, sentence[j])
        if (sentence[j] == i):
            duplicates = True
            #return True or False
            print(duplicates)
            #Restart
            sentence = input("Enter a sentence:")
            checkLetters(sentence)
#Run the program
checkLetters(sentence)