import random
pedraPapelTesoura= ['papel','tesoura','pedra']

player1= random.choice (pedraPapelTesoura)
player2= random.choice (pedraPapelTesoura)


if player1 == "tesoura" and player2 == "papel":
   print(f'o jogador 1 ganhou jogando {player1} e o jogador 2 jogou {player2}')

elif player1== "pedra" and player2 == "tesoura":
   print(f'o jogador 1 ganhou jogando {player1} e o jogador 2 jogou {player2}')

elif player1== "papel" and player2 == "pedra":
   print(f'o jogador 1 ganhou jogando {player1} e o jogador 2 jogou {player2}')

elif player1 == "tesoura" and player2 == "tesoura":
   print(f'empate, ambos jogaram {player1}')

elif player1 == "pedra" and player2 == "pedra":
   print(f'empate, ambos jogaram {player1}')

elif player1 == "papel" and player2 == "papel":
   print(f'empate, ambos jogaram {player1}')

elif player1 == "pedra" and player2== "papel"  :
   print(f'o jogador 2 ganhou jogando {player2} e o jogador 1 jogou {player1}')

elif player1 == "tesoura" and player2== "pedra"  :
   print(f'o jogador 2 ganhou jogando {player2} e o jogador 1 jogou {player1}')

elif player1 == "papel" and player2 == "tesoura":
   print(f'o jogador 2 ganhou jogando {player2} e o jogador 1 jogou {player1}')
