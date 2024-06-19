# File: allThatDice.py
# Description: Class codes for AllThatDice and main code.
# Author: Aakarsh Singh
# Email: aak444@icloud.com

from abc import ABC, abstractmethod
import random

class AllThatDice:
    """
    This class runs the AllThatDice application and allows users to register and play either OddOrEven, Maxi or Bunco.
    It houses two nested classes which have a composition relationship with it, Player (which houses player details 
    and chips to be bid when playing dice games) and Leaderboard (which shows player statistics).

    Attributes:
        players (list): A list of registered player objects.
    
    Methods:
        menu: Displays the main menu.
        run: Runs the application.
        registerPlayer: Registers a new player.
        playGame: Initiates a game.
        addPlayers: Adds players to a game.
    """
    class Player:
        """
        Represents a player in the AllThatDice game.

        Attributes:
            name (str): Player's name.
            chips (int): Number of chips player has.
            gamesPlayed (int): Number of games played.
            gamesWon (int): Number of games won.
        
        Methods:
            getName: Returns the player's name.
            increaseGamesPlayed: Increments the number of games played.
            getGamesPlayed: Returns the number of games played.
            getGamesWon: Returns the number of games won.
            increaseGamesWon: Increments the number of games won.
            getChips: Returns the number of chips.
            bidChips: Bids a number of chips.
            increaseChips: Increases the number of chips.
        """
        def __init__(self, name, chips=100):
            """
            Initializes a new player with a name and an initial number of chips.

            Args:
                name (str): The name of the player.
                chips (int, optional): The initial number of chips. Defaults to 100.
            """
            self.__name = name
            self.__chips = chips
            self.__gamesPlayed = 0
            self.__gamesWon = 0

        def getName(self):
            """
            Gets the name of the player.

            Returns:
                str: The name of the player.
            """
            return self.__name
        
        def increaseGamesPlayed(self):
            """
            Increments the count of games played by the player by one.
            """
            self.__gamesPlayed += 1

        def getGamesPlayed(self):
            """
            Gets the total number of games played by the player.

            Returns:
                int: The total number of games played.
            """
            return self.__gamesPlayed
        
        def getGamesWon(self):
            """
            Gets the total number of games won by the player.

            Returns:
                int: The total number of games won.
            """
            return self.__gamesWon

        def increaseGamesWon(self):
            """
            Increments the count of games won by the player by one.
            """
            self.__gamesWon += 1
        
        def getChips(self):
            """
            Gets the current number of chips the player has.

            Returns:
                int: The current number of chips.
            """
            return self.__chips
        
        def bidChips(self, numOfChips):
            """
            Bids a specified number of chips, deducting them from the player's total.

            Args:
                numOfChips (int): The number of chips to bid.

            Returns:
                bool: True if the bid is successful, False otherwise.
            """
            if numOfChips < 0:
                return False
            elif numOfChips <= self.__chips:
                self.__chips -= numOfChips
                return True
            else:
                return False
            
        def increaseChips(self, numOfChips):
            """
            Increases the player's chip count by a specified number.

            Args:
                numOfChips (int): The number of chips to add.
            """
            self.__chips += numOfChips

    class Leaderboard:
        """
        Represents the leaderboard in the AllThatDice game. 
        This class is responsible for displaying the player statistics based on their performance.

        Attributes:
            players (list): A list of registered player objects.
            sortedPlayers (list): A list of players sorted based on their chips and winning rate.

        Methods:
            display: Displays the leaderboard with player statistics.
            winning_rate: Calculates the winning rate of a player.
        """
        def __init__(self, players):
            """
            Initializes the Leaderboard with a list of players.

            Args:
                players (list): A list of Player objects representing the registered players.
            """
            self.__players = players
            # Sort players by chips in descending order (-p.getChips())
            # If chips are equal, sort by winning rate in descending order (-self.winning_rate(p))
            # Use lambda function for custom sorting criteria
            # Result is a sorted list of players for the leaderboard
            self.__sortedPlayers = sorted(self.__players, key=lambda p: (-p.getChips(), -self.winning_rate(p)))

        def display(self):
            """
            Displays the leaderboard showing player names, games played, games won, and chips.
            The leaderboard is sorted by the number of chips and then by the winning rate.
            """
            print("==============================")
            print("Name    Played    Won    Chips")
            print("==============================")
            for player in self.__sortedPlayers:
                print(f"{player.getName():<13}{player.getGamesPlayed():<7}{player.getGamesWon():<6}{player.getChips():<8}")
            print("==============================")

        def winning_rate(self, player):
            """
            Calculates the winning rate of a player.

            Args:
                player (Player): The player for whom the winning rate is to be calculated.

            Returns:
                float: The winning rate of the player. It is calculated as games won divided by games played.
            """
            if player.getGamesPlayed() == 0:
                return 0
            return player.getGamesWon() / player.getGamesPlayed()

    def __init__(self):
        """
        Initializes the AllThatDice game with an empty list of players.
        """
        self.__players = []

    def menu(self):
        """
        Prints the main menu options to the console.
        """
        print("\nWhat would you like to do?")
        print(" (r) register a new player")
        print(" (s) show the leader board")
        print(" (p) play a game")
        print(" (q) quit")

    def run(self):
        """
        Runs the main loop of the application. Allows users to choose from different options such as registering a new player, 
        playing a game, viewing the leaderboard, or quitting the application.
        """
        print("\nWelcome to All-That-Dice!")
        print("Developed by Aakarsh Singh")

        while True:
            self.menu()
            userInput = input("> ")
            
            try:
                if userInput == "q":
                    print("Thank you for playing All-That-Dice!")
                    break
                elif userInput == "r":
                    self.registerPlayer()
                elif userInput == "s":
                    self.showLeaderBoard()
                elif userInput == "p":
                    self.playGame()
                else:
                    raise ValueError("Please enter either r, s, p or q")
            except ValueError as e:
                print(e)

    def showLeaderBoard(self):
        """
        Displays the leaderboard if there are registered players. The leaderboard shows player names, games played, games won, and chips.
        """
        if len(self.__players) >= 1:
            leaderboard = self.Leaderboard(self.__players)
            leaderboard.display()
            return True
        else:
            print("No players yet!")

    def registerPlayer(self):
        """
        Registers a new player in the game. It prompts the user for a player name and ensures the uniqueness of the name.
        Raises a ValueError if the entered name is empty, non-alphabetic, or already taken.
        """
        try:
            name = input("What is the name of the new player?\n> ").strip()
            if not name:
                raise ValueError("The name cannot be empty.")

            if not all(part.isalpha() for part in name.split()):
                raise ValueError("Name must contain only letters and spaces.")

            # Check for name uniqueness
            for player in self.__players:
                if player.getName().lower() == name.lower():
                    raise ValueError("Sorry, the name is already taken.")
            
            self.__players.append(self.Player(name))
            print(f'Welcome, {name}!')
        except (ValueError) as e:
                print(e)

    def playGame(self):
        """
        Initiates the game selection process. Players choose which game to play: OddOrEven, Maxi, or Bunco.
        Raises a ValueError if an invalid option is chosen.
        """
        print("Which game would you like to play?")
        print("(o) Odd-or-Even")
        print("(m) Maxi")
        print("(b) Bunco")
        gameChoice = input("> ")

        try:
            if gameChoice == "o":
                game = OddOrEven(1, 1, self.__players, 1)
            elif gameChoice == "m":
                game = Maxi(3, 5, self.__players, 2)
            elif gameChoice == "b":
                game = Bunco(2, 4, self.__players, 3)
            else:
                raise ValueError("Please enter o, m, or b only.")
        except ValueError as e:
            print(e)
            return

        print(f"Let's play the game of {game.__class__.__name__}!")
        self.addPlayers(game)

    def addPlayers(self, game):
        """
        Adds players to a selected game. It prompts the user to specify the number of players and their names.
        It also handles chip bidding for the game.

        Args:
            game (DiceGame): The game to which players are to be added.
        """
        while True:
            try:
                print(f"How many players ({game.getMinPlayers()}-{game.getMaxPlayers()})?")
                numOfPlayers = int(input("> "))

                if numOfPlayers < game.getMinPlayers() or numOfPlayers > game.getMaxPlayers():
                    raise Exception
                break
            except ValueError:
                print("Please enter a number into the input only!")
            except Exception:
                print(f"Enter a value between {game.getMinPlayers()} and {game.getMaxPlayers()}!")

        players = []
        chipsBid = 0

        # Loop over each player number up to the number of players needed for the game
        for playerNumber in range(numOfPlayers):
            playerAdded = False  # Flag to indicate if a player has been successfully added to the game

            # Continue looping until a player is successfully added
            while not playerAdded:
                try:
                    print(f"What is the name of player #{playerNumber + 1}")
                    name = input("> ").strip()

                    # Check if the name is valid (only letters and spaces)
                    if not all(part.isalpha() for part in name.split()):
                        raise ValueError("Name must contain only letters and spaces.")
                    
                    # Check if the player is already registered in the game
                    player = None
                    for playerObject in self.__players:
                        if playerObject.getName() == name:
                            player = playerObject
                            break
                    
                    # Handle scenarios based on the player's existence and status
                    if player is None:
                        print(f"There is no player named {name}")
                    elif player in players:
                        print(f"{name} is already in the game.")
                    else:
                        # Player is valid and not yet in the game, proceed with chip bidding
                        if player.getChips() > 0:
                            # Loop for chip bidding
                            while True:
                                try:
                                    print(f"How many chips would you bid {name} (1-{player.getChips()})?")
                                    chips = int(input("> "))

                                    # Check if the bid is valid and add the player if so
                                    if player.bidChips(chips):
                                        players.append(player)
                                        playerAdded = True  # Set flag to true as player is successfully added
                                        chipsBid += chips # Add to the total chips bid in the game
                                        game.addInitialPlayerBids(player.getName(), chipsBid)
                                        break
                                    else:
                                        print("Invalid number of chips.")
                                except ValueError:
                                    print("Enter an integer only when bidding chips!")
                        else:
                            # Player has no chips to bid and cannot play
                            print(f"No chips to bid {player.getName()}! You cannot play!")
                            break  # Exit the loop as the player cannot participate
                except ValueError as e:
                    print(e)

        # After adding all players, check if the game has enough players to start
        if len(players) < game.getMinPlayers():
            print(f"Not enough players with chips to play {game.__class__.__name__}. Need at least {game.getMinPlayers()} player/s.")
        else:
            # Set the players and start the game if enough players are present
            game.setPlayers(players)
            game.setChipsBid(chipsBid)
            game.playGame()

