from board import Board
class Connect4:

    def __init__(self):
        self.game = Board(0,0)

    def turn(self, color, column):
        place = self.game.addDisc(column, color)
        self.game.checkWinner(place, column, color)
       
        




