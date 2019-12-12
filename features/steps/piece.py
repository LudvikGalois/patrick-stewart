from behave import *
from othello import Piece, parse_piece_face

@given('a {colour} piece')
def step_impl(context, colour):
    face = parse_piece_face(colour)
    context.piece = Piece(face)

@when('I flip it {n:d} time(s)')
def step_impl(context, n):
    for _ in range(n):
        context.piece.flip()

@then('it should be a {colour} piece')
def step_impl(context, colour):
    face = parse_piece_face(colour)
    assert context.piece.face is face

@then('the flip count should be {n:d}')
def step_impl(context, n):
    assert context.piece.flip_count == n
