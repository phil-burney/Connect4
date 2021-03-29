import enum



ROWS = 6
COLS = 7
CONNECT_FOUR = 4
RED = 'r'
BLACK = 'b'

class Colors(enum.Enum):
    Red = 1
    Black = 2

class Board:

    def __init__ (self, board, connect4):
        
        self.board = [[0 for i in range(COLS)] for j in range(ROWS)]
        self.connect4 = False

    def getColor(self, row, col):
        return self.board[row][col]

    def addDisc(self, col, color):
        if not self.board[0][col] == 0:
            return "Full column!"

        for i in range(ROWS):
            if not self.board[i][col] == 0:
                i = i - 1
                self.board[i][col] = color
                return i
        self.board[ROWS - 1][col] = color
        return ROWS - 1

    def seeIfWinner(self):
        return self.connect4

    def checkWinner(self, row, col, color):
        fourScore = 1
        thiscolor = color

        up = row
        down = row
        while thiscolor == color and down + 1 < ROWS:
            thiscolor = self.board[down + 1][col]
            down = down + 1
            if thiscolor == color:
                fourScore = fourScore + 1
        
        thiscolor = color

        while thiscolor == color and up - 1 > 0:
            
            thiscolor = self.board[up - 1][col]
            up = up - 1
            if thiscolor == color:
                fourScore = fourScore + 1

        if(fourScore == CONNECT_FOUR):
            self.connect4 = True

        fourScore = 1
        thiscolor = color

        left = col
        right = col

        while thiscolor == color and right + 1 < COLS:
            
            thiscolor = self.board[row][right + 1]
            right = right + 1
            if thiscolor == color:
                fourScore = fourScore + 1

        thiscolor = color

        while thiscolor == color and left - 1 > 0:
            
            thiscolor = self.board[row][left - 1]
            left = left - 1
            if thiscolor == color:
                fourScore = fourScore + 1

        if fourScore >= CONNECT_FOUR:
            self.connect4 = True

        fourScore = 1
        thiscolor = color

        up = row
        down = row
        left = col
        right = col

        while thiscolor == color and left - 1 > 0 and up - 1 > 0:
            
            thiscolor = self.board[up - 1][left - 1]
            up = up - 1
            left = left - 1
            if thiscolor == color:
                fourScore = fourScore + 1

        thiscolor = color

        while thiscolor == color and right + 1 < COLS and down + 1 < ROWS:
            
            thiscolor = self.board[down + 1][right + 1]
            down = down + 1
            right = right + 1
            if color == thiscolor:
                fourScore = fourScore + 1
            
        if fourScore >= CONNECT_FOUR:
            self.connect4 = True

        fourScore = 1
        thiscolor = color

        up = row
        down = row
        left = col
        right = col

        while thiscolor == color and up - 1 > 0 and right + 1 < COLS:
            
            thiscolor = self.board[up - 1][right + 1]
            up = up - 1
            right = right + 1
            if thiscolor == color:
                fourScore = fourScore + 1
        
        thiscolor = color

        while thiscolor == color and down + 1 < ROWS and left - 1> 0:
            
            thiscolor = self.board[down + 1][left - 1]
            down = down + 1
            left = left - 1
            if thiscolor == color:
                fourScore = fourScore + 1
            
        if fourScore >= CONNECT_FOUR:
            self.connect4 = True

        fourScore = 1
        thiscolor = color

        

        

