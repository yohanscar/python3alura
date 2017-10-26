# -*- coding: utf-8 -*-

import random

def jogar():
    print("********************************")
    print("Bem vindo ao jogo de adivinação!")
    print("********************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nivel de dificuldade?")
    print("1-Facil , 2-Medio, 3-Dificil")

    nivel = int(input(">>>>> "))

    if(nivel==1):
        total_de_tentativas = 20
    elif(nivel==2):
        total_de_tentativas = 10
    elif(nivel==3):
        total_de_tentativas = 5

    for rodada in range(1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada,total_de_tentativas))
        chute_str = input("Digite o seu número: ")
        print("Você digitou", chute_str)

        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = (chute == numero_secreto)
        maior = (chute > numero_secreto)
        menor = (chute < numero_secreto)

        if (acertou):
            print("Você acertou e fez {} pontos!!!".format(pontos))
            break

        else:
            if (maior):
                print("Você errou! O seu chute foi MAIOR que o Numero secreto")
            elif (menor):
                print("Você errou! O seu chute foi MENOR que o Numero secreto")
            pontos = pontos - abs(numero_secreto - chute)
    print('O numero secreto era: ',numero_secreto)
    print('Fim do Jogo! thanks!')

if(__name__ == "__main__"):
    jogar()