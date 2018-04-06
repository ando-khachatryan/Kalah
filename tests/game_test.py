from game import *
import unittest as ut

class GameTests(ut.TestCase):

    def assertGamesEqual(self, game1: KalahGame, game2: KalahGame):
        self.assertSequenceEqual(list(game1.pits[Side.SOUTH]), list(game2.pits[Side.SOUTH]))
        self.assertSequenceEqual(list(game1.pits[Side.NORTH]), list(game2.pits[Side.NORTH]))

        self.assertEqual(game1.kalah[Side.SOUTH], game2.kalah[Side.SOUTH])
        self.assertEqual(game1.kalah[Side.NORTH], game2.kalah[Side.NORTH])
        self.assertEqual(game1.side, game2.side)


    def test_make_move_1(self):
        game = KalahGame([2, 2, 3], [1, 1, 1], Side.SOUTH)
        game.make_move(0)
        game.assertCorrect()
        should_be = KalahGame([0, 3, 4], [1, 1, 1], Side.NORTH, 0, 0)
        self.assertGamesEqual(game, should_be)

    def test_make_move_2(self):
        game = KalahGame([2, 2, 3], [1, 1, 1], Side.SOUTH)
        game.make_move(1)
        game.assertCorrect()
        should_be = KalahGame([2, 0, 4], [1, 1, 1], Side.SOUTH, 1, 0)
        self.assertGamesEqual(game, should_be)

    def test_make_move_3(self):
        game = KalahGame([2, 2, 3], [1, 1, 1], Side.SOUTH)
        game.make_move(2)
        game.assertCorrect()
        should_be = KalahGame([2, 2, 0], [2, 2, 1], Side.NORTH, 1, 0)
        self.assertGamesEqual(game, should_be)


    def test_make_move_4(self):
        game = KalahGame([2, 2, 3], [1, 1, 1], Side.NORTH)
        game.make_move(0)
        game.assertCorrect()
        should_be = KalahGame([2, 2, 3], [0, 2, 1], Side.SOUTH, 0, 0)
        self.assertGamesEqual(game, should_be)
    #
    #
    def test_make_move_5(self):
        game = KalahGame([2, 2, 3], [1, 1, 1], Side.NORTH)
        game.make_move(1)
        game.assertCorrect()
        should_be = KalahGame([2, 2, 3], [1, 0, 2], Side.SOUTH, 0, 0)
        self.assertGamesEqual(game, should_be)

    def test_make_move_6(self):
        game = KalahGame([2, 2, 3], [1, 1, 1], Side.NORTH)
        game.make_move(2)
        game.assertCorrect()
        should_be = KalahGame([2, 2, 3], [1, 1, 0], Side.NORTH, 0, 1)
        self.assertGamesEqual(game, should_be)

    def test_make_move_7(self):
        game = KalahGame([2, 2, 8], [0, 0, 0], Side.SOUTH)
        game.make_move(2)
        game.assertCorrect()
        should_be = KalahGame([3, 3, 1], [1, 1, 1], Side.SOUTH, 2, 0)
        self.assertGamesEqual(game, should_be)

    def test_make_move_8(self):
        game = KalahGame([3, 1, 1, 0, 1, 1], [2, 1, 3, 1, 4, 4], Side.SOUTH)
        game.make_move(0)
        game.assertCorrect()
        should_be = KalahGame([0, 2, 2, 0, 1, 1], [2, 1, 0, 1, 4, 4], Side.NORTH, 4, 0)
        self.assertGamesEqual(game, should_be)

    def test_make_move_9(self):
        game = KalahGame([1, 2, 3, 4, 5, 6], [1, 0, 3, 13, 2, 4], Side.NORTH)
        game.make_move(3)
        print(game.to_string())
        game.assertCorrect()
        should_be = KalahGame([2, 3, 0, 5, 6, 7], [2, 1, 4, 0, 3, 5], Side.SOUTH, 0, 6)
        self.assertGamesEqual(game, should_be)

    def test_make_move_10(self):
        game = KalahGame([0, 2, 0, 8], [1, 0, 0, 0], Side.NORTH, 8, 13)
        (finished, res) = game.make_move(0)
        self.assertEqual(finished, False)
        should_be = KalahGame([0, 2, 0, 8], [0, 1, 0, 0], Side.SOUTH, 8, 13)
        self.assertGamesEqual(game, should_be)

    def test_make_move_11(self):
        game = KalahGame([0, 2, 6, 6], [5, 0, 5, 5], Side.NORTH, 1, 2)
        (finished, res) = game.make_move(3)
        print(game.to_string())
        game.assertCorrect()
        should_be = KalahGame([1, 3, 7, 7], [5, 0, 5, 0], Side.SOUTH, 1, 3)
        self.assertGamesEqual(game, should_be)

    def testGameEndCondition1(self):
        game = KalahGame([1, 2, 1, 3, 1, 4], [0, 0, 0, 0, 0, 1], Side.NORTH)
        (finished, res) = game.make_move(5)
        self.assertEqual(finished, True)
        self.assertEqual(res, 1)

    def testGameEndCondition2(self):
        game = KalahGame([1, 2, 3, 4, 5, 6], [1, 0, 3, 13, 2, 4], Side.NORTH, 0, 35)
        (finished, res) = game.make_move(3)
        print(game.to_string())
        game.assertCorrect()
        self.assertEqual(finished, True)
        self.assertEqual(res, -1)

    def testOppositePit(self):
        game = KalahGame([1, 2, 3, 4, 5, 6], [1, 0, 3, 13, 2, 4], Side.NORTH)
        self.assertEqual(game.opposite_pit(0), 5)
        self.assertEqual(game.opposite_pit(1), 4)
        self.assertEqual(game.opposite_pit(2), 3)
        self.assertEqual(game.opposite_pit(3), 2)
        self.assertEqual(game.opposite_pit(4), 1)
        self.assertEqual(game.opposite_pit(5), 0)
        

def main():
    ut.main()


if __name__ == '__main__':
    main()





