# -*- coding: utf-8 -*-

def jogar():
    print("********************************")
    print("   Bem vindo ao jogo de Forca !")
    print("********************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False
    chute = ""

    while( not (enforcou and acertou)):
        print("jogando ...")
        print(letras_acertadas)
        chute = input("Qual a Letra?: ")
        chute = chute.strip()

        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra

            index = index + 1
    print('Fim do Jogo! thanks!!')


if(__name__ == "__main__"):
    jogar()