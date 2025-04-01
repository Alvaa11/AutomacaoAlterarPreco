import pyautogui as py

def moverMouse(x, y):
    py.moveTo(x, y)

    return

def clicar():
    py.click()
    
    return

def doisCliques():
    py.doubleClick()
    
    return

def pressionarTecla(tecla):
    py.press(tecla)

    return

def escrever(frase):
    py.write(frase)

    return

def segurarTecla(tecla):
    py.keyDown(tecla)

    return

def soltarTecla(tecla):
    py.keyUp(tecla)

def alerta(title, mess, button):
    py.alert(title=title, text=mess, button=button)