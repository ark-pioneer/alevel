from game.game import Game
from game.constants import constants

class App():
    def run():
        game = Game()
        print(constants["welcome"])
        for command in constants["commands"]:
            print(command + ":", constants["commands"][command])
        while True:
            data = input("Enter command: ")
            if data == "h":
                for command in constants["commands"]:
                    print(command + ":", constants["commands"][command])
            elif data == "s":
                print(game.get_board())
            elif data == "q":
                print("Application quitting...")
                break
            else:
                print("Invalid command (type 'h' for help)")
        print("App closed")