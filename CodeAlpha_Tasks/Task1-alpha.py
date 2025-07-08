import random

#List of words to choose from
list_of_words = ["codealpha","internship","python","program"]

#Randomly selects a word from the given list
word_to_guess = random.choice(list_of_words)
guessed_letters = []
#Number of allowed wrong guesses
guess_limit=6

#Creating a display format of the word (with underscore)
word_to_display = ["_" for _ in word_to_guess]

print(" WELCOME TO HANGMAN !!! ")
print(" Guess the Word , One Letter at a Time.")

#Main loop

while guess_limit > 0 and "_" in word_to_display:
    print("\n Word: ", " ".join(word_to_display))
    print(f"Guessed Letters: {', '.join(guessed_letters)}")
    print(f"Remaining Guessing Limits: {guess_limit}")

    guess = input("Enter a letter: ").lower()

    #Check if the input is valid
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabetical letter.")
        continue
    #Check if the letter was guessed already
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        # Reveal the guessed letter in the word_to_display
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                word_to_display[i] = guess
        print("Your Guess is Correct !")
    else:
        guess_limit-=1
        print("Wrong Guess. Try again..")

# Game Ending Messages
if "_" in word_to_display:
    print("\n GAME OVER ! The Word Was : ", word_to_guess)
else:
    print("\n CONGRATULATIONS ! You Have Guessed the Word : ", word_to_guess)