class DiceGame(ABC):
    """
    Abstract base class for dice games in the AllThatDice application.

    Attributes:
        minimumPlayers (int): Minimum number of players required for the game.
        maximumPlayers (int): Maximum number of players allowed in the game.
        players (list): List of Player objects participating in the game.
        numberOfDice (int): Number of dice used in the game.
        chipsBid (int): Total number of chips bid in the game.
        initialPlayerBids (dict): Mapping of player names to their initial bids.
        winner (Player): The player who wins the game.

    Methods:
        playGame: Abstract method to start and play the game.
        payoutAndStatistics: Abstract method to handle payouts and update player statistics.
        setWinner: Sets the winner of the game.
        getWinner: Returns the winner of the game.
        getInitialBid: Returns the initial bid of a specified player.
        addInitialPlayerBids: Records the initial bid of a player.
        checkInitialPlayers: Checks if the required minimum number of players is met.
        setPlayers: Sets the players participating in the game.
        getMinPlayers: Returns the minimum number of players required.
        getMaxPlayers: Returns the maximum number of players allowed.
        getChipsBid: Returns the total number of chips bid in the game.
        setChipsBid: Sets the total number of chips bid in the game.
        getPlayerList: Returns the list of players in the game.
        getNumberOfDice: Returns the number of dice used in the game.
    """

    def __init__(self, minimumPlayers, maximumPlayers, players, numberOfDice):
        """
        Initializes a new DiceGame with specified parameters.

        Args:
            minimumPlayers (int): The minimum number of players required to start the game.
            maximumPlayers (int): The maximum number of players allowed in the game.
            players (list): The list of Player objects who will participate in the game.
            numberOfDice (int): The number of dice to be used in the game.
        """
        self.__minimumPlayers = minimumPlayers
        self.__maximumPlayers = maximumPlayers
        self.__players = players
        self.__numberOfDice = numberOfDice
        self.__chipsBid = 0
        self.__initialPlayerBids = {}
        self.__winner = None

    @abstractmethod
    def playGame(self):
        """
        Abstract method that must be implemented in subclasses to start and play the game.
        """
        pass
    
    @abstractmethod
    def payoutAndStatistics(self):
        """
        Abstract method that must be implemented in subclasses to handle the distribution of chips 
        after the game and update player statistics like games played.
        """
        for player in self.getPlayerList():
            player.increaseGamesPlayed()

    def setWinner(self, winner):
        """
        Sets the winner of the game.

        Args:
            winner (Player): The player object who won the game.
        """
        self.__winner = winner

    def getWinner(self):
        """
        Returns the winner of the game.

        Returns:
            Player: The player who won the game.
        """
        return self.__winner
    
    def getInitialBid(self, playerName):
        """
        Retrieves the initial bid amount of a specified player.

        Args:
            playerName (str): The name of the player.

        Returns:
            int: The amount of chips initially bid by the player.
        """
        return self.__initialPlayerBids.get(playerName)

    def addInitialPlayerBids(self, playerName, initialBid):
        """
        Records the initial bid of a player.

        Args:
            playerName (str): The name of the player making the bid.
            initialBid (int): The amount of chips being bid by the player.
        """
        self.__initialPlayerBids[playerName] = initialBid

    def checkInitialPlayers(self):
        """
        Checks if the game has the minimum required number of players.

        Raises:
            ValueError: If the number of players is less than the minimum required.
        """
        if (len(self.__players) < self.__minimumPlayers):
            raise ValueError(f"Not enough players to play {self.__class__.__name__}")
        
    def setPlayers(self, playerList):
        """
        Sets the players who will participate in the game.

        Args:
            playerList (list): A list of Player objects participating in the game.
        """
        self.__players = playerList

    def getMinPlayers(self):
        """
        Returns the minimum number of players required for the game.

        Returns:
            int: The minimum number of players required.
        """
        return self.__minimumPlayers
    
    def getMaxPlayers(self):
        """
        Returns the maximum number of players allowed in the game.

        Returns:
            int: The maximum number of players allowed.
        """
        return self.__maximumPlayers
    
    def getChipsBid(self):
        """
        Returns the total number of chips bid in the game.

        Returns:
            int: The total number of chips bid.
        """
        return self.__chipsBid
    
    def setChipsBid(self, chipsBid):
        """
        Sets the total number of chips bid in the game.

        Args:
            chipsBid (int): The total number of chips bid.
        """
        self.__chipsBid = chipsBid

    def getPlayerList(self):
        """
        Returns the list of players participating in the game.

        Returns:
            list: A list of Player objects.
        """
        return self.__players
    
    def getNumberOfDice(self):
        """
        Returns the number of dice used in the game.

        Returns:
            int: The number of dice.
        """
        return self.__numberOfDice

    class Dice:
        """
        Represents a dice used in the DiceGame.

        Attributes:
            faces (dict): A dictionary mapping dice face symbols to their corresponding values.

        Methods:
            getStrengthInput: Prompts the user to input the strength of the dice throw.
            rollDice: Rolls the dice based on the given strength input.
            getDiceValue: Returns the value of the dice based on the rolled symbol.
            checkOddOrEven: Determines if the value of the dice roll is odd or even.
        """
        def __init__(self):
            """
            Initializes a Dice object with predefined dice faces and their corresponding values.
            """
            self.__faces = {'⚀': 1, '⚁': 2, '⚂': 3, '⚃': 4, '⚄': 5, '⚅': 6}

        def getStrengthInput(self):
            """
            Prompts the user to input the strength of the dice throw.

            Returns:
                int: The strength level input by the user, ranging from 0 to 5.

            Raises:
                ValueError: If the input is not an integer within the specified range.
            """
            while True:
                try:
                    strength = int(input("How strong will you throw (0-5)?\n> "))
                    if not 0 <= strength <= 5:
                        raise ValueError("Invalid choice.")
                    break
                except ValueError as e:
                    print(e)
            
            return strength
        
        def rollDice(self, strengthInput):
            """
            Rolls the dice based on the given strength input and calculates the result.

            Args:
                strengthInput (int): The strength level used for the dice throw.

            Returns:
                str: The symbol of the dice face that is the result of the roll.
            """
            strength = strengthInput

            baseRoll = random.randint(1, 6)
            adjustedRoll = (baseRoll + strength)

            if adjustedRoll > 6:
                adjustedRoll %= 6

            for key, value in self.__faces.items():
                if value == adjustedRoll:
                    diceFace = key

            return diceFace
        
        def getDiceValue(self, diceSymbol):
            """
            Returns the numerical value of a given dice face symbol.

            Args:
                diceSymbol (str): The symbol of the dice face.

            Returns:
                int: The numerical value corresponding to the dice face symbol.
            """
            return self.__faces.get(diceSymbol, 0)
        
        def checkOddOrEven(self, diceSymbol):
            """
            Determines whether the value of a given dice roll is odd or even.

            Args:
                diceSymbol (str): The symbol of the dice face.

            Returns:
                str: 'even' if the dice value is even, 'odd' if it is odd.
            """
            diceValue = self.getDiceValue(diceSymbol)
            return 'even' if diceValue % 2 == 0 else 'odd'
            
