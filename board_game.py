from collections import namedtuple
import random


class BoardGame:

    # Board coordinates
    BOARD_X = None
    BOARD_Y = None

    SQUARE_TYPES = {}
    SQUARE_COORDS = {}
    TILES = {}
    INITIAL_TILE_COUNT = None
    DEFAULT_SQUARE = None

    Square = namedtuple("Square", "tile type")
    SquareMultiplier = namedtuple("SquareMultiplier", "letter word")
    Tile = namedtuple("Tile", "count value")

    def __init__(self, player_count):
        self.player_count = player_count
        self.board = []
        self.players = []
        self.tile_bag = []

        self.__populate_board()
        self.__initialize_players()
        self.__initialize_tiles()

    def __populate_board(self):

        # Populate with default squares

        for i in range(self.BOARD_Y):
            row = []
            for j in range(self.BOARD_X):
                square = self.Square(None, self.DEFAULT_SQUARE)
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

    def __initialize_players(self):
    
        for player in range(self.player_count):
            tile_set = []
            self.players.append(tile_set)

    def __initialize_tiles(self):

        for tile_type in self.TILES:
            for i in range(self.TILES[tile_type].count):
                self.tile_bag.append(tile_type)

        random.shuffle(self.tile_bag)

        for player in self.players:
            for i in range(self.INITIAL_TILE_COUNT):
                player.append(self.tile_bag.pop())
