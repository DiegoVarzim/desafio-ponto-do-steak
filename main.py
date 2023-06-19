# Desafio com If, Elif, ELse

'''
Criar um programa que dependendo da temperatura (em Celsius) do steak ele retorna o ponto de cozimento em Português. O usuário deverá forncecer a temperatura.


Temperaturas - Cozimento
120º F ou 48º C - Rare (Selada)
130º F ou 54º C - Medium rare (Ao ponto para o mal)
140º F ou 60º C - Medium (Ao ponto)
150º F ou 65º C - Medium well (Ao ponto para o bem)
160º F ou 71º C - Well done (Bem passada)

'''

tem_cel = int(input('Qual é a temperatura da carne? '))

if tem_cel < 48:
    print('Cozinhar por mais alguns minutos')
elif tem_cel in range(48, 54):
    print('Selada')
elif tem_cel in range(54, 60):
    print('Ao ponto para o mal')
elif tem_cel in range(60, 64):
    print('Ao ponto')    
elif tem_cel in range(64, 70):
    print('Ao ponto para o bem')
elif tem_cel in range(70, 75):
    print('Bem passada')
else:
    print('Sua carne está queimada')














