import subprocess
import os

#APAGAR TELA
def cls():
    #Limpa a tela
    if os.name == "nt":
        #Se o sistema é Windows 
        subprocess.run("cls", shell=True)
    else:
        #Outros S.O, Linux e MacOS
        subprocess.run("clear", shell=True)

#CONTA MULTIPLICAÇÃO
def multiplication():
    pass

def division():
    pass

def addition():
    pass

def subtraction ():
    pass

def main():
    #Programa principal
    while True:
        cls()
        print("[CALCULADORA: ADIÇÃO, SUBTRAÇÃO, MULTIPLICAÇÃO, DIVISÃO]")
        break


