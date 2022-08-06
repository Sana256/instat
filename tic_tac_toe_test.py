from tic_tac_toe import BoardStatus, Field, TicTacToeBoard


def test_is_empty():
    tic_tac_toe = TicTacToeBoard()
    assert tic_tac_toe.is_board_empty() is True

def test_is_empty_return_false():
    tic_tac_toe = TicTacToeBoard()
    tic_tac_toe.set_field(0, 0, Field.X)
    assert tic_tac_toe.is_board_empty() is False


def test_get_board_status_empty():
    tic_tac_toe = TicTacToeBoard()
    assert tic_tac_toe.get_board_status() == BoardStatus.Empty


def test_get_board_status_in_progress():
    tic_tac_toe = TicTacToeBoard()
    tic_tac_toe.set_field(0, 0, Field.X)
    assert tic_tac_toe.get_board_status() == BoardStatus.InProgress

def test_get_board_status_x_wins():
    tic_tac_toe = TicTacToeBoard()
    tic_tac_toe.set_field(0, 0, Field.X)
    tic_tac_toe.set_field(0, 1, Field.X)
    tic_tac_toe.set_field(0, 2, Field.X)
    assert tic_tac_toe.get_board_status() == BoardStatus.X_Wins


def test_get_board_status_player_y_diagonal_wins():
    tic_tac_toe = TicTacToeBoard()
    tic_tac_toe.set_field(0, 0, Field.O)
    tic_tac_toe.set_field(1, 1, Field.O)
    tic_tac_toe.set_field(2, 2, Field.O)
    assert tic_tac_toe.get_board_status() == BoardStatus.O_Wins


if __name__ == "__main__":
    test_is_empty()
    test_is_empty_return_false()
    test_get_board_status_empty()
    test_get_board_status_in_progress()
    test_get_board_status_x_wins()
    test_get_board_status_player_y_diagonal_wins()
    print("done")