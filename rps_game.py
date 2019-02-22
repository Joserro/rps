import random

moves = ['rock', 'paper', 'scissors']


class Player():

    def __init__(self):
        self.score = 0

    def move(self):
        return moves[0]

    def learn(self, learn_move):
        pass


class RandomPlayer(Player):
    def move(self):
        random_move = random.choice(moves)
        return (random_move)


class ReflectPlayer(Player):
    def __init__(self):
        Player.__init__(self)
        self.learn_move = None

    def move(self):
        if self.learn_move is None:
            random_move = moves[0]
        else:
            random_move = self.learn_move
            return (random_move)

    def learn(self, learn_move):
        self.learn_move = learn_move


class Cycles(Player):

    def __init__(self):

        Player.__init__(self)
        self.step = 0

    def move(self):
        random_move = None
        if self.step == 0:
            random_move = moves[0]
            self.step += 1
        elif self.step == 1:
            random_move = moves[1]
            self.step += 1
        else:
            random_move = moves[2]
            self.step += 1
        return random_move


class HumanPlayer(Player):
    def move(self):
        random_move = input('Enter your move:\nrock,\npaper,\nscissors\n? ')
        while random_move not in moves:
            print('Sorry try again')
            random_move = input(
                          'Enter your move:\nrock,\npaper,\nscissors\n? ')
        return (random_move)


class Game():

    def __init__(self, p2):
        self.p1 = HumanPlayer()
        self.p2 = p2

    def play_game(self):

        print("Game Start, Go!")
        for round in range(3):
            print(f"Round {round}:")
            self.play_round()
        if self.p1.score > self.p2.score:
            print('Player 1 Wins!')
        elif self.p1.score < self.p2.score:
            print('Player 2 Wins!')
        else:
            print('Draw!')
        print('Final score: Player 1: ' + str(self.p1.score)
              + '| ** vs ** |Player 2: ' +
              str(self.p2.score))

    def play_single(self):
        print("Game Start, Go!")
        print(f"Round 1 of 1:")
        self.play_round()
        if self.p1.score > self.p2.score:
            print('Player 1 Wins!')
        elif self.p1.score < self.p2.score:
            print('Player 2 Wins!')
        else:
            print('Draw!')
            print('Final score: Player 1: ' + str(self.p1.score)
                  + ' ** vs ** Player 2: ' +
                  str(self.p2.score))

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        result = Game.play(move1, move2)
        self.p1.learn(move2)
        self.p2.learn(move1)

    def play(self, move1, move2):
            print(f"You played {move1}")
            print(f"Opponent played {move2}")
            if beats(move1, move2):
                self.p1.score += 1
                print("^^ PLAYER ONE WINS ^^")
                print(f"Score: Player 1: {str(self.p1.score)} | \
                      Player 2: {str(self.p2.score)}\n\n")
                return 1
            elif beats(move2, move1):
                self.p2.score += 1
                print("^^ PLAYER TWO WINS ^^")
                print(f"Score: Player 1: {str(self.p1.score)} | \
                      Player 2: {str(self.p2.score)}\n\n")
                return 2
            else:
                print("^^ It's A TIE ^^")
                print(f"Score: Player 1: {str(self.p1.score)} | \
                      Player 2: {str(self.p2.score)}\n\n")
                return 0


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


if __name__ == '__main__':
    answer = [Player(), RandomPlayer(), Cycles(), ReflectPlayer()]
    p2 = input('Select the RPS game you would like to play:\n(Hit any\
 key and enter for random game)\n[1]Rock, [2]Random,\
[3]Reflective, or [4]Cycles: ')

    while p2 != 1 or p2 != 2 or p2 != 3 or p2 != 4:
        p2 = random.choice(answer)
        break
    if p2 == '1':
        p2 = Player()
    elif p2 == '2':
        p2 = RandomPlayer()
    elif p2 == '3':
        p2 = Cycles()
    elif p2 == '4':
        p2 = ReflectPlayer()

    rounds = input('Enter for [s]ingle game or [f]ull game: ')
    Game = Game(p2)
    while True:
        if rounds == 's':
            Game.play_single()
            break
        elif rounds == 'f':
            Game.play_game()
            break
        else:
            print('Sorry try again')
            rounds = input('Enter s for a single game or f for a full game: ')
