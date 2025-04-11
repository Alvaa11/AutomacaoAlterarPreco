import pyautogui as py

def moverMouse(x : int, y : int):
    py.moveTo(x, y)

    return

def clicar(button : str = 'left'):
    py.click(button=button)
    
    return

def doisCliques():
    py.doubleClick()
    
    return

def pressionarTecla(tecla : str):
    py.press(tecla)

    return

def combinarTeclas(tecla1 : str, tecla2: str):
    py.hotkey(tecla1, tecla2)

    return

def escrever(frase : str):
    py.write(frase)

    return

def segurarTecla(tecla : str):
    py.keyDown(tecla)

    return

def soltarTecla(tecla : str):
    py.keyUp(tecla)

def alerta(title : str, mess : str, button : str):
    py.alert(title=title, text=mess, button=button)