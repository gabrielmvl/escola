import random
from tqdm import tqdm

destino = "outros/rockyou/rockyou-nums6.csv"
numero = 0
numeros = []

for i in tqdm(range(1000000)):
    numeros.append(numero)
    numero += 1

with open(destino, "w", encoding="UTF-8") as f:
    for n in numeros:
        num = f"{n:06d}"
        if num == "999999":
            f.write(f'{num}')
        else:
            f.write(f'{num};\n')
