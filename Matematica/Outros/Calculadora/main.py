import time
import os
import sys
from statistics import mean, median, multimode

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
    # pontos_de_espera("calculando", 3, (1/3))
    # limpar()

    with open('poligonos.txt', 'r', encoding='utf-8') as f:
        conteudo = f.readlines()

    poligonos = [poligono.strip() for poligono in conteudo]

    ordem = n - 3
    try:
        poligono_ordenado = poligonos[ordem]
    except IndexError:
        poligono_ordenado = f"poligono de {n} lados"
        pass

    diagonais = (n * (n - 3)) / 2
    d = int(diagonais)
    soma_dos_angulos_internos = (n - 2) * 180
    si = int(soma_dos_angulos_internos)

    print(f"O {poligono_ordenado} possui {d} diagonais, e a soma dos angulos internos é de {si}º.")

# Amplitude

def amplitude():
    numeros = []
    contador = 1
    while True:
        print("Digite 'x' para finalizar")
        numero = input(f"Digite o {contador}º número: ")
        limpar()
        contador += 1
        try:
            numero = int(numero)
            numeros.append(numero)
        except ValueError:
            if numero.lower() == "x":
                break
            else:
                print("anotação invalida!")
                timer(3)
                contador -= 1
    resposta = max(numeros) - min(numeros)
    print(f"A amplitude de {numeros} é {resposta}")

# Media

def media():
    numeros = []
    contador = 1
    while True:
        print("Digite 'x' para finalizar")
        numero = input(f"Digite o {contador}º número: ")
        limpar()
        contador += 1
        try:
            numero = int(numero)
            numeros.append(numero)
        except ValueError:
            if numero.lower() == "x":
                break
            else:
                print("anotação invalida!")
                timer(3)
                contador -= 1
    resposta = mean(numeros)
    print(f"A media de {numeros} é {resposta}")

# Mediana

def mediana():
    numeros = []
    contador = 1
    while True:
        print("Digite 'x' para finalizar")
        numero = input(f"Digite o {contador}º número: ")
        limpar()
        contador += 1
        try:
            numero = float(numero)
            numeros.append(numero)
        except ValueError:
            if numero.lower() == "x":
                break
            else:
                print("anotação invalida!")
                timer(3)
                contador -= 1
    resposta = median(numeros)
    print(f"A mediana de {numeros} é {resposta}")

# Moda

def moda():
    numeros = []
    contador = 1
    while True:
        print("Digite 'x' para finalizar")
        numero = input(f"Digite o {contador}º número: ")
        limpar()
        contador += 1
        try:
            numero = float(numero)
            numeros.append(numero)
        except ValueError:
            if numero.lower() == "x":
                break
            else:
                print("anotação invalida!")
                timer(3)
                contador -= 1
    resposta = multimode(numeros)
    contador2 = 1
    contador3 = 1
    for item in resposta:
        if contador2 == 1:
            resposta_atu = f"{item}"
        elif contador3 == len(resposta):
            resposta_atu = f"{resposta_atu} e {item}"
        else:
            resposta_atu = f"{resposta_atu}, {item}"
        contador2 += 1
        contador3 += 1
    print(f"A moda de {numeros} é {resposta_atu}")


# Amplitude2

def amplitude2(numeros):
    resposta = max(numeros) - min(numeros)
    return resposta

# Media2

def media2(numeros):
    resposta = mean(numeros)
    return resposta

# Mediana2

def mediana2(numeros):
    resposta = median(numeros)
    return resposta

# Moda2

def moda2(numeros):
    resposta = multimode(numeros)
    resposta_atu = ""
    contador2 = 1
    contador3 = 1
    for item in resposta:
        if contador2 == 1:
            resposta_atu = f"{item}"
        elif contador3 == len(resposta):
            resposta_atu = f"{resposta_atu} e {item}"
        else:
            resposta_atu = f"{resposta_atu}, {item}"
        contador2 += 1
        contador3 += 1
    return resposta_atu

# Geral

def geral():
    numeros = []
    contador = 1
    while True:
        print("Digite 'x' para finalizar")
        numero = input(f"Digite o {contador}º número: ")
        limpar()
        contador += 1
        try:
            numero = float(numero)
            numeros.append(numero)
        except ValueError:
            if numero.lower() == "x":
                break
            else:
                print("anotação invalida!")
                timer(3)
                contador -= 1
    media = media2(numeros)
    mediana = mediana2(numeros)
    moda = moda2(numeros)
    amplitude = amplitude2(numeros)
    print(f"""Media: {media}
Mediana: {mediana}
Moda: {moda}
Amplitude: {amplitude}
Lista: {sorted(numeros)}
Soma: {sum(numeros)}
Quantidade: {len(numeros)}
          """)
# Menu

def menu():
    while True:

        menu = "Bem vindo a sua calculadora\n\n1 - Calculo de poligonos\n2 - Media\n3 - Mediana\n4 - Moda\n5 - Amplitude\n6 - Tudo\n0 - Sair"
        print(menu)

        menu_choose = input("Digite qual função deseja: ")

        match menu_choose:

            case '1':
                limpar()
                calcular_poligonos()
                return

            case '2':
                limpar()
                media()
                return

            case '3':
                limpar()
                mediana()
                return

            case '4':
                limpar()
                moda()
                return
            
            case '5':
                limpar()
                amplitude()
                return
            
            case '6':
                limpar()
                geral()
                return
                
            case '0':
                limpar()
                return
                
            case _:
                limpar()
                continue

if __name__ == '__main__':
    menu()