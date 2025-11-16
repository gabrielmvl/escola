import numpy as np
from tqdm import tqdm
import os

def limpar():
    os.system('cls' if os.name=='nt' else 'clear')

destino = "outros/rockyou/arquivos/rockyou-nums6"
numeros = []

def txt_finalizar():
    ultimo = numeros[-1]
    with open(f"{destino}.txt", "w", encoding="UTF-8") as f:
        for n in numeros:
            num = f"{n:06d}"
            if n == ultimo:
                f.write(f'{num}')
            else:
                f.write(f'{num}\n')

def csv_finalizar():
    ultimo = numeros[-1]
    with open(f"{destino}.csv", "w", encoding="UTF-8") as f:
        for n in numeros:
            num = f"{n:06d}"
            if n == ultimo:
                f.write(f'{num}')
            else:
                f.write(f'{num};\n')

def menu_finalizar():

    while True:
        menu = "Qual tipo de arquivo?\n\n1 - .txt\n2 - .csv\n0 - Sair"
        print(menu)

        menu_choose = input("Digite qual função deseja: ")

        match menu_choose:

            case '1':
                limpar()
                txt_finalizar()
                return
                

            case '2':
                limpar()
                csv_finalizar()
                return
                
            case '0':
                limpar()
                return
                
            case _:
                limpar()
                continue

def lista6nums():
    limpar()
    while True:
        menu = "Bem vindo ao seu gerador de lista de numeros de 6 algarismos\n\n1 - Normal\n2 - Reverse\n3 - Random\n0 - Sair"
        print(menu)

        menu_choose = input("Digite qual função deseja: ")

        match menu_choose:

            case '1':
                limpar()
                numero = 0
                for i in range(1000000):
                    numeros.append(numero)
                    numero += 1
                break
                

            case '2':
                limpar()
                numero = 999999
                for i in range(1000000):
                    numeros.append(numero)
                    numero -= 1
                break
                

            case '3':
                limpar()
                nums = np.random.permutation(1000000)
                numeros.extend(nums)
                break
                
            case '0':
                limpar()
                return
                
            case _:
                limpar()
                continue
    menu_finalizar()

def menu():
    while True:
        menu = "Qual o tipo de rockyou?\n\n1 - 6 algarismos\n0 - Sair"
        print(menu)

        menu_choose = input("Digite qual função deseja: ")

        match menu_choose:

            case '1':
                limpar()
                lista6nums()
                return
                
            case '0':
                limpar()
                return
                
            case _:
                limpar()
                continue

if __name__ == '__main__':
    menu()