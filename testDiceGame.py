# File: testDiceGame.py
# Description: Test code for DiceGame.
# Author: Aakarsh Singh
# Email: aak444@icloud.com

import unittest
from unittest.mock import patch
from allThatDice import AllThatDice, DiceGame

class Test_DiceGame(unittest.TestCase):
    """
    Test cases for the DiceGame class in the AllThatDice module.

    These tests validate the functionality of the abstract DiceGame class methods,
    including checking the payout and statistics updating, and ensuring the game
    has a sufficient number of players.
    """
    @patch("allThatDice.DiceGame.__abstractmethods__", set())
    def setUp(self):
        """
        Set up the test environment before each test.

        Initializes a DiceGame instance with a list of players. The patch decorator
        is used to bypass the abstract methods in the DiceGame class to allow instantiation.
        """
        self.allThatDice = AllThatDice()
        self.playerList = [AllThatDice.Player("Adam"),
                           AllThatDice.Player("Steve")]
        self.diceGame = DiceGame(3, 5, self.playerList, 1)
    
    def test_payout_and_statistics(self):
        """
        Test the payoutAndStatistics method of the DiceGame class.

        Asserts that the method correctly increments the games played for each player.
        """
        print("Running test_payout_and_statistics...")
        self.diceGame.payoutAndStatistics()

        self.assertEqual(self.playerList[0].getGamesPlayed(), 1)
        self.assertEqual(self.playerList[1].getGamesPlayed(), 1)

    def test_check_initial_players(self):
        """
        Test the checkInitialPlayers method of the DiceGame class.

        Asserts that the method raises a ValueError when the number of players
        is insufficient for the game to start.

        Raises:
            ValueError: If the number of players is less than the minimum required players.
        """
        print("Running test_check_initial_players")
        # This test passes because the minimum players passed in is 3, and only 2 players
        # are in the playerList passed into the DiceGame object.
        with self.assertRaises(ValueError):
            self.diceGame.checkInitialPlayers()

if __name__=='__main__':
    unittest.main()