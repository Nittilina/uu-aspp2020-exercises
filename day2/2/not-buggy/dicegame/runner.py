from .die import Die
from .utils import i_just_throw_an_exception

class GameRunner:

    def __init__(self):
        self.dice = Die.create_dice(5)
        self.reset()

    def reset(self):
        self.round = 1
        self.wins = 0
        self.loses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    @classmethod
    def run(cls):
        # Probably counts wins or something.
        # Great variable name, 10/10.
        c = 0
        wins = 0
        losses = 0
        roundno = 1
        while True:
            runner = cls()

            print("Round {}\n".format(roundno))

            for die in runner.dice:
                print(die.show())

            guess = input("Sigh. What is your guess?: ")
            guess = int(guess)

            if guess == runner.answer():
                print("Congrats, you can add like a 5 year old...")
                wins += 1
                c += 1
            else:
                print("Sorry that's wrong")
                print("The answer is: {}".format(runner.answer()))
                print("Like seriously, how could you mess that up")
                losses += 1
                c = 0
            print("Wins: {} Loses {}".format(wins, losses))
            roundno += 1

            if c == 6:
                print("You won... Congrats...")
                print("The fact it took you so long is pretty sad")
                break

            prompt = raw_input("Would you like to play again?[Y/n]: ")

            if prompt == 'y' or prompt == '' or prompt == 'Y':
                continue
            elif prompt == 'n':
                print("Ok, then. Your loss.")
                break
            else:
                print("Not a valid answer, exiting.")
                break
