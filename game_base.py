import numpy as np
from enum import Enum
import abc

class Side(Enum):
    SOUTH = 0
    NORTH = 1

class KalahGameBase(metaclass=abc.ABCMeta):

    def __init__(self, south_pits, north_pits, side_to_move, south_kalah = 0, north_kalah = 0, verbose = False):
        pass
        # assert len(south_pits) == len(north_pits)
        # self.pit_count = len(south_pits)
        # self.pits = {}
        # self.pits[Side.SOUTH] = np.array(south_pits)
        # self.pits[Side.NORTH] = np.array(north_pits)
        #
        # self.kalah = {}
        # self.kalah[Side.SOUTH] = south_kalah
        # self.kalah[Side.NORTH] = north_kalah
        #
        # self.all_stone_count = self.count_all_stones()
        #
        # self.side = side_to_move
        # self.verbose = verbose

    @abc.abstractmethod
    def copy(self):
        pass
        # return KalahGameBase(self.pits[Side.SOUTH], self.pits[Side.NORTH], self.side,
        #                  self.kalah[Side.SOUTH], self.kalah[Side.NORTH])

    @classmethod
    def new_game(cls, pits = 6, stones = 6):
        game = KalahGameBase([stones]*pits, [stones]*pits, Side.SOUTH)
        return game

    @abc.abstractmethod
    def make_move(self, from_pit) -> (bool, int):
        pass

    @abc.abstractmethod
    def check_finished(self) -> (bool, int):
        pass
        # if self.kalah[Side.SOUTH] > self.all_stone_count // 2:
        #     return (True, 1)
        # if self.kalah[Side.NORTH] > self.all_stone_count // 2:
        #     return (True, -1)
        # if self.kalah[Side.SOUTH] + self.kalah[Side.NORTH] == self.all_stone_count:
        #     return (True, 0)
        #
        # return (False, -2)

    @abc.abstractmethod
    def to_string(self):
        pass
        # pits_template = '   {}   \n'
        # s = pits_template.format(self.pits[Side.NORTH][::-1])
        # kalah_str = (str(self.kalah[Side.NORTH])).ljust(len(s) - len(str(self.kalah[Side.SOUTH])))
        # kalah_str += '{}\n'.format(self.kalah[Side.SOUTH])
        # s += kalah_str
        # s += pits_template.format(self.pits[Side.SOUTH])
        # if self.side == Side.SOUTH:
        #     ss = 'South'
        # else:
        #     ss = 'North'
        # s += '\nTurn: {} #Stones : {} \n'.format(ss, self.count_all_stones())
        # return s

    @abc.abstractmethod
    def assertCorrect(self):
        pass
        # assert self.count_all_stones() == self.all_stone_count
        # assert np.all(self.pits[Side.SOUTH] >= 0)
        # assert np.all(self.pits[Side.NORTH] >= 0)
        # assert self.kalah[Side.SOUTH] >= 0
        # assert self.kalah[Side.NORTH] >= 0

    @abc.abstractmethod
    def count_all_stones(self) -> int:
        pass
        #return (np.sum(self.pits[Side.SOUTH]) + np.sum(self.pits[Side.NORTH]) + self.kalah[Side.NORTH] + self.kalah[Side.SOUTH])


    @abc.abstractmethod
    def opposite_pit(self, pit_no) -> int:
        pass
        #return self.pit_count - pit_no - 1


    @abc.abstractmethod
    def switch_side(self):
        pass
        #self.side = KalahGameBase.other_side(self.side)

    @staticmethod
    def other_side(side):
        if side == Side.NORTH:
            return Side.SOUTH
        else:
            return Side.NORTH


    @abc.abstractmethod
    def gen_moves(self):
        pass
        # # All pits that contain stones can be moves
        # return np.flatnonzero(self.pits[self.side])


    # def show_playout(self, move_seq: list):
    #     print('Playout on moves: {}\n'.format( move_seq))
    #     print('Initial position: \n {0}'.format(self.to_string()))
    #     for move in move_seq:
    #         print('Move: {0}'.format(move))
    #         (finished, res) = self.make_move(move)
    #         if finished:
    #             print('Game finished. Result: {0}'.format(res))
    #         else:
    #             print('{0}\n'.format(self.to_string()))

