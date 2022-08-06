from enum import Enum

class Field(str, Enum):
    X = 'X'
    O = 'O'
    Empty = ' '


class Player(str, Enum):
    X = 'X'
    O = 'O'

class BoardStatus(str, Enum):
    X_Wins = 'X wins'
    O_Wins = 'O wins'
    Empty = 'empty'
    InProgress = 'In progress'


class TicTacToeBoard:

    def __init__(self):
        self.board = [[Field.Empty] * 3 for i in range(3)]
        self.players = (Field.X, Field.O)

    def __str__(self):
        s = ''
        for i in range(3):
            for j in range(3):
                s += self.board[i][j]
                if j != 2:
                    s += ' | '
            s += '\n'
        return s
    
    def set_field(self, row: int, col: int, field: Field) -> None:
        self.board[row][col] = field
        
    def get_board_status(self) -> BoardStatus:
        if self.is_player_win(Field.X):
            return BoardStatus.X_Wins

        elif self.is_player_win(Field.O):
            return BoardStatus.O_Wins

        elif self.is_board_empty():
            return BoardStatus.Empty

        else:
            return BoardStatus.InProgress

    def is_player_win(self, player: Player) -> bool:
        for i in range(3):
            if self.board[i][0] == player and self.board[i][1] == player and self.board[i][2] == player:
                return True

            if self.board[0][i] == player and self.board[1][i] == player and self.board[2][i] == player:
                return True

        if self.board[0][0] == player and self.board[1][1] == player and self.board[2][2] == player:
            return True

        if self.board[0][2] == player and self.board[1][1] == player and self.board[2][0] == player:
            return True

        return False

    def is_board_empty(self):
        for i in range(3):
            for j in range(3):
                if not self.is_empty(i, j):
                    return False

        return True
    
    def is_empty(self, row, col):
        return self.board[row][col] == Field.Empty


if __name__ == "__main__":
    board = TicTacToeBoard()
    print(board)

