# -*- coding: utf-8 -*-
import forca
import adivinhacao

print("********************************")
print("ESCOLHA O GAME QUE DESEJA JOGAR:")
print("********************************")

print('1-Forca 2-Adivinhação')

jogo = int(input('>>>>>'))

if(jogo == 1):
    print("Iniciando a Forca...")
    forca.jogar()
elif(jogo == 2):
    print("Iniciando a Adivinhação")
    adivinhacao.jogar()