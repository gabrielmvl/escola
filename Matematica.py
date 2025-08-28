import time
import os
import sys

# def para limpar terminal

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# def para timer

def timer(tempo):
    time.sleep(tempo)

# def para pontos de espera

def pontos_de_espera(mensagem, repeticoes, delay):
    for _ in range(repeticoes):
        for i in range(4):  # de 0 até 3 pontos
            pontos = '.' * i
            sys.stdout.write('\r' + mensagem + pontos + ' ' * (3 - i))  # limpa os restos
            sys.stdout.flush()
            timer(delay)
    print()

# calcular poligonos

def calcular_poligonos():
# cola: diagonais = n * (n - 3) / 2 
# cola: soma dos internos = (n - 2) * 180
    while True:
        try:
            num_lados = int(input("digite o numero de lados do poligono: "))
            
        except ValueError:
            limpar()
            print("digite valores inteiros!")
            timer(3)
            limpar()
            continue

        n = num_lados
        if n < 3:
            limpar()
            print("Não é poligono")
            timer(3)
            limpar()
            continue
        else:
            break
    limpar()
    pontos_de_espera("calculando", 3, (1/3))
    limpar()

    poligonos = ["Triângulo", "Quadrilátero", "Pentágono", "Hexágono", "Heptágono", "Octógono", "Eneágono", "Decágono", "Undecágono", "Dodecágono", "Tridecágono", "Tetradecágono", "Pentadecágono", "Hexadecágono", "Heptadecágono", "Octodecágono", "Eneadecágono", "Icoságono", "Icosihenágono", "Icosidigono", "Icositricono", "Icositetrágono", "Icosipentágono", "Icosihexágono", "Icosiheptágono", "Icosioctógono", "Icosieneágono", "Triacontágono"]
    ordem = n - 3
    try:
        poligono_ordenado = poligonos[ordem]
    except IndexError:
        poligono_ordenado = "(poligono não computado, temos apenas até 30 lados)"
        pass

    diagonais = (n * (n - 3)) / 2
    d = int(diagonais)
    soma_dos_angulos_internos = (n - 2) * 180
    si = int(soma_dos_angulos_internos)

    print(f"O {poligono_ordenado} possui {d} diagonais, e a soma dos angulos internos é de {si}º.")

# Menu

def menu():
    while True:

        menu = "Bem vindo a sua calculadora\n\n1 - Calculo de poligonos\n0 - Sair"
        print(menu)

        menu_choose = input("Digite qual função deseja: ")

        match menu_choose:

            case '1':
                limpar()
                calcular_poligonos()
                return
                
            case '0':
                limpar()
                return
                
            case _:
                limpar()
                continue

menu()