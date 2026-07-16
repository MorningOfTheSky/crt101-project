
333
#things to add: documentation, better visuals or something maybe ascii idk

import random


with open("words_alpha.txt", "r") as f:
    words = [w.strip().lower() for w in f]

print("Let's play Hangman!!!")
print("-----")



lives = 6
secret = random.choice(words)
guessed = ["_"] * len(secret)
wrong_letters = []


while lives > 0:
    print("Lives:", lives)
    print("Word:", " ".join(guessed))
    print("Wrong letters:", ", ".join(wrong_letters))

    letter = input("Guess a letter please: ").lower()

    if letter in secret:
        for i, ch in enumerate(secret):
            if ch == letter:
                guessed[i] = letter
    else:
        if letter not in wrong_letters:
            wrong_letters.append(letter)
        lives -= 1
        print("INCORRECT")

    if "_" not in guessed:
        print("Congrats! You found the correct word:", secret)
        break

if "_" in guessed:
    print("Sorry you lose! The secret word was:", secret)