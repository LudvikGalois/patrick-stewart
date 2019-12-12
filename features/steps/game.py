from behave import *
from othello import Game, Position, light, dark

@given('we have a new game')
def step_impl(context):
    context.game = Game()

@then('there is a {colour} piece at {position}')
def step_impl(context, colour, position):
    assert colour in {'light', 'dark'}
    game = context.game
    board = game.board
    square = board[Position.from_str(position)]
    assert square.is_occupied()
    piece = square.piece
    assert piece is not None
    face = light if colour == 'light' else dark
    assert piece.face is face
