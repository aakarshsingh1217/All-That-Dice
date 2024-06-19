# File: testMaxi.py
# Description: Test code for Maxi
# Author: Aakarsh Singh
# Email: aak444@icloud.com

import unittest
from unittest.mock import patch
from allThatDice import AllThatDice, Maxi

class TestMaxi(unittest.TestCase):
    """
    Test cases for the Maxi class in the AllThatDice module.

    These tests cover the functionality of the Maxi dice game,
    including dice rolling, scoring, payout, and updating game statistics.

    Methods:
        setUp: Sets up test environment for each method tested.
        test_dice_rolling: Test the dice rolling and scoring mechanism in the Maxi game.
        test_payout_and_statistics: Test the payout and statistics updating mechanism in the Maxi game.

    """
    def setUp(self):
        """
        Set up test environment for each test method.

        Initializes a Maxi game with three players and sets up
        necessary attributes for testing.
        """
        print("\nRunning setUp method...")
        self.players = [AllThatDice.Player("Alan"), 
                        AllThatDice.Player("Steve"),
                        AllThatDice.Player("Bob")]
        self.maxi = Maxi(3, 5, self.players, 2)

    @patch('random.randint', return_value=3)
    @patch('allThatDice.DiceGame.Dice.getStrengthInput', return_value=3)
    def test_dice_rolling(self, mock_getStrengthInput, mock_randint):
        """
        Test the dice rolling and scoring mechanism in the Maxi game.

        Uses patch decorators to mock random.randint and Dice.getStrengthInput methods,
        ensuring a predictable and testable outcome for dice rolls.
        
        Args:
            mock_getStrengthInput (MagicMock): Mocks the method that gets strength input from players (3).
            mock_randint (MagicMock): Mocks the random number generator to always return a fixed value (3).
        """
        player = self.players[0]
        score = self.maxi.rollsAndScore(player)
        expected_score = 12  # Expected score based on the mocked dice rolls, which each have a value of 6
        self.assertEqual(score, expected_score)

    def test_payout_and_statistics(self):
        """
        Test the payout and statistics updating mechanism in the Maxi game.

        Verifies if the game correctly updates the winner's chips and the games won count
        after a game round is completed.
        """
        self.maxi.setChipsBid(60) # Total chips bid in the game
        self.players[0].bidChips(20) # Alan bids 20 chips
        self.maxi.setWinner(self.players[0]) # Alan set as the winner
        self.maxi.payoutAndStatistics() # Call payoutAndStatistics method of Maxi class

        self.assertEqual(self.players[0].getChips(), 140)  # Alan should win his own bid back and other player's bids
        self.assertEqual(self.players[0].getGamesWon(), 1)  # Alan's win counter should be incremented by 1

if __name__ == '__main__':
    unittest.main()