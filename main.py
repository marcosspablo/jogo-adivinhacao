from random import randint

jogar = True
tentativas = 0
palpite = 0
resposta = randint(0,100)

print("Bem-vindo ao Jogo de Advinhação! Advinhe um número entre 0 e 100.")
while jogar:
    palpite = int(input("Escolha um número inteiro entre 0 e 100:"))

    if palpite >= 0 and palpite <= 100:
        if palpite == resposta:
            tentativas = tentativas + 1
            print("Parabens, você acertou!")
            print(f"O número de tentativas necessarias para acertar o número foi: {tentativas}")
            jogar = False

        elif palpite > resposta:
            tentativas = tentativas + 1
            print("Seu palpite está acima da resposta, tente novamente.")
        else:
            tentativas = tentativas + 1
            print("Seu palpite está abaixo da resposta, tente novamente")
    else:
        print("O número informado é invalido. Tente com um número entre 0 e 100.")