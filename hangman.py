from random_word import RandomWords

print("Let's play Hangman!")
print("-----")

playing = True

while playing == True:

    word = RandomWords().get_random_word()

    for lives in range(6):
        print("Lives left: " + str(6 - lives))
        guess = input("Guess a letter:\n")
        
        if len(guess) > 1:
            print("Not a valid guess. Please enter a single letter.")
        else:    
            for letter in guess:
                if letter in word:
                    print("Correct!")
                else:
                    print("Incorrect!")
