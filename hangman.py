import random

def hangman():
    words = ["python", "java", "ruby", "javascript", "html"]
    word_to_guess = random.choice(words)
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    while incorrect_guesses < max_incorrect_guesses:
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word_to_guess])
        print("Word:", display_word)

        user_guess = input("Guess a letter: ")

        if user_guess in guessed_letters:
            print("You already guessed that letter. Try again.")
        elif user_guess in word_to_guess:
            print("Correct guess!")
            guessed_letters.append(user_guess)
        else:
            print("Incorrect guess.")
            incorrect_guesses += 1

        if set(guessed_letters) == set(word_to_guess):
            print("Congratulations! You guessed the word.")
            break

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you've reached the maximum number of incorrect guesses. The word was {word_to_guess}.")

hangman()
