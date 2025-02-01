nome = input ("qual o seu nome")
pontos1 = input ("qual o seu placar na rodada 1")
pontos2 = input ("qual o seu placar na rodada 2")
pontos3 = input ("qual o seu placar na rodada 3")
pontos4 = input ("qual o seu placar na rodada 4")
pontos5 = input ("qual o seu placar na rodada 5")

pontuação_player1 = int(pontos1)+20+int(pontos2)-1+int(pontos3)*39+int(pontos4)+22+int(pontos5)*20


nome2 = input ("qual o seu nome")
pontos12 = input ("qual o seu placar na rodada 1")
pontos22= input ("qual o seu placar na rodada 2")
pontos32 = input ("qual o seu placar na rodada 3")
pontos42 = input ("qual o seu placar na rodada 4")
pontos52 = input ("qual o seu placar na rodada 5")

pontuação_player2 = int(pontos12)+20+int(pontos22)-1+int(pontos32)*39+int(pontos42)+22+int(pontos52)*20


if pontuação_player1 > pontuação_player2:
        print(f'{nome},venceu e possui um placar de {pontuação_player1} pontos, e seu adeversario {nome2} ficou em ultimo lugar com um placar de {pontuação_player2}')
else:
          print(f'{nome2},venceu e possui um placar de {pontuação_player2} pontos, e seu adeversario {nome} ficou em ultimo lugar com um placar de {pontuação_player1}')