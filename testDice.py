# File: testDice.py
# Description: Test code for Dice.
# Author: Aakarsh Singh
# Email: aak444@icloud.com

import unittest
from unittest.mock import patch
from allThatDice import DiceGame

class Test_Dice(unittest.TestCase):
    """
    Test cases for the Dice nested class within the DiceGame class of the AllThatDice module.

    These tests verify the functionality of the Dice class methods, including 
    getting the dice value based on a symbol and checking if the result is odd or even.
    """
    @patch("allThatDice.DiceGame.__abstractmethods__", set())
    def setUp(self):
        """
        Set up the test environment before each test.

        Initializes a Dice instance from the DiceGame class. The patch decorator
        is used to bypass the abstract methods in the DiceGame class to allow 
        instantiation of the Dice nested class.
        """
        self.dice = DiceGame.Dice()

    def test_get_dice_value(self):
        """
        Test the getDiceValue method of the Dice class.

        Asserts that the method correctly returns the numerical value for a given dice symbol.
        """
        self.assertEqual(self.dice.getDiceValue('⚀'), 1)

    def test_check_odd_or_even(self):
        """
        Test the checkOddOrEven method of the Dice class.

        Asserts that the method correctly determines whether the value of a given dice symbol is odd or even.
        """
        # Passes because the dice face passed into checkOddOrEven is 3, which is an odd number and returns 'odd'.
        self.assertEqual(self.dice.checkOddOrEven('⚂'), 'odd')

if __name__ == '__main__':
    unittest.main()