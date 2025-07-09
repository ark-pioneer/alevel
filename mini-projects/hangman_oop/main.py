from wonderwords import RandomWord

class Guess():
    def __init__(self, data, guessed):
        self.data = data
        self.guessed = guessed
        
    def valid(self):
        return self.data.isalpha() and len(self.data) == 1 and self.data not in self.guessed

class Turn():
    def __init__(self, display_word, guessed, lives):
        self.summary = "\n".join([
            "------------------",
            f"TURN: {len(guessed) + 1}",
            f"\tlives: {lives}",
            f"\tguessed: {guessed}",
            f"\tword: {" ".join(display_word)}"  
        ])
    
class Hangman():
    def __init__(self, word=RandomWord().word(), Turn=Turn):
        self.word = word
        self.Turn = Turn
        self.guessed = []
        self.lives = 7

    def game_over_win(self):
        return len([i for i in self.word if i not in self.guessed]) == 0

    def create_display_word(self):
        return [char if char in self.guessed else "_" for char in self.word]

    def turn_summary(self):
        turn = self.Turn(self.create_display_word(), self.guessed, self.lives)
        return turn.summary

    def get_letter(self):
        while True:
            print("guess a letter: ", end="")
            guess = Guess(input(), self.guessed)
            if guess.valid():
                break
        return guess.data

    def play(self):
        print("Welcome to Hangman")
        print(self.turn_summary())
        while True:
            letter = self.get_letter()
            self.guessed.append(letter)
            if letter not in self.word:
                self.lives -=1
                print("sorry, try again")
            else:
                print("nice")

            print(self.turn_summary())

            if self.lives <= 0:
                print("you lose")
                print(f"word: {self.word}")
                break
            elif self.game_over_win():
                print("you win")
                break

hangman = Hangman()
hangman.play()
        


    