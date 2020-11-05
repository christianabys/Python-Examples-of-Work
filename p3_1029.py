######Hangman Game
#Christian Abys
#function to convert list to string
def list_string(lst):   #define list to string conversion
    str1 = ""      #empty string
    for i in lst:  #for each element in list
        str1 += i  #add each element to the string
    return(str1)   #return
import random                           #import packages
repeat = 'Y'                            #repeat will first equal yes to start program
while repeat == 'Y':                    #while repeat equals Y
    words = ['write','that','program']  #words
    sel_word = random.choice(words)     #select word
    char = list(sel_word)               #seperate selected string word into characters in a list
    word_comp = list_string(char)       #call function to convert list back to a string
    blank_ast = '*' * len(char)         #get asterisk blanks
    letter_list = []                    #create letter list
    count = 0                           #initalize count
    while blank_ast != word_comp:                           #run loop while blank_ast does not equal word comp
        letter = input("Here is the current world: {}\nEnter a letter to make a guess: ".format(blank_ast))
        if letter in letter_list:                           #if letter already exists print letter is already a word
            print(letter,"is already a word")
        if letter not in char:                              #if letter is not in char list
            count += 1                                      #add to count if missed
            print(letter,"is not in the word")              #print to user
        else:
            for i in range(len(char)):                      #Replace blanks with correctly guessed letters
                    if char[i] in letter:                   #if the letter equals an element [i] in char
                        blank_ast = blank_ast[:i] + char[i] + blank_ast[i+1:]      #add letter to the appropiate element
                        letter_list.append(letter)              #store guessed letter=
    else:
        print("The word is",blank_ast,".","You missed",count,"time(s)")    #display results 
        repeat = input("Do you want to guess another word? Enter Y or N: ") #ask if user wants to repeat
