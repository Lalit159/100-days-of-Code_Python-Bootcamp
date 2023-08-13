import random
from hangman_words import word_list
from hangman_art import stages, logo


print(logo)
print("Hello and Welcome to the HANGMAN GAME!! So nice to see you here")


def done(s):
    if('_' in s): return False
    return True    

n = len(word_list)
word = word_list[random.randint(0,n-1)]

count = 0

temp_word = []
for i in range(len(word)):
    temp_word.append('_')

guesses_letters = []    

while(count!=len(stages)):
    ch = input("Guess a character to check\n").lower()
    if(ch in guesses_letters):
        print("You already guessed this letter earlier. Try again")
    else:
        guesses_letters.append(ch)
        check = False

        for char in word:
            if(char==ch):
                check = True
                break

        if(check==False):
            print(stages[6-count])
            count+=1
            print("Your guess was incorrect")
            if(count!=7): 
                print(temp_word)
            else:
                print("You lost the game")    

        else:
            for i in range(len(word)):
                if(word[i]==ch):
                    temp_word[i] = ch

            print("Your guess was correct") 
            print(temp_word)
            if(done(temp_word)==True):
                print("You have WON this game. CONGRATS!!")    
                break;   
