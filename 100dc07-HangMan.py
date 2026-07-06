import random
words_list = ["javascript"]

word_to_guess = random.choice(words_list)


print(word_to_guess)

for letter in word_to_guess:
    print("_", end=" ")
print("\n\n\nWelcome to Hangman!")

word_guessed = False
attempts_left = 6
guessed_letters = [""]*len(word_to_guess)

while not word_guessed:
    print("Guessed letters: {guessed_letters}".format(guessed_letters=guessed_letters))

    print("Guess a letter:")
    guess = input().lower()
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    if guess in word_to_guess:
        for index,letter in enumerate(word_to_guess):
            print("letter in word_to_guess: {letter}".format(letter=letter))
            print("Your guess: {guess}".format(guess=guess))

            if letter == guess:
                guessed_letters[index] = guess
            else:
                if ((guessed_letters[index] == '' or guessed_letters[index] == '_')): 
                    guessed_letters[index] = "_"
    else:   
        attempts_left -= 1
        print("You have {attempts_left} attempts left".format(attempts_left=attempts_left))
    
    
    if attempts_left == 0:
        print("You lost! The word was: {word}".format(word=word_to_guess))
        break
    if all(letter in guessed_letters for letter in word_to_guess):  
        word_guessed = True
        print("Congratulations! You guessed the word: {word}".format(word=word_to_guess))   

