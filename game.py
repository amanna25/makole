print('Rock')
print('Paper')
print('Scissors')


player1 = input('Player 1, Make Your Move ')
player2 = input('Player 2, Make Your Move ')



if player1 == 'rock' and player2 == 'paper':
    print('Player 1 Wins')
elif player1 == 'rock' and player2 == 'scissors':
    print('Player 2 Wins')    
elif player1 == 'scissors' and player2 == 'paper':
    print('Player 2 Wins')   
elif player1 == 'paper' and player2 == 'rock':
    print('Player 1 Wins')           
elif player1 == 'rock' and player2 == 'rock':
    print('Player 1 Wins')       


elif player1 == player2:
     print('its a lie')

else:
    print('something went wrong')