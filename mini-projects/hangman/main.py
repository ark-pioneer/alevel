import random

words = [
    "banana",
    "tomato",
    "cauliflower",
    "mango",
    "lychee"
]

word = words[random.randint(0, len(words)-1)]
guessed = []
lives = 7

def game_over_win():
    for letter in word:
        if letter not in guessed:
            return False
    return True

def summary():
    display = ["------------------"]
    display_word = []
    for char in word:
        if char not in guessed:
            display_word.append("_")
        else:
            display_word.append(char)
    display.append(f"\tlives: {lives}")
    display.append(f"\tguessed: {guessed}")
    display.append(f"\tword: {" ".join(display_word)}")
    return "\n".join(display)

print("Welcome to Hangman")

print(summary())
while True:  
    valid_guess = False
    letter = ""
    while not valid_guess:
        print("guess a letter: ", end="")
        letter = input()
        if letter.isalpha() and len(letter) == 1 and letter not in guessed:
            valid_guess = True
    guessed.append(letter)
    if letter not in word:
        lives -=1
        print("sorry, try again")
    else:
        print("nice")

    print(summary())

    if lives <= 0:
        print("you lose")
        break
    elif game_over_win():
        print("you win")
        break
    