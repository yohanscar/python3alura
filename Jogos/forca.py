# -*- coding: utf-8 -*-

def jogar():
    print("********************************")
    print("   Bem vindo ao jogo de Forca !")
    print("********************************")

    palavra_secreta = "banana".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    for x in palavra_secreta:
        letras_acertadas.append("_")
    
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