from behave import *
from othello import Square, Piece, OccupiedSquare


@given("a square")
def step_impl(context):
    context.square = Square()
    context.was_occupied = False


@when("I put a piece into it")
def step_impl(context):
    try:
        context.piece = Piece()
        context.square.place(context.piece)
    except OccupiedSquare:
        context.was_occupied = True


@then("it is empty")
def step_impl(context):
    assert not context.was_occupied
    assert context.square.is_empty()


@then("it is occupied")
def step_impl(context):
    assert not context.was_occupied
    assert context.square.is_occupied()


@then("it contains the same piece that I placed")
def step_impl(context):
    assert context.piece is context.square.piece


@then("it throws an OccupiedSquare error")
def step_impl(context):
    assert context.was_occupied
