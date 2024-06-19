# File: testOddOrEven.py
# Description: Test code for OddOrEven.
# Author: Aakarsh Singh
# Email: aak444@icloud.com

import unittest
from unittest.mock import patch
from allThatDice import OddOrEven, AllThatDice

class Test_OddOrEven(unittest.TestCase):
    """
    A suite of unit tests for the OddOrEven class in the AllThatDice module.
    These tests validate the game's logic, especially for handling user inputs,
    and the correct update of game statistics and payouts.
    """
    def setUp(self):
        """
        Set up test conditions before each test is executed.

        This setup initializes an OddOrEven game instance with a single player
        and configures necessary game settings for testing purposes.
        """
        self.playerList = [AllThatDice.Player("Alan")]
        self.playerList[0].bidChips(50)
        self.oddOrEven = OddOrEven(1, 1, self.playerList, 1)
        self.oddOrEven.setWinner(self.playerList[0])
        self.oddOrEven.addInitialPlayerBids(self.playerList[0].getName(), 50)
        self.oddOrEven.setChipsBid(50)

    @patch('builtins.input', side_effect=["invalid_input", "o", 3])
    @patch('builtins.print')
    def test_play_game_invalid_input(self, mock_print, mock_input):
        """
        Test the playGame method for handling invalid inputs.

        This test uses the patch decorator to simulate user input and capture print statements.
        It asserts whether the game correctly identifies and notifies about invalid inputs.
        
        Args:
            mock_print (MagicMock): Mock object for built-in print function.
            mock_input (MagicMock): Mock object for built-in input function. The side_effect attribute
                                    is used to simulate a sequence of user inputs, first invalid and then
                                    2 valid inputs.
        """
        self.oddOrEven.playGame()
        """
        Check if "Invalid choice." was part of any print call.
        The any() function checks if any of the calls to the print function
        contained "Invalid choice." in their arguments.
        mock_print.call_args_list holds all the arguments with which print() was called.
        call_arg[0][0] refers to the first argument of each print call.
        """

        invalid_choice_found = any("Invalid choice." in str(call_arg[0][0]) for call_arg in mock_print.call_args_list)
        self.assertTrue(invalid_choice_found, "Invalid choice. was not printed")
        
        # Assert that "Invalid choice." was found among the print calls.
        # If not found, the test will fail with the message "Invalid choice. was not printed".

    def test_payout_and_statistics(self):
        """
        Test the payoutAndStatistics method for its correctness.

        This method asserts the correct update of a player's chips and games won after a round of OddOrEven.
        """
        self.oddOrEven.payoutAndStatistics()
        self.assertEqual(self.playerList[0].getChips(), 200)
        self.assertEqual(self.playerList[0].getGamesWon(), 1)

if __name__ == '__main__':
    unittest.main()
