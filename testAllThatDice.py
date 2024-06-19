# File: testAllThatDice.py
# Description: Test code for AllThatDice.
# Author: Aakarsh Singh
# Email: aak444@icloud.com

import unittest
from allThatDice import AllThatDice
from unittest.mock import patch

class Test_AllThatDice(unittest.TestCase):
    """
    Test cases for the AllThatDice class.

    This test suite checks the functionality of the AllThatDice application, 
    including player registration and game initiation processes.
    """
    def setUp(self):
        """
        Set up the test environment for each test method.

        Initializes an instance of the AllThatDice application for testing.
        """
        print("\nRunning setUp method...")
        self.allThatDice = AllThatDice()

    def test_register_player(self):
        """
        Test the registerPlayer method of AllThatDice.

        Simulates user input for player registration and verifies if the player 
        is correctly added to the application.
        """
        # Assuming the registerPlayer method interacts with the user via input
        # Mock the input to simulate user entering a valid name (Alan)
        print("Running test_register_player...")
        with patch('builtins.input', return_value="Alan"):
            self.allThatDice.registerPlayer()

            # Assuming the last player in the list is the one most recently added
            last_added_player = self.allThatDice._AllThatDice__players[-1]

            # Check if the player was added
            self.assertEqual(last_added_player.getName(), "Alan")

    @patch('builtins.input', side_effect=["invalid_input"])
    @patch('builtins.print')
    def test_play_game(self, mock_print, mock_input):
        """
        Test the playGame method of AllThatDice.

        Simulates user input for game selection and verifies the handling of invalid input.
        Uses patch decorators to mock user input and capture print output.

        Args:
            mock_print (Mock): Mock object for the print function.
            mock_input (Mock): Mock object for the input function.
        """
        self.allThatDice.playGame()
        invalid_input_found = any("Please enter o, m, or b only." in str(call_arg[0][0]) for call_arg in mock_print.call_args_list)
        self.assertTrue(invalid_input_found, "Please enter o, m, or b only. was not printed")
         

if __name__=='__main__':
	unittest.main()