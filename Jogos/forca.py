# -*- coding: utf-8 -*-

import random

def jogar():
    print("********************************")
    print("   Bem vindo ao jogo de Forca !")
    print("********************************")

    arquivo = open("palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0,len(palavras))

    print(palavras)
    palavra_secreta = palavras[numero].upper() ## posicao numero
    print("########")
    print("dica: {}".format(len(palavra_secreta)))
    letras_acertadas = ["_" for letra in palavra_secreta]

    ##for x in palavra_secreta:
    ##    letras_acertadas.append("_")
    
    enforcou = False
    acertou = False
    chute = ""
    erros = 0

    while( not enforcou and not acertou):
        print("jogando ...")
        print(letras_acertadas)
        chute = input("Qual a Letra?: ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):

            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra

                index += 1
        else:
            erros +=1

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas

    print('Fim do Jogo! thanks!!')


if(__name__ == "__main__"):
    jogar()