class OddOrEven(DiceGame):
    """
    Represents the OddOrEven dice game, derived from the DiceGame class. In this game, players guess 
    whether the outcome of a dice roll will be odd or even.

    Inherits from:
        DiceGame: The abstract base class for dice games.

    Methods:
        playGame: Conducts the OddOrEven game, where each player guesses the outcome and rolls the dice.
        payoutAndStatistics: Handles the distribution of winnings and updates player statistics.
    """
    def __init__(self, minimumPlayers, maximumPlayers, players, numberOfDice):
        """
        Initializes the OddOrEven game with the specified number of players and dice.

        Args:
            minimumPlayers (int): Minimum number of players required for the game.
            maximumPlayers (int): Maximum number of players allowed in the game.
            players (list): List of Player objects participating in the game.
            numberOfDice (int): Number of dice to be used in the game.
        """
        super().__init__(minimumPlayers, maximumPlayers, players, numberOfDice)
        self.checkInitialPlayers()

    def playGame(self):
        """
        Conducts the OddOrEven game. Each player chooses either 'odd' or 'even', rolls the dice, 
        and checks if their guess matches the outcome. The winner is determined based on their guess and the dice roll.

        Overrides the abstract method from DiceGame.
        """
        for player in self.getPlayerList():
            while True:
                try:
                    # Prompt the player to choose either 'odd' or 'even'
                    choice = input(f"Hey {player.getName()}, Odd (o) or Even (e)?\n> ")
                    
                    # Validate the player's choice
                    if choice not in ['o', 'e']:
                        raise ValueError("Invalid choice.")
                    
                    # Exit the loop if the choice is valid
                    break
                except ValueError as e:
                    print(e)

            die = self.Dice()
            strengthInput = die.getStrengthInput()
            diceResult = die.rollDice(strengthInput)
            print(diceResult)

            # Determine if the player's choice matches the dice roll result
            if (choice == 'e' and die.checkOddOrEven(diceResult) == 'even') or \
               (choice == 'o' and die.checkOddOrEven(diceResult) == 'odd'):
                # Announce the player's victory and update payout and statistics
                print(f"Congratulations, {player.getName()}! You win!")
                self.setWinner(player)
                self.payoutAndStatistics()
            else:
                print(f"Sorry, {player.getName()}! You lose!")

    def payoutAndStatistics(self):
        """
        Handles the distribution of winnings based on the game's outcome and updates player statistics. 
        The winner recieve's their initial bid and gets double the chips they bid by 2.

        Overrides the abstract method from DiceGame.
        """
        super().payoutAndStatistics()
        winner = self.getWinner()
        initialPlayerBid = self.getInitialBid(winner.getName())
        winner.increaseChips(initialPlayerBid + (self.getChipsBid() * 2))
        winner.increaseGamesWon()

