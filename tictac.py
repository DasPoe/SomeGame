gb = ['   1', '  2', '  3', 
   '1 ', '[_]', '[_]', '[_]',
   '2 ', '[_]', '[_]', '[_]', 
   '3 ', '[_]', '[_]', '[_]']

xy = {'x1y1':gb[12], 'x2y1':gb[13], 'x3y1':gb[14],
      'x1y2': gb[12], 'x2y2':gb[13], 'x3y2':gb[14],
      'x1y3': gb[12], 'x2y3':gb[13], 'x3y3':gb[14],}

def gameBoard():
    print(''.join(gb[0:3]))
    print(''.join(gb[3:7]))
    print(''.join(gb[7:11]))
    print(''.join(gb[11:15]))


def startGame():
    start = False
    if start == False:
        print("\nWould you like to start?\n")
        start_choice = input(">")
        if start_choice.lower() == "yes" or start_choice == 'ok':
            start = True
            return start
        elif start_choice.lower() == "no":
            print("\nGoodbye.")
            quit()
        else:
            print("\nI don't understand. Try again.")
            startGame()

gameBoard()
startGame()
