from time import sleep
from Controller import bots_functions as bf
import pyautogui as py

# print(py.position())

def rodar_altera(senha):

    # Alertando o usuário
    bf.alerta(mess='''
                  O robô começará a controlar o teclado

              Por favor, aperte OK e não mexa no mouse e teclado
              ''',
         title='AVISO!!!',
         button='OK')

    # Abrir o Putty.exe e o servidor DB662
    
    # Abrir o Putty.exe
    bf.moverMouse(999, 871)
    bf.clicar()

    # Abrir servido DB662 e fazendo login
    bf.moverMouse(785, 488)
    bf.doisCliques()
    bf.escrever(senha)
    bf.pressionarTecla('enter')
    sleep(4)

    # Entrando no Shell Disparados de Jobs
    sleep(4)
    bf.escrever('02')
    bf.pressionarTecla('enter')
    sleep(1)
    bf.escrever('662')
    bf.pressionarTecla('enter')
    bf.escrever('sjbaibm')
    bf.pressionarTecla('enter')

    # Processo de apertar "s" e "enter"
    ps = 16
    jump = 7
    for p in range(0, 3):
        bf.pressionarTecla('s')
        bf.pressionarTecla('enter')
        #print('s')
        sleep(ps)
        ps = ps - jump
        jump = jump - 3

    # Sair do Shell
    bf.pressionarTecla('esc')
    sleep(1)
    bf.pressionarTecla('left')
    bf.pressionarTecla('enter')
    sleep(0.5)

    # Fechar o Putty
    bf.segurarTecla('ctrl')
    bf.pressionarTecla('d')
    bf.soltarTecla('ctrl')
    