class Maxi(DiceGame):
    """
    Represents the Maxi dice game, derived from the DiceGame class. In Maxi, players roll a pair of dice,
    and the player with the highest sum of the face-up values wins the game. If there is a tie for the highest sum,
    the tied players continue playing until a winner is determined.

    Inherits from:
        DiceGame: The abstract base class for dice games.

    Attributes:
        minimumPlayers (int): Minimum number of players required for the game.
        maximumPlayers (int): Maximum number of players allowed in the game.
        players (list): List of Player objects participating in the game.
        numberOfDice (int): Number of dice to be used in the game (always 2 for Maxi).

    Methods:
        rollsAndScore: Conducts a dice roll for a player and calculates their score.
        playGame: Conducts the Maxi game, where each player rolls dice to achieve the highest score.
        payoutAndStatistics: Handles the distribution of winnings and updates player statistics.
    """
    def __init__(self, minimumPlayers, maximumPlayers, players, numberOfDice):
        """
        Initializes the Maxi game with the specified number of players and dice.

        Args:
            minimumPlayers (int): Minimum number of players required for the game.
            maximumPlayers (int): Maximum number of players allowed in the game.
            players (list): List of Player objects participating in the game.
            numberOfDice (int): Number of dice to be used in the game (always 2 for Maxi).
        """
        super().__init__(minimumPlayers, maximumPlayers, players, numberOfDice)
        self.checkInitialPlayers()

    def rollsAndScore(self, player):
        """
        Rolls a pair of dice for the given player and calculates their total score.

        Args:
            player (Player): The player object who is rolling the dice.

        Returns:
            int: The total score from the dice roll, which is the sum of the face values of the dice.
        """
        print(f"It's {player.getName()}'s turn.")
        die1 = self.Dice()
        die2 = self.Dice()
        strengthInput = die1.getStrengthInput()
        roll1 = die1.rollDice(strengthInput)
        roll2 = die2.rollDice(strengthInput)
        score = die1.getDiceValue(roll1) + die2.getDiceValue(roll2)
        print(f"{roll1} {roll2}")
        return score

    def playGame(self):
        """
        Conducts the Maxi game. Each player rolls a pair of dice, and the highest total score wins. 
        If there's a tie for the highest score, the tied players continue until a winner emerges.

        Overrides the abstract method from DiceGame.
        """
        print("Let the game begin!")
        currentPlayers = self.getPlayerList()

        while True:
            playersAndScores = {}
            highestScore = 0

            # Roll the dice for each player and calculate their score
            for player in currentPlayers:
                score = self.rollsAndScore(player)
                highestScore = max(highestScore, score) # highestScore keeps track of the highest dice roll total in the current round
                playersAndScores[player.getName()] = score

            # playersWithHighestScore is a list of player names who have scored the highest in this round
            playersWithHighestScore = [name for name, score in playersAndScores.items() if score == highestScore]

            # Check if the game has a clear winner or if a tiebreaker is needed
            if len(playersWithHighestScore) == 1:
                winnerName = playersWithHighestScore[0]
                print(f"Congratulations, {winnerName}! You win!")
                for player in self.getPlayerList():
                    if winnerName == player.getName():
                        self.setWinner(player)
                self.payoutAndStatistics()
                break
            else:
                # If there's a tie, print the names of the players who will continue in the tiebreaker
                print(f"Players remaining: {', '.join(playersWithHighestScore)}")

                # currentPlayers is updated to include only those players who are in the tiebreaker 
                # (those with the highest score from the previous round)
                currentPlayers = [player for player in self.getPlayerList() if player.getName() in playersWithHighestScore]

    def payoutAndStatistics(self):
        """
        Handles the distribution of winnings based on the game's outcome and updates player statistics. 
        The winner receives the total number of chips bid in the game.

        Overrides the abstract method from DiceGame.
        """
        super().payoutAndStatistics()
        winner = self.getWinner()
        winner.increaseChips(self.getChipsBid())
        winner.increaseGamesWon()

