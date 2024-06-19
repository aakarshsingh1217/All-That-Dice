# File: testPlayer.py
# Description: Test code for Player.
# Author: Aakarsh Singh
# Email: aak444@icloud.com

import unittest
from allThatDice import AllThatDice

class Test_Player(unittest.TestCase):
    """
    Test cases for the Player class in the AllThatDice module.

    Methods:
        setUp: Sets up test environment for each method tested.
        test_dice_rolling: Test the dice rolling and scoring mechanism in the Maxi game.
    """

    def setUp(self):
        """Set up test environment for each test method."""
        print("\nRunning setUp method...")

        self.player1 = AllThatDice.Player("Alan") # Create a player called Alan
        self.player2 = AllThatDice.Player("Steve") # Create a player called Steve

    def test_get_name(self):
        """Test the getName method of Player class."""
        print("Running test_get_name...")

        self.assertEqual(self.player1.getName(), "Alan") 
        self.assertEqual(self.player2.getName(), "Steve")

    def test_increase_chips_and_get_chips(self):
        """Test increaseChips and getChips methods of Player class."""
        print("Running test_increase_chips_and_get_chips...")

        self.player1.increaseChips(10)
        self.player2.increaseChips(20)

        self.assertEqual(self.player1.getChips(), 110)
        self.assertEqual(self.player2.getChips(), 120)

if __name__=='__main__':
	unittest.main()