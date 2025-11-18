import numpy as np
import os

def limpar():
    os.system('cls' if os.name=='nt' else 'clear')

destino = "outros/rockyou/arquivos/rockyou"
numeros = []

def txt_finalizar():
    ultimo = numeros[-1]
    with open(f"{destino}.txt", "w", encoding="UTF-8") as f:
        for n in numeros:
            if n == ultimo:
                f.write(n)
            else:
                f.write(f'{n}\n')

def csv_finalizar():
    ultimo = numeros[-1]
    with open(f"{destino}.csv", "w", encoding="UTF-8") as f:
        for n in numeros:
            if n == ultimo:
                f.write(n)
            else:
                f.write(f'{n};\n')

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

def ListaNums():
    limpar()
    while True:
        Qtd = int(input("Bem vindo ao seu gerador de lista de numeros!\n\ndigite quantos algarismos deseja: "))
        limpar()
        menu = "Tipos de geração:\n\n1 - Normal\n2 - Reverse\n3 - Random\n0 - Sair"
        print(menu)

        menu_choose = input("Digite qual função deseja: ")

        match menu_choose:

            case '1':
                limpar()
                numero = 0
                for i in range(10**Qtd):
                    numeros.append(f"{numero:0{Qtd}d}")
                    numero += 1
                break
                

            case '2':
                limpar()
                numero = 10*Qtd-1
                for i in range(10**Qtd):
                    numeros.append(f"{numero:0{Qtd}d}")
                    numero -= 1
                break
                

            case '3':
                limpar()
                nums = np.random.permutation(10**Qtd)
                for num in nums:
                    numeros.append(f"{num:0{Qtd}d}")
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
        menu = "Qual o tipo de rockyou?\n\n1 - Lista de números\n0 - Sair"
        print(menu)

        menu_choose = input("Digite qual função deseja: ")

        match menu_choose:

            case '1':
                limpar()
                ListaNums()
                return
                
            case '0':
                limpar()
                return
                
            case _:
                limpar()
                continue

if __name__ == '__main__':
    menu()