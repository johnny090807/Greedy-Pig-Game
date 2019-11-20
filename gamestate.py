import player, random

class GameState:
    def __init__(self):
        self.__difficulty = 0
        self.__amountOfPlayers = 0
        self.__maxPoints = 0
        self.__players = []
        self.__round = 0
        self.startGame()

    def startGame(self):
        print("********************************************")
        print("Welcome to GAME OF PIG")
        print("********************************************")
        print("To start the game, please set up the game:\n")
        running = True
        while running:
            difficulty = input("Please choose the mode of the game: '1': Beginners '2': Advanced ---  ")
            try:
                if int(difficulty) == 1 or int(difficulty) == 2:
                    self.__difficulty = difficulty
                    running = False
                else:
                    print("That wasnt right.")
            except:
                print("That wasnt right.")

        amountPlayerCheck = [2, 3, 4, 5, 6]
        running = True
        while running:
            amountOfPlayers = input("Please enter the number of players (2-6): ")
            for i in amountPlayerCheck:
                try:
                    if int(amountOfPlayers) == i:
                        self.__amountOfPlayers = int(amountOfPlayers)
                        running = False
                except:
                    print("That wasnt right.")
                    break
        if int(difficulty) == 1:
            self.__maxPoints = 50
        else:
            self.__maxPoints = 100

        for i in range(1, self.__amountOfPlayers + 1):
            playerName = input("enter the name of player " + str(i) + ": ")
            self.__players.append(player.Player(playerName))
        self.startRound()

    def startRound(self):
        playing = True
        while playing:
            for i in range(len(self.__players)):
                running = True
                while running:
                    player = self.__players[i]
                    alive = True
                    self.printAllPlayerScores()
                    print("Current Player: " + player.getName() +
                          "\nYour score at this turn: " + str(player.getCurrentPoints()) + "\n")
                    if self.__round == 0:
                        print(player.getName()+" your first dice at this turn will be automatically rolled!")
                        print("\nready?\n")
                        input("press enter to continue... ")
                        alive = self.rollTheDice(player)
                        if alive:
                            running = True
                            self.__round += 1
                        else:
                            running = False
                            self.__round = 0
                    else:
                        choiceMade = False
                        while not choiceMade:
                            choice = input(
                                player.getName() + " choose your next decision: 'r' to roll the dice  "
                                "'p': pass the turn and save your score:\n")
                            if choice == 'r':
                                alive = self.rollTheDice(player)
                                choiceMade = True
                                if alive:
                                    running = True
                                    self.__round += 1
                                else:
                                    running = False
                                    self.__round = 0
                            elif choice == 'p':
                                player.addCurrentPointstoSavedPoints()
                                if int(i+2) > len(self.__players):
                                    print("Pass the dice over to " + self.__players[0].getName())
                                else:
                                    print("Pass the dice over to " + self.__players[i+1].getName())

                                self.__round = 0
                                choiceMade = True
                                running = False
                                break
                    if player.getSavedPoints() >= self.__maxPoints:
                        playing = False
                        print(player.getName() + " won the game with a score of " + str(player.getCurrentPoints() + player.getSavedPoints()))
                        return

    def rollTheDice(self, player):
        diceRoll = random.randint(1, 6)
        print("*******************************")
        print("********** " + "Rolled " + str(diceRoll) + " ***********")
        print("*******************************")
        if diceRoll > 1:
            print("new collected score = " + str(player.getCurrentPoints()) + " + " +  str(diceRoll) + " = " + str(player.getCurrentPoints() + diceRoll))
            player.addPointsToCurrentPoints(diceRoll)
            return True
        else:
            print("Oops! you lose your " + str(player.getCurrentPoints()) + " but still keep your previous " + str(player.getSavedPoints()))
            player.resetCurrentPoints()
            return False

    def printAllPlayerScores(self):
        print("=======================================")
        print("Total saved scores:")
        for i in range(len(self.__players)):
            print(self.__players[i].getName(), '=', self.__players[i].getSavedPoints())
        print('---------------------------------------')
