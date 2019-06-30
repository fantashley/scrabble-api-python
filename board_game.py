from collections import namedtuple


class BoardGame:

    # Board coordinates
    BOARD_X = None
    BOARD_Y = None
    
    SQUARE_TYPES = {}
    SQUARE_COORDS = {}
    TILES = {}

    Square = namedtuple("Square", "tile type")
    SquareMultiplier = namedtuple("SquareMultiplier", "letter word")
    Tile = namedtuple("Tile", "count value")

    def __init__(self, default_square_type):
        self.default_square = self.Square(None, default_square_type)
        self.board = []
        self.__populate_board()

    def __populate_board(self):

        # Populate with default squares

        for i in range(self.BOARD_Y):
            row = []
            for j in range(self.BOARD_X):
                square = self.default_square
                row.append(square)
            self.board.append(row)

        # Populate special types

        for square_type in self.SQUARE_COORDS:

            for y, x in self.SQUARE_COORDS[square_type]:
                # Quadrant 1
                self.board[y][self.BOARD_X - 1 - x] = self.Square(None,
                                                                  square_type)
                # Quadrant 2
                self.board[y][x] = self.Square(None, square_type)
                # Quadrant 3
                self.board[self.BOARD_Y - 1 - y][x] = self.Square(None,
                                                                  square_type)
                # Quadrant 4
                self.board[self.BOARD_Y - 1 - y][self.BOARD_X - 1 - x] = \
                    self.Square(None, square_type)
