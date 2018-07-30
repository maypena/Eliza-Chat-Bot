# May Pena
# This is an AI bot with comprehensive responses for emotinal support.
# It responds to mention of family members and also reads into
# wether the user is saying positive things or negative things
# and provides a canned answer based on that. 

import random

canned = [ "\nPlease tell me more.",
           "\nI see...",
           "\nI am listening...",
           "\nPlease go on.",
           "\nThank you for sharing that."]

nCanned = [ "No?",
            "Really?",
            "You are awfully negative!",
            "Why not?",
            "You are being very negative today!",
            "We need to work on your pessimism!",
            "Don't be so negative, think of chocolate!"]

# This makes Eliza say hello 
def greetings():
    print(  "Welcome.  Please tell me of your problems: " )
    print( '(You may quit at any time by answering "bye")' )

# This helps Eliza find family keywords
def findFam( answer ):
    family = ['father','brother','son','sister','daughter','mother', 'cousin']
    for member in family:
        if answer.lower().find( member ) != -1:
            return True
        
# This tells Eliza the replacements for keywords she can reflect 
def reflection( words, newWords ):

    for i in range(len(words)):
        if words[i] == "I":
            newWords[i] = "you"

        if words[i] == "i":
            newWords[i] = "you"
            
        if words[i] == "me":
            newWords[i] = "are"

        if words[i] == "my":
            newWords[i] = "your"

        if words[i] == "me":
            newWords[i] = "you"
            
        if words[i] == "i've":
            newWords[i] = "you've"
            
        if words[i] == "i'm":
            newWords[i] = "you're"
            
        if words[i] == "i'll":
            newWords[i] = "you'll"
            
        if words[i] == "was":
            newWords[i] = "were"
            
        if words[i] == "mine":
            newWords[i] = "yours"

        if words[i] == "you":
            newWords[i] = "I"
            
        if words[i] == "your":
            newWords[i] = "my"
            
        if words[i] == "yours":
            newWords[i] = "mine"
            
        if words[i] == "you're":
            newWords[i] = "I'm"
            
        if words[i] == "you'll":
            newWords[i] = "I'll"
            
        if words[i] == "were":
            newWords[i] = "was"
            
        if words[i] == "you've":
            newWords[i] = "I've"
            
        if words[i] == "are":
            newWords[i] = "am"

    sentence = " ".join(newWords) + "?"
    return sentence

# This tells Eliza the answer for negative keywords
def pessimism( newWords ):
    for word in newWords:
        if word in [ "no", "not", "niet", "never", "can't", "hate" ]:
            sentence =  random.choice( nCanned )
            return sentence


# This function checks for relfection keywords in the user's answer
def checkRef( newWords ):
    for word in newWords:
        if word in ["I", "i", "are", "you've", "were", "you'll", "you're",
                    "yours", "your", "you", "my", "mine", "was",
                    "I'll", "I'm", "I've", "am","me"]:
            return True
    return False

# This function checks for pessimism in the user's answer
def checkPessi( newWords ):
    for word in newWords:
        if word in [ "no", "not", "niet", "never", "can't", "hate" ]:
            return True
    return False

'''
                      _
                     (_)      
      _ __ ___   __ _ _ _ __  
     | '_ ` _ \ / _` | | '_ \ 
     | | | | | | (_| | | | | |
     |_| |_| |_|\__,_|_|_| |_|
'''
       
def main():
    greetings() # greet and start the problem

    for i in range( 10000 ):  
        answer = input( "\n> " ).lower().strip()
        words = answer.split( )
        newWords = []

        for word in words:
            newWords.append( word )

        if answer == "bye" : # this ends the program 
            break

        elif findFam( answer ): # if family was mentioned, give family answer
            print( "Tell me more about your family." )
            continue

        elif checkRef( newWords) == True: # check if the user has said something that can be reflected
            sentence = ( reflection( words, newWords ) )
            canned.append("Is that why " + sentence.lower())
            print( sentence )
            continue

        elif checkPessi( newWords ) == True: # check to see if there is pessimism
            sentence2 = ( pessimism( newWords) )
            print( sentence2 )
            continue
        
        else: # if no other condition is met, say a canned answer
            print( random.choice( canned ) )
            continue
                    
     
main()
