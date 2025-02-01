#  Faça um programa que leia uma quantidade não determinada de números positivos. Calcule a
# quantidade de números pares e ímpares, a média de valores pares e a média geral dos números
# lidos. O número que encerrará a leitura será zero.

par= 0 
impar =0 
m_v_par= 0 
m_g = 0
total= 0

while True:
    num= int(input("numero?"))
    if num == 0:
        break
    total += 1
    m_g += num
    if num% 2 == 0:
        par += 1
        m_v_par +=num
    else:
        impar += 1

print(f'par {par}\n impar {impar}\n media par {m_v_par/par}\n media numeros {m_g/total} ')
