class Game:
    options = {
        "1": "Rock",
        "2": "Scissors",
        "3": "Paper",
    }
    systemCalls = ["exit"]
    comparison = {
        "Rock": {"Rock": "Draw", "Scissors": "Win", "Paper": "Loss", },
        "Scissors": {"Rock": "Loss", "Scissors": "Draw", "Paper": "Win", },
        "Paper": {"Rock": "Win", "Scissors": "Loss", "Paper": "Draw", },
    }
    resultLabel = {"Win": "CONGRATULATIONS, YOU WON =)", "Loss": "SORRY, BUT YOU LOSS =(", "Draw": "OKAY, IT'S DRAW "
                                                                                                   "=|"}

    def playGame(self, chosenPlayer, chosenEnemy):
        if self.inputVerify(chosenPlayer):
            gameResult = self.playCompare(self.pick(chosenPlayer), self.pick(chosenEnemy))
            self.resultPrint(gameResult)

    def playCompare(self, playerOption, enemyOption):
        return self.comparison[playerOption][enemyOption]

    def resultPrint(self, result):
        print(self.resultLabel[result])

    def pick(self, pick):
        choose = self.options[pick]
        print(choose)
        return choose

    def inputVerify(self, inputPlayer):
        if inputPlayer in self.options:
            return inputPlayer
        elif inputPlayer in self.systemCalls:
            print("SYSTEM CALL DETECTED")
            return None
        else:
            print("WRONG INPUT")
            return None
