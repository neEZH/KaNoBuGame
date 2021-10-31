import os
from rules import Game
import enemy
clear = lambda: os.system('cls')
clear()
# Here is welcome screen

print("RULES\nRock > Scissors > Paper > Rock")
print("Select your choose:\n1. Rock\n2. Scissors\n3. Paper\nType \"exit\" to "
      "exit game")
# Here is rules explanation

# Here goes game cycle
ifPlay = True
play = Game()
while ifPlay:
    print("\nTurnStarts")
    turn = input("Your choose: ")
    if turn == "exit":
        ifPlay = False
    else:
        enemyChoose = enemy.enemyTurn()
        print("Enemy choose: " + enemyChoose)
        play.playGame(turn, enemyChoose)

