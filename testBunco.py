# File: testBunco.py
# Description: Test code for Bunco.
# Author: Aakarsh Singh
# Email: aak444@icloud.com

import unittest
from allThatDice import AllThatDice, Bunco

class Test_Bunco(unittest.TestCase):
    """
    Test cases for the Bunco class in the AllThatDice module.

    This test suite checks the functionality of the Bunco game mechanics, 
    including score calculation and game outcome processing.
    """
    def setUp(self):
        """
        Set up the test environment for each test method.

        Initializes an instance of Bunco game with two players and sets 
        up the necessary attributes for testing.
        """
        self.players = [AllThatDice.Player("Alan"),
                        AllThatDice.Player("Steve")]
        self.bunco = Bunco(2, 4, self.players, 3)

    def test_calculate_score(self):
        """
        Test the calculateScore method of the Bunco class.

        Verifies if the method accurately calculates scores based on the dice values 
        and the current round number.
        """
        roundNumber = 2
        diceValues1 = [2, 2, 2] # All 3 match the round number, a Bunco (21 point)
        diceValues2 = [5, 5, 5] # All 3 have the same value, which is 5 points
        diceValues3 = [2, 2, 4] # 2 match the round number, which is 2 points
        diceValues4 = [1, 1, 3] # None match the round number and aren't all the same, 0 points

        # Now checks calculateScore method of Bunco to see if the right number of points are returned
        self.assertEqual(self.bunco.calculateScore(diceValues1, roundNumber), 21)
        self.assertEqual(self.bunco.calculateScore(diceValues2, roundNumber), 5)
        self.assertEqual(self.bunco.calculateScore(diceValues3, roundNumber), 2)
        self.assertEqual(self.bunco.calculateScore(diceValues4, roundNumber), 0)

    def test_payout_and_statistics(self):
        """
        Test the payoutAndStatistics method of the Bunco class.

        Verifies if the method correctly updates the winner's chips and games won 
        after a game is concluded.

        Returns:
            None
        """
        self.bunco.setChipsBid(60) # Total chips in the pot
        self.players[0].bidChips(20) # Alan bids 20 chips
        self.bunco.setWinner(self.players[0]) # Alan set as winner of Bunco
        self.bunco.payoutAndStatistics() # Perform payout and update statistics

        self.assertEqual(self.players[0].getChips(), 140)  # Alan should win his own bid back and other player's bids
                                                           # (which is 60 chips).
        self.assertEqual(self.players[0].getGamesWon(), 1) # Alan's win counter should be incremented by 1.
        self.assertEqual(self.players[0].getGamesPlayed(), 1)

if __name__ == '__main__':
    unittest.main()