import numpy as np

destino = "outros/rockyou/rockyou-nums6.csv"
numeros = []
while len(numeros) != 1000000:
    numero = np.random.randint(0, 999999)
    if numero in numeros:
        pass
    else:
        numeros.append(numero)

with open(destino, "w", encoding="UTF-8") as f:
    for n in numeros:
        num = f"{n:06d}"
        if num == "999999":
            f.write(f'{num}')
        else:
            f.write(f'{num};\n')
    print('pronto')
