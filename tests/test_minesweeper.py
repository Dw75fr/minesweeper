import pytest
import minesweeper

def test_module_exists():
    assert minesweeper

def test_place_mines():
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    # TODO : Add assertions
    assert len(game.mines) == 2

def test_reveal():
    import random 
    random.seed(0)
    game = minesweeper.Minesweeper(3, 3, 2)
    game.place_mines()
    game.reveal(0, 0)
    # TODO : Add assertions
    assert game.board[0][0] == 1
    assert game.revealed == {(0, 0)}

def test_fail():
    assert False