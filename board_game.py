from collections import namedtuple
import numpy as np
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
        self.first_turn = True

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

    def place_tiles(self, tiles):
        min_x = self.BOARD_X
        max_x = -1
        min_y = self.BOARD_Y
        max_y = -1
        for tile in tiles:
            if self.board[tile.y][tile.x].tile is None:
                self.board[tile.y][tile.x].tile = tile.letter[0]
                min_x = min(tile.x, min_x)
                min_y = min(tile.y, min_y)
                max_x = max(tile.x, max_x)
                max_y = max(tile.y, max_y)
            else:
                return False
        # Find word in direction of tile placement
        start_x, start_y, end_x, end_y = \
            __find_word(tiles[0].x, tiles[0].y, x_axis=int(min_x == max_x), \
                        y_axis=int(min_y == max_y))
        
        

        
    def __is_valid_word()
    def __find_word(self, x_coord, y_coord, x_axis=0, y_axis=0):
        # Find beginning of word
        cur_x = x_coord
        cur_y = y_coord
        
        while cur_x >= 0 and cur_y >= 0:
            if self.board[cur_y][cur_x].tile is not None:
                cur_x -= x_axis
                cur_y -= y_axis
            else:
                break
        
        start_x = cur_x + 1 * x_axis
        start_y = cur_y + 1 * y_axis

        # Find ending of word
        cur_x = x_coord
        cur_y = y_coord

        while cur_x < self.BOARD_X and cur_y < self.BOARD_Y:
            if self.board[cur_y][cur_x].tile is not None:
                cur_x += x_axis
                cur_y += y_axis
            else:
                break

        end_x = cur_x - 1 * x_axis
        end_y = cur_y - 1 * y_axis

        np_array = np.array(self.board)

        return np_array[start_y:(end_y + 1), start_x:(end_x + 1)]