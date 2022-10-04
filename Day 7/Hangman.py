import random
import hangman_words
import Hangman_art


print(Hangman_art.logo)

# wordList = ["Variables", "Functions", "Python", "Object", "Class", "Typecasting", "Operators"]
'''
numberOfWords= len(wordList)                                
chosenWord_index= random.randint(0,numberOfWords-1)
chosenWord =  (wordList[chosenWord_index]).lower()          
'''    
#above is a longer way to choose random string from the list
lives = 6

chosenWord = random.choice(hangman_words.wordList).lower()
#testing code
# print(f"the choosen word is {chosenWord}")
display =[]
wordLength = len(chosenWord)
for letter in range(wordLength):                #loop to display same number of _ as the character in chosen word
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    userGuess = input("Guess the letter: ").lower()
    if userGuess in display:                    #condition to tell user that he has already used this word and present in the display
        print(f"You have alreay guess the letter {userGuess}")
    for position in range(wordLength):          #loop to change the _ to letter is userGuess is right
        letter = chosenWord[position]
        if letter == userGuess:
            display[position] = letter
    
    if userGuess not in chosenWord:             #loop for game lose
        lives -= 1
        print(f'You have guess the letter {userGuess}, which is not in the word, You lose 1 life')
        if lives == 0:
            end_of_game = True
            print("You lose.")
    if "_" not in display:                      #loop for game win
        end_of_game = True
        print("You Win")
    print(f"{' '.join(display)}")               #Join all the elements in the list and turn it into a String.

    print(Hangman_art.stages[lives])
    


