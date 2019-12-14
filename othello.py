from functools import singledispatch
from itertools import product
from time import time


class Game:
    def __init__(self):
        self.board = Board()


class Square:
    def __init__(self):
        self.piece = None
        self.placed_at = None

    def is_empty(self):
        return self.piece is None

    def is_occupied(self):
        return not self.is_empty()

    def place(self, piece):
        if self.is_occupied():
            raise OccupiedSquare
        self.piece = piece
        self.occupied_at = time()


class OccupiedSquare(Exception):
    pass


class InvalidPosition(Exception):
    pass


class InvalidPieceFace(Exception):
    pass


def _invert(dic):
    return {v: k for k, v in dic.items()}


class Position:

    _col_table = {chr(ord("a") + i): i for i in range(8)}
    _col_table_inv = _invert(_col_table)

    _row_table = {str(i + 1): i for i in range(8)}
    _row_table_inv = _invert(_row_table)

    @classmethod
    def from_str(cls, s):
        if len(s) != 2:
            raise InvalidPosition
        [col, row] = s.lower()
        try:
            x = cls._col_table[col]
            y = cls._row_table[row]
        except KeyError:
            raise InvalidPosition
        return Position(x, y)

    def __init__(self, x, y):
        try:
            assert 0 <= x < 8
            assert 0 <= y < 8
        except AssertionError:
            raise InvalidPosition
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self._col_table_inv[self.x]}{self._row_table_inv[self.y]}"


@singledispatch
def as_position(arg):
    raise InvalidPosition


@as_position.register
def _(arg: Position):
    return arg


@as_position.register
def _(arg: str):
    return Position.from_str(arg)


@as_position.register
def _(arg: tuple):
    if len(arg) != 2:
        raise InvalidPosition
    x, y = arg
    if not isinstance(x, int) or not isinstance(y, int):
        raise InvalidPosition
    return Position(x, y)


class Board:
    def __init__(self, initial_position=True):
        self._squares = [[Square() for _j in range(8)] for _i in range(8)]
        if initial_position:
            self.set_initial_position()

    def squares(self):
        """Return an iterator over the squares on the Board."""
        all_positions = map(as_position, product(range(8), repeat=2))
        return ((position, self[position]) for position in all_positions)

    def clear_board(self):
        for pos, _ in self.squares():
            self[pos] = Square()

    def set_initial_position(self):
        self.clear_board()
        self["d4"].place(Piece(light))
        self["e4"].place(Piece(dark))
        self["d5"].place(Piece(dark))
        self["e5"].place(Piece(light))

    def __getitem__(self, key):
        position = as_position(key)
        return self._squares[position.y][position.x]

    def __setitem__(self, key, value):
        position = as_position(key)
        self._squares[position.y][position.x] = value


class _Light:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(_Light, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def complement(self):
        return _Dark()


class _Dark:
    _singleton = None

    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(_Dark, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def complement(self):
        return _Light()


light = _Light()
dark = _Dark()


def parse_piece_face(s):
    if s in {"light", "l", "L"}:
        return light
    if s in {"dark", "d", "D"}:
        return dark
    raise InvalidPieceFace


class Piece:
    def __init__(self, face=light):
        self.face = face
        self.flip_count = 0

    def flip(self):
        self.face = self.face.complement()
        self.flip_count += 1
