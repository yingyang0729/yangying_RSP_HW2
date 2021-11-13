from random import randint
from gameComponents import winlose, gameVars, what


# set up our game loop so that we can keep playing and not exit
while gameVars.player is False:
    print("\033[1;33;40m==================*/ RPS GAME /*====================")
    print("\033[1;33;40m====================================================")
    gameVars.player = input("\033[1;33;40m choose your weapon: rock,paper or scissors:")
    gameVars.computer = gameVars.choices[randint(0,2)]

    print("\033[1;34;40m player chose: " + gameVars.player)
    print("\033[1;34;40m computer chose: " + gameVars.computer)
    
    gameVars = what.whoWinAtThisRound(gameVars)

    print("player life count:" + str(gameVars.playerLives))
    print("computer life count:" + str(gameVars.computerLives))

    if gameVars.playerLives == 0:
        winlose.winorlose("lost")  

    elif gameVars.computerLives == 0:
        winlose.winorlose("you won!")
    
    print("")
    gameVars.player = False
