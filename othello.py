class Game:
    def __init__(self):
        self.board = Board()

class Square:
    def __init__(self):
        self.piece = None
    def is_empty(self):
        return self.piece is None
    def is_occupied(self):
        return not self.is_empty()
    def place(self, piece):
        if self.is_occupied():
            raise OccupiedSquare
        self.piece = piece

class OccupiedSquare(Exception):
    pass

class InvalidPosition(Exception):
    pass

def _invert(dic):
    return {v: k for k, v in dic.items()}

class Position:

    _col_table = {chr(ord('a') + i): i for i in range(8)}
    _col_table_inv = _invert(_col_table)
    
    _row_table = {str(i+1): i for i in range(8)}
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
        assert 0 <= x < 8
        assert 0 <= y < 8
        self.x = x
        self.y = y

    def __str__(self):
        return f'{self._col_table_inv[self.x]}{self._row_table_inv[self.y]}'

class Board:
    def __init__(self, empty=False):
        if empty:
            self.clear_board()
        else:
            self.set_initial_position()

    def clear_board(self):
        self._squares = [[Square() for _j in range(8)] for _i in range(8)]

    def set_initial_position(self):
        self.clear_board()
        self[Position.from_str('d4')].place(Piece(light))
        self[Position.from_str('e4')].place(Piece(dark))
        self[Position.from_str('d5')].place(Piece(dark))
        self[Position.from_str('e5')].place(Piece(light))

    def __getitem__(self, position):
        return self._squares[position.y][position.x]

class _Light():
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(_Light, cls).__new__(cls, *args, **kwargs)
        return cls._singleton

    def complement(self):
        return _Dark()

class _Dark():
    _singleton = None
    def __new__(cls, *args, **kwargs):
        if not cls._singleton:
            cls._singleton = super(_Dark, cls).__new__(cls, *args, **kwargs)
        return cls._singleton
    def complement(self):
        return _Light()

light = _Light()
dark = _Dark()

class Piece:
    def __init__(self, face=light):
        self.face = face
        self.flip_count = 0
    def flip(self):
        self.face = face.complement()
        self.flip_count += 1