class Bunco(DiceGame):
    """
    Represents the Bunco dice game, a specific variant within the AllThatDice application. 
    Bunco is played over six rounds with each round corresponding to a number from 1 to 6. 
    Players take turns rolling three dice and earn points based on the values shown on the dice, 
    relative to the current round number. A "Bunco" occurs when all three dice match the round number, 
    awarding the player 21 points. The game aims to score 21 points in each round, and the player 
    who does so first wins the round. The overall game winner is determined by the number of rounds won, 
    total points scored, and the number of Buncos rolled.

    Inherits from:
        DiceGame: The abstract base class for dice games.

    Methods:
        playGame: Executes the game logic for Bunco, including rolling dice and scoring for each round.
        calculateScore: Calculates the score for a player based on their dice roll and the current round number.
        determineOverallWinner: Determines the overall winner of the game based on rounds won, total scores, and Buncos.
        displayLeaderboard: Displays the leaderboard showing the scores and Buncos for each player after all rounds.
        payoutAndStatistics: Handles the distribution of chips to the winner and updates player statistics.

    Overrides:
        playGame, payoutAndStatistics
    """
    def __init__(self, minimumPlayers, maximumPlayers, players, numberOfDice):
        """
        Initializes the Bunco game with the specified number of players and dice.

        Args:
            minimumPlayers (int): Minimum number of players required for the game.
            maximumPlayers (int): Maximum number of players allowed in the game.
            players (list): List of Player objects participating in the game.
            numberOfDice (int): Number of dice to be used in the game (always 3 for Bunco).
        """
        super().__init__(minimumPlayers, maximumPlayers, players, numberOfDice)
        self.checkInitialPlayers()

    def playGame(self):
        """
        Executes the main game logic for Bunco. Manages the game flow across six rounds, 
        tracks scores, and determines the winner of each round. Also handles the transition 
        between rounds and manages player turns.

        Overrides the abstract method from DiceGame.
        """
        roundWinners = []
        totalScores = {player.getName(): 0 for player in self.getPlayerList()}
        totalBuncos = {player.getName(): 0 for player in self.getPlayerList()}
        roundDetails = {player.getName(): [0] * 6 for player in self.getPlayerList()}  # Track round details

        for roundNumber in range(1, 7):
            print(f"\n<Round {roundNumber}>")
            roundScores = {player.getName(): 0 for player in self.getPlayerList()}
            currentPlayerIndex = (roundNumber - 1) % len(self.getPlayerList())

            while True:
                currentPlayer = self.getPlayerList()[currentPlayerIndex]
                print(f"It's {currentPlayer.getName()}'s turn.")

                while True:
                    die = self.Dice()
                    strengthInput = die.getStrengthInput()
                    diceResults = [die.rollDice(strengthInput) for _ in range(self.getNumberOfDice())]
                    diceValues = [die.getDiceValue(diceResult) for diceResult in diceResults]
                    print(" ".join(diceResults))

                    roundScore = self.calculateScore(diceValues, roundNumber)
                    roundScores[currentPlayer.getName()] += roundScore
                    totalScores[currentPlayer.getName()] += roundScore

                    if roundScore == 0:
                        print(f"You earned no points, {roundScores[currentPlayer.getName()]} points in total.")
                        break
                    else:
                        if roundScore == 21:
                            totalBuncos[currentPlayer.getName()] += 1
                            print("Bunco!")  # Print Bunco
                        print(f"You earned {roundScore} points, {roundScores[currentPlayer.getName()]} points in total.")

                        # If the player reaches or exceeds 21 points, they win the round
                        if roundScores[currentPlayer.getName()] >= 21:
                            print(f"{currentPlayer.getName()} is the winner in round {roundNumber}!")
                            roundWinners.append(currentPlayer.getName())
                            break  # Break out of the while loop for this player's turn
                        
                        print(f"Keep playing {currentPlayer.getName()}.")  # Keep playing message

                # Break out of the while loop for the round
                if roundScores[currentPlayer.getName()] >= 21:
                    break

                currentPlayerIndex = (currentPlayerIndex + 1) % len(self.getPlayerList())

            for playerName, score in roundScores.items():
                roundDetails[playerName][roundNumber - 1] = score  # Track round details

        self.displayLeaderboard(roundDetails, totalScores, totalBuncos)  # Display leaderboard
        overallWinner = self.determineOverallWinner(roundWinners, totalScores, totalBuncos)

        # Print winner's statistics
        print(f"\n{overallWinner} won {roundWinners.count(overallWinner)} rounds, scoring {totalScores[overallWinner]} points, with {totalBuncos[overallWinner]} Buncos.")
        print(f"Congratulations, {overallWinner}! You win!")  # Winner announcement

        for playerObject in self.getPlayerList():
            if overallWinner == playerObject.getName():
                self.setWinner(playerObject)

        self.payoutAndStatistics()

    def calculateScore(self, diceValues, roundNumber):
        """
        Executes the main game logic for Bunco. Manages the game flow across six rounds, 
        tracks scores, and determines the winner of each round. Also handles the transition 
        between rounds and manages player turns.

        Overrides the abstract method from DiceGame.
        """
        if diceValues.count(roundNumber) == 3:
            return 21  # Bunco
        elif diceValues[0] == diceValues[1] == diceValues[2]:
            return 5  # All dice match but not a Bunco
        else:
            return diceValues.count(roundNumber)

    def determineOverallWinner(self, roundWinners, totalScores, totalBuncos):
        """
        Determines the overall winner of the Bunco game based on the number of rounds won, 
        total scores, and Buncos. In case of a tie in rounds won, total scores and Buncos are used as tiebreakers.

        Args:
            roundWinners (list): A list of player names who won each round.
            totalScores (dict): A dictionary mapping player names to their total scores.
            totalBuncos (dict): A dictionary mapping player names to their total number of Buncos.

        Returns:
            str: The name of the overall winner.
        """
        roundWins = {player: roundWinners.count(player) for player in totalScores.keys()}
        maxRoundsWon = max(roundWins.values())
        potentialWinners = [player for player, wins in roundWins.items() if wins == maxRoundsWon]

        if len(potentialWinners) == 1:
            return potentialWinners[0]
        else:
            highestScore = max(totalScores[player] for player in potentialWinners)
            potentialWinners = [player for player in potentialWinners if totalScores[player] == highestScore]
            
            if len(potentialWinners) > 1:
                highestBuncos = max(totalBuncos[player] for player in potentialWinners)
                potentialWinners = [player for player in potentialWinners if totalBuncos[player] == highestBuncos]

            return potentialWinners[0]

    def displayLeaderboard(self, roundDetails, totalScores, totalBuncos):
        """
        Displays the leaderboard after all rounds of Bunco are complete. Shows round-wise scores, 
        total scores, and total Buncos for each player.

        Args:
            roundDetails (dict): A dictionary mapping player names to a list of their scores in each round.
            totalScores (dict): A dictionary mapping player names to their total scores.
            totalBuncos (dict): A dictionary mapping player names to their total number of Buncos.
        """
        print("======================================")
        print("Round", " ".join([name.center(6) for name in roundDetails.keys()]))
        print("======================================")
        for i in range(6):
            print(f"{i + 1:<6}", end="")
            for player in roundDetails.keys():
                print(f"{roundDetails[player][i]:<6}", end="")
            print()
        print("======================================")
        print("Total ", end="")
        for player in roundDetails.keys():
            print(f"{totalScores[player]:<6}", end="")
        print("\n======================================")
        print("Bunco ", end="")
        for player in roundDetails.keys():
            print(f"{totalBuncos[player]:<6}", end="")
        print("\n======================================")

    def payoutAndStatistics(self):
        """
        Handles the distribution of chips to the winner and updates player statistics at the end of the Bunco game.
        The winner is awarded the total number of chips bid in the game. Also, updates the games played and games 
        won statistics for each player.

        Overrides the abstract method from DiceGame.
        """
        super().payoutAndStatistics()
        winner = self.getWinner()
        winner.increaseChips(self.getChipsBid())
        winner.increaseGamesWon()


def main():
    my_all_that_dice = AllThatDice()
    my_all_that_dice.run()

if __name__ == '__main__':
    main()