from board_game import BoardGame


class ScrabbleBoard(BoardGame):

    BOARD_X = 15
    BOARD_Y = 15

    DEFAULT_SQUARE = "PLAIN"
    INITIAL_TILE_COUNT = 7

    SQUARE_TYPES = {
        "PLAIN": BoardGame.SquareMultiplier(1, 1),
        "STAR": BoardGame.SquareMultiplier(1, 1),
        "DLS": BoardGame.SquareMultiplier(2, 1),
        "DWS": BoardGame.SquareMultiplier(1, 2),
        "TLS": BoardGame.SquareMultiplier(3, 1),
        "TWS": BoardGame.SquareMultiplier(1, 3)
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

    TILES = {
        ' ': BoardGame.Tile(2, 0),
        'A': BoardGame.Tile(9, 1),
        'B': BoardGame.Tile(2, 3),
        'C': BoardGame.Tile(2, 3),
        'D': BoardGame.Tile(4, 2),
        'E': BoardGame.Tile(12, 1),
        'F': BoardGame.Tile(2, 4),
        'G': BoardGame.Tile(3, 2),
        'H': BoardGame.Tile(2, 4),
        'I': BoardGame.Tile(9, 1),
        'J': BoardGame.Tile(1, 8),
        'K': BoardGame.Tile(1, 5),
        'L': BoardGame.Tile(4, 1),
        'M': BoardGame.Tile(2, 3),
        'N': BoardGame.Tile(6, 1),
        'O': BoardGame.Tile(8, 1),
        'P': BoardGame.Tile(2, 3),
        'Q': BoardGame.Tile(1, 10),
        'R': BoardGame.Tile(6, 1),
        'S': BoardGame.Tile(4, 1),
        'T': BoardGame.Tile(6, 1),
        'U': BoardGame.Tile(4, 1),
        'V': BoardGame.Tile(2, 4),
        'W': BoardGame.Tile(2, 4),
        'X': BoardGame.Tile(1, 8),
        'Y': BoardGame.Tile(2, 4),
        'Z': BoardGame.Tile(1, 10)
    }

    def __init__(self, player_count):
        super().__init__(player_count)
