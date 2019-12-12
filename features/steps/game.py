from behave import *
from othello import Game, Position, parse_piece_face

@given('we have a new game')
def step_impl(context):
    context.game = Game()

@then('there is a {colour} piece at {position}')
def step_impl(context, colour, position):
    game = context.game
    board = game.board
    square = board[Position.from_str(position)]
    assert square.is_occupied()
    piece = square.piece
    assert piece is not None
    face = parse_piece_face(colour)
    assert piece.face is face
