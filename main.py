from dotenv import load_dotenv
from time import sleep
import os
from Controller.functions import moverMouse, clicar, doisCliques, pressionarTecla, escrever, segurarTecla, soltarTecla

load_dotenv(override=True)


senha = os.getenv('SENHA')
filial = os.getenv('FILIAL')
job = os.getenv('JOB')

# Abrir o Putty.exe e o servidor DB662 
#py.position()
# Abrir o Putty.exe
moverMouse(999, 871)
clicar()

# Abrir servido DB662 e fazendo login
moverMouse(773, 514)
doisCliques()
escrever(senha)
pressionarTecla('enter')
sleep(4)

# Entrando no Shell Disparados de Jobs
sleep(4)
escrever('02')
pressionarTecla('enter')
sleep(1)
escrever(filial)
pressionarTecla('enter')
escrever(job)
pressionarTecla('enter')

# Processo de apertar "s" e "enter"
ps = 16
jump = 7
for p in range(0, 3):
    pressionarTecla('s')
    pressionarTecla('enter')
    #print('s')
    sleep(ps)
    ps = ps - jump
    jump = jump - 3

# Sair do Shell
pressionarTecla('esc')
sleep(1)
pressionarTecla('left')
pressionarTecla('enter')
sleep(0.5)

# Fechar o Putty
segurarTecla('ctrl')
pressionarTecla('d')
soltarTecla('ctrl')