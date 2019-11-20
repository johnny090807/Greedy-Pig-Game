class GameState:
    def __init__(self, players = [], difficulty = 0, amountOfPlayers = 0 , maxPoints = 0):
        self.__difficulty = difficulty
        self.__amountOfPlayers = amountOfPlayers
        self.__maxPoints = maxPoints
        self.__players = players
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
                        self.__amountOfPlayers = amountOfPlayers
                        running = False
                except:
                    print("That wasnt right.")
                    break
        if self.__difficulty == 1:
            self.__maxPoints = 50
        else:
            self.__maxPoints = 100

