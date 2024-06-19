# File: testLeaderboard.py
# Description: Test code for Leaderboard.
# Author: Aakarsh Singh
# Email: aak444@icloud.com

import unittest
from allThatDice import AllThatDice

class Test_Leaderboard(unittest.TestCase):
    """
    Test cases for the Leaderboard class in the AllThatDice module.

    These tests validate the leaderboard's functionality, including the calculation
    of winning rates and the correctness of the leaderboard sorting based on player statistics.
    """
    def setUp(self):
        """
        Set up the test environment before each test.

        Initializes a list of players and updates their statistics to set up 
        a leaderboard for testing.
        """
        print("\nRunning setUp method...")

        self.playerList = [AllThatDice.Player("Alan"),
                           AllThatDice.Player("Steve"),
                           AllThatDice.Player("Bob")]

        for player in self.playerList:
            if player.getName() == "Alan":
                for gamesPlayed in range(3): # 3 games played
                    player.increaseGamesPlayed()
                for gamesWon in range(3): # 3 games won
                    player.increaseGamesWon()
                player.increaseChips(50) # 150 chips

            if player.getName() == "Steve":
                for gamesPlayed in range(4): # 4 games played
                    player.increaseGamesPlayed()
                for gamesWon in range(2): # 2 games won
                    player.increaseGamesWon()
                player.increaseChips(100) # 100 chips

            if player.getName() == "Bob":
                for gamesPlayed in range(3): # 3 games played
                    player.increaseGamesPlayed()
                for gamesWon in range(2): # 2 games won
                    player.increaseGamesWon()
                player.increaseChips(50) # 150 chips

        self.leaderboard = AllThatDice.Leaderboard(self.playerList)

    def test_winning_rate(self):
        """
        Test the winning_rate method of the Leaderboard class.

        Asserts the correctness of the winning rate calculation for each player.
        """
        print("Running test_winning_rate...")

        self.assertEqual(self.leaderboard.winning_rate(self.playerList[0]), 3/3)
        self.assertEqual(self.leaderboard.winning_rate(self.playerList[1]), 2/4)
        self.assertEqual(self.leaderboard.winning_rate(self.playerList[2]), 2/3)

    def test_sorted_list(self):
        """
        Test the sorting functionality of the Leaderboard class.

        Validates that the players are correctly sorted in the leaderboard based on their
        chips and winning rates.
        """
        print("Running test_sorted_list...")

        sortedList = self.leaderboard._Leaderboard__sortedPlayers
        # The sorted list should have the player with the highest chips first (Steve),
        # and then sort by winning rate for players with the same chips,
        # (Alan and Bob have the same chips, but Alan has a better winning rate)
        testList = [self.playerList[1], self.playerList[0], self.playerList[2]]

        self.assertListEqual(sortedList, testList)

if __name__=='__main__':
	unittest.main()