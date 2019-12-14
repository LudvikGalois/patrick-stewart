from behave import *
from othello import parse_piece_face, light, dark, InvalidPieceFace


@given('the string "{s}"')
def step_impl(context, s):
    context.s = s


@given('the string ""')
def step_impl(context):
    context.s = ""


@when("I parse it")
def step_impl(context):
    try:
        face = parse_piece_face(context.s)
        context.face = face
    except InvalidPieceFace:
        context.face = None


@then("I should get {result}")
def step_impl(context, result):
    if result == "light":
        assert context.face is light
    elif result == "dark":
        assert context.face is dark
    else:
        assert context.face is None
