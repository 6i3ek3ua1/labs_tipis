class Game:
    def __init__(self):
        self.field = [["*" for _ in range(3)] for _ in range(3)]

    def step(self, x, y, player):
        if self.field[y][x] == "*":
            self.field[y][x] = player.symbol
            return 1
        else:
            print("Illegal move")
            return 0

    def check_winner(self, players):
        winner = 0
        for y in self.field:
            if y[0] == y[1] == y[2] and y[0] != "*":
                if y[0] == "O":
                    winner = players[0]
                else:
                    winner = players[1]
        for y in range(3):
            if self.field[0][y] == self.field[1][y] == self.field[2][y] and self.field[0][y] != "*":
                if self.field[0][y] == "O":
                    winner = players[0]
                else:
                    winner = players[1]
        if self.field[0][0] == self.field[1][1] == self.field[2][2] and self.field[0][0] != "*":
            if self.field[0][0] == "O":
                winner = players[0]
            else:
                winner = players[1]

        if self.field[0][2] == self.field[1][1] == self.field[2][0] and self.field[0][2] != "*":
            if self.field[0][2] == "O":
                winner = players[0]
            else:
                winner = players[1]
        return winner

    def display(self):
        for i in self.field:
            print(' '.join(i))


class Player:
    def __init__(self, name, choose):
        self.name = name
        if choose == 0:
            self.symbol = "O"
        else:
            self.symbol = "X"


game = Game()
print("Игрок номер 1, вы будете играть символом О, введите имя: ")
player1 = Player(input(), 0)
print("Игрок номер 2, вы будете играть символом X, введите имя: ")
player2 = Player(input(), 1)
win_flag = 0
count = 0
players = [player1, player2]
while win_flag == 0:
    game.display()
    print(f"Твой ход, {players[count].name}, выбери координату хода \n"
          f"(левый верхний угол - (0, 0))")
    x = int(input("x - "))
    y = int(input("y - "))
    if 0 <= x < 3 and 0 <= y < 3:
        if game.step(x, y, players[count]) != 0:
            if game.check_winner(players) != 0:
                win_flag = 1
                print(f"Победитель - {game.check_winner(players).name}")
            count += 1
            if count == 2:
                count = 0
    else:
        print("Введи нормальные координаты")
