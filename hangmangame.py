import random

# this list is for chosing random word
words = ["mango","apple","banana","fig","watermellon","pineapple"]

# now  we choose a random word
word = random.choice(words)
word_letters = list(word)
guessed_letters = ['_'] * len(word)

# these are game variable whish is used for store the value of no of attemps and used letters
attempts = 6
used_letters = []

print("Welcome to Hangman Game!")
print("\nThis word is also a fruits name")
# now we apply the looping concept for performing the operation for the task
while attempts > 0 and '_' in guessed_letters:
    print("\nWord: ", ' '.join(guessed_letters))
    print("Used letters:", ', '.join(used_letters))
    print(f"Remaining attempts: {attempts}")

    guess = input("Guess a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet.")
        continue

    if guess in used_letters:
        print("You've already guessed that letter.")
        continue

    used_letters.append(guess)

    if guess in word_letters:
        print("Correct!")
        for i in range(len(word)):
            if word[i] == guess:
                guessed_letters[i] = guess
                break
    else:
        print("Wrong guess.")
        attempts -= 1

#  this step is for final result 
if '_' not in guessed_letters:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nGame Over! The word was:", word)

