from flask import Flask, send_file, send_from_directory
import pyautogui,time
import os

app = Flask(__name__)

comandos_permitidos = ['tab','space','enter','backspace','esc','f','left','right']

def alt_tab(tab):
    pyautogui.keyDown('alt')
    pyautogui.press('tab')
    r = 1
    if tab[-1:] != 'b':
        r = int(tab[-1:])
    for i in range(1,r):
        pyautogui.press('tab')
    
    pyautogui.keyUp('alt')
    # time.sleep(1)
    print("alt tab")

def desligar():
    os.system("shutdown /s /t 1")

def desktop():
    pyautogui.keyDown('win')
    pyautogui.press('d')
    pyautogui.keyUp('win')

def fechar():
    pyautogui.keyDown('alt')
    pyautogui.press('F4')
    pyautogui.keyUp('alt')

def comandos(comando):
    global comandos_permitidos
    print(comando)
    if comando in comandos_permitidos:
        pyautogui.press(comando)
    elif comando[:7] == 'alt+tab':
        alt_tab(comando)
    elif comando == 'desligar':
        desligar()
    elif comando == 'desktop':
        desktop()
    elif comando == 'fechar':
        fechar()

@app.route("/")
def home():
    return send_file("static/index.html")

@app.route("/comando/")
@app.route("/comando/<comando>")
def comando(comando = ""):
    comando = comando.lower()
    comandos(comando)
    return f"{comando}"

app.run(debug=True, host="0.0.0.0")
