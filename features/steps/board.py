from behave import *
from othello import Board

@given('an empty board')
def step_impl(context):
    context.board = Board(initial_position=False)

@given('the initial board')
def step_impl(context):
    context.board = Board()

@when('I clear the board')
def step_impl(context):
    context.board.clear_board()

@then('all squares on the board are empty')
def step_impl(context):
    assert all(s.is_empty() for _, s in context.board.squares())

@then('{n:d} squares on the board are not empty')
def step_impl(context, n):
    assert n == sum(0 if s.is_empty() else 1 for _, s in context.board.squares())
