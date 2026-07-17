"""
Hangman Game

By: Anay Mediwala, Kyle Arnold, Jayvant Rajesh
"""

#import the random module to select a random word from the list of words
import random

#Read in the words from the file and store them in a list
with open("words_alpha.txt", "r") as f:
    words = [w.strip().lower() for w in f]

#Introduce the game to the player
print("\n---------------------")
print("Let's play Hangman!!!")
print("---------------------")

playing = True

#Overarching game loop, check if the player wants to play again after each game
while playing:
    
    #Initialize game variables
    lives = 6
    secret = random.choice(words)
    guessed = ["_"] * len(secret)
    wrong_letters = []

    #Game loop, runs until the player runs out of lives or guesses the word
    while lives > 0:
        print("\nLives:", lives)
        print("Word:", " ".join(guessed))
        print("Wrong letters:", ", ".join(wrong_letters))

        letter = input("Guess a letter please: ").lower()

        #Check if the input is valid, if not, ask for a new letter
        if letter.isalpha() == False or len(letter) != 1:
                print("Please enter a valid letter.")
                continue
        

        #Check if the letter has already been guessed, if so, ask for a new letter
        else:
            
            #Check if the letter has already been guessed, if so, ask for a new letter
            if letter in guessed or letter in wrong_letters:
                print("You have already guessed that letter, please try again.")
                continue

            #Check if the letter is in the secret word, if so, update the guessed list, if not, add to wrong letters and decrement lives
            if letter.lower() in secret:
                
                #Update the guessed list with the correct letter
                for i, ch in enumerate(secret):
                    if ch == letter:
                        guessed[i] = letter
            
            #If the letter is not in the secret word, check if it has already been guessed incorrectly, if not, add to wrong letters and decrement lives
            else:
                
                #Check if the letter has already been guessed incorrectly, if not, add to wrong letters and decrement lives
                if letter not in wrong_letters:
                    wrong_letters.append(letter)
                lives -= 1
                print("INCORRECT")

        #Check if the player has won
        if "_" not in guessed:
            print("Congrats! You found the correct word:", secret)
            break
    
    #Check if the player has lost
    if "_" in guessed:
        print("Sorry you lose! The secret word was:", secret)

    #Ask the player if they want to play again and proceed accordingly
    play_again = input("Do you want to play again? (yes/no): ").lower();

    #Check if the input is valid, if not, ask for a new response
    while play_again != "yes" and play_again != "no":
        print("Please enter a valid response.")
        play_again = input("Do you want to play again? (yes/no): ").lower();

    #If the player does not want to play again, set playing to False and print a message, otherwise print a separator
    if play_again != "yes":
        playing = False
        print("Thanks for playing!")

    #If the player wants to play again, print a separator
    elif play_again == "no":
        print("-----\n")
