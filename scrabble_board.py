from collections import namedtuple


class ScrabbleBoard:

    # Scrabble Constants

    # Board Dimensions

    BOARD_X = 15
    BOARD_Y = 15

    # Square Types

    SquareMultiplier = namedtuple("SquareMultiplier", "letter word")

    SQUARE_TYPES = {
        "PLAIN": SquareMultiplier(1, 1),
        "STAR": SquareMultiplier(1, 1),
        "DLS": SquareMultiplier(2, 1),
        "DWS": SquareMultiplier(1, 2),
        "TLS": SquareMultiplier(3, 1),
        "TWS": SquareMultiplier(1, 3)
    }

    SQUARE_COORDS = {
        "STAR": [(7, 7)],
        "DLS": [
            (0, 3),
            (2, 6),
            (3, 0), (3, 7),
            (6, 2), (6, 6),
            (7, 3)
        ],
        "DWS": [
            (1, 1),
            (2, 2),
            (3, 3),
            (4, 4)
        ],
        "TLS": [
            (1, 5),
            (5, 1), (5, 5)
        ],
        "TWS": [
            (0, 0), (0, 7),
            (7, 0)
        ]
    }

    # Tiles

    Tile = namedtuple("Tile", "count value")

    TILES = {
        ' ': Tile(2, 0),
        'A': Tile(9, 1),
        'B': Tile(2, 3),
        'C': Tile(2, 3),
        'D': Tile(4, 2),
        'E': Tile(12, 1),
        'F': Tile(2, 4),
        'G': Tile(3, 2),
        'H': Tile(2, 4),
        'I': Tile(9, 1),
        'J': Tile(1, 8),
        'K': Tile(1, 5),
        'L': Tile(4, 1),
        'M': Tile(2, 3),
        'N': Tile(6, 1),
        'O': Tile(8, 1),
        'P': Tile(2, 3),
        'Q': Tile(1, 10),
        'R': Tile(6, 1),
        'S': Tile(4, 1),
        'T': Tile(6, 1),
        'U': Tile(4, 1),
        'V': Tile(2, 4),
        'W': Tile(2, 4),
        'X': Tile(1, 8),
        'Y': Tile(2, 4),
        'Z': Tile(1, 10)
    }

    Square = namedtuple("Square", "tile type")

    def __init__(self):
        self.board = []
        self.__populate_board()

    def __populate_board(self):

        # Populate with PLAIN squares

        for i in range(self.BOARD_Y):
            row = []
            for j in range(self.BOARD_X):
                square = self.Square(None, "PLAIN")
                row.append(square)
            self.board.append(row)

        # Populate special types

        for square_type in self.SQUARE_COORDS:

            for y, x in self.SQUARE_COORDS[square_type]:
                # Quadrant 1
                self.board[y][self.BOARD_X - 1 - x] = self.Square(None, square_type)
                # Quadrant 2
                self.board[y][x] = self.Square(None, square_type)
                # Quadrant 3
                self.board[self.BOARD_Y - 1 - y][x] = self.Square(None, square_type)
                # Quadrant 4
                self.board[self.BOARD_Y - 1 - y][self.BOARD_X - 1 - x] = self.Square(None, square_type)
