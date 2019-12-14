from behave import *
from othello import Position, InvalidPosition, as_position

@given('"{pos_str}" as a position')
def step_impl(context, pos_str):
    try:
        pos = eval(pos_str)
        _ = as_position(pos)
        context.valid = True
    except InvalidPosition:
        context.valid = False

@then('it should be {valid_str}')
def step_impl(context, valid_str):
    valid = valid_str == 'True'
    assert context.valid == valid
