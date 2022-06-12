def playGame(wordList):
    
    letterEntry = ""
    lastHand = ''
    while letterEntry != 'e':
        letterEntry = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if letterEntry not in 'nre':
            print('Invalid command.')
        else:
            if letterEntry == 'n':
               player = input('Enter u to have yourself play, c to have the computer play: ')
               if player == 'u':
                        lastHand = dealHand(HAND_SIZE)
                        playHand(lastHand,wordList,HAND_SIZE)
               else:
                        lastHand = compChooseWord(HAND_SIZE)
                        compPlayHand(lastHand,wordList,HAND_SIZE)
                        
            elif letterEntry == 'r':
               player = input('Enter u to have yourself play, c to have the computer play: ')
               if player =='u:'
                  if lastHand:
                    playHand(lastHand,wordList,HAND_SIZE)
                  else:
                    print('You have not played a hand yet. Please play a new hand first!')
               else:
                  if lastHand:
                    compPlayHand(lastHand,wordList,HAND_SIZE)
                  else:
                    print('You have not played a hand yet. Please play a new hand first!